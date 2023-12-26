# Generated by Django 4.1.7 on 2023-08-09 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('description', models.TextField()),
                ('authname', models.CharField(max_length=15)),
                ('img', models.ImageField(blank=True, null=True, upload_to='blog')),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', models.CharField(max_length=10)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Internship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=60)),
                ('usn', models.CharField(max_length=60)),
                ('email', models.CharField(max_length=60)),
                ('college_name', models.CharField(max_length=100)),
                ('offer_status', models.CharField(max_length=60)),
                ('start_date', models.CharField(max_length=60)),
                ('end_date', models.CharField(max_length=60)),
                ('proj_report', models.CharField(max_length=60)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
