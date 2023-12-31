# Generated by Django 2.2.3 on 2023-07-22 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RequestHandler', '0009_doctor_license_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='image',
            field=models.ImageField(default='pat1.png', upload_to='patients'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='image',
            field=models.ImageField(default='doc1.png', upload_to='doctors'),
        ),
    ]
