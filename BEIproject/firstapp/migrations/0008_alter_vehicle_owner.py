# Generated by Django 3.2.5 on 2022-02-04 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0007_auto_20220204_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='firstapp.dealer'),
        ),
    ]
