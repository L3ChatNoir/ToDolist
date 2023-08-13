from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import *
from datetime import date, datetime
from django.db.models import F

def index(request):
    '''
        Return home page
    '''

    #Place all task in a list
    task_list = Task.objects.order_by(F('do'), F('deadline').asc(nulls_last=True))[:]
    template = loader.get_template('index.html')
    context = {
        'task_list' : task_list,
        'today' : date.today()
    }

    #return index templates with list of task
    return HttpResponse(template.render(context, request))

def create_task(request):
    '''
        Get new task information and create task
    '''
    if request.GET.get('name')!= None and request.GET.get('name')!='':
        if request.GET.get('deadtask') == '':
            Task(name=request.GET.get('name'), deadline=None).save()
        else: 
            try:
                Task(name= request.GET.get('name'), deadline= request.GET.get('deadtask', None)).save()
            except:
                pass
    return redirect('/')

def task_action(request):
    '''
         Delete or Update task according user
    '''
    if request.method == 'GET':
        #Delete task
        if request.GET.get('action') == 'delete':
            Task.objects.filter(idtask= request.GET.get('task_id')).delete()

        #Update task
        elif request.GET.get('action') == 'update':

            #take task with id
            task = Task.objects.get(idtask =  request.GET.get('task_id'))

            try:
                date = task.deadline.strftime('%Y-%m-%d')
            except:
                date = None

            #Go to /update to call update function
            context = {
                'task' : task,
                'date' : date,
            }
            template = loader.get_template('update.html')
            return HttpResponse(template.render(context, request))

        # if checkbox check or uncheck, change boolean
        elif request.GET.get('do') == 'check':
            Task.objects.filter(idtask= request.GET.get('task_id')).update(do= True)
        else:
            Task.objects.filter(idtask= request.GET.get('task_id')).update(do= False)

    #Go to home page
    return redirect('/')

def update(request):
    '''
        take new information and update task
    '''
    if request.method == 'GET':
        task = Task.objects.filter(idtask= request.GET.get('id'))
        if request.GET.get('name') != '':
            task.update(name= request.GET.get('name'))
            try:
                task.update(deadline= request.GET.get('deadtask'))
            except:
                task.update(deadline= None)
            
    return redirect('/')