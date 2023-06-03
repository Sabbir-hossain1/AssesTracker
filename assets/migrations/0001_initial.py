# Generated by Django 4.2.1 on 2023-06-03 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.company')),
            ],
        ),
        migrations.CreateModel(
            name='DeviceAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assign_date', models.DateField()),
                ('return_date', models.DateField(blank=True, null=True)),
                ('assigned_for_years', models.PositiveIntegerField(default=0)),
                ('assigned_for_months', models.PositiveIntegerField(default=0)),
                ('assigned_for_days', models.PositiveIntegerField(default=0)),
                ('device_condition_when_assigned', models.CharField(max_length=100)),
                ('device_condition_when_returned', models.CharField(blank=True, max_length=100, null=True)),
                ('assign_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='device_assignment_to_employee', to='employee.employee')),
                ('devices', models.ManyToManyField(related_name='device_assignment_employee', to='assets.device')),
            ],
        ),
    ]
