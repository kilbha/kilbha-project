# Generated by Django 3.0.8 on 2020-09-06 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedarea', '0002_auto_20200905_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='questioninput',
            name='NCU',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='questioninput',
            name='YCU',
            field=models.TextField(default=''),
        ),
    ]
