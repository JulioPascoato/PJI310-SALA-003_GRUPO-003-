# Generated by Django 4.1.2 on 2022-11-02 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='dados_bancarios',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='professor',
            name='data_nascimento',
            field=models.DateField(blank=True, null=True, verbose_name='%m/%d/%y'),
        ),
    ]
