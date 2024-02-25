# Amir Abu Hani
schedular = {"sunday": {8: "", 9: "", 10: "mentoring", 11: "mentoring", 12: "", 13: "", 14: "", 15: ""},
             "monday": {8: "", 9: "", 10: "babysitter", 11: "", 12: "", 13: "", 14: "", 15: ""},
             "tuesday": {8: "", 9: "", 10: "", 11: "", 12: "", 13: "", 14: "", 15: ""},
             "wednesday": {8: "programming", 9: "programming", 10: "programming", 11: "", 12: "", 13: "", 14: "",
                           15: ""},
             "thursday": {8: "", 9: "", 10: "", 11: "", 12: "", 13: "", 14: "", 15: ""}
             }


def check_populated(day, time, duration):
    day_schedule = schedular[day]
    for i in range(time, time + duration):
        if day_schedule.get(i) != "":
            print(f"Sorry! In this time the {day_schedule.get(i)} task is populated there. ")
            return False
    return True


def set_task(day, time, duration, task):
    day_schedule = schedular[day]
    for i in range(time, time + duration):
        day_schedule[i] = task


def check_range_availability(schedule, duration):
    for day_schedule in schedule.values():
        empty_spots = 0
        for time, spot in day_schedule.items():
            if spot == "":
                empty_spots += 1
                if empty_spots >= duration:
                    for i in range(time - duration + 1, time + 1):
                        day_schedule[i] = task_name
                    return True

            else:
                empty_spots = 0
    return False


def print_schedule(schedule):
    for day, day_schedule in schedule.items():
        print(day + ":")
        for time, task in day_schedule.items():
            print(f"  {time}: {task}")


add_tasking = True
while add_tasking:
    task_name = input("Enter your task name: ")
    task_duration = int(input("Enter your task duration in hours please:"))
    specific_timeday_check = input("Are you want to add your task in specific day and starting hour? yes or no: ")
    # if the user give specific day and starting hour
    if specific_timeday_check == "yes":
        is_continue = True
        while is_continue:
            specific_day = input("Enter your favorite day: ")
            specific_time = int(input("Enter your starting hour: "))
            populated_or_not = check_populated(specific_day, specific_time, task_duration)
            if populated_or_not:
                set_task(day=specific_day, time=specific_time, duration=task_duration, task=task_name)
                print(
                    f"Your {task_name} task is scheduled to {specific_day} at {specific_time} clock for {task_duration} hours ")
                another_task = input("Would you like to add another task? yes or no ")
                if another_task == "no":
                    add_tasking = False
                is_continue = False
            else:
                # which_task = schedular[specific_day][specific_time]
                # print(f"Sorry! In this time the {which_task} task is populated there. ")
                user_choise = input("1- overwrite the old task with the new task \n2- give new time for the new task\n")
                if user_choise == "1":
                    set_task(day=specific_day, time=specific_time, duration=task_duration, task=task_name)
                    another_task = input("Would you like to add another task? yes or no ")
                    if another_task == "no":
                        add_tasking = False
                    is_continue = False
    # if the user not give specific day and starting time
    else:
        succeeded = check_range_availability(schedular, task_duration)
        if succeeded:
            print(f"Your {task_name} task populated successfully!")
            another_task = input("Would you like to add another task? yes or no ")
            if another_task == "no":
                add_tasking = False
        else:
            print("You cant add tasks. your schedular is full!")


print("Here is your schedular:")
print_schedule(schedular)
