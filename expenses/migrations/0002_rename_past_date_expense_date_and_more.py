# Generated by Django 4.1.7 on 2023-03-14 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='past_date',
            new_name='date',
        ),
        migrations.RemoveField(
            model_name='expense',
            name='future_date',
        ),
        migrations.AlterField(
            model_name='expense',
            name='description',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]