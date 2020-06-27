# Generated by Django 2.1.5 on 2020-06-27 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LaptopData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('processor', models.CharField(max_length=100)),
                ('ram', models.IntegerField()),
                ('hard_drive_capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MobileData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('processor', models.CharField(max_length=100)),
                ('ram', models.IntegerField()),
                ('screen_size', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('description', models.TextField(max_length=500)),
                ('type', models.CharField(choices=[('Mobile', 'Mobile'), ('Laptop', 'Laptop')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserLogin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='mobiledata',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.Product'),
        ),
        migrations.AddField(
            model_name='laptopdata',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.Product'),
        ),
    ]