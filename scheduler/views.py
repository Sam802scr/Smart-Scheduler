from django.shortcuts import render, redirect
from .models import Event, Task, Schedule
from .scheduler_engine import schedule_tasks


def home(request):
    events = Event.objects.all()
    tasks = Task.objects.all()
    schedules = Schedule.objects.all()

    return render(request, 'home.html', {
        'events': events,
        'tasks': tasks,
        'schedules': schedules
    })


def add_event(request):
    if request.method == 'POST':
        title = request.POST['title']
        start = request.POST['start']
        end = request.POST['end']

        Event.objects.create(
            title=title,
            start_time=start,
            end_time=end
        )
        return redirect('home')

    return render(request, 'add_event.html')


def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        duration = request.POST['duration']
        deadline = request.POST['deadline']

        Task.objects.create(
            title=title,
            duration=duration,
            deadline=deadline
        )
        return redirect('home')

    return render(request, 'add_task.html')


def run_scheduler(request):
    schedule_tasks()
    return redirect('home')
