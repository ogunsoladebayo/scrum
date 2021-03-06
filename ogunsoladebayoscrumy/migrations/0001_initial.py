# Generated by Django 3.1 on 2020-09-03 02:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GoalStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ScrumyGoals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal_name', models.CharField(max_length=255)),
                ('goal_id', models.IntegerField(max_length=18, unique=True)),
                ('created_by', models.CharField(max_length=255)),
                ('moved_by', models.CharField(max_length=255)),
                ('owner', models.CharField(max_length=255)),
                ('goal_status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ogunsoladebayoscrumy.goalstatus')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ScrumyHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moved_by', models.CharField(max_length=255)),
                ('created_by', models.CharField(max_length=255)),
                ('moved_from', models.CharField(max_length=255)),
                ('moved_to', models.CharField(max_length=255)),
                ('time_of_action', models.DateTimeField()),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ogunsoladebayoscrumy.scrumygoals')),
            ],
        ),
    ]
