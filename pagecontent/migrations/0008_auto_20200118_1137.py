# Generated by Django 3.0.2 on 2020-01-18 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagecontent', '0007_auto_20200118_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='generalsetting',
            name='footer_background_color',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='generalsetting',
            name='header_background_color',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
