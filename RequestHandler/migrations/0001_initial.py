# Generated by Django 2.2.3 on 2023-07-16 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('section', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=250)),
                ('type', models.CharField(max_length=30)),
                ('result', models.BooleanField()),
                ('code', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('department', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone_number', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('section', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=250)),
                ('type', models.CharField(max_length=30)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('price', models.IntegerField()),
                ('code', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.DateField(max_length=30)),
                ('treatment_prescribed', models.BooleanField()),
                ('diagnosis', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='RequestHandler.Diagnosis')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RequestHandler.Doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RequestHandler.Patient')),
                ('treatment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='RequestHandler.Treatment')),
            ],
        ),
    ]
