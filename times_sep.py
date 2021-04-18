s = "Ye2Nu3U3JIG2B2Lo3M"
elem = []
times = []
checking_pro = False
last = 0
for i in range(len(s)):
    if checking_pro:        
        if s[i].isalpha() and not s[i].islower() or s[i].isdigit():
            elem.append(s[last])
        checking_pro = False
    if s[i].islower() and s[i].isalpha():
        elem.append(s[i-1]+s[i])
    if s[i].isupper():
        checking_pro = True
    if s[i].isupper() and i == len(s)-1:
        elem.append(s[i])

    last = (i)
last = 0
checking_pro = False
for i in range(1, len(s)):
    if checking_pro:
        if s[i].isupper():
            times.append(1)       
        checking_pro = False
    if s[i].isdigit():times.append(int(s[i]))
    if s[i].isalpha():
        checking_pro = True
    if s[i].isupper() and i == len(s)-1:
            times.append(1)
    
print(elem, times)

        



