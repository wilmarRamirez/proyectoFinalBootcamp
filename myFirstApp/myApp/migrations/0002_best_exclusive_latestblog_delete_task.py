# Generated by Django 4.2.1 on 2023-06-03 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Best',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciudad_pais', models.CharField(max_length=100)),
                ('url_imagen', models.CharField(max_length=100)),
                ('dia_prueba', models.CharField(max_length=100)),
                ('valor', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Exclusive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciudad', models.CharField(max_length=100)),
                ('pais', models.CharField(max_length=100)),
                ('url_imagen', models.CharField(max_length=100)),
                ('valor_anterior', models.CharField(max_length=100)),
                ('valor_actualizado', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='latestBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('fecha', models.CharField(max_length=100)),
                ('url_imagen', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
