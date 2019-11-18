# Generated by Django 2.1.1 on 2018-11-29 18:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(blank=True, max_length=30, null=True)),
                ('lastname', models.CharField(blank=True, max_length=25, null=True)),
                ('rollnumber', models.IntegerField(blank=True, null=True)),
                ('profileimage', models.ImageField(blank=True, null=True, upload_to='')),
                ('user', models.OneToOneField(on_delete='CASCADE', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('rollnumber',),
            },
        ),
    ]