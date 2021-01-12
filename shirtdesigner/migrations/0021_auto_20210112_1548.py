# Generated by Django 2.2.2 on 2021-01-12 10:48

from django.db import migrations, models
import django.db.models.deletion
import shirtdesigner.models


class Migration(migrations.Migration):

    dependencies = [
        ('shirtdesigner', '0020_auto_20210112_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='bottomcutmodel',
            name='bottomcut_img',
            field=models.ImageField(blank=True, null=True, upload_to=shirtdesigner.models.upload_location),
        ),
        migrations.AlterField(
            model_name='bottomcutmodel',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bottomtype', to='shirtdesigner.SubSideBarModel'),
        ),
    ]