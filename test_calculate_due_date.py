from datetime import datetime
from calculate_due_date import calculate_days_to_skip, calculate_due_date

def test_calculate_days_to_skip():
    assert calculate_days_to_skip(5) == 2

def test_calculate_due_date_correct():
    expected_due_date = datetime(2023, 8, 22, 14, 12, 0)
    assert calculate_due_date("08/18/2023 14:12", 16) == expected_due_date

def test_calculate_due_date_outside_of_business_hours():
    assert calculate_due_date("08/18/2023 18:12", 16) == "Please submit between the hours of 9am and 5pm"

def test_handle_improper_date_input():
    assert calculate_due_date("Some invalid input", 16) == "Please enter a proper date and time"

def test_handle_turnaround_type():
    assert calculate_due_date("08/18/2023 14:12", "Non-integer value") == "Turnaround time must be a number"