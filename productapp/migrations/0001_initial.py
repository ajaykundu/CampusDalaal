# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-29 09:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategoryModel',
            fields=[
                ('typeOfProduct', models.CharField(max_length=150, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='ProductsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
                ('prize', models.DecimalField(decimal_places=2, max_digits=8)),
                ('Description', models.TextField()),
                ('productImage1', models.ImageField(blank=True, upload_to='photos/')),
                ('productImage2', models.ImageField(blank=True, upload_to='photos/')),
                ('productImage3', models.ImageField(blank=True, upload_to='photos/')),
                ('productImage4', models.ImageField(blank=True, upload_to='photos/')),
                ('soldFlag', models.BooleanField(default=False)),
                ('createdTime', models.DateTimeField(auto_now=True)),
                ('categoryid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='productapp.ProductCategoryModel')),
                ('sellerid', models.ForeignKey(default='ajay', on_delete=django.db.models.deletion.CASCADE, related_name='products', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-createdTime'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='productsmodel',
            unique_together=set([('sellerid', 'categoryid', 'title')]),
        ),
    ]