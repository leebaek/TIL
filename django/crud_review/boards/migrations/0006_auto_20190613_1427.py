# Generated by Django 2.2.1 on 2019-06-13 14:27

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0005_auto_20190613_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(upload_to='boards/images'),
        ),
    ]
