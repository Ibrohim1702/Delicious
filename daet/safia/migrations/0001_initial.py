# Generated by Django 4.0.6 on 2022-07-23 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=56)),
                ('slug', models.SlugField(max_length=56)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('date', models.DateField(auto_now_add=True)),
                ('img', models.ImageField(upload_to='')),
                ('rate', models.IntegerField()),
                ('prep', models.IntegerField()),
                ('cook', models.IntegerField()),
                ('yields', models.IntegerField()),
                ('step', models.TextField()),
                ('ingredients', models.TextField()),
                ('ctg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='safia.category')),
            ],
        ),
    ]
