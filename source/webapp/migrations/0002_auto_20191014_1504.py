# Generated by Django 2.2 on 2019-10-14 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('description', models.TextField(blank=True, max_length=400, null=True, verbose_name='Описание')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('update_at', models.DateTimeField(auto_now_add=True, verbose_name='Время обновления')),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tasks', to='webapp.Project', verbose_name='Проект'),
        ),
    ]