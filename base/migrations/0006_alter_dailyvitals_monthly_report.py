# Generated by Django 4.0.4 on 2022-05-20 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_dailyvitals_monthly_report'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyvitals',
            name='monthly_report',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]