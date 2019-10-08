import math
r = 6371.01

#v1
v1x = 33.749099 
v1y = -84.390185
print('The GPS ycation of Atlanta, Georgia is: ', v1x, ', ', v1y, sep='')

#v2
v2x = 28.54211
v2y = -81.3790388
print('The GPS ycation of Orlando, Florida is: ', v2x, ', ', v2y, sep='')

#v3
v3x = 32.080926
v3y = -81.091177
print('The GPS ycation of Savannah, Georgia is: ', v3x, ', ',  v3y, sep='')

#v4
v4x = 35.227087
v4y = -80.843127
print('The GPS ycation of Charlotte, North Carolina is: ', v4x, ', ', v4y, sep='')
print('')

#first triangle
d13 = r * math.acos(math.sin(math.radians(v1x)) * math.sin(math.radians(v3x)) + math.cos(math.radians(v1x)) * math.cos(math.radians(v3x)) * math.cos(math.radians(v1y - v3y)))
d14 = r * math.acos(math.sin(math.radians(v1x)) * math.sin(math.radians(v4x)) + math.cos(math.radians(v1x)) * math.cos(math.radians(v4x)) * math.cos(math.radians(v1y - v4y)))
d34 = r * math.acos(math.sin(math.radians(v3x)) * math.sin(math.radians(v4x)) + math.cos(math.radians(v3x)) * math.cos(math.radians(v4x)) * math.cos(math.radians(v3y - v4y)))
s134 = (d13 + d14 + d34) / 2
area134 = math.sqrt(s134 * (s134 - d13) * (s134 - d14) * (s134 - d34))

#second triangle
d12 = r * math.acos(math.sin(math.radians(v1x)) * math.sin(math.radians(v2x)) + math.cos(math.radians(v1x)) * math.cos(math.radians(v2x)) * math.cos(math.radians(v1y - v2y)))
d23 = r * math.acos(math.sin(math.radians(v2x)) * math.sin(math.radians(v3x)) + math.cos(math.radians(v2x)) * math.cos(math.radians(v3x)) * math.cos(math.radians(v2y - v3y)))
s123 = (d12 + d13 + d23) / 2

area123 = math.sqrt(s123 * (s123 - d12) * (s123 - d13) * (s123 - d23))
#result
area1234 = area123 + area134
print('The estimated area enclosed by these four cities is:', area1234, 'square kilometers')