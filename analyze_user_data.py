import pandas as pd

def analyze_user_types_per_city(file_path):
    # Load data from CSV
    data = pd.read_csv(file_path)
    
    # Group data by 'Location' and 'User Type', and count occurrences
    grouped_data = data.groupby(['Location', 'User Type']).size().unstack(fill_value=0)
    
    # Calculate the total number of users per city
    grouped_data['Total Users'] = grouped_data.sum(axis=1)
    
    # Save the results to a new CSV file
    grouped_data.to_csv('user_types_per_city_with_totals.csv')
    
    # Determine the city with the most users
    max_city = grouped_data['Total Users'].idxmax()
    max_users = grouped_data['Total Users'].max()
    
    # Output the city with the most users
    print(f"The city with the most users is {max_city} with {max_users} users.")
    
    return grouped_data

# Path to the obfuscated CSV file.
file_path = 'user_survey_data_obfuscated.csv'

# Call the function and print the results
result = analyze_user_types_per_city(file_path)
print(result)
