def water_capacity_calc(input_array):
    max_height = max(input_array)
    total_water_count = 0

    for height_level in range(max_height):
        water_count = 0
        black_block_encountered = False

        for i in range(len(input_array)):
            if black_block_encountered is False and input_array[i] != 0:
                black_block_encountered = True

            if black_block_encountered:
                if input_array[i] == 0:
                    water_count += 1
                else:
                    total_water_count += water_count
                    water_count = 0

        input_array = [x - 1 if x > 0 else x for x in input_array]
    return total_water_count


heights = [
    # example 1
    [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],

    # example 2
    [4, 2, 0, 3, 2, 5],

    # smallest (allowed) array without 'black blocks'
    [0],

    # arrays with n == 1 and a certain non-zero height
    [1],
    [10],

    [10, 0, 10],
    [10, 1, 10],
    [10, 1, 1, 10],
    [10, 1, 0, 1, 10]
]

for height in heights:
    print(height, "->", water_capacity_calc(height))
