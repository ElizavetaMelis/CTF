# Generated by Django 4.0.3 on 2022-04-10 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_profile_point_user_student_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='student_num',
            field=models.IntegerField(default=0, max_length=15),
        ),
    ]
