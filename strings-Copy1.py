"""# Accesing the string character by using indexing
s="codegnan"
print(s[0])
print(s[-1],s[-2],s[-6])
#Accesing the string character by using slicing
print(s[:6])
print(s[:])
print(s[-1:-5:1])
print(s[2:6])
print(s[::-1])
print(s[3::-1])
s="codegnan"
print(s[:4]+'z'+s[5:])"""
string = "HACK"
for i in range(len(string)):
    for j in range(i+1, len(string)):
        print(string[i],string[j])
