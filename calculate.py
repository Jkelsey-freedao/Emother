from language_data import translations, report_text
from datetime import datetime

# Function to reduce a number to a single digit or return the number if it's a Master number (11, 22, or 33)
def reduce_to_single_digit(number, keep_master_numbers=True):
    if keep_master_numbers and number in [11, 22, 33]:
        return number
    return sum(int(digit) for digit in str(number)) % 9 or 9

# Function to calculate the Life Path number based on the birth date
def calculate_life_path(birth_date):
    month, day, year = map(int, birth_date.split('/'))
    month = reduce_to_single_digit(month)
    day = reduce_to_single_digit(day)
    year_sum = reduce_to_single_digit(sum(int(digit) for digit in str(year)))
    life_path = month + day + year_sum
    if life_path not in [11, 22, 33]:
        life_path = reduce_to_single_digit(life_path)
    return life_path

# Function to calculate the Birth Day number based on the birth date
def calculate_birth_day(birth_date):
    _, day, _ = map(int, birth_date.split('/'))
    return reduce_to_single_digit(day)

# Function to calculate the Challenge numbers based on the birth date
def calculate_challenges(birth_date):
    month, day, year = map(int, birth_date.split('/'))
    
    # Reduce month, day, and year to single digits (excluding Master numbers)
    month = reduce_to_single_digit(month, keep_master_numbers=False)
    day = reduce_to_single_digit(day, keep_master_numbers=False)
    year = reduce_to_single_digit(sum(int(digit) for digit in str(year)), keep_master_numbers=False)

    first_challenge = abs(month - day)
    second_challenge = abs(day - year)
    third_challenge = abs(first_challenge - second_challenge)
    fourth_challenge = abs(month - year)

    return first_challenge, second_challenge, third_challenge, fourth_challenge

# Function to calculate the Period Cycle numbers based on the birth date
def calculate_period_cycles(birth_date):
    month, day, year = map(int, birth_date.split('/'))
    month = 11 if month == 11 else (month - 1) % 9 + 1
    day = reduce_to_single_digit(day)
    year = reduce_to_single_digit(sum(int(digit) for digit in str(year)))

    return month, day, year

# Function to calculate the Sun Number based on the birth date
def calculate_sun_number(birth_date):
    month, day, _ = map(int, birth_date.split('/'))
    sun_number = reduce_to_single_digit(month + day, keep_master_numbers=False)
    return sun_number

# Function to calculate the Personal Year number based on the birth date and current year
def calculate_personal_year(birth_date, current_year):
    sun_number = calculate_sun_number(birth_date)
    personal_year = reduce_to_single_digit(sun_number + current_year, keep_master_numbers=False)
    return personal_year

# Function to calculate the Personal Month number based on the birth date and current date
def calculate_personal_month(birth_date, current_date):
    personal_year = calculate_personal_year(birth_date, current_date.year)
    current_month = reduce_to_single_digit(current_date.month, keep_master_numbers=False)
    personal_month = reduce_to_single_digit(personal_year + current_month, keep_master_numbers=False)
    return personal_month

# Function to calculate the Personal Day number based on the birth date and current date
def calculate_personal_day(birth_date, current_date):
    personal_month = calculate_personal_month(birth_date, current_date)
    current_day = reduce_to_single_digit(current_date.day, keep_master_numbers=False)
    personal_day = reduce_to_single_digit(personal_month + current_day, keep_master_numbers=False)
    return personal_day

# Function to calculate the Daily Challenge number based on the birth date and current date
def calculate_daily_challenge(birth_date, current_date):
    personal_month = calculate_personal_month(birth_date, current_date)
    personal_day = calculate_personal_day(birth_date, current_date)
    daily_challenge = abs(personal_month - personal_day)
    return daily_challenge

# Function to generate a numerology report for a specific category and value
def generate_report(category, value, language, number=None):
    # Handle challenge categories which require 'number' in their key
    if 'challenges' in category or 'period_cycles' in category:
        category_key = f"{category}_{number}".lower()
    else:
        category_key = category.lower()
    
    key = (category_key, value)
    
    # Check if the text is available in the dictionary
    if key in report_text[language]:
        report = report_text[language][key]
    else:
        # If no text is available, generate a default message
        report = f"{translations[language][category]} {number if number else ''}: {value}\n"
        report += translations[language]["no_text_available"]
    
    return report
