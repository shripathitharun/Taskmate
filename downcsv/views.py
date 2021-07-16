from django.shortcuts import render,redirect
from django.http import HttpResponse
import csv
from todolist_app.models import TaskList
from django.contrib.auth.models import User
# Create your views here.

def download_tasks(request):
     response = HttpResponse(content_type='text/csv')
     response['Content-Disposition'] = 'attachment; filename=tasks.csv'
     csv_writer=csv.writer(response)
     csv_writer.writerow(['Task Name','Done'])
     if 'query' in request.GET:
         search=request.GET['query']
         all_tasks=TaskList.objects.filter(task__icontains=search)
     else:
         all_tasks = TaskList.objects.filter(manage=request.user)
     for obj in all_tasks:
         csv_writer.writerow([obj.task,obj.done])
     return response
