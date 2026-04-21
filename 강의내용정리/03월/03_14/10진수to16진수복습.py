def dec_to_hex(n):
    hex = ""
    change_to_hex = "0123456789ABCDEF"
    if n == 0:
        return "0"

    while n > 0 :
        remain = n % 16
        hex = change_to_hex[remain] + hex
        n = n // 16
    
    return hex

print(dec_to_hex(0))
print(dec_to_hex(31))