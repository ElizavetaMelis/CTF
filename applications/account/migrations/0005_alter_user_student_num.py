# Generated by Django 4.0.3 on 2022-04-10 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_user_student_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='student_num',
            field=models.IntegerField(default=0),
        ),
    ]