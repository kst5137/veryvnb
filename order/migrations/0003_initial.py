# Generated by Django 4.0.4 on 2022-05-31 08:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0002_initial'),
        ('coupon', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='username',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='order',
            name='coupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='order_coupon', to='coupon.coupon'),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order_list_products', to='shop.product'),
        ),
        migrations.AddField(
            model_name='order',
            name='username',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
