from django.db import models


class ETF(models.Model):
    DIVIDEND_FREQUENCY_CHOICES = [
        ('monthly', '每月'),
        ('quarterly', '每季'),
        ('semi_annual', '每半年'),
        ('annual', '每年'),
    ]

    securities_abbreviation = models.CharField('證券簡稱', max_length=50)
    securities_code = models.CharField('證券代號', max_length=20, unique=True)
    issuer = models.CharField('發行人', max_length=100)
    target_index = models.CharField('標的指數', max_length=200)
    management_fee = models.DecimalField('經理費(%)', max_digits=6, decimal_places=4)
    custody_fee = models.DecimalField('保管費(%)', max_digits=6, decimal_places=4)
    dividend_frequency = models.CharField('配息頻率', max_length=20, choices=DIVIDEND_FREQUENCY_CHOICES)
    dividend_bank = models.CharField('配息銀行', max_length=100)
    latest_price = models.DecimalField('最新股價', max_digits=10, decimal_places=2, null=True, blank=True, default=None)
    holdings = models.PositiveIntegerField('存量(股)', default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'ETF'
        verbose_name_plural = 'ETF'
        ordering = ['securities_code']

    def __str__(self):
        return f'{self.securities_code} {self.securities_abbreviation}'


class DividendRecord(models.Model):
    etf = models.ForeignKey(ETF, on_delete=models.CASCADE, related_name='dividend_records', verbose_name='ETF')
    ex_dividend_date = models.DateField('除息日')
    dividend_amount = models.DecimalField('配息金額(元)', max_digits=10, decimal_places=4)
    closing_price = models.DecimalField('除息日收盤價(元)', max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '歷史配息紀錄'
        verbose_name_plural = '歷史配息紀錄'
        ordering = ['-ex_dividend_date']
        unique_together = ['etf', 'ex_dividend_date']

    def __str__(self):
        return f'{self.etf.securities_code} {self.ex_dividend_date} ${self.dividend_amount}'
