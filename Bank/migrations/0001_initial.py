# Generated by Django 2.2.8 on 2020-02-05 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('farmers', '0009_bankexecutive'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amt', models.PositiveIntegerField()),
                ('Rate', models.FloatField()),
                ('Year', models.PositiveIntegerField()),
                ('Publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmers.BankExecutive')),
            ],
        ),
        migrations.CreateModel(
            name='LoanIssue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Approved_Bank', models.BooleanField()),
                ('Approved_Farmer', models.BooleanField()),
                ('Issued_To', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmers.Farmer')),
                ('Issuer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmers.BankExecutive')),
                ('Loan_Ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bank.Loan')),
            ],
        ),
    ]
