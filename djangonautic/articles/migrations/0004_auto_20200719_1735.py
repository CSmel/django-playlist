# Generated by Django 3.0.8 on 2020-07-19 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20200719_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='thumb',
            field=models.ImageField(blank=True, default='defaults.gif', upload_to=''),
        ),
    ]
