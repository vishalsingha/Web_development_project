# Generated by Django 2.1 on 2020-12-10 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spiciyo', '0003_call_request'),
    ]

    operations = [
        migrations.CreateModel(
            name='newsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
