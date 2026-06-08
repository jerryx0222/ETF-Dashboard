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
            'dividend_records',
            'created_at',
            'updated_at',
        ]


class ETFListSerializer(serializers.ModelSerializer):
    dividend_frequency_display = serializers.CharField(source='get_dividend_frequency_display', read_only=True)

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
        ]
