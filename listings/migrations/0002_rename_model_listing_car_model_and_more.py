# Generated by Django 4.1.3 on 2022-11-05 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='model',
            new_name='car_model',
        ),
        migrations.AlterField(
            model_name='listing',
            name='picture1',
            field=models.ImageField(blank=True, null=True, upload_to='pictures/%Y/%m/%d/'),
        ),
    ]
