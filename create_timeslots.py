import datetime
from blog.models import TimeSlot

# Create a range of dates and time slots
start_date = datetime.date(2024, 7, 14)
end_date = datetime.date(2024, 12, 31)
start_time = datetime.time(11, 0)
end_time = datetime.time(21, 0)
delta = datetime.timedelta(days=1)

while start_date <= end_date:
    TimeSlot.objects.create(date=start_date, start_time=start_time, end_time=end_time, available=True)
    start_date += delta


# python manage.py makemigrations
# python manage.py migrate
# python manage.py createsuperuser
# python manage.py shell < create_timeslots.py 運行程式碼

# django-admin startproject restaurant_reservation
# cd restaurant_reservation
# django-admin startapp reservations

# windows 操作指令

# 1.python manage.py shell

# 2.exec(open('create_timeslots.py').read())
