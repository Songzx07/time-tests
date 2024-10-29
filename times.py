import datetime
import requests
import json


def time_range(start_time, end_time, number_of_intervals=1, gap_between_intervals_s=0):
    start_time_s = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    end_time_s = datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    d = (end_time_s - start_time_s).total_seconds() / number_of_intervals + \
        gap_between_intervals_s * (1 / number_of_intervals - 1)
    if d < 0:
        raise ValueError('Time range d='+str(d)+'is negative')
    sec_range = [(start_time_s + datetime.timedelta(seconds=i * d + i * gap_between_intervals_s),
                  start_time_s + datetime.timedelta(seconds=(i + 1) * d + i * gap_between_intervals_s))
                 for i in range(number_of_intervals)]
    return [(ta.strftime("%Y-%m-%d %H:%M:%S"), tb.strftime("%Y-%m-%d %H:%M:%S")) for ta, tb in sec_range]


def compute_overlap_time(range1, range2):
    overlap_time = []

    if range1[-1][1] == range2[0][0]:
        overlap_time.append(tuple([range1[-1][1]]))
        return overlap_time
    if range2[-1][1] == range1[0][0]:
        overlap_time.append(tuple([range2[-1][1]]))
        return overlap_time

    for start1, end1 in range1:
        for start2, end2 in range2:
            low = max(start1, start2)
            high = min(end1, end2)
            if high > low:
                overlap_time.append((low, high))
    return overlap_time


def get_data(id, observer_lat, observer_lng, observer_alt, days, min_visibility):
    base = 'https://api.n2yo.com/rest/v1/satellite/visualpasses/25544/56/0/0/5/50&apiKey=33Q884-HFUV8K-SCS3LG-55CU'
    params = dict(id=id, observer_lat=observer_lat, observer_lng=observer_lng,
                  observer_alt=observer_alt, days=days, min_visibility=min_visibility)
    return requests.get(base, params=params)


def iss_passes(data):
    time_range = []
    for item in data['passes']:
        start = datetime.datetime.fromtimestamp(
            item['startUTC']).strftime("%Y-%m-%d %H:%M:%S")
        end = datetime.datetime.fromtimestamp(
            item['endUTC']).strftime("%Y-%m-%d %H:%M:%S")
        time_range.append((start, end))

    return time_range
