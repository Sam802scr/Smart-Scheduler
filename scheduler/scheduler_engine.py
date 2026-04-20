from datetime import timedelta
from .models import Event, Task, Schedule


def get_free_slots(events):
    events = sorted(events, key=lambda x: x.start_time)
    free_slots = []

    for i in range(len(events) - 1):
        gap_start = events[i].end_time
        gap_end = events[i + 1].start_time

        if gap_start < gap_end:
            free_slots.append([gap_start, gap_end])

    return free_slots


def schedule_tasks():
    events = list(Event.objects.all())
    tasks = list(Task.objects.filter(scheduled=False))

    # Sort tasks by deadline (greedy)
    tasks.sort(key=lambda x: (x.deadline, -x.priority))

    free_slots = get_free_slots(events)

    for task in tasks:
        for slot in free_slots:
            start, end = slot
            available_minutes = (end - start).total_seconds() / 60

            if available_minutes >= task.duration and start < task.deadline:
                task_start = start
                task_end = start + timedelta(minutes=task.duration)

                # Save schedule
                Schedule.objects.create(
                    task=task,
                    start_time=task_start,
                    end_time=task_end
                )

                # Mark as scheduled
                task.scheduled = True
                task.save()

                # Update slot
                slot[0] = task_end
                break
