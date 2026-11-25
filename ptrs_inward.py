from typing import TypeVar
from LL.LinkedList import Node

T = TypeVar("T")


def reverse_val[T](vals: list[T]) -> list[T]:
    l = 0
    r = len(vals) - 1

    while l < r:
        vals[l], vals[r] = vals[r], vals[l]
        l += 1
        r -= 1
    return vals


def reverse_str(vals: list[str]) -> list[str]:
    l = 0
    r = len(vals) - 1

    while l <= r:
        # Manually reverse the string element at index l
        chars_l = list(vals[l])
        i, j = 0, len(chars_l) - 1
        while i < j:
            chars_l[i], chars_l[j] = chars_l[j], chars_l[i]
            i += 1
            j -= 1
        rev_l = "".join(chars_l)

        # In case, l and r are not equal, that is, len(vals)%2 == 0
        if l != r:
            chars_r = list(vals[r])
            p, q = 0, len(chars_r) - 1
            while p < q:
                chars_r[p], chars_r[q] = chars_r[q], chars_r[p]
                p += 1
                q -= 1
            rev_r = "".join(chars_r)

            # Swap positions in the main list
            vals[l], vals[r] = rev_r, rev_l
        # len(vals) % 2 != 0
        else:
            vals[l] = rev_l
        l += 1
        r -= 1
    return vals


s_vals: list[str] = ["ABC", "DEF", "GHI", "jkl"]

vals: list[int] = [10, 9, 1999, 27]

print(f"Values: {vals}")
reverse_val(vals)
print(f"Values reversed: {vals}")
