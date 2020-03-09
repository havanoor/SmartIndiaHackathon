# Generated by Django 2.2.8 on 2020-02-06 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farmers', '0009_bankexecutive'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(blank=None, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dname', models.CharField(blank=None, max_length=100)),
                ('ph', models.FloatField()),
                ('N', models.FloatField()),
                ('P', models.FloatField()),
                ('K', models.FloatField()),
                ('OC', models.FloatField()),
                ('Fe', models.FloatField()),
                ('sref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmers.State')),
            ],
        ),
        migrations.CreateModel(
            name='CropStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ph', models.ImageField(upload_to='')),
                ('N', models.ImageField(upload_to='')),
                ('P', models.ImageField(upload_to='')),
                ('K', models.ImageField(upload_to='')),
                ('OC', models.ImageField(upload_to='')),
                ('Fe', models.ImageField(upload_to='')),
                ('dref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmers.District')),
            ],
        ),
        migrations.AddField(
            model_name='farmer',
            name='fdis',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='farmers.District'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='farmer',
            name='fstate',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='farmers.State'),
            preserve_default=False,
        ),
    ]
