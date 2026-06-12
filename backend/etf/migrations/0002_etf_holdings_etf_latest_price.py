from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etf', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='etf',
            name='latest_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=10, null=True, verbose_name='最新股價'),
        ),
        migrations.AddField(
            model_name='etf',
            name='holdings',
            field=models.PositiveIntegerField(default=0, verbose_name='存量(股)'),
        ),
    ]
