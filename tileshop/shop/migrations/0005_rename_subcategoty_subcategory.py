# Generated by Django 4.2 on 2023-06-12 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_category_options_product_price_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SubCategoty',
            new_name='SubCategory',
        ),
    ]