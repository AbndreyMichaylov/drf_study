# Generated by Django 3.1.6 on 2021-02-09 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heroes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='hp',
            field=models.IntegerField(verbose_name='Health oint'),
        ),
        migrations.AlterField(
            model_name='hero',
            name='mana',
            field=models.IntegerField(verbose_name='Health oint'),
        ),
    ]
