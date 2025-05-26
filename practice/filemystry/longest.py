#2️⃣ Write a script to find the longest word in a text file
length = []
with open('lines.txt','r') as file:
    content = file.read().split()
    for i in content:
        values = [len(i),i]
        length.append(values)
    
    max_pair=max(length , key=lambda x: x[0])
    print("longest word:",max_pair[1])
    print("longest word length:",max_pair[0])
                  
file.close()