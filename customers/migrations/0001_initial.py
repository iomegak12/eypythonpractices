# Generated by Django 2.0.4 on 2018-04-26 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerId', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('credit', models.IntegerField()),
                ('status', models.BooleanField()),
                ('joinedDate', models.DateTimeField()),
            ],
        ),
    ]
