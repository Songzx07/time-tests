from times import compute_overlap_time, time_range
import pytest

def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    
    result = compute_overlap_time(large,short) 
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected

def test_no_overlap():
    large = time_range("2008-01-12 10:00:00", "2009-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)

    result = compute_overlap_time(large,short)
    expected = []
    assert result == expected

def test_several_interval():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 2, 60*10)
    short = time_range("2010-01-12 10:30:00", "2010-01-12 11:45:00", 2, 60)

    result = compute_overlap_time(large,short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:55:00'), ('2010-01-12 11:05:00', '2010-01-12 11:07:00'), ('2010-01-12 11:08:00', '2010-01-12 11:45:00')]
    assert result == expected

def test_same_end_start():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 2, 60*10)
    short = time_range("2010-01-12 12:00:00", "2010-01-13 12:00:00", 2, 60)

    result = compute_overlap_time(large,short)
    expected = []
    assert result == expected

def test_raise():
    with pytest.raises(ValueError):
        large = time_range("2010-01-12 10:00:00", "2009-01-12 12:00:00")
