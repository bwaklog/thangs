def format_duration(seconds):
    dur = {
        'y' : seconds//31536000,
        'd' : (seconds%31536000)//86400,
        'h' : (seconds%86400)//3600,
        'm' : (seconds%3600)//60,
        's' : seconds%60
    }
    r = {
        'y' : [None, 'year', 'years'][int((dur['y']==1 or dur['y'] > 0)) + int(dur['y'] > 1)],
        'd' : [None, 'day', 'days'][int((dur['d']==1 or dur['d'] > 0)) + int(dur['d'] > 1)],
        'h' : [None, 'hour', 'hours'][int((dur['h']==1 or dur['h'] > 0)) + int(dur['h'] > 1)],
        'm' : [None, 'minute', 'minutes'][int((dur['m']==1 or dur['m'] > 0)) + int(dur['m'] > 1)],
        's' : [None, 'second', 'seconds'][int((dur['s']==1 or dur['s'] > 0)) + int(dur['s'] > 1)]
    }
    y = f"{dur['y']} {r['y']}" if r['y'] != None else ""
    d = f"{dur['d']} {r['d']}" if r['d'] != None else ""
    h = f"{dur['h']} {r['h']}" if r['h'] != None else ""
    m = f"{dur['m']} {r['m']}" if r['m'] != None else ""
    s = f"{dur['s']} {r['s']}" if r['s'] != None else ""


    def se(l, r, *args):
        
        if args[0] not in (None, ""):
            follow = True
        else:
            follow =  False

        # 2 hours<sep>2 minutes and 2 seconds
        if l!="" and r!="" and follow:
            return ", "

        # # <sep>2 minutes
        elif l=="" and r!="" and not follow:
            return ""

        # # 2 years<sep>2 minutes
        # # 2 years<sep>2 seconds
        elif l!="" and r!="" and not follow:
            
        # elif r != "" and l != "" and not follow:
        #     return " and "

    yd = se(y, d, h)
    dh = se(d, h, m)
    hm = se(h, m, s)
    ms = se(m, s)
    if (y, d, h, m, s) == ('', '', '', '', ''):
        return "now"

    if m not in (None, "") and ms not in (None, ""):
        m = f"{str(m)} and "

    return y +str(yd).replace("None", "")+ d +str(dh).replace("None", "")+ h +str(hm).replace("None", "")+ m + s

print(format_duration(1))
print(format_duration(62))
print(format_duration(120))
print(format_duration(3600))
print(format_duration(3662))
print(format_duration(0))