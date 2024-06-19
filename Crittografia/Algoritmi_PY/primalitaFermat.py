def square_and_multiply(base, exponent, modulus):
    result = 1
    base = base % modulus

    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent // 2
        base = (base * base) % modulus

    return result

def thPrimalitaFermat(a, n):
    a = pow(a, n) % n
    return a

# Esempio di utilizzo
base = 5
exponent = 3
modulus = 13
#Calcolo di N 
n = square_and_multiply(base, exponent, modulus)
a = 2501
print(square_and_multiply(base, exponent, modulus))
#Ciclo
