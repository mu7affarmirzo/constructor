# Generated by Django 2.2.2 on 2020-12-29 04:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shirtdesigner', '0012_auto_20201229_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stylesidebarmodel',
            name='sub_side',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_side', to='shirtdesigner.SubSideBarModel'),
        ),
    ]
