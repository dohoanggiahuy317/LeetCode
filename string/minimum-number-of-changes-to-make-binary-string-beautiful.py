def min_changes(s):
    count = 0
    i = 0
    while i < len(s) - 1:
        if s[i] != s[i + 1]:
            count += 1
        i += 2
    return count