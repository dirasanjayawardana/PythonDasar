# di python membuat function dengan kata kunci --> def
def sum(number1, number2):
    return number1 + number2

# contoh rekursive function --> function yang memanggil dirinya sendiri
def factorial(number):
    if (number <= 1):
        return 1
    else:
        return number * factorial(number-1)

def ubahKalimat(kalimat):
    temp = ""
    for index, value in enumerate(kalimat):
        if index % 2 == 0:
            temp += value.upper()
        else:
            temp += value.lower()
    return temp

print(f"hasil dari 10 + 20 = {sum(10, 20)}")
print(f"faktorial dari 10 = {factorial(10)}")
print(ubahKalimat("Dirasanjayawardana"))
