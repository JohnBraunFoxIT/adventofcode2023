from scan_line import scan_row

def main():
    engine_symbols = ('*', '$', '#', '+', '&', '@', '-', '%', '/', '=')
    valid_digits = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    engine_grid = []
    gear_ratio_values = []

    # Parse input to list
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            engine_grid.append([character for character in line.strip()])

    # get the coordinates of digits
    # adjacent to an engine symbol.
    for row_index, row in enumerate(engine_grid):
        for column_index, column in enumerate(row):
            if column in engine_symbols:
                if column == '*':
                    coordinates = []
                    for adjacent_row_index in (row_index-1, row_index, row_index+1):
                        for relative_column in (-1, 0, +1):
                            try:
                                value = engine_grid[adjacent_row_index][column_index+relative_column]
                                if value in valid_digits:
                                    coordinates.append((adjacent_row_index, column_index+relative_column))
                            except IndexError:
                                # If the cell doesn't exist in the grid this error is raised.
                                pass

                    values = []
                    coordinates = filter_coordinates(coordinates)
                    for (row, column) in coordinates:
                        # Make sure the value is not inserted twice
                        value = int(scan_row(row, column, engine_grid))
                        values.append(value)

                        print(f'Appending {values}')

                    if len(values) == 2:
                        gear_ratio = values[0] * values[1]
                        gear_ratio_values.append(gear_ratio)
                        print(f'Found a gear: {values[0]} x {values[1]} = {gear_ratio}')


    print(f'Found values: {gear_ratio_values}')
    print(f'Sum: {sum(gear_ratio_values)}')


def filter_coordinates(coordinates):
    """Filter coordindate list to unique part numbers.
    
    As an engine part can be adjacent to multiple digits of
    the same number, the coordinate list must be filtered to
    only consider a single coordinate for each adjacent number.
    """
    filtered_coordinates = []

    for row, column in coordinates:
        if not (row, column-1) in coordinates:
            filtered_coordinates.append((row, column))

    return filtered_coordinates


if __name__ == "__main__":
    main()
