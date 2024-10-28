import datetime
import time


def time_range(start_time, end_time, number_of_intervals=1, gap_between_intervals_s=0):
    start_time_stamp = time.mktime(time.strptime(start_time,"%Y-%m-%d %H:%M:%S"))
    end_time_stamp = time.mktime(time.strptime(end_time,"%Y-%m-%d %H:%M:%S"))
    if end_time_stamp < start_time_stamp:
        raise ValueError()
    inter = ((end_time_stamp - start_time_stamp) - gap_between_intervals_s * (number_of_intervals-1))/number_of_intervals
    ranges = [(start_time_stamp + i*inter + i*gap_between_intervals_s,
               start_time_stamp + (i+1)*inter + i*gap_between_intervals_s) for i in range(number_of_intervals)]
    return ranges


def compute_overlap_time(range1, range2):
    overlap_time = []
    for start1, end1 in range1:
        for start2, end2 in range2:
            if end1 <= start2 or end2 <= start1:
                continue
            low = max(start1, start2)
            high = min(end1, end2)
            overlap_time.append((time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(low)), time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(high))))
    return overlap_time

if __name__ == "__main__":
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    print(compute_overlap_time(large, short))