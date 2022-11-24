# Generated by Django 4.1.1 on 2022-09-06 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_branches_contacts_remove_courses_address_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacts',
            name='contacts',
        ),
        migrations.AddField(
            model_name='contacts',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='contacts', to='courses.courses'),
        ),
    ]
