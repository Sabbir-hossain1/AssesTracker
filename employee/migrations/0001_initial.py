# Generated by Django 4.2.1 on 2023-06-03 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('date_of_birth', models.DateField()),
                ('department', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('joining_dae', models.DateField()),
                ('phone_number', models.CharField(max_length=20)),
                ('emergency_phone_number', models.CharField(max_length=20)),
                ('photo', models.ImageField(upload_to='employee_img/')),
                ('branch_name', models.CharField(max_length=50)),
                ('bank_account_name', models.CharField(max_length=30)),
                ('bank_account_no', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_company', to='companies.company')),
            ],
        ),
    ]