# Generated by Django 4.1.4 on 2022-12-15 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=10)),
                ('lastname', models.CharField(max_length=10)),
                ('username', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=15)),
                ('cpassword', models.CharField(max_length=15)),
                ('mailid', models.EmailField(max_length=254)),
                ('mobno', models.IntegerField()),
            ],
        ),
    ]