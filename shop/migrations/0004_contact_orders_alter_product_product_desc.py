# Generated by Django 4.1.7 on 2023-04-30 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80)),
                ('email', models.CharField(default='', max_length=50)),
                ('phone', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=5000)),
                ('name', models.CharField(max_length=90)),
                ('email', models.CharField(max_length=900)),
                ('address', models.CharField(max_length=112)),
                ('city', models.CharField(max_length=122)),
                ('state', models.CharField(max_length=112)),
                ('zip_code', models.CharField(max_length=112)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='product_desc',
            field=models.CharField(max_length=1000),
        ),
    ]
