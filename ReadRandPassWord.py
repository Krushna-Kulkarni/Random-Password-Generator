import random

wordlist = []

with open ('ReadRandPassWord.txt','r') as file:
    data= file.readlines()
    for line in data:
        words = line.split() 

        for item in words:
            if len(item)> 5:
                wordlist.append(item.capitalize())

digits =list( map(chr, range(ord('0'), ord('9')+1)))
schar = ['!', '@', '#' , '$', '%', '^', '&', '*']
Password = random.choice(wordlist) +random.choice(digits) + random.choice(schar) 
print(Password) 
