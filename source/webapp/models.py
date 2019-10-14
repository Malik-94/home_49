from django.db import models


class Task(models.Model):
    summary = models.CharField(max_length=200, null=False, blank=False, verbose_name='Заголовок')
    description = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Текст')
    status = models.ForeignKey('webapp.Status', related_name='task_status', on_delete=models.PROTECT , verbose_name='Статус')
    type = models.ForeignKey('webapp.Type' , related_name='task_type', on_delete=models.PROTECT , verbose_name='Тип')
    project = models.ForeignKey('webapp.Project', null=True, related_name='tasks', on_delete=models.PROTECT , verbose_name='Проект')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Время обновления')


    def __str__(self):
        return "{}. {}".format(self.pk, self.summary)


class Status(models.Model):
    statuses = models.CharField(max_length=20, verbose_name='Статус')
    def __str__(self):
        return self.statuses


class Type(models.Model):
    types = models.CharField(max_length=20, verbose_name='Тип')
    def __str__(self):
        return self.types


class Project (models.Model):
    summary = models.CharField(max_length=200, null=False, blank=False, verbose_name='Заголовок')
    description = models.TextField(max_length=400, null=True, blank=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Время обновления')