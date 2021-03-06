# Generated by Django 3.2.12 on 2022-04-04 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patchistiks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='effect',
            name='make',
        ),
        migrations.AddField(
            model_name='effect',
            name='effectMake',
            field=models.ManyToManyField(through='patchistiks.Make', to='patchistiks.Items'),
        ),
        migrations.AddField(
            model_name='make',
            name='makeEffect',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='patchistiks.effect'),
        ),
        migrations.AddField(
            model_name='make',
            name='makeItems',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='patchistiks.items'),
        ),
        migrations.AlterField(
            model_name='effect',
            name='effectText',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
