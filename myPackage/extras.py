class Data:
    def __init__(self, x, y):
        self.x = x
        self.y = y


f = [Data(-4, 1), Data(-2, 5), Data(5, 2), Data(6, 4), Data(13, 12)]


def interpolate(f: list, xi: int, n: int) -> float:

    # Initialize result
    result = 0.0
    for i in range(n):

        # Compute individual terms of above formula
        term = f[i].y
        for j in range(n):
            if j != i:
                term = term * (xi - f[j].x) / (f[i].x - f[j].x)

        # Add current term to result
        result += term

    return result


v = 1
d = 3
print(poly_interpolate(X, Y, v, d), interpolate(f, v, d))
