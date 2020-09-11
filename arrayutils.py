def get_diffs(array):
    diffs = []
    for i in range(1, len(array)):
        diffs.append(array[i] - array[i-1])
    return diffs


def get_undiff(array, start_value):
    current_value = start_value
    for i in range(len(array)):
        array[i] = array[i] + current_value
        current_value = array[i]
    return [start_value] + array
