# Generated by Django 4.0.4 on 2022-05-03 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('bio', models.CharField(max_length=510)),
                ('rating', models.PositiveIntegerField()),
                ('image', models.ImageField(default="default_pic.img", upload_to='profile_pics')),
            ],
        ),
    ]
