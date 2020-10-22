from typing import List


def restore_string(s: str, indices: List[int]) -> str:
    result = [''] * len(s)

    for i, j in enumerate(indices):
        result[j] = s[i]

    return ''.join(result)


print(restore_string('codeleet', [4, 5, 6, 7, 0, 2, 1, 3]))
