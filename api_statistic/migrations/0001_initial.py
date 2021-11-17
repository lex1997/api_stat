# Generated by Django 3.2.2 on 2021-11-17 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата события')),
                ('views', models.IntegerField(blank=True, null=True, verbose_name='Количество показов')),
                ('clics', models.IntegerField(blank=True, null=True, verbose_name='Количество кликов')),
                ('cost', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Стоимость клика')),
            ],
            options={
                'ordering': ('date',),
            },
        ),
    ]