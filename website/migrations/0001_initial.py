# Generated by Django 2.2.5 on 2019-10-10 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PCat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='PCat_img/')),
                ('content', models.TextField(blank=True)),
                ('upvotes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PSubCat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcat', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='PSubCat_img/')),
                ('content', models.TextField(blank=True)),
                ('upvotes', models.IntegerField(default=0)),
                ('cat', models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='website.PCat')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, upload_to='Product_img/')),
                ('GTIN', models.CharField(max_length=20)),
                ('Name', models.CharField(max_length=100)),
                ('Brand', models.CharField(max_length=50)),
                ('upvotes', models.IntegerField(default=0)),
                ('subcat', models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='website.PSubCat')),
            ],
        ),
    ]