import datetime
import schedule

day_names = dict({
    1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday",
    6: "Saturday", 7: "Sunday"
})


def get_org_template_from_date(day: datetime.datetime, date_format) -> str:
    org_template = "#+TITLE:" \
        + f'{day.strftime(str(day_names[day.isoweekday()]))}\n'\
        + f'#+DATE: {day.strftime(date_format)}\n'\
        + "#+CATEGORY: daily\n\n" + "* Schedule [0/0]\n** ... \n"
    org_template += '''
* Deadline [0/0]
** ...\n
* Tasks [0/0]
** ...\n
* Events [0/0]
** ...\n
* Notes
** ...
'''
    return org_template
