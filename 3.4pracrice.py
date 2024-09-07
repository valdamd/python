from datetime import datetime, timedelta

def validate_birthdate(birthdate_str):
    try:
        datetime.strptime(birthdate_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def calculate_birthday(birthdate_str, days):
    if not validate_birthdate(birthdate_str):
        raise ValueError('Invalid date format. Use YYYY-MM-DD')

    birthdate = datetime.strptime(birthdate_str, '%Y-%m-%d')
    future_birthday = birthdate + timedelta(days=days)
    return future_birthday.strftime('%Y-%m-%d')

# Пример использования:
birthdate = input('Enter your birthdate (YYYY-MM-DD): ')
days = int(input('Enter the number of days: '))

try:
    future_birthday = calculate_birthday(birthdate, days)
    print('Your birthday in', days, 'days will be on', future_birthday)
except ValueError as e:
    print(e)