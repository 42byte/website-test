# Generated by Django 2.2.5 on 2019-10-14 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(default='This is my awesome bio...'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='products_watchlist',
            field=models.ManyToManyField(blank=True, to='website.Product'),
        ),
    ]
