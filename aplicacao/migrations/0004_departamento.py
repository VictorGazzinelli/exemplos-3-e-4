# Generated by Django 3.1 on 2021-06-27 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacao', '0003_pessoa_escolaridade'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla', models.CharField(max_length=6)),
                ('descricao', models.CharField(max_length=30)),
            ],
        ),
    ]
