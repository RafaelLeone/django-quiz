# Generated by Django 4.0.6 on 2022-07-28 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pergunta', models.CharField(max_length=128, unique=True)),
                ('descricao', models.TextField()),
                ('autor', models.CharField(max_length=128, unique=True)),
                ('imagem', models.URLField(max_length=1024)),
            ],
        ),
    ]
