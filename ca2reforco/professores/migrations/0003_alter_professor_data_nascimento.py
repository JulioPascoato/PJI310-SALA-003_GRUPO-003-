# Generated by Django 4.1.2 on 2022-11-02 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professores', '0002_alter_professor_dados_bancarios_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='data_nascimento',
            field=models.DateField(blank=True, null=True),
        ),
    ]
