a = input()
output = ""
for i in range(len(str(a))):
    for j in range(len(str(a))):
        for k in range(len(str(a))):
            for t in range(len(str(a))):
                output += f'{a[i]}{a[j]}{a[k]} -- "{a[t]}" --> '
print(output)
 

 #IDK HOW TO MAKE IT ORGERRED))