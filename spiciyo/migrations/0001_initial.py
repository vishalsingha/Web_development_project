# Generated by Django 2.1 on 2020-12-06 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('des', models.TextField()),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='pics')),
            ],
        ),
    ]
