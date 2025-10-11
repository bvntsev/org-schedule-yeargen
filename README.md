# org-schedule-yeargen


## IMPORTANT  
  
Concretely this program works in my university's system.  
Our schedule changes every week (alternates). In odd weeks  
(starting 1st September) one schedule is in effect, and in even weeks, another.
  
In schedule file i said check README file **here.**.  
My org_schedule, time_schedule and get_org_schedule are selected only for my  
personal university schedule. You can use this template to the change schedule  
for your requirments, but you should know what are you doing and how 
get_org_schedule works. My university schedule is alternates every week and 
there  are cases when only on N-weeks and when N is even or not. Therefore  
i made many crutches and some parts are difficult to understand.  
So i don't recommend using my code, but actually is good foundation  
if you will be as soon make changes for yourself.  
  
## Extra info

Argument requirment: python org-yeargen.py **path** **year**  
**year** in [0, 9999]  
Path format: 
- /your_path/2025/10_October/41W_10_11_Saturday_2025.org  
- ~/2025/10_October/41W_10_11_Saturday_2025.org  
- ../2025/10_October/41W_10_11_Saturday_2025.org  

