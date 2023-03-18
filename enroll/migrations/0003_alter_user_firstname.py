# Generated by Django 3.2.16 on 2023-02-25 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0002_user_firstname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='firstname',
            field=models.CharField(choices=[('red', 'Red'), ('green', 'Green'), ('blue', 'Blue')], max_length=5),
        ),
    ]
