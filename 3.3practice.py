from datetime import datetime

def validate_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d %H:%M')
        return True
    except ValueError:
        return False

def calculate_travel_time(departure_date, arrival_date):
    if not validate_date(departure_date) or not validate_date(arrival_date):
        raise ValueError('Invalid date format. Use YYYY-MM-DD HH:MM')

    departure = datetime.strptime(departure_date, '%Y-%m-%d %H:%M')
    arrival = datetime.strptime(arrival_date, '%Y-%m-%d %H:%M')

    travel_time = arrival - departure
    return travel_time

# Пример использования:
departure_date = input('Enter departure date (YYYY-MM-DD HH:MM): ')
arrival_date = input('Enter arrival date (YYYY-MM-DD HH:MM): ')

try:
    travel_time = calculate_travel_time(departure_date, arrival_date)
    print('Travel time:', travel_time)
except ValueError as e:
    print(e)

"Узнать как правильно вводить эту фигню"