# Generated by Django 4.0.4 on 2022-05-07 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(),
        ),
    ]
