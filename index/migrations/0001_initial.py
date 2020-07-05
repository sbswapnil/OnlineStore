# Generated by Django 2.1.15 on 2020-06-26 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCatagory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20, unique=True)),
                ('department', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='index.Department')),
            ],
            options={
                'ordering': ('category',),
            },
        ),
    ]