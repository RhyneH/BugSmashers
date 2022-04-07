from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='input',
            old_name='carbs',
            new_name='carbs_in_grams',
        ),
        migrations.RenameField(
            model_name='input',
            old_name='insulin',
            new_name='insulin_in_units',
        ),
    ]
