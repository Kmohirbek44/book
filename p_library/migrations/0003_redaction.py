# Generated by Django 2.2.6 on 2019-11-06 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0002_auto_20191028_1332'),
    ]

    operations = [
        migrations.CreateModel(
            name='Redaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
    ]
