import datetime
from definitions import org_schedule, time_schedule
NUMERATOR = 1
DENOMINATOR = 0

day_names = dict({
    1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday",
    6: "Saturday", 7: "Sunday"
})

# Your schedule, check README important
# This schedule is only an example


# Function to write schedule to str. Check README important
def get_org_schedule(day: datetime.datetime, num_week: int):

    curr_schedule = org_schedule[num_week % 2][day.weekday()]

    if (day.isoweekday() == 4 and num_week % 2 == DENOMINATOR):
        if (num_week // 2 % 2 == 0):
            curr_schedule = curr_schedule[ :curr_schedule.rfind("** 5.")]
    ret_val = ""

    min_num_class = \
    min([int(x) for x in range(0, 10) if str(x)+'.' in curr_schedule] + [10])

    if min_num_class == 10: return curr_schedule

    for iter in range\
        (min_num_class, min_num_class + curr_schedule.count('\n')):
        
        ret_val += curr_schedule[:curr_schedule.find('\n')] + '\n'
        
        num_classes = int\
(''.join('0'+curr_schedule[curr_schedule.find('.')-1:curr_schedule.find('.')]))

        curr_schedule = curr_schedule[curr_schedule.find('\n') + 1:]

        schedule_status = \
        f'SCHEDULED: <{day.strftime("%Y-%m-%d")} ' + \
        f'{day_names[day.isoweekday()][:3]} ' + \
        f'{time_schedule[num_classes] if num_classes != 3 else \
        (time_schedule[num_classes] if day.isoweekday in [1, 5]\
        or (day.isoweekday() == 4 and num_week % 2 == 0) else "12:30")}>\n'

        ret_val += schedule_status

    return ret_val
