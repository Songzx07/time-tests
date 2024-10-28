from times import compute_overlap_time, time_range
from pytest import raises

def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    
    result = compute_overlap_time(large,short) 
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected

def test_non_overlap():
    large = time_range("2010-01-13 05:00:00", "2010-01-13 10:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    
    result = compute_overlap_time(large,short) 
    expected = []
    assert result == expected

def test_just_touching():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 12:00:00", "2010-01-12 13:45:00", 2, 60)
    
    result = compute_overlap_time(large,short) 
    expected = ['2010-01-12 12:00:00']
    assert result == expected