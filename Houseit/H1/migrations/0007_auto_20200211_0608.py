# Generated by Django 3.0.3 on 2020-02-11 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('H1', '0006_auto_20200211_0603'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='s_email',
        ),
        migrations.AddField(
            model_name='flat',
            name='f_email',
            field=models.CharField(default='', max_length=100),
        ),
    ]