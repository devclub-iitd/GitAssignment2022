def magic(arr):
    return [[arr[7], arr[0], arr[5]], [arr[2], arr[4], arr[6]], [arr[3], arr[8], arr[1]]]


def check_magic():
    assert magic([10, 12, 14, 16, 18, 20, 22, 24, 26]) == [
        [24, 10, 20], [14, 18, 22], [16, 26, 12]]
