# Generated by Django 2.0.4 on 2018-04-28 11:56

from django.db import migrations, models
import helpers.files


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_userdocument'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=64)),
            ],
            options={
                'abstract': False,
                'ordering': ['-created'],
            },
        ),
        migrations.AlterField(
            model_name='userdocument',
            name='file',
            field=models.FileField(upload_to=helpers.files.upload_to_generic),
        ),
    ]
