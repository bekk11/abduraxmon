# Generated by Django 3.2.15 on 2022-10-12 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authors', '0001_initial'),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Book Name')),
                ('description', models.TextField(verbose_name='Book Description')),
                ('file', models.FileField(upload_to='files/books/%Y/%m/%d', verbose_name='File of this Book')),
                ('image', models.ImageField(upload_to='files/images/%Y/%m/%d', verbose_name='Image of this Book')),
                ('video', models.FileField(blank=True, null=True, upload_to='files/videos/%Y/%m/%d', verbose_name='Video of this Book')),
                ('year', models.IntegerField(verbose_name='Year of Publication of the Book')),
                ('language', models.CharField(choices=[('EN', 'English'), ('UZ', 'Uzbek'), ('RU', 'Russian')], max_length=7, verbose_name='Language od Book')),
                ('size', models.FloatField(blank=True, null=True, verbose_name='Book Size (DO NOT WRITE)')),
                ('size_type', models.CharField(blank=True, max_length=10, null=True, verbose_name='Type of Book Size (DO NOT WRITE)')),
                ('file_type', models.CharField(blank=True, max_length=20, null=True, verbose_name='Type of Book File (DO NOT WRITE)')),
                ('rate', models.IntegerField(blank=True, null=True, verbose_name='Rate. (DO NOT WRITE)')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='Last Update')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='authors.author', verbose_name='Book Author')),
                ('category', models.ManyToManyField(related_name='category', to='categories.Category', verbose_name='Book Category')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]
