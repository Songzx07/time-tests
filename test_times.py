from times import compute_overlap_time, time_range, get_data, iss_passes
import pytest
import yaml
from unittest.mock import patch
import requests

with open('fixture.yaml', 'r') as f:
    data = yaml.safe_load(f)

test_data = []
for case in data.values():
    element = (time_range(case['time_range_1']['start'], case['time_range_1']['end'], int(case['time_range_1']['range_num']), int(case['time_range_1']['range_gap'])),
               time_range(case['time_range_2']['start'], case['time_range_2']['end'], int(
                   case['time_range_2']['range_num']), int(case['time_range_2']['range_gap'])),
               [tuple(expected) for expected in case['expected']])
    test_data.append(element)


@pytest.mark.parametrize('first_range,second_range,expected', test_data)
def test_overlap_cases(first_range, second_range, expected):
    assert compute_overlap_time(first_range, second_range) == expected


def test_backward_time_range():
    with pytest.raises(ValueError):
        time_range('2010-10-02 10:00:00', '2010-10-01 10:00:00')


def test_iss_passes():

    mock_response = {'passes':
                     [{'startAz': 247.04, 'startAzCompass': 'WSW', 'startEl': 12.26, 'startUTC': 1730172375,
                       'maxAz': 172.51, 'maxAzCompass': 'S', 'maxEl': 35.37, 'maxUTC': 1730172685, 'endAz': 95.2,
                       'endAzCompass': 'E', 'endEl': 0.38, 'endUTC': 1730172995, 'mag': 0.1,
                       'duration': 145, 'startVisibility': 1730172850}]}

    with patch.object(requests, 'get') as mock_get:
        mock_get.return_value.json = lambda: mock_response

        time_data = get_data(25544, 41.702, -76.014, 0, 2, 300)
        mock_get.assert_called_with(
            'https://api.n2yo.com/rest/v1/satellite/visualpasses/25544/56/0/0/5/50&apiKey=33Q884-HFUV8K-SCS3LG-55CU',
            params={
                'id': 25544,
                'observer_lat': 41.702,
                'observer_lng': -76.014,
                'observer_alt': 0,
                'days': 2,
                'min_visibility': 300})

        result = iss_passes(time_data.json())
        expected = [('2024-10-29 03:26:15', '2024-10-29 03:36:35')]

        assert result == expected
