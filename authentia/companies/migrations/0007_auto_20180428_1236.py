# Generated by Django 2.0.4 on 2018-04-28 17:36

from django.db import migrations, models
import helpers.files


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0006_auto_20180428_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companydocument',
            name='file',
            field=models.FileField(upload_to=helpers.files.upload_to_generic),
        ),
    ]