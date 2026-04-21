binary = "1100101111"
dec = int(binary, 2)


def dec_to_hex(n):
    hexa = ""
    pyo = "0123456789ABCDEF"

    if n == 0:
        return "0"

    while n > 0:
        hexa = pyo[n%16] + hexa
        n = n // 16
    
    return hexa

hexadecimal = dec_to_hex(dec)
print(hexadecimal)