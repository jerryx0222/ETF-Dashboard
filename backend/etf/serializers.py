from rest_framework import serializers
from .models import ETF, DividendRecord


class DividendRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = DividendRecord
        fields = ['id', 'ex_dividend_date', 'dividend_amount', 'closing_price', 'annualized_yield_rate']


class ETFSerializer(serializers.ModelSerializer):
    dividend_frequency_display = serializers.CharField(source='get_dividend_frequency_display', read_only=True)
    dividend_records = DividendRecordSerializer(many=True, read_only=True)

    class Meta:
        model = ETF
        fields = [
            'id',
            'securities_abbreviation',
            'securities_code',
            'issuer',
            'target_index',
            'management_fee',
            'custody_fee',
            'dividend_frequency',
            'dividend_frequency_display',
            'dividend_bank',
            'latest_price',
            'holdings',
            'dividend_records',
            'created_at',
            'updated_at',
        ]


class ETFListSerializer(serializers.ModelSerializer):
    dividend_frequency_display = serializers.CharField(source='get_dividend_frequency_display', read_only=True)
    annualized_yield = serializers.SerializerMethodField()
    annualized_yield_complete = serializers.SerializerMethodField()

    class Meta:
        model = ETF
        fields = [
            'id',
            'securities_abbreviation',
            'securities_code',
            'issuer',
            'target_index',
            'management_fee',
            'custody_fee',
            'dividend_frequency',
            'dividend_frequency_display',
            'dividend_bank',
            'latest_price',
            'holdings',
            'annualized_yield',
            'annualized_yield_complete',
        ]

    def _compute_yearly_yields(self, obj):
        if hasattr(obj, '_yield_cache'):
            return obj._yield_cache

        from datetime import date
        current_year = date.today().year
        target_years = set(range(current_year - 5, current_year))

        yearly_yields = {}
        yearly_stored_rates = {}
        for record in obj.dividend_records.all():
            year = record.ex_dividend_date.year
            if year not in target_years:
                continue
            price = float(record.closing_price or 0)
            if price > 0:
                yearly_yields[year] = yearly_yields.get(year, 0) + float(record.dividend_amount) / price
            elif record.annualized_yield_rate:
                yearly_stored_rates.setdefault(year, []).append(float(record.annualized_yield_rate))

        for year, rates in yearly_stored_rates.items():
            if year not in yearly_yields:
                yearly_yields[year] = sum(rates) / len(rates) / 100

        # 排除殖利率為 0 的年份（收盤價為 0 且無年化配息率）
        result = {y: v for y, v in yearly_yields.items() if v > 0}
        obj._yield_cache = result
        return result

    def get_annualized_yield(self, obj):
        yearly_yields = self._compute_yearly_yields(obj)
        if not yearly_yields:
            return None
        return round(sum(yearly_yields.values()) / len(yearly_yields) * 100, 2)

    def get_annualized_yield_complete(self, obj):
        return len(self._compute_yearly_yields(obj)) >= 5
