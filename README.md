# org-schedule-yeargen

**org-schedule-yeargen** is the tool which can make your manual work  
completely automated. If you use org as your main tool for daily scheduling and notes,  
you almost always write down your study or work schedule by hand, but thanks to this  
tool, it creates a schedule for the whole year, while alternating weeks of the schedule  
and doing so safely, without losing data in case the day has already been recorded.  
It creates files for the year with the schedule already recorded (convenient if  
you have a schedule for the entire academic year). The main convenience is to place  
your schedule in the agenda, which the program achieves using SCHEDULED:.  
This makes your tasks/subjects visible. (You can set up recursive agenda parsing  
so that it sees all tasks, deadlines, and schedules).

The program may be refined with a more user-friendly interface for beginners, but for now, it has been created in a hurry for immediate practical use.
  
## IMPORTANT  
  
Concretely this program works in my university's system.  
Our schedule changes every week (alternates). In odd weeks  
(starting 1st September) one schedule is in effect, and in even weeks, another.
  
In schedule file i said check README file **here**.  
My org_schedule, time_schedule and get_org_schedule are selected only for my  
personal university schedule. You can use this template to the change schedule  
for your requirments, but you should know what are you doing and how 
get_org_schedule works.  
My university schedule is alternates every week and
there are cases when only on N-weeks  and when N is even or not.  
Therefore  i made many crutches and some parts are difficult to understand.  
So i don't recommend using my code, but actually is good foundation  
if you will be as soon make changes for yourself.  
  
## Extra info

### Argument requirment:
- python org-yeargen.py **[PATH]** **[YEAR]**  
**YEAR** in [0, 9999]  
**PATH** any path.
> Sudo if you need to do it in the root directory.  

### Result path format to your files:  
- /your_path/2025/10_October/41W_10_11_Saturday_2025.org
  
## Example org format day schedule
```org
#+TITLE:2025-09-02 Tuesday
#+DATE: 2025-09-02
#+CATEGORY: daily

* Schedule
** 1. Thermodynamics [Lec]       1210
SCHEDULED: <2025-09-02 Tue 09:00>
** 2. Database Systems [Lab]     3134
SCHEDULED: <2025-09-02 Tue 10:30>
** 3. Database Systems [Lab]     3134
SCHEDULED: <2025-09-02 Tue 12:30>
** 4. Sociology [Sem]            3310
SCHEDULED: <2025-09-02 Tue 14:00>

* Deadline [/]
** ...

* Tasks [/]
** ...

* Events [/]
** ...

* Notes
** ...

```

