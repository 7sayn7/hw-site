# Generated by Django 3.2 on 2023-05-17 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Geography',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('data', models.CharField(max_length=1000)),
                ('cities', models.CharField(max_length=1000)),
                ('individual_id', models.CharField(max_length=300)),
                ('added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
