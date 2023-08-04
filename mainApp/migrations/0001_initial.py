# Generated by Django 4.2.1 on 2023-07-28 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(choices=[(1, 'Active'), (2, 'Done')], default=1)),
            ],
        ),
    ]
