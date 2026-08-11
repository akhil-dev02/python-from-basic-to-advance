# opening file in 'w' mode
# file =open("sample.txt",'w')
# file.write("my name is Bomma")
# file.close()
# print("content added")

# opening file in 'a' append
# file =open("sample.txt",'a')
# file.write("my name is Bomma")
# file.close()
# print("content added")



# file = open("sample.txt",'r+')
# string = """I am a student
# i am a learning python course"""
# file.seek(0)
# file.write(string)
# file.close()
# print("content added")

# open a file in read mode
file = None
try:
    file = open("sample1.txt",'r')
    # Takes cursor to 0th position
    data  = file.readlines()
    print(data)
except Exception as e:
    print(f"Something Wrong, because: {e}")
finally: 
    if file is not None:
        file.close()
    