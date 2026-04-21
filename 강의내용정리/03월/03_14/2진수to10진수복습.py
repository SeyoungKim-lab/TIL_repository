def bin_to_dec(bin_num):
    dec_num = 0
    pow = 0

    for i in range(len(bin_num)-1,-1,-1):
        if bin_num[i] == "1":
            dec_num = dec_num + 2**pow
        pow += 1

    return dec_num

print(bin_to_dec("11101"))
