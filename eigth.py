import math

def bin_to_dec(binarni_cislo):
    binarni_cislo = str(binarni_cislo)
    sum = 0
    for i in range(len(binarni_cislo)):
        sum = sum * 2
        if binarni_cislo[i] == "1":
            sum = sum + 1
    return sum
    
def test_bin_to_dec():
    assert bin_to_dec("0") == 0
    assert bin_to_dec(1) == 1
    assert bin_to_dec("100") == 4
    assert bin_to_dec(101) == 5
    assert bin_to_dec("010101") == 21
    assert bin_to_dec(10000000) == 128
    assert bin_to_dec("10011101") == 157
    assert bin_to_dec(10011101) == 167 #pro vyvolání assertionErroru

if __name__ == "__main__":

    print(bin_to_dec("10011101")) #chyba v zadání, výsledek je 157 ne 167
    test_bin_to_dec()
