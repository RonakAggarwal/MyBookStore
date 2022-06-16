# Generated by Django 3.2.3 on 2022-06-16 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AuthorName', models.CharField(max_length=30, unique=True)),
                ('PhoneNumber', models.CharField(max_length=15, unique=True)),
                ('BirthDate', models.DateField()),
                ('DeathDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CategoryName', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50, unique=True)),
                ('Publisher', models.CharField(max_length=50)),
                ('PublishDate', models.DateField()),
                ('Price', models.FloatField()),
                ('SoldCount', models.IntegerField()),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Book.author')),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Book.category')),
            ],
        ),
    ]
