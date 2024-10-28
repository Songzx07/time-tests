from times import compute_overlap_time, time_range
import pytest
import yaml

with open('fixture.yaml','r') as f:
    data = yaml.safe_load(f)

test_data=[]
for case in data.values():
    element = (time_range(case['time_range_1']['start'], case['time_range_1']['end'],int(case['time_range_1']['range_num']),int(case['time_range_1']['range_gap'])),
               time_range(case['time_range_2']['start'], case['time_range_2']['end'],int(case['time_range_2']['range_num']),int(case['time_range_2']['range_gap'])),
               [tuple(expected) for expected in case['expected']])
    test_data.append(element)

@pytest.mark.parametrize('first_range,second_range,expected',test_data)
def test_overlap_cases(first_range,second_range,expected):
    assert compute_overlap_time(first_range,second_range)==expected


def test_backward_time_range():
    with pytest.raises(ValueError):
        time_range('2010-10-02 10:00:00','2010-10-01 10:00:00')