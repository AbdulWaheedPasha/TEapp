# Generated by Django 3.2.6 on 2021-08-29 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_image',
            field=models.ImageField(blank=True, help_text='Best Image Resolution width: 580 x Height: 565', null=True, upload_to='images/event/thumbnail/'),
        ),
        migrations.AlterField(
            model_name='eventimages',
            name='images',
            field=models.ImageField(blank=True, help_text='Best Image Resolution width: 1280 x Height: 720', null=True, upload_to='images/event/banner/'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='person_image',
            field=models.ImageField(blank=True, help_text='Best Image Resolution width: 640 x Height: 825', null=True, upload_to='images/staff/'),
        ),
    ]