# Generated by Django 3.0.8 on 2020-09-05 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedarea', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='questioninput',
            name='NCnt',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questioninput',
            name='YCnt',
            field=models.IntegerField(default=0),
        ),
    ]
