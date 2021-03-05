# Generated by Django 3.1.7 on 2021-02-24 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrapp', '0006_auto_20210224_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Enter Salary', max_digits=14, null=True),
        ),
    ]