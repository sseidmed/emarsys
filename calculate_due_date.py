from datetime import datetime, timedelta, time

def calculate_due_date(submission_date, turnaround):
    """
    :param submission_time: Date and time when the issue was submitted
    :type submission_time: str
    :param turnaround: The turnaround time is defined in working hours (e.g. 2 days are equal to 16 hours)
    :type turnaround: int
    :return: The date/time when the issue is resolved
    :rtype: datetime object
    """
    
    # Validate input
    try:
        submission_date = datetime.strptime(submission_date, "%m/%d/%Y %H:%M")
    except ValueError:
        return "Please enter a proper date and time"
    
    if not isinstance(turnaround, int):
        return "Turnaround time must be a number"
    
    submission_time = submission_date.time()
    
    if submission_time < time(9, 0, 0) or submission_time > time(17, 0, 0):
        return "Please submit between the hours of 9am and 5pm"
    
    end_time = datetime.strptime("5:00pm", "%I:%M%p").time()
    
    while turnaround > 0:
        hours_remaining_for_today = end_time.hour - submission_date.time().hour
        minute = submission_date.time().minute
        day_of_week = submission_date.weekday()

        if day_of_week in [5, 6]:
            days_to_skip = calculate_days_to_skip(day_of_week)
            submission_date += timedelta(days=days_to_skip)
            submission_date = datetime.combine(
                submission_date.date(), time(9, minute, 0)
            )
        
        if turnaround > hours_remaining_for_today:
            submission_date += timedelta(hours=hours_remaining_for_today)
            turnaround -= hours_remaining_for_today
            submission_date += timedelta(days=1)
            submission_date = datetime.combine(
                submission_date.date(), time(9, minute, 0)
            )
        else:
            submission_date += timedelta(hours=turnaround)
            break

    return submission_date


def calculate_days_to_skip(day_of_week):
    """
    :param day_of_week: A number that is either 5 or 6, signifies Saturday or Sunday
    :type day_of_week: int
    :return: A number 1 or 2 and it will be added to move us to the next week
    :rtype: int
    """
    if day_of_week == 5:
        return 2
    if day_of_week == 6:
        return 1


result = calculate_due_date("08/18/2023 14:12", 16)

if isinstance(result, datetime):
    print("Due date for this issue is: ", result)  # Should return: 08/22/2023 14:12pm
else:
    print(result)