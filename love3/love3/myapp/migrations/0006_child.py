# Generated by Django 3.2 on 2021-07-20 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_activity3'),
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='static/pictures/')),
                ('name', models.CharField(max_length=20)),
                ('sex', models.CharField(max_length=3)),
                ('birthday', models.CharField(max_length=20)),
                ('place', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=20)),
                ('detaile', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Child',
            },
        ),
    ]