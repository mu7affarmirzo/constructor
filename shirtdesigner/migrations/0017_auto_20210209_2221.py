# Generated by Django 2.2.2 on 2021-02-09 17:21

from django.db import migrations, models
import django.db.models.deletion
import shirtdesigner.models


class Migration(migrations.Migration):

    dependencies = [
        ('shirtdesigner', '0016_stylemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='StyleSideBarModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(blank=True, null=True, upload_to=shirtdesigner.models.upload_location)),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('url', models.CharField(blank=True, max_length=250, null=True)),
                ('sub_stat', models.BooleanField(blank=True, default=False, null=True)),
                ('search_url', models.CharField(blank=True, max_length=250, null=True)),
                ('search_stat', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubSideBarModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(blank=True, null=True, upload_to=shirtdesigner.models.upload_location)),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('url', models.CharField(blank=True, max_length=250, null=True)),
                ('sub_stat', models.BooleanField(blank=True, default=False, null=True)),
                ('search_url', models.URLField(blank=True, null=True)),
                ('search_stat', models.BooleanField(blank=True, default=False, null=True)),
                ('global_menu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_bar', to='shirtdesigner.SideBarModel')),
            ],
        ),
        migrations.DeleteModel(
            name='CollarObjModel',
        ),
        migrations.AddField(
            model_name='stylesidebarmodel',
            name='sub_side',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shirtdesigner.SubSideBarModel'),
        ),
    ]