# Generated by Django 5.0.7 on 2024-08-12 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_userprofile_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=''),
        ),
    ]
