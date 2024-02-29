import sys
import string
from random import randint, shuffle, choice, choices
from typing import List

sys.stdout = open("testcase.txt", "w")

MULTI_TESTCASES = False

LOWERCASE_ALPHABET = string.ascii_lowercase
UPPERCASE_ALPHABET = string.ascii_uppercase

MAX_N = 10
MAX_VALUE = 200000


def generate_tree(size: int) -> None:
    edges = []
    for i in range(2, size + 1):
        low = 1
        # modify low to:
        # 1:             star graph
        # i-1:           line
        # max(1, i - 2): almost a line
        # i//2:          binary tree
        edges.append((randint(low, i - 1), i))
    perm = [i for i in range(1, size + 1)]
    shuffle(perm)
    perm = [0] + perm
    shuffle(edges)
    for u, v in edges:
        if randint(1, 2) & 1:
            u, v = v, u
        print(perm[u], perm[v])


def generate_unique_random_array(size: int, low: int = 1, high: int = MAX_VALUE) -> List[int]:
    assert high - low + 1 >= size
    s = set()
    while len(s) < size:
        s.add(randint(low, high))
    ans = list(s)
    shuffle(ans)
    return ans


def generate_random_permutation(size: int) -> List[int]:
    perm = [i for i in range(1, size + 1)]
    shuffle(perm)
    return perm


def generate_random_string(size: int, letters: str = LOWERCASE_ALPHABET) -> str:
    return "".join(choices(letters, k=size))


def generate_random_lowercase_string(size: int) -> str:
    return generate_random_string(size, LOWERCASE_ALPHABET)


def generate_random_uppercase_string(size: int) -> str:
    return generate_random_string(size, UPPERCASE_ALPHABET)


def generate_random_array(size: int, low: int = 1, high: int = MAX_VALUE) -> List[int]:
    return [randint(low, high) for _ in range(size)]


def print_array(arr: List) -> None:
    for element in arr:
        print(element, end=" ")
    print()


# modify this function
def generate_and_print_testcase() -> None:
    n = randint(0, 25)
    print(n)


def main():
    testcases = 1  # should be 1, otherwise hard to see which test got us
    if MULTI_TESTCASES:  # boolean variable at the top, change if needed
        print(testcases)
    for _ in range(testcases):
        generate_and_print_testcase()


if __name__ == "__main__":
    main()
