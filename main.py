def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def main():
    print("=== Kalkulator CLI ===")
    a = float(input("Masukkan angka pertama: "))
    b = float(input("Masukkan angka kedua: "))
    operasi = input("Operasi (+ atau -): ")
    
    if operasi == "+":
        print("Hasil:", tambah(a, b))
    elif operasi == "-":
        print("Hasil:", kurang(a, b))
    else:
        print("Operasi tidak dikenali")

if __name__ == "__main__":
    main()
