def romans_to_int(s):
    IV = s.count("IV")
    IX = s.count("IX")
    XL = s.count("XL")
    XC = s.count("XC")
    CD = s.count("CD")
    CM = s.count("CM")

    I = s.count('I') - IV - IX
    V = s.count('V') - IV
    X = s.count('X') - IX - XL - XC
    L = s.count('L') - XL
    C = s.count('C') - XC - CD - CM
    D = s.count('D') - CD
    M = s.count('M') - CM

    return I*1 + V*5 + X*10 + L*50 + C*100 + D*500 + M*1000 + IV*4 + IX*9 + XL*40 + XC*90 + CD*400 + CM*900

print(romans_to_int("III"))
print(romans_to_int("LVIII"))
print(romans_to_int("MCMXCIV"))