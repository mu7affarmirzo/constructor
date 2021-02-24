# Generated by Django 2.2.2 on 2021-02-24 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shirtdesigner', '0020_auto_20210224_2142'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomShirt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('back_style', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shirtdesigner.BackStyleModel')),
                ('bottom_style', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shirtdesigner.BottomStyleModel')),
                ('collar_band_buttons', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shirtdesigner.CollarBandBtntModel')),
                ('collar_band_height', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shirtdesigner.CollarBandHeightModel')),
                ('collar_stiffness', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shirtdesigner.CollarStiffnessModel')),
                ('collar_style', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shirtdesigner.CollarStyleModel')),
                ('cuff_buttons', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shirtdesigner.CuffBtntModel')),
                ('cuff_stiffness', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shirtdesigner.CuffStiffnessModel')),
                ('cuff_style', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shirtdesigner.CuffStyleModel')),
                ('fabric', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shirtdesigner.FabricModel')),
                ('front_style', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shirtdesigner.PlacketStyleModel')),
                ('pocket_style', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shirtdesigner.PocketStyleModel')),
                ('shoulders', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shirtdesigner.ShouldersStyleModel')),
                ('silhouette', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shirtdesigner.SiluetStyleModel')),
                ('sleeve_style', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shirtdesigner.SleeveStyleModel')),
                ('yoke_style', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shirtdesigner.YokeStyleModel')),
            ],
        ),
    ]