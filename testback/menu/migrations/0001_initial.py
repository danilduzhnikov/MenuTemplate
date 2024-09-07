# Generated by Django 5.1.1 on 2024-09-07 06:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuExample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название категории')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='menu.menuexample', verbose_name='Родительская категория')),
            ],
            options={
                'verbose_name': 'Категория меню',
                'verbose_name_plural': 'Категории меню',
            },
        ),
    ]
