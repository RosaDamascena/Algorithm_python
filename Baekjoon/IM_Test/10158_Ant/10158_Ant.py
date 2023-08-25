# 10158 - 개미
import sys
sys.stdin = open('input.txt')

w, h = map(int, sys.stdin.readline().split())
p, q = map(int, sys.stdin.readline().split())
t = int(sys.stdin.readline())
x, y = 0, 0

# x
if ((t-(w - p)) // w) % 2 == 0:
    x = w - ((t-(w - p)) % w)
else:
    x = ((t-(w - p)) % w)

# y
if ((t-(h - q)) // h) % 2 == 0:
    y = h - ((t-(h - q)) % h)
else:
    y = ((t-(h - q)) % h)

print(x, y)