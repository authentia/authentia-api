# Generated by Django 2.0.4 on 2018-04-28 11:37

from django.db import migrations, models
import helpers.files


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_auto_20180428_0619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companydocument',
            name='file',
            field=models.FileField(upload_to=helpers.files.upload_to_generic),
        ),
    ]
