import pandas as pd
import pytest
from analyze_user_data import process_data, find_max_user_city

def test_process_data():
    # Create a sample DataFrame
    data = pd.DataFrame({
        'Location': ['City A', 'City A', 'City B', 'City B'],
        'User Type': ['New user', 'Returning user', 'New user', 'Power user'],
        'Count': [1, 2, 1, 1]
    })
    result = process_data(data)
    assert result.loc['City A', 'New user'] == 1
    assert result.loc['City A', 'Returning user'] == 2
    assert result.loc['City B', 'New user'] == 1
    assert result.loc['City B', 'Power user'] == 1
    assert 'Total Users' in result.columns
    assert result.loc['City A', 'Total Users'] == 3
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
