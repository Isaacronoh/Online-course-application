# Generated by Django 5.1.3 on 2024-12-03 07:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineapp', '0012_rename_year_of_admission_application_year_of_admission'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Finance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_billed', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('total_paid', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]