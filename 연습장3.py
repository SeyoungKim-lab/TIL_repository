import math

r =  3
hall = [100,0]
target_ball = [70,20]
white_ball = [10,50]

w = math.sqrt((hall[0] - white_ball[0])**2 + (hall[1] - white_ball[1])**2)
x = abs(hall[0] - white_ball[0])
y = abs(hall[1] - white_ball[1])
alpha = math.atan(y/x)
n = math.sqrt((hall[0] - target_ball[0]) ** 2 + (hall[1] - target_ball[1]) ** 2)
v = math.sqrt((white_ball[0] - target_ball[0]) ** 2 + (white_ball[1] - target_ball[1]) ** 2)
cos_gamma = (w**2 + n**2 - v**2)/(2*w*n)
gamma = math.acos(cos_gamma)
k = n + 2*r
c = math.sqrt(w**2 + k**2 - 2*w*k*cos_gamma)
cos_betta = (w**2+c**2-k**2)/(2*w*c)
betta = math.acos(cos_betta)
theta = alpha - betta
power = 0.5 * c

print(power, math.degrees(theta))
