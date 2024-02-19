data_nilai = [2, 5, 10, 5, 6]

# if else
if 10 in data_nilai:
    print(f"exsekusi if code")
elif 20 in data_nilai:
    print(f"exsekusi else if code")
else:
    print("eksekusi else code")
    
# if else cara cepat
print("nilai kondisi true" if True else "nilai kondisi else")

# Try-exception (mirip try catch)
try:
    print(data_nilai[10])
except Exception as e:
    print(f"eksekusi block except karena ada error di blok try : {e}")
else:
    print("eksekusi blok else karena blok try dieksekusi")
finally:
    print("eksekusi blok finally setelah try atau except dieksekusi")