from datetime import datetime, timedelta

users = [{'name': 'Андрій',  'birthday': datetime(year=1984, month=3, day=18)}, {'name': 'Богдан',  'birthday': datetime(year=2000, month=3, day=20)}, {
    'name': 'Максим',  'birthday': datetime(year=2000, month=3, day=23)}, {'name': 'Володимир',  'birthday': datetime(year=2000, month=3, day=19)}]


def get_birthdays_per_week(users):
    difrent = 7 - (datetime.now().weekday())
    next_monday = datetime.now() + timedelta(days=difrent)
    start_period = next_monday - timedelta(days=3)
    end_period = next_monday + timedelta(days=4)
    birthday_people = {}
    for i in users:

        if start_period < (i['birthday']).replace(year=start_period.year) and (i['birthday']).replace(year=end_period.year) <= end_period:
            if i['birthday'].strftime('%A') == 'Saturday' or i['birthday'].strftime('%A') == 'Sunday':
                day_of_week = 'Monday'
            else:
                day_of_week = i['birthday'].strftime('%A')

            if day_of_week not in birthday_people:
                birthday_people[day_of_week] = []
            birthday_people[day_of_week].append(i['name'])

    return birthday_people


result = get_birthdays_per_week(users)
print(result)
