def calculate_max_speed(data_points):
    max_speed = 0
    for i in range(len(data_points)-1):
        time_1 = data_points[i][0]
        time_2 = data_points[i+1][0]
 
        pos_1 = data_points[i][1]
        pos_2 = data_points[i+1][1]
 
        speed = abs((pos_2 - pos_1) / (time_2 - time_1))

        if speed > max_speed:
            max_speed = speed
    return max_speed


def read_input(input_file):
    f = open(input_file, 'r')
    num_data_points = int(f.readline())
    print('Input:')
    print(num_data_points)
    data_points = []
    for data_point in range(num_data_points):
        data = f.readline().strip('\n')
        print(data)
        data = data.split(' ')
        data = (int(data[0]), int(data[1]))
        data_points.append(data)
    data_points.sort()
    return data_points

data_points = read_input('input_1.txt')
max_speed = calculate_max_speed(data_points)
print('Output:', max_speed)
print('-------------------')

data_points = read_input('input_2.txt')
max_speed = calculate_max_speed(data_points)
print('Output:', max_speed)
print('-------------------')