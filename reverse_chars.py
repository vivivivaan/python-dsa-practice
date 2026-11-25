def reverse_string(chars: list[str]) -> list[str]:
    left, right = 0, len(chars) - 1
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    return chars


def reverse_vowels(s: list[str]) -> list[str]:
    v: set[str] = set("aeiouAEIOU")
    c: list[str] = list(s)

    l: int = 0
    r: int = len(c) - 1

    while l < r:
        while l < r and c[l] not in v:
            l += 1
        while l < r and c[r] not in v:
            r -= 1
        c[l], c[r] = c[r], c[l]
        l += 1
        r -= 1
    return "".join(c)


chars: list[str] = ["h", "e", "l", 'a', "l", "o", 'p', 'i', 'q', 'u']

print(
    f"Chars before reversing vowels: {chars}\nChars after reverse: {reverse_vowels(chars)}"
)
