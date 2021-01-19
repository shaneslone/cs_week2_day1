def validParenthesesSequence(s):
    openings = 0
    for i in range(len(s)):
        if s[i] == "(":
            openings += 1
        if s[i] == ")":
            if openings > 0:
                openings -= 1
            else:
                return False
    return openings == 0

