from times import compute_overlap_time, time_range
import pytest

@pytest.mark.parametrize("time_range_1,time_range_2,expected",
                         [(
                             time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"),
                             time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60),
                             [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
                         ),
                          (
                              time_range("2008-01-12 10:00:00", "2009-01-12 12:00:00"),
                              time_range("2010-01-12 10:30:00", "2010-01-12 11:45:00", 2, 60),
                              []
                          ),
                          (
                              time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 2, 60*10),
                              time_range("2010-01-12 10:30:00", "2010-01-12 11:45:00", 2, 60),
                              [('2010-01-12 10:30:00', '2010-01-12 10:55:00'), ('2010-01-12 11:05:00', '2010-01-12 11:07:00'), ('2010-01-12 11:08:00', '2010-01-12 11:45:00')]
                          ),
                          (
                              time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 2, 60*10),
                              time_range("2010-01-12 12:00:00", "2010-01-13 12:00:00", 2, 60),
                              []
                          )
                          ])
def test_positive(time_range_1, time_range_2, expected):
    result = compute_overlap_time(time_range_1,time_range_2)
    assert result == expected

def test_raise():
    with pytest.raises(ValueError):
        large = time_range("2010-01-12 10:00:00", "2009-01-12 12:00:00")
