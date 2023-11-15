# Generated by Django 4.2.7 on 2023-11-15 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('condition', models.CharField(choices=[('PGT', 'Price >'), ('PLT', 'Price <'), ('PGE', 'Price >='), ('PLE', 'Price <='), ('QGT', 'Quantity >'), ('QLT', 'Quantity <'), ('QGE', 'Quantity >='), ('QLE', 'Quantity <=')], max_length=3)),
                ('test_value', models.FloatField(default=0)),
                ('type', models.CharField(choices=[('PCT', 'Discount %'), ('PRC', 'New price per unit')], default='PRC', max_length=3)),
                ('discount_value', models.FloatField(default=0)),
                ('priority', models.IntegerField()),
            ],
            options={
                'ordering': ['priority'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.TextField(default='<product name>')),
                ('price', models.FloatField(default=0.0)),
                ('currency_symbol', models.CharField(max_length=3)),
                ('discounts', models.ManyToManyField(to='api.discount')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quantity', models.IntegerField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]