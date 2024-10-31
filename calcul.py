# Python program to check if
# two strings are rotations
# of each other
def isRotation(a: str, b: str) -> bool:
    n = len(a)
    m = len(b)
    if (n != m):
        return False

    # create lps[] that
    # will hold the longest
    # prefix suffix values
    # for pattern
    lps = [0 for _ in range(n)]

    # length of the previous
    # longest prefix suffix
    length = 0
    i = 1

    # lps[0] is always 0
    lps[0] = 0

    # the loop calculates
    # lps[i] for i = 1 to n-1
    while (i < n):
        if (a[i] == b[length]):
            length += 1
            lps[i] = length
            i += 1
        else:
            if (length == 0):
                lps[i] = 0
                i += 1
            else:
                length = lps[length - 1]
    i = 0

    # Match from that rotating
    # point
    for k in range(lps[n - 1], m):
        if (b[k] != a[i]):
            return False
        i += 1
    return True

# Driver code
if __name__ == "__main__":

    s1 = "ABACD"
    s2 = "CDABA"
    print("1" if isRotation(s1, s2) else "0")

