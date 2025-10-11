import datetime

NUMERATOR = 1
DENOMINATOR = 0

day_names = dict({
    1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday",
    6: "Saturday", 7: "Sunday"
})

# Your schedule, check README important
# This schedule is only an example
org_schedule = [
    # DENOMINATOR
    [
        # MONDAY
        '''** 0. Computer Networks [Lec]    4231
** 6. Modern Art [Sem]           3124
''',
        # TUESDAY
        '''** 1. Thermodynamics [Lec]       1342
** 2. Linear Programming [Sem]   4153
** 3. Creative Writing [Sem]     3011
** 4. Robotics [Lab]             4420
** 5. Philosophy of Mind [Lec]   4007
** 6. Mechanical Design [Cons]   3508
''',
        # WEDNESDAY
        '''** 1. Machine Learning [Sem]     3225
** 2. PE [Sem]                   5120
** 3. Quantum Physics [Sem]      3333
** 4. Data Structures [Lec]      1212
** 6. Programming in C [Cons]    3246
''',
        # THURSDAY
        '''** 1. Algorithms [Sem]           4113
** 2. Circuit Analysis [Lab]     3348
** 3. Neural Networks [Sem]      3107
** 4. Calculus [Lec]             1208
** 5. Ethics in AI [Cons]        3419
** 6. Digital Systems [Cons]     3264
** 6. Cybersecurity [Sem]        4117
''',
        # FRIDAY
        '''** 1. History of Science [Lec]   1221
** 2. PE [Sem]                   5108
** 3. Philosophy [Sem]           3213
''',
        # SATURDAY
        '''** 4. Programming in C [Cons]    4142
        ''',
        # SUNDAY
        '''** ...'''
    ],
    # NUMERATOR
    [
        # MONDAY
        '''** 0. Discrete Math [Cons]       3247
** 2. Database Systems [Lec]     1204
** 3. Embedded Systems [Sem]     4108
** 4. Cyber Law [Cons]           4208
** 6. Linguistics [Cons]         3330
''',
        # TUESDAY
        '''** 1. Thermodynamics [Lec]       1210
** 2. Database Systems [Lab]     3134
** 3. Database Systems [Lab]     3134
** 4. Sociology [Sem]            3310
''',
        # WEDNESDAY
        '''** 2. PE [Sem]                   5102
** 3. Statistics [Sem]           3341
** 4. Computer Graphics [Lec]    1205
** 5. Artificial Intelligence [Cons] 3218
** 6. Data Analysis [Cons]       3221
''',
        # THURSDAY
        '''** 2. Linear Algebra [Sem]       3235
** 3. Quantum Computing [Sem]    3312
** 4. Probability Theory [Lec]   1213
** 5. English [Sem]              3115
** 6. Machine Learning [Cons]    3245
''',
        # FRIDAY
        '''** 1. Ethics [Lec]               1207
** 2. PE [Sem]                   5111
** 3. Software Engineering [Lec] 1209
** 4. Web Development [Lec]      1211
''',
        # SATURDAY
        '''** 4. Data Science [Cons]        4110
        ''',
        # SUNDAY
        '''** ...
        '''
    ]
]

# Your a time schedule. Check README important
time_schedule = dict({ 
    0: "08:00",
    1: "09:00",
    2: "10:30",
    3: "12:00",
    4: "14:00",
    5: "15:30",
    6: "17:00",
    7: "18:30",
    8: "20:00"
})


# Function to write schedule to str. Check README important
def get_org_schedule(day: datetime.datetime, num_week: int):

    curr_schedule = org_schedule[num_week % 2][day.weekday()]

    if (day.isoweekday() == 4 and num_week % 2 == DENOMINATOR):
        match (num_week // 2 % 2):
            case 0:
                curr_schedule = curr_schedule[ :curr_schedule.rfind("** 6.")]
            case 1:
                curr_schedule = curr_schedule[curr_schedule.find("** 2.") : ]
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
