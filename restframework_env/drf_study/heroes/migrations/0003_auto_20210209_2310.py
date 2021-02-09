# Generated by Django 3.1.6 on 2021-02-09 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heroes', '0002_auto_20210209_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='name',
            field=models.CharField(db_index=True, max_length=100, unique=True, verbose_name='Name of hero'),
        ),
    ]