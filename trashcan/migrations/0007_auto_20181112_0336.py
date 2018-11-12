# Generated by Django 2.1.2 on 2018-11-12 08:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trashcan', '0006_auto_20181112_0316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='harvest',
            name='trash_can',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='TrashCan', to='trashcan.TrashCan'),
        ),
        migrations.AlterField(
            model_name='harvest',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Level', to=settings.AUTH_USER_MODEL),
        ),
    ]
