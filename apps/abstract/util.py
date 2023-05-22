import datetime

def string_to_date(date):
    return datetime.datetime.strptime(date, '%d/%m/%Y').date()