def get_vector_diffs(array):
    diffs = []
    for i in range(1, len(array)):
        diffs.append(array[i] - array[i-1])
    return diffs
