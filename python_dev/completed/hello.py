from datetime import datetime, timedelta

def get_username():
    name = input("What is your name: ")
    return name

def get_dob():
    
    """
    No arg, one return value.

    Use an input to get user's date of birth.
    I'd recommend going with YYYYMMDD format.
    Return the dob.
    """
    dob = input("Enter date of birth: ")
    year = int(dob[:4])
    month = int(dob[4:6])
    day = int(dob[6:])
    dob = datetime(year, month, day)
    return dob


def calc_age(dob):
   
    """
    One arg, one return value.

    Use datetime to get today's date.
    Use timedelta to figure out time diff.

    There will be a problem to figure out here...
    Think about what datatype input returns,
    and what datatype timedelta needs.

    Timedelta returns a timedelta object.
    Find out if it has something to return the value in days.

    Return age.
    """
    today = datetime.today()
    age = (today - dob) 
    return age

def greet(name, age):
    print(f"Hello {name}, you are {age} days old.")

name = get_username()
dob = get_dob()
print(dob)
age = calc_age(dob)

greet(name, age)