from libc.math cimport sqrt

import cython as c


def process(start:c.int,end:c.int) -> None:
    pos: c.int = start
    fator: c.int = 10000 * 10000

    while pos < end:
        pos += 1
        sqrt((pos - fator) * (pos - fator))
