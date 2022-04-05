# Generated by Django 3.1 on 2020-09-06 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0003_tutorial_course_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial',
            name='thumbnail',
            field=models.ImageField(default=1, upload_to='thumbnails/%Y/%m/%d/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='course_name',
            field=models.CharField(max_length=100),
        ),
    ]
