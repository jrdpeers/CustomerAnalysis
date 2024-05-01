import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def process_data(data):
    grouped_data = data.groupby(['Location', 'User Type']).size().unstack(fill_value=0)
    grouped_data['Total Users'] = grouped_data.sum(axis=1)
    return grouped_data

def find_max_user_city(grouped_data):
    max_city = grouped_data['Total Users'].idxmax()
    max_users = grouped_data['Total Users'].max()
    return max_city, max_users

def save_data(grouped_data, filename):
    grouped_data.to_csv(filename)

def main(file_path, output_filename):
    data = load_data(file_path)
    grouped_data = process_data(data)
    max_city, max_users = find_max_user_city(grouped_data)
    save_data(grouped_data, output_filename)
    print(f"The city with the most users is {max_city} with {max_users} users.")
    return max_city, max_users

if __name__ == "__main__":
    # Example usage:
    main('user_survey_data_obfuscated.csv', 'user_types_per_city_with_totals.csv')
