from django.contrib import admin
from .models import ETF, DividendRecord


class DividendRecordInline(admin.TabularInline):
    model = DividendRecord
    extra = 0
    ordering = ['-ex_dividend_date']


@admin.register(ETF)
class ETFAdmin(admin.ModelAdmin):
    list_display = [
        'securities_code', 'securities_abbreviation', 'issuer',
        'management_fee', 'custody_fee', 'dividend_frequency', 'dividend_bank'
    ]
    search_fields = ['securities_code', 'securities_abbreviation', 'issuer']
    list_filter = ['dividend_frequency', 'issuer']
    inlines = [DividendRecordInline]


@admin.register(DividendRecord)
class DividendRecordAdmin(admin.ModelAdmin):
    list_display = ['etf', 'ex_dividend_date', 'dividend_amount', 'closing_price']
    list_filter = ['etf', 'ex_dividend_date']
    ordering = ['-ex_dividend_date']
