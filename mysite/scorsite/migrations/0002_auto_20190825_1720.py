# Generated by Django 2.2.4 on 2019-08-25 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scorsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postuserscore',
            name='UserName',
            field=models.CharField(default='xxxxxxxx', max_length=100),
        ),
        migrations.AlterField(
            model_name='postuserscore',
            name='FirstName',
            field=models.CharField(default='stanley', max_length=100),
        ),
        migrations.AlterField(
            model_name='postuserscore',
            name='LastName',
            field=models.CharField(default=' charlston', max_length=100),
        ),
        migrations.AlterField(
            model_name='postuserscore',
            name='Score',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
