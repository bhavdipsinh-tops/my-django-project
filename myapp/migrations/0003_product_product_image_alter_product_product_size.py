# Generated by Django 4.1.7 on 2023-02-22 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default=1, upload_to='product_pic/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='product_size',
            field=models.TextField(choices=[('s', 's'), ('m', 'm'), ('l', 'l'), ('xl', 'xl'), ('xxl', 'xxl')], max_length=100),
        ),
    ]
