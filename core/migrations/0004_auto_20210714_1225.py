# Generated by Django 2.1.5 on 2021-07-14 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_item_supplier'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='capital_price_bulk',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='capital_price_per_piece',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='discount',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='item',
            name='sell_price_retail',
            field=models.IntegerField(default=0),
        ),
    ]