# Generated by Django 4.0.4 on 2022-07-25 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentinfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('father_name', models.CharField(max_length=150)),
                ('mother_name', models.CharField(max_length=150)),
                ('mobile_number', models.IntegerField()),
                ('date_of_birth', models.DateField()),
                ('blood_group', models.CharField(max_length=10)),
                ('result', models.CharField(max_length=10)),
                ('address', models.TextField()),
                ('roll', models.IntegerField()),
                ('class_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Eight',
        ),
        migrations.DeleteModel(
            name='Nine',
        ),
        migrations.DeleteModel(
            name='Seven',
        ),
        migrations.DeleteModel(
            name='Six',
        ),
        migrations.DeleteModel(
            name='Ten',
        ),
    ]
