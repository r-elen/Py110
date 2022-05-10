def distance(pair):
    ax, ay = pair[0][0], pair[0][1]
    bx, by = pair[1][0], pair[1][1]
    dist = ((bx-ax)**2 + (by-ay)**2)**0.5
    return dist


def distance_3d(pair):
    ax, ay, az = pair[0][0], pair[0][1], pair[0][2]
    bx, by, bz = pair[1][0], pair[1][1], pair[1][2]
    dist = ((bx-ax)**2 + (by-ay)**2 + (bz-az)**2) ** 0.5
    return dist


def pairwise(iterable):
    for i in range(len(iterable) - 1):
        yield iterable[i], iterable[i+1]


def task(collect):
    len_ = 0
    for pair in pairwise(collect):
        len_ += distance_3d(pair)
    return len_


if __name__ == "__main__":
    pts = [
        (3.3, 4, 1),
        (4.5, 3, 1),
        (2.1, -1, 2),
        (6.8, -3, 3),
        (1.4, 2.9, 2)
    ]

    print(f'{task(pts):.1f}')
