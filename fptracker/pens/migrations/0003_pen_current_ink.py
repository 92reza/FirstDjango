# Generated by Django 2.1.7 on 2020-03-02 01:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pens', '0002_ink'),
    ]

    operations = [
        migrations.AddField(
            model_name='pen',
            name='current_ink',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pens.Ink'),
        ),
    ]