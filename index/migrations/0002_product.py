# Generated by Django 2.1.15 on 2020-06-26 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('quantity', models.FloatField(default=0.0)),
                ('price', models.FloatField(default=0.0)),
                ('unit', models.CharField(choices=[('gm', 'gm'), ('kg', 'kg'), ('liter', 'liter'), ('dozens', 'dozens'), ('unit', 'unit')], default='kg', max_length=20)),
                ('offer', models.BooleanField(default=False)),
                ('img', models.ImageField(upload_to='Product/')),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='index.ProductCatagory')),
            ],
        ),
    ]