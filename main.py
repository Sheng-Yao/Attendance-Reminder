import sys
from datetime import date
from plyer import notification

if __name__ == "__main__":
    today = date.today()
    workingDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    if (today.strftime('%A') in workingDays):
        notification.notify(
            title="Attendance Reminder",
            message="Check In / Resume in to TimeTec HR",
            app_name="reminder",
            timeout=60,
        )
    else:
        notification.notify(
            title="Rest Day Reminder",
            message="Is Rest Day !!!!",
            app_name="reminder",
            timeout=60,
        )
    sys.exit(0)
