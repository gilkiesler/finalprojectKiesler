# Generated by Django 3.1.7 on 2021-04-25 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coursedetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseid', models.IntegerField()),
                ('coursetitle', models.CharField(max_length=500)),
                ('coursename', models.TextField()),
                ('coursesection', models.IntegerField()),
                ('coursedepartment', models.TextField()),
                ('courseinstructor', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Studentdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentid', models.IntegerField()),
                ('firstname', models.CharField(max_length=500)),
                ('lastname', models.CharField(max_length=500)),
                ('studentmajor', models.CharField(max_length=500)),
                ('studentyear', models.CharField(max_length=500)),
                ('studentgpa', models.DecimalField(decimal_places=2, default=None, max_digits=3)),
            ],
        ),
    ]
