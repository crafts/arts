import calendar
import time


TIME_FMT_STR = "%Y-%m-%dT%H:%M:%S"

def _convert_time(time_val):
    if type(time_val) is unicode:
        return int(calendar.timegm(time.strptime(time_val, TIME_FMT_STR)))
    elif type(time_val) is int:
        return time_val
    else:
        raise ValueError("Unrecognized time format")

def outage(data, start, end):
    start = _convert_time(start)
    end = _convert_time(end)

    for idx, (time, value) in enumerate(data):
        if time >= start and time <= end:
            data[idx] = (time, 0)

    return data

def spike(data, start, end, peak):
    start = _convert_time(start)
    end = _convert_time(end)

    for idx, (time, value) in enumerate(data):
        if time >= start and time <= end:
            data[idx] = (time, value * peak)

    return data
