# Generated by Django 5.0.3 on 2025-03-21 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_job'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.PositiveIntegerField()),
                ('qualification', models.CharField(max_length=200)),
                ('skill', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=30)),
                ('resume', models.FileField(upload_to='files,null=True')),
                ('experience', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], default='male', max_length=20)),
            ],
        ),
    ]
