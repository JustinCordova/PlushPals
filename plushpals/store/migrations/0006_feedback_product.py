# Generated by Django 5.1.7 on 2025-04-27 01:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_product_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='feedback_set', to='store.product'),
            preserve_default=False,
        ),
    ]
