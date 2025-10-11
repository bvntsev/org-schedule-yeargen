import time
import datetime
import sys
import os
import calendar

NUMERATOR = 1
DENOMINATOR = 0


def ck_exist_path(path: str) -> bool:
    return os.path.exists(path)


def mk_dir(path: str):
    try:
        os.mkdir(path)
    except FileExistsError:
        print(f'LOG: path \"{path}\" already exist. Pass create argument')
    except FileNotFoundError:
        print(f'ERROR: Incorrect path to create dir ({path})')
        exit(-1)




if len(sys.argv) != 3:
    print("Incorrect argument.\'mk_year_org {path_to_dir} {year}\'")
    sys.exit(-1)


user_path = sys.argv[1]
user_path = user_path[:-1] if user_path[-1] == '/' else user_path
user_year = sys.argv[2]
user_year_i = int(user_year)


if not user_year.isdecimal() or \
    not (datetime.MINYEAR <= user_year_i <= datetime.MAXYEAR):
    print("Incorrect a year number {only decimal}")
    print(f'Correct year interval is [{datetime.MINYEAR}, {datetime.MAXYEAR}]')
    exit(-1)

path = f'{user_path}/{user_year}/'

'''
Example current day:
(f'{user_path}/{user_year}/%m_%B/{weekN}W_%d_%m_%A_{user_year}.org')
'''
print("======PATH======")
print(path)



months = dict({
    1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June",
    7: "July", 8: "August", 9: "September", 10: "October",
    11: "November", 12: "December"
})
day_names = dict({
    1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday",
    6: "Saturday", 7: "Sunday"
})

print("====MK_YEAR====")

if not ck_exist_path(path):
    print("LOG: Year folder isn't exist")
    mk_dir(path)
print("LOG: Year folder already exist")

# date_data = datetime.datetime(int(user_year))
# print(type(date_data))

first_study_day = datetime.datetime(user_year_i, 9, 1)


print("====MK_MONTHS====")
for iter_month in range(1, 12+1):
    curr_month = months[iter_month]

    # date_data.month = curr_month

    print(f'---{curr_month}')
    path_temp_month = path + \
        f'{(str(iter_month) if iter_month > 9 else '0' + str(iter_month))}' + \
        '_' + f'{curr_month}/'

    if not(ck_exist_path(path_temp_month)):
        print("LOG:", curr_month, "isn't exist, mk new dir")
        mk_dir(path_temp_month)
    print("LOG:", curr_month, "is already exist")

    for \
    iter_day in range(1, calendar.monthrange(user_year_i, iter_month)[1] + 1):

        curr_day = datetime.datetime(user_year_i, iter_month, iter_day)

        delta_week_fweek = (abs(first_study_day - curr_day)).days // 7 + 1

        ISO_week_n = datetime.date.\
        fromisoformat(curr_day.isoformat()[:curr_day.isoformat().find('T')]).\
        isocalendar().week
        
        path_temp_day = \
        path_temp_month + f'{ISO_week_n}W_{iter_day}_{iter_month}' + '_' +\
        f'{day_names[curr_day.isoweekday()]}.org'
        print(path_temp_day)
        continue
        if (not ck_exist_path):
            file = open()
        file = open()
    

# ~/sync/org/2025/10-October/41W-2025-10-11-Saturday.org -> old
# ~/sync/org/2025/10_October/41W_10_11_Saturday_2025.org -> new
