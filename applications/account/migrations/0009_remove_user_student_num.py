# Generated by Django 4.0.3 on 2022-04-11 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_alter_user_student_num'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='student_num',
        ),
    ]