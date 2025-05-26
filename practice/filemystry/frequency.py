#3️⃣ Count the frequency of each word in a file and store the result in another file.

from collections import Counter
List=[]
with open('lines.txt','r') as file:
    content = file.read().split()
    content_list = Counter(content)
    for word,count  in content_list.items():
        List.append((word,count))
    



with open('line.txt','w') as num:
    for word,count in List:
        num.write(f'{word}: {count}\n')
    
    




