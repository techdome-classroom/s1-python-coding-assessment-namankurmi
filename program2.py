def decode_message(s: str, p: str) -> bool:
    # Memoization table to store intermediate results
    memo = {}

    # Helper function for recursion
    def match(i, j):
        # Base cases
        if (i, j) in memo:
            return memo[(i, j)]
        if j == len(p):  # If pattern is exhausted, string must also be exhausted
            return i == len(s)
        if i == len(s):  # If string is exhausted, pattern must be only '*' to match
            return all(x == '*' for x in p[j:])
        
        # Match current characters
        if p[j] == '*':
            # '*' can match 0 characters (move to next pattern) or 1 or more characters (move to next string character)
            memo[(i, j)] = match(i, j + 1) or match(i + 1, j)
        elif p[j] == '?' or p[j] == s[i]:
            # '?' matches any character, or exact match
            memo[(i, j)] = match(i + 1, j + 1)
        else:
            # Characters don't match
            memo[(i, j)] = False

        return memo[(i, j)]

    # Start matching from the beginning of both the string and the pattern
    return match(0, 0)
