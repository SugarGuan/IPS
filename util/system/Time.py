import datetime
from  util.system import Message as SystemMessage


def current_time():
    now = datetime.datetime.now()
    try:
        time = {
            'year': str(now.year),
            'month': single_number_format(now.month),
            'day': single_number_format(now.day),
            'hour': single_number_format(now.hour),
            'minute': single_number_format(now.minute),
            'second': single_number_format(now.second)
        }
    except TypeError as te:
        SystemMessage.error(2300101)
    return time


def current_time_dict():
    return current_time()


def current_time_string():
    time = current_time()
    return time.get('year') + '/' + time.get('month') + '/' + time.get('day') + ' ' + time.get('hour') + ':' + \
           time.get('minute') + ':' + time.get('second')


def print_current_time():
    print(current_time_string())


def single_number_format(number):
    number_dict = {
        0: '00',
        1: '01',
        2: '02',
        3: '03',
        4: '04',
        5: '05',
        6: '06',
        7: '07',
        8: '08',
        9: '09'
    }
    if number in range(0, 10):
        return number_dict.get(number)
    else:
        return str(number)

