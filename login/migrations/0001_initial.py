# Generated by Django 4.0.4 on 2022-05-15 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('foto', models.ImageField(null=True, upload_to='imagenes/')),
            ],
        ),
    ]
