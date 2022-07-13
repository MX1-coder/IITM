# Generated by Django 4.0.4 on 2022-05-19 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('product_quentity', models.IntegerField(max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('discription', models.CharField(max_length=100)),
            ],
        ),
    ]
