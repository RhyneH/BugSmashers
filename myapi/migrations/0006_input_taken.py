# Generated by Django 4.0.4 on 2022-05-05 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0005_rename_insulin_in_units_input_blood_sugar'),
    ]

    operations = [
        migrations.AddField(
            model_name='input',
            name='taken',
            field=models.BooleanField(default=False),
        ),
    ]