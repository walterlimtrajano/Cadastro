# Generated by Django 4.2.5 on 2023-09-09 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='idade',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]
