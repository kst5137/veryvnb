# Generated by Django 4.0.4 on 2022-05-18 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_u_phonenum'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='u_sex',
            field=models.CharField(choices=[('F', '여자'), ('M', '남자'), ('U', '선택 안함')], max_length=10, null=True),
        ),
    ]
