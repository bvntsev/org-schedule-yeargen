import datetime
import sys
import os
import calendar
import schedule

def get_org_template(day: datetime.datetime, stage) -> str:
    match stage:
        case 1:
            org_template = "#+TITLE:" \
            + f'{day.strftime(f'%Y-%m-%d {day_names[day.isoweekday()]}')}\n'\
            + f'#+DATE: {day.strftime("%Y-%m-%d")}\n' + "#+CATEGORY: daily\n\n"\
            + "* Schedule\n"
        case 2:
            org_template = '''
* Deadline [/]
** ...\n
* Tasks [/]
** ...\n
* Events [/]
** ...\n
* Notes
** ...
'''
    return org_template


def get_day_content(day: datetime.datetime, num_week) -> str:
    org_content = get_org_template(day, 1)
    org_content += schedule.get_org_schedule(day, num_week)
    org_content += get_org_template(day, 2)

    return org_content
