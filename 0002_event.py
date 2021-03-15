# Generated by Django 2.2.16 on 2021-03-15 05:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Eventname', models.CharField(max_length=250)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='')),
                ('category', models.CharField(max_length=250)),
                ('body', models.TextField()),
                ('venue', models.CharField(max_length=250)),
                ('DateAndTime', models.DateTimeField()),
                ('TotalAvailableSeats', models.IntegerField()),
                ('Name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]