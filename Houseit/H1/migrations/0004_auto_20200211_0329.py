# Generated by Django 3.0.3 on 2020-02-10 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('H1', '0003_auto_20200211_0241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='b_pass',
            field=models.CharField(max_length=110),
        ),
        migrations.AlterField(
            model_name='seller',
            name='s_pass',
            field=models.CharField(max_length=110),
        ),
    ]