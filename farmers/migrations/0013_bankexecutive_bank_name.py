# Generated by Django 2.2.8 on 2020-02-06 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmers', '0012_farmer_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankexecutive',
            name='Bank_Name',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
