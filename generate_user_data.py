from faker import Faker
import csv
import random
from hashlib import sha256

fake = Faker()

def obfuscate_data(data):
    """Obfuscate the data by hashing."""
    return sha256(data.encode()).hexdigest()[:10]  # Returns the first 10 characters of the hash for brevity

def generate_canadian_sin():
    """Generates a valid Canadian SIN using the Luhn algorithm."""
    def luhn_checksum(num):
        digits = [int(d) for d in num]
        odd_sum = sum(digits[-1::-2])
        even_sum = sum([sum(divmod(2 * d, 10)) for d in digits[-2::-2]])
        return (odd_sum + even_sum) % 10

    while True:
        num = str(random.randint(100000000, 999999999))
        if luhn_checksum(num) == 0:
            return num

def create_user_data(num_users):
    canadian_cities = ['Toronto', 'Montreal', 'Vancouver', 'Calgary', 'Edmonton', 'Ottawa', 'Winnipeg', 'Quebec City', 'Hamilton', 'Kitchener', 'London', 'Victoria', 'Halifax', 'Oshawa', 'Windsor', 'Saskatoon', 'Regina', 'St. John\'s', 'Sherbrooke', 'Barrie', 'Kelowna', 'Abbotsford', 'Sudbury', 'Kingston', 'Saguenay']
    headers = ['User ID', 'First Name', 'Last Name', 'SIN Number', 'Age', 'Location', 'User Type', 'Satisfaction Rating', 'Feature Importance', 'Comments']

    with open('user_survey_data.csv', 'w', newline='') as file, open('user_survey_data_obfuscated.csv', 'w', newline='') as file_obf:
        writer = csv.writer(file)
        writer_obf = csv.writer(file_obf)

        writer.writerow(headers)
        writer_obf.writerow(headers)
        
        for _ in range(num_users):
            user_id = fake.unique.uuid4()
            first_name = fake.first_name()
            last_name = fake.last_name()
            sin_number = generate_canadian_sin()
            age = random.randint(18, 70)
            location = random.choice(canadian_cities)  # Select a random Canadian city from the list
            user_type = random.choice(['New user', 'Returning user', 'Power user'])
            satisfaction_rating = random.randint(1, 5)
            feature_importance = random.randint(1, 5)
            comments = fake.text(max_nb_chars=100)
            
            row = [user_id, first_name, last_name, sin_number, age, location, user_type, satisfaction_rating, feature_importance, comments]
            writer.writerow(row)

            row_obfuscated = [user_id, obfuscate_data(first_name), obfuscate_data(last_name), obfuscate_data(sin_number), age, location, user_type, satisfaction_rating, feature_importance, comments]
            writer_obf.writerow(row_obfuscated)

num_users = 500
create_user_data(num_users)
