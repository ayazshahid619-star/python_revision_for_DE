x = ["cat", "house", "tree", "sun", "five", "ayaz", "shahid", "python"]
y = [i.upper() for i in x if len(i) > 3 ]
print(y)
z = sorted(y[0:3])
print(z)