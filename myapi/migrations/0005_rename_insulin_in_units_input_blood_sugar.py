# Generated by Django 4.0.4 on 2022-05-03 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0004_alter_input_carbs_in_grams_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='input',
            old_name='insulin_in_units',
            new_name='blood_sugar',
        ),
    ]
