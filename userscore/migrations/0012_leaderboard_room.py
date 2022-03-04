# Generated by Django 3.2.9 on 2021-12-14 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userscore', '0011_alter_user_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='leaderboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userscore.room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userscore.user')),
            ],
        ),
    ]