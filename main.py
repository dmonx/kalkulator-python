def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    return a / b if b != 0 else "Tak terdefinisi"


def main():
    print("=== Kalkulator CLI ===")
    a = float(input("Masukkan angka pertama: "))
    b = float(input("Masukkan angka kedua: "))
    operasi = input("Operasi (+ atau -): ")
    
    if operasi == "+":
        print("Hasil:", tambah(a, b))
    elif operasi == "-":
        print("Hasil:", kurang(a, b))
    elif operasi == "*":
        print("Hasil:", kali(a, b))
    elif operasi == "/":
        print("Hasil:", bagi(a, b))
    else:
        print("Operasi tidak dikenali")

if __name__ == "__main__":
    main()
