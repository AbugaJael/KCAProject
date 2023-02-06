# Generated by Django 3.2.6 on 2022-03-24 12:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0005_auto_20220324_0000'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=200)),
                ('owner_email', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('bsn_location', models.CharField(max_length=200)),
                ('bsn_type', models.CharField(max_length=200)),
                ('phone_number', models.CharField(blank=True, max_length=10, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
