# Generated by Django 3.1.3 on 2021-07-24 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0008_auto_20210724_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='neighbourhood',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hood.neighbourhood'),
        ),
    ]