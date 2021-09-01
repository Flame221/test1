def positive_sum(arr):
    sum_of_numbers = 0
    for i in arr:
        if i >= 0:
            sum_of_numbers += i
    return sum_of_numbers


def sum_array(arr):
    if arr is None or len(arr) < 3:
        return 0
    else:
        return sum(arr) - max(arr) - min(arr)


def validate_pin(pin):
    if pin.isdigit():
        if len(pin) == 4 or len(pin) == 6:
            return True
        else:
            return False
    else:
        return False
