# Generated by Django 3.0.6 on 2020-05-26 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('routine', '0004_routineinstruction_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routineinstruction',
            name='routine',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='routine.Routine', verbose_name='routine'),
        ),
    ]
