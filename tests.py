
str = "/('((30, 250, 20, 100), (211, 38, 38), 3)', '((770, 250, 20, 100), (0, 173, 181), 3)', '((400, 300, 10), (255, 255, 255), 2, 2)')/"
msg = "".join(list([val for val in str if val.isalnum() or val==" " or val=="/"]))
msg = msg[msg.find('/')+len('/'):msg.rfind('/')]
msg = msg.split()
for i in range(len(msg)):
    msg[i] = int(msg[i])

p1=[]
p2=[]
ball = []
print(len(msg))

for i in range(len(msg)):
    if i < 8:
        p1.append(msg[i])
    elif i < 16:
        p2.append(msg[i])
    else: ball.append(msg[i])

print(p1)
print(p2)
print(ball)
