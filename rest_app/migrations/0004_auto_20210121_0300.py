# Generated by Django 3.1.5 on 2021-01-20 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_app', '0003_auto_20210121_0249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='rating',
            field=models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default=5),
        ),
    ]
