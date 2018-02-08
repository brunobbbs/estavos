from mezzanine.pages.page_processors import processor_for
from .models import Club

def _get_schedules(schedules):
    result = []
    for schedule in schedules:
        result.append({
            'start': schedule.start_time,
            'end': schedule.end_time,
        })
    return result


@processor_for(Club)
def classes(request, page):
    classes = page.club.classes.all()
    result = []
    for clas in classes:
        result.append({
            'name': clas.name,
            'weekday': clas.weekday,
            'schedules': _get_schedules(clas.schedules.all()),
        })
    return {'classes': result}
