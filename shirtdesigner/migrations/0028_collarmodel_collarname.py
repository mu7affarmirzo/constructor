# Generated by Django 2.2.2 on 2021-01-12 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shirtdesigner', '0027_remove_collarmodel_typename'),
    ]

    operations = [
        migrations.AddField(
            model_name='collarmodel',
            name='collarname',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]