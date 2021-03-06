# Generated by Django 3.0.2 on 2020-01-17 10:12

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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('is_publish', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('is_publish', models.BooleanField(default=True)),
                ('main_category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='category.Category')),
            ],
        ),
    ]
