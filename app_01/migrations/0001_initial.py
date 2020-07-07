# Generated by Django 3.0.7 on 2020-07-06 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Oaadmin',
            fields=[
                ('ldap', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'oaadmin',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Oaapprover',
            fields=[
                ('ldap', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('leave', models.CharField(blank=True, max_length=255, null=True)),
                ('dimission', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'oaapprover',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Oaexecutives',
            fields=[
                ('ldap', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'oaexecutives',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Oafinance',
            fields=[
                ('ldap', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'oafinance',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Oahr',
            fields=[
                ('ldap', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('company', models.CharField(blank=True, max_length=255, null=True)),
                ('exportstaff', models.CharField(blank=True, db_column='exportStaff', max_length=255, null=True)),
                ('confirmentry', models.CharField(blank=True, db_column='confirmEntry', max_length=255, null=True)),
                ('cancel_ack_leave_auth', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'oahr',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Oaother',
            fields=[
                ('ldap', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('qr_code_auth', models.CharField(blank=True, max_length=255, null=True)),
                ('password_auth', models.CharField(blank=True, max_length=255, null=True)),
                ('add_ldap_auth', models.CharField(blank=True, max_length=255, null=True)),
                ('cancel_ack_leave_auth', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'oaother',
                'managed': False,
            },
        ),
    ]
