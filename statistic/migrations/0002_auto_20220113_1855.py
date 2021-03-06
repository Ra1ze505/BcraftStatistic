# Generated by Django 3.2.9 on 2022-01-13 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staticitem',
            name='click',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='staticitem',
            name='cost',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='staticitem',
            name='views',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
