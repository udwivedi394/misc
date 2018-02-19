#https://www.interviewbit.com/problems/integer-to-roman/

def integer2Roman(A):
    units = ['','I','II','III','IV','V','VI','VII','VIII','IX']
    tens = ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
    hundred = ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
    thousand = ['','M','MM','MMM']

    string = ''
    string += thousand[A/1000]
    A %= 1000
    string += hundred[A/100]
    A %= 100
    string += tens[A/10]
    A %= 10
    string += units[A]

    return string

print integer2Roman(933)
