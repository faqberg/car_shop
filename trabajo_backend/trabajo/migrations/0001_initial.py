# Generated by Django 5.0.3 on 2024-03-09 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car_Features',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_car', models.CharField(max_length=100000)),
                ('title', models.CharField(max_length=10000)),
                ('description', models.CharField(max_length=10000)),
                ('photo', models.CharField(max_length=1000000)),
            ],
        ),
        migrations.CreateModel(
            name='Car_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_car', models.CharField(max_length=100000)),
                ('photo', models.CharField(max_length=1000000)),
                ('title', models.CharField(max_length=100000)),
                ('descrition', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('name', models.CharField(max_length=1000)),
                ('year', models.CharField(max_length=5)),
                ('price', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=1000)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('photo', models.CharField(max_length=1000000)),
                ('description', models.CharField(max_length=10000000)),
                ('title_description', models.CharField(max_length=100000)),
            ],
        ),
    ]