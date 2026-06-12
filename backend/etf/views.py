import io
import openpyxl
from django.http import HttpResponse
from rest_framework import viewsets, filters, status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import ETF, DividendRecord
from .serializers import ETFSerializer, ETFListSerializer, DividendRecordSerializer
from .twse import fetch_twse_etfs, fetch_etf_dividends


class ETFViewSet(viewsets.ModelViewSet):
    queryset = ETF.objects.prefetch_related('dividend_records').all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['dividend_frequency', 'issuer']
    search_fields = ['securities_code', 'securities_abbreviation', 'issuer']
    ordering_fields = ['securities_code', 'management_fee', 'custody_fee']

    def get_serializer_class(self):
        if self.action == 'list':
            return ETFListSerializer
        return ETFSerializer

    @action(detail=True, methods=['post'], url_path='import_dividends')
    def import_dividends(self, request, pk=None):
        etf = self.get_object()
        try:
            records = fetch_etf_dividends(etf.securities_code)
        except Exception as e:
            msg = str(e)
            if 'rate' in msg.lower() or '429' in msg:
                msg = 'Yahoo Finance 請求次數過多，請稍候 30 秒再試'
            return Response({'error': msg}, status=status.HTTP_502_BAD_GATEWAY)

        if not records:
            return Response({'error': '未從 TWSE 取得配息資料'}, status=status.HTTP_404_NOT_FOUND)

        created, updated = 0, 0
        for rec in records:
            _, was_created = DividendRecord.objects.update_or_create(
                etf=etf,
                ex_dividend_date=rec['ex_dividend_date'],
                defaults={
                    'dividend_amount': rec['dividend_amount'],
                    'closing_price': rec['closing_price'],
                },
            )
            if was_created:
                created += 1
            else:
                updated += 1

        return Response({'created': created, 'updated': updated, 'total': len(records)})


class DividendRecordViewSet(viewsets.ModelViewSet):
    queryset = DividendRecord.objects.select_related('etf').all()
    serializer_class = DividendRecordSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['etf', 'ex_dividend_date']
    ordering_fields = ['ex_dividend_date', 'dividend_amount', 'closing_price']


def export_etf_excel(request):
    etfs = ETF.objects.prefetch_related('dividend_records').all()

    wb = openpyxl.Workbook()

    ws_info = wb.active
    ws_info.title = 'ETF基本資料'
    headers_info = [
        '證券簡稱', '證券代號', '發行人', '標的指數',
        '經理費(%)', '保管費(%)', '配息頻率', '配息銀行'
    ]
    ws_info.append(headers_info)
    for etf in etfs:
        ws_info.append([
            etf.securities_abbreviation,
            etf.securities_code,
            etf.issuer,
            etf.target_index,
            float(etf.management_fee),
            float(etf.custody_fee),
            etf.get_dividend_frequency_display(),
            etf.dividend_bank,
        ])

    ws_div = wb.create_sheet('歷史配息紀錄')
    headers_div = ['證券代號', '證券簡稱', '除息日', '配息金額(元)', '除息日收盤價(元)']
    ws_div.append(headers_div)
    for etf in etfs:
        for record in etf.dividend_records.all():
            ws_div.append([
                etf.securities_code,
                etf.securities_abbreviation,
                record.ex_dividend_date.strftime('%Y-%m-%d'),
                float(record.dividend_amount),
                float(record.closing_price),
            ])

    buffer = io.BytesIO()
    wb.save(buffer)
    buffer.seek(0)

    response = HttpResponse(
        buffer,
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename="etf_data.xlsx"'
    return response


@api_view(['GET'])
def twse_etf_list(request):
    try:
        etfs = fetch_twse_etfs()
        existing = set(ETF.objects.values_list('securities_code', flat=True))
        for etf in etfs:
            etf['already_imported'] = etf['securities_code'] in existing
        return Response(etfs)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_502_BAD_GATEWAY)


@api_view(['POST'])
def import_etfs(request):
    items = request.data if isinstance(request.data, list) else []
    if not items:
        return Response({'error': '未選擇任何 ETF'}, status=status.HTTP_400_BAD_REQUEST)

    created, skipped = [], []
    for item in items:
        code = item.get('securities_code', '').strip()
        if not code:
            continue
        try:
            mgmt_fee = float(item.get('management_fee') or 0)
            cust_fee = float(item.get('custody_fee') or 0)
        except (ValueError, TypeError):
            mgmt_fee, cust_fee = 0, 0

        freq = item.get('dividend_frequency', 'annual')
        valid_freqs = {'monthly', 'quarterly', 'semi_annual', 'annual'}
        if freq not in valid_freqs:
            freq = 'annual'

        _, was_created = ETF.objects.update_or_create(
            securities_code=code,
            defaults={
                'securities_abbreviation': item.get('securities_abbreviation', code),
                'issuer': item.get('issuer', ''),
                'target_index': item.get('target_index', ''),
                'management_fee': mgmt_fee,
                'custody_fee': cust_fee,
                'dividend_frequency': freq,
                'dividend_bank': item.get('dividend_bank', ''),
            }
        )
        (created if was_created else skipped).append(code)

    return Response({
        'created': len(created),
        'updated': len(skipped),
        'codes': created + skipped,
    })
