# Generated by Django 4.0.4 on 2022-05-05 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='condition',
            field=models.CharField(default='good', max_length=255),
            preserve_default=False,
        ),
    ]
