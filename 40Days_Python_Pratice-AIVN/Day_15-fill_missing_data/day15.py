def find_end (data, start):
    for i in range(start + 1, len(data)):
        if data[i] != None:
            return i - 1
        elif i == len(data) - 1:
            return i
    return start

def interpolate(data, start, end):
    length = end - start
    if start == 0:
        return [data[end]] * length
    elif end == len(data):
        return [data[start-1]] * length
          
    midpoint = end - length // 2    
    return [data[start-1]]*(midpoint - start) + [data[end]]*(end - midpoint)

def predicted_data(data):
    while None in data:
        start = data.index(None)
        end = find_end(data, start) + 1
        data[start:end] = interpolate(data, start, end)

    return data

def main():
    data = [None, 1.1, 1.2, None, None, None, 1.4, None, 1.5, None, None, 1.6, 1.8, None, None]
    print(predicted_data(data))
    #expected output: [1.1, 1.1, 1.2, 1.2, 1.2, 1.4, 1.4, 1.4, 1.5, 1.5, 1.6, 1.6, 1.8, 1.8, 1.8]

main()