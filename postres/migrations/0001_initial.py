# Generated by Django 3.1.4 on 2021-07-07 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Postres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='DEFAULT VALUE', max_length=100)),
                ('precio', models.CharField(default='DEFAULT VALUE', max_length=20)),
                ('stock', models.CharField(default='DEFAULT VALUE', max_length=100)),
                ('img', models.FileField(upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'postres',
            },
        ),
    ]
