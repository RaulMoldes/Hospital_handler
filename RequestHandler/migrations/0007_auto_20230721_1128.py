# Generated by Django 2.2.3 on 2023-07-21 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RequestHandler', '0006_visit_hp_uuid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='doc_uuid',
            new_name='doctor',
        ),
        migrations.RemoveField(
            model_name='visit',
            name='treatment_prescribed',
        ),
        migrations.AddField(
            model_name='diagnosis',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='RequestHandler.Doctor'),
        ),
        migrations.AddField(
            model_name='diagnosis',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='RequestHandler.Patient'),
        ),
        migrations.AddField(
            model_name='treatment',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='RequestHandler.Doctor'),
        ),
        migrations.AddField(
            model_name='treatment',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='RequestHandler.Patient'),
        ),
        migrations.AlterField(
            model_name='visit',
            name='diagnosis',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='RequestHandler.Diagnosis'),
        ),
        migrations.AlterField(
            model_name='visit',
            name='treatment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='RequestHandler.Treatment'),
        ),
    ]
