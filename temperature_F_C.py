def fahrenheit(t):
    return (float(9/5)*t+32)
def celsius(t):
    return (float(5/9)*t-32)
temp=(39.2,36.5,37.3,37.8)
F=map(fahrenheit,temp)
C=map(celsius,temp)
print(list(F))
print(list(C))