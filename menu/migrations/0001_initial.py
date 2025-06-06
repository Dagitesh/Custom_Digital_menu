# Generated by Django 5.2.1 on 2025-05-27 18:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='logos/')),
                ('background_image', models.ImageField(upload_to='backgrounds/')),
                ('layout', models.CharField(choices=[('grid', 'Grid'), ('list', 'List')], default='grid', max_length=20)),
                ('font_family', models.CharField(choices=[('Arial', 'Arial'), ('Helvetica', 'Helvetica'), ('Georgia', 'Georgia'), ('Times New Roman', 'Times New Roman'), ('Courier New', 'Courier New'), ('Verdana', 'Verdana'), ('Poppins', 'Poppins'), ('Roboto', 'Roboto'), ('Lobster', 'Lobster'), ('Pacifico', 'Pacifico')], default='Roboto', max_length=100)),
                ('font_size', models.CharField(default='16px', max_length=10)),
                ('letter_spacing', models.CharField(default='0.5px', max_length=10)),
                ('line_height', models.CharField(default='1.6', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('menu_config', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='menu.menuconfig')),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image', models.ImageField(blank=True, upload_to='menu_items/')),
                ('position', models.PositiveIntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='menu.category')),
            ],
            options={
                'ordering': ['position'],
            },
        ),
    ]
