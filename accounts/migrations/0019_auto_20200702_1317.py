# Generated by Django 2.2.9 on 2020-07-02 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_entry_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='name',
            new_name='Location_Name',
        ),
    ]
