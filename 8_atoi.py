# 8. String to Integer (atoi)

def myAtoi(s):
    s = s.strip()
    l = len(s)
    if l == 0:
        return 0

    i = 0
    sign = 1
    val = 0

    if s[i] == "-":
        sign = -1
        i += 1
    elif s[i] == "+":
        i += 1

    int_min = -1 * 2**31
    int_max = 2**31 - 1

    while i < l and ord(s[i]) >= ord("0") and ord(s[i]) <= ord("9"):
        val *= 10
        val += int(s[i])

        if sign == 1:
            if val >= int_max:
                return int_max
        else:
            if sign * val <= int_min:
                return int_min
        i += 1
    return sign * val
