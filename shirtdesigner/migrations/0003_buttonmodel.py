# Generated by Django 2.2.2 on 2020-11-20 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shirtdesigner', '0002_backdetailsmodel_backdetailstypemodel_bottomcutmodel_bottomcuttypemodel_collarmodel_collartypemodel_'),
    ]

    operations = [
        migrations.CreateModel(
            name='ButtonModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('collorbtn', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='collarbtn', to='shirtdesigner.CollarTypeModel')),
                ('cuffbtn', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cuffbtn', to='shirtdesigner.CuffTypeModel')),
                ('placketbtn', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='placketbtn', to='shirtdesigner.PlacketTypeModel')),
            ],
        ),
    ]
