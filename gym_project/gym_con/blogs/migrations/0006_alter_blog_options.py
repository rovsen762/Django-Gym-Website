# Generated by Django 4.0.4 on 2022-05-17 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_alter_blog_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-date']},
        ),
    ]
