# Generated by Django 3.2.16 on 2022-11-14 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('l_id', models.AutoField(db_column='l-id', primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('u_id', models.IntegerField()),
            ],
            options={
                'db_table': 'login',
                'managed': False,
            },
        ),
    ]
