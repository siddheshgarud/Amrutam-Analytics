# Generated by Django 4.0.3 on 2022-03-22 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0008_remove_orders_customer_id_remove_orders_line_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='customer_id',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orders',
            name='line_items_id',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
