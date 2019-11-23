N = input(' Enter flag parameter (It shall be an integer even number): ')


class ArgumentError(Exception):
    def __init__(self, message):
        super().__init__(message)


if N.isdigit():
    N = int(N)
    if N % 2 or N < 2:
        raise ArgumentError('Value must be an even number greater than 1')
else:
    raise ArgumentError('Value must be an integer number')


def flag(n):
    flag_output = '\n'
    height = n * 2 + 2
    width = n * 3 + 2
    for i in range(height):
        for j in range(width):
            if (
                    (i == 0) or
                    (j == 0 and i < height) or
                    (i == height - 1) or
                    (j == width - 1 and i < height)
            ):
                flag_output += '#'
            elif ((height - 4) / 2 - n / 2) ** 2 < (i - (height - 1) / 2) ** 2 + (j - (width - 1) / 2) ** 2 < (
                    (height - 2.2) / 2 - n / 2) ** 2:
                flag_output += '*'
            elif (i - (height - 1) / 2) ** 2 + (j - (width - 1) / 2) ** 2 <= ((height - 4) / 2 - n / 2) ** 2:
                flag_output += 'o'
            else:
                flag_output += ' '
        flag_output += '\n'
    return flag_output


print(flag(N))
