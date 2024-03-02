# Generated by Django 5.0.2 on 2024-03-02 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('cor', models.CharField(max_length=20)),
                ('marca', models.CharField(max_length=20)),
                ('condicao', models.CharField(choices=[('O', 'OTIMO'), ('B', 'BOM'), ('R', 'RUIM'), ('P', 'PESSIMO')], max_length=1)),
            ],
        ),
    ]