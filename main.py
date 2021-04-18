test = """2H2 + O2 -> 2H2O"""

def times_sep(s):
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
    return elem, times
    
def coeff_sep(ele):
    d = {}
    for i in ele:
        coeff = ""
        for j in i:
            if not j.isdigit():
                break
            coeff += j
        d.update({i[len(coeff):]: coeff if coeff != "" else 1})
    return d


def checker(equation):
    a = equation.split(" -> ")
    reactants = a[0].split(" + ")
    products = a[1].split(" + ")
    stoichiometry = coeff_sep(reactants), coeff_sep(products)

    print(*stoichiometry, sep="\n")

checker(test)