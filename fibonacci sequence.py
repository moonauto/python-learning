#fibonacci sequence
def fibonacci (max):
    n, a, b =0, 0, 1
    while n < max:
        print(b)
        a, b = b, a+b
        n = n + 1
    return 'done'


def fibonacci (max):
    n, a, b =0, 0, 1
    while n < max:
        yield b#print(b)
        a, b = b, a+b
        n = n + 1
    return 'done'
