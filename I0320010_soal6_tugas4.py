#Operator Bitwise
a = 4
b = 11

#bitwise OR |
print(".........OR...........")
c = a | b
print('nilai a :', a, 'binary a: ', format(a,'08b'))
print('nilai b :', b, 'binary b: ', format(b,'08b'))
print('nilai c :', c, 'binary c: ', format(c,'08b'))

#bitwise right shift >>
print(".....RIGHT SHIFT.....")
c = a >> b
print('nilai a :', a, 'binary a: ', format(a,'08b'))
print('nilai b :', b, 'binary b: ', format(b,'08b'))
print('nilai c :', c, 'binary c: ', format(c,'08b'))

#bitwise XOR ^
print(".........XOR.........")
c = a ^ b
print('nilai a :', a, 'binary a: ', format(a,'08b'))
print('nilai b :', b, 'binary b: ', format(b,'08b'))
print('nilai c :', c, 'binary c: ', format(c,'08b'))

#bitwise NOT ~
print(".........NOT.........")
c = ~ a
print('nilai a :', a, 'binary a: ', format(a,'08b'))
print('nilai b :', b, 'binary b: ', format(b,'08b'))
print('nilai c :', c, 'binary c: ', format(c,'08b'))

#bitwise AND &
print(".........AND.........")
c = b & a
print('nilai a :', a, 'binary a: ', format(a,'08b'))
print('nilai b :', b, 'binary b: ', format(b,'08b'))
print('nilai c :', c, 'binary c: ', format(c,'08b'))