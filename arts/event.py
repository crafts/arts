def outage(data, start, end):
    for idx, (time, value) in enumerate(data):
        if time >= start and time <= end:
            data[idx] = (time, 0)

    return data

def spike(data, start, end, peak):
    mid = (start + end) / 2
    tail_size = mid - start
    for idx, (time, value) in enumerate(data):
        if time >= start and time <= end:
            magnitude = 1 + ((1 - (abs(time - mid) / tail_size)) * (peak - 1))
            data[idx] = (time, value * magnitude)

    return data
