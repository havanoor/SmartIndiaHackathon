# Generated by Django 2.2.8 on 2020-02-05 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmers', '0006_dealer'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='Contact',
            field=models.CharField(default=0, max_length=13),
            preserve_default=False,
        ),
    ]