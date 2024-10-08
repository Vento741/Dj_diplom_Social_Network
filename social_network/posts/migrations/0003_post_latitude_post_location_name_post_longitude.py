# Generated by Django 5.0.2 on 2024-08-16 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_remove_post_image_postimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='location_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
