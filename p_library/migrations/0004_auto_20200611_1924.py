# Generated by Django 3.0.7 on 2020-06-11 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0003_auto_20200611_1916'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='publisher',
            new_name='redactor',
        ),
    ]
