import pandas as pd
import pytest
from analyze_user_data import process_data, find_max_user_city

def test_process_data():
    # Create a sample DataFrame with multiple entries per user type and city
    data = pd.DataFrame({
        'Location': ['City A', 'City A', 'City B', 'City B', 'City A'],
        'User Type': ['New user', 'Returning user', 'New user', 'Power user', 'Returning user']
    })
    # Mimic the original function setup
    result = process_data(data)
    # Validate total users calculation
    assert result.loc['City A', 'New user'] == 1
    assert result.loc['City A', 'Returning user'] == 2  # Expecting 2 here because 'Returning user' appears twice for 'City A'
    assert result.loc['City B', 'New user'] == 1
    assert result.loc['City B', 'Power user'] == 1
    assert 'Total Users' in result.columns
    assert result.loc['City A', 'Total Users'] == 3  # Total should reflect the sum across user types
    assert result.loc['City B', 'Total Users'] == 2

def test_find_max_user_city():
    data = pd.DataFrame({
        'New user': [1, 2],
        'Returning user': [2, 1],
        'Total Users': [3, 3]
    }, index=['City A', 'City B'])
    max_city, max_users = find_max_user_city(data)
    assert max_city in ['City A', 'City B']
    assert max_users == 3

# Optionally add more tests for loading and saving functions
