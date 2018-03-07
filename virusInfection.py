import sys
"""
for t in range(int(sys.stdin.readline())):
    n,m = map(int,sys.stdin.readline().split())
    r,c = map(int,sys.stdin.readline().strip().strip('(').strip(')').split(','))
    sec = max(r-1,c-1,n-r,m-c)
    minutes,seconds = sec/60,sec%60
    if minutes > 0:
        print minutes,"minutes" if minutes>1 else "minute",
    if seconds >= 0:
        print seconds,"seconds" if seconds>1 or seconds==0 else "second"
"""
"""
for t in range(int(raw_input())):
    n,m = map(int,raw_input().split())
    r,c = map(int,raw_input().strip().strip('(').strip(')').split(','))
    sec = max(r-1,c-1,n-r,m-c)
    minutes,seconds = sec/60,sec%60
    if minutes > 0:
        print minutes,"minutes" if minutes>1 else "minute",
    if seconds >= 0:
        print seconds,"seconds" if seconds>1 or seconds==0 else "second"
"""
for t in range(int(input())):
    n,m = map(int,input().split())
    r,c = map(int,input().strip().strip('(').strip(')').split(','))
    sec = max(r-1,c-1,n-r,m-c)
    minutes,seconds = sec//60,sec%60
    if minutes > 0:
        print (minutes,"minutes" if minutes>1 else "minute", end=' ')
    if seconds >= 0:
        print (seconds,"seconds" if seconds>1 or seconds==0 else "second")
"""
for t in range(int(raw_input())):
    n,m = map(int,raw_input().split())
    r,c = map(int,raw_input().strip().strip('(').strip(')').split(','))
    sec = max(r-1,c-1,n-r,m-c)
    minutes,seconds = sec/60,sec%60
    if minutes > 0:
        print minutes,"minutes" if minutes>1 else "minute",
    if seconds >= 0:
        print seconds,"seconds" if seconds>1 or seconds==0 else "second"
"""
