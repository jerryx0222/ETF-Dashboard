from rest_framework import serializers
from .models import ETF, DividendRecord


class DividendRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = DividendRecord
        fields = ['id', 'ex_dividend_date', 'dividend_amount', 'closing_price']


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
        ]

    def get_annualized_yield(self, obj):
        from datetime import date
        current_year = date.today().year
        target_years = set(range(current_year - 5, current_year))  # 5 complete years before this year

        yearly_yields = {}
        for record in obj.dividend_records.all():
            year = record.ex_dividend_date.year
            if year not in target_years:
                continue
            price = float(record.closing_price or 0)
            if price == 0:
                continue
            yearly_yields[year] = yearly_yields.get(year, 0) + float(record.dividend_amount) / price

        if len(yearly_yields) < 5:
            return None
        if any(v == 0 for v in yearly_yields.values()):
            return None

        return round(sum(yearly_yields.values()) / 5 * 100, 2)
