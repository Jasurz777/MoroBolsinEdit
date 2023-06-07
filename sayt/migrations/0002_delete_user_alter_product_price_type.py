# Generated by Django 4.1.7 on 2023-02-15 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sayt', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AlterField(
            model_name='product',
            name='price_type',
            field=models.CharField(choices=[('sum', 'sum'), ('$', '$'), ('₽', '₽')], max_length=5),
        ),
    ]
