# Generated by Django 3.1.4 on 2020-12-25 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20201225_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='note',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]