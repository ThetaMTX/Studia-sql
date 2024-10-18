# Generated by Django 5.1.1 on 2024-10-18 11:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0004_alter_examination_date_alter_examination_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='examination',
            old_name='image',
            new_name='images',
        ),
        migrations.AlterField(
            model_name='examination',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='examination',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='examinations', to='patients.patient'),
        ),
    ]
