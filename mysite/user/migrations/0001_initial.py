# Generated by Django 3.2.6 on 2021-08-29 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, verbose_name='사용자명')),
                ('useremail', models.EmailField(max_length=128, verbose_name='사용자이메일')),
                ('password', models.CharField(max_length=64, verbose_name='비밀번호')),
                ('registered_dttm', models.DateTimeField(auto_now_add=True, verbose_name='등록시간')),
            ],
            options={
                'verbose_name': '패스트캠퍼스 사용자',
                'verbose_name_plural': '패스트캠퍼스 사용자',
                'db_table': 'fastcampus_fcuser',
            },
        ),
    ]
