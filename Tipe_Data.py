# variabel
contoh = "contoh string"
print(contoh)
print(''' jika ingin print string
      yang panjang agar bisa
      lebih dari satu baris
      ''')

# membuat variabel dengan tipe data tertentu
contoh_string = str("Hello World")
contoh_integer = int(20)
contoh_float = float(20.5)
contoh_complex = complex(1j)
contoh_list = list(("apple", "banana", "cherry")) # menggunakan kurung []
contoh_tuple = tuple(("apple", "banana", "cherry")) # sama dengan list, tetapi nilainya tidak bisa dirubah, menggunakan kurung ()
contoh_set = set(("apple", "banana", "cherry")) # sama seperti list, tetapi nilainya tidak boleh ada yg sama, indexnya acak, tidak berurutan, menggunakan kurung {}
contoh_range = range(6)
contoh_dictionary = dict(name="John", age=36) # {"key": "value"}
contoh_frozenset = frozenset(("apple", "banana", "cherry"))
contoh_boolean = bool(5)
contoh_byte = bytes(5)
contoh_bytearray = bytearray(5)
contoh_memoryview = memoryview(bytes(5))

#  Tipe data List
contoh_list = ['value0', 'value1', 'value2', 'value3', 'value4']
for item in contoh_list:
    print(item)
    

contoh_list.append('value5') #  menambah satu data dalam list
contoh_list.extend(['value6', 'value7']) #  menambah data lebih dari satu dalam list
print("contoh list = " + str(contoh_list))

print(contoh_list[2]) # menakses data tertentu dalam list
print(contoh_list[2:]) # mengakses data pada index ke 2 sampai akhir ([dariIndexKeBerapa : sampaiIndexKeBerapa - 1])
print(contoh_list[2:5]) # mengakses data pada index ke 2 sampai index ke 5-1(4)
print(contoh_list[-2:]) # jika index negatif, maka dihitung dari belakang
print(contoh_list[:-2]) # jika index negatif, maka dihitung dari belakang

# mengambil index dan value dalam list
# enumerate digunakan untuk mengambil indeks dan nilai dari suatu iterable (seperti list) 
for index, value in enumerate(contoh_list):
    print(f"{index} : {value}")
    
# sama dengan list, tetapi nilainya tidak bisa dirubah
contoh_tuple = ("apple", "banana", "cherry")
print(contoh_tuple)

# sama seperti list, tetapi nilainya tidak boleh ada yg sama, indexnya acak, tidak berurutan
contoh_set = {"apple", "banana", "cherry"}
print(contoh_set)

# Tipe data Dictionary
contoh_dictionary = {"name":"dira", "age":24, "address": "jakarta"}
# hanya mengaskses valuenya saja
for key in contoh_dictionary:
    print(contoh_dictionary[key])
# mengambil key dan valuenya
for key, value in contoh_dictionary.items():
    print(f"{key} : {value}")