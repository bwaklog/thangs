def format_duration(seconds):  # sourcery skip: avoid-builtin-shadow
    dur = [seconds//3600, (seconds%3600)//60, seconds%60]

    def suffix(div, d):
        if d > 1:
            return f"{d} {div[0]}" if d==1 else f"{d} {div[1]}"


    hour = suffix(('hour', 'hours'), dur[0])
    if hour is None:
        hour = ""
    min = suffix(('minute', 'minutes'), dur[1])
    if min is None:
        min = ""
    sec = suffix(('second', 'seconds'), dur[2])
    if sec is None:
        sec = ""

    def sep(l, r, *args):
        trail = sum(i not in ("", None) for i in args)
        # print(trail)

        if l!="" and r!="" and trail!=(1, 0):
            # print("<comma>")
            return " "
        elif l=="" and r!="" and trail in (0, 1):
            # print("<empty>")
            return ""
        elif l=="" and r=="" and trail>1:
            return ""
        elif l!="" and r=="" and trail>1:
            # print("<comma>")
            return ", "
        elif l!="" and r!="" and trail==0:
            return " and "
        elif l!="" and r=="" and trail==1:
            # print("<and seperator>")
            return " and "
        elif l!="" and r=="" and trail==0:
            # print("<end>")
            return ""

    print(hour, min, sec)

    hm = sep(hour, min, sec)
    if hm is None:
        hm = ""
    ms = sep(min, sec, )
    if ms is None:
        ms = ""
    return hm, ms




print(format_duration(12))


# print(format_duration(1))
# print(format_duration(62))
# print(format_duration(120))
# print(format_duration(3600))
# print(format_duration(3602))
# print(format_duration(3662))
# print(format_duration(0))



    # def and_sep(n):
    #     print(dur[n], dur[n-1], dur[n-2])
    #     if dur[n] > 0 and dur[n-1] > 0:
    #         return " and "
    #     elif dur[n] > 0 and dur[n-1] == 0:
    #         if dur[n] > 1 and dur[n-2] > 0:
    #             return " and "
    #         elif dur[n] > 1 and dur[n-2] == 0:
    #             return ""

    #     elif dur[n] == 0:
    #         return ""

    # gap = and_sep(2)