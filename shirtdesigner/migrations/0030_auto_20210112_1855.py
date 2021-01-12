# Generated by Django 2.2.2 on 2021-01-12 13:55

from django.db import migrations, models
import django.db.models.deletion
import shirtdesigner.models


class Migration(migrations.Migration):

    dependencies = [
        ('shirtdesigner', '0029_auto_20210112_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placketmodel',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='plackettype', to='shirtdesigner.SubSideBarModel'),
        ),
        migrations.CreateModel(
            name='PocketModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pocketname', models.CharField(blank=True, max_length=400, null=True)),
                ('pocket_img', models.ImageField(blank=True, null=True, upload_to=shirtdesigner.models.upload_location)),
                ('fabric', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pocket', to='shirtdesigner.FabricModel')),
                ('type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='plackettype', to='shirtdesigner.StyleSideBarModel')),
            ],
        ),
    ]