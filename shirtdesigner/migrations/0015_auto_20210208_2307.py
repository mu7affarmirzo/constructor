# Generated by Django 2.2.12 on 2021-02-08 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shirtdesigner', '0014_backobjmodel_backstylemodel_bottomobjmodel_bottomstylemodel_placketobjmodel_placketstylemodel_pocket'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sleevestylemodel',
            old_name='siluet_bar',
            new_name='sleeve_bar',
        ),
    ]
