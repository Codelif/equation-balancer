test = """2H2 + O2 -> 2H2O"""

def times_sep(ele):
    lst = []
    for i in ele:
        times = ""
        if i == i.lower():
            pass
        elif i.isdigit():
            times+=i
        # elif 
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