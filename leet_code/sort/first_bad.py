def is_bad_factory(bad=4):
    def is_bad(n):
        return n >= bad
    return is_bad


def first_bad_version(n, is_bad):
    left, mid, right = 1, n, n

    while left < right:
        if is_bad(mid):
            right = mid
        else:
            left = mid + 1

        mid = (left + right) // 2
    return right


def test():
    for bad in range(1, 10):
        is_bad = is_bad_factory(bad)
        for n in range(bad, bad+4):
            fb = first_bad_version(n, is_bad)
            print(f'bad - {bad}, n - {n},  fb - {fb}')
            assert bad == fb


if __name__ == '__main__':
    test()
