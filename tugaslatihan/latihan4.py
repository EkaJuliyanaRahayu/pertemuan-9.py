
print("=====================Akses list=================")
# Akses list
list1 = ["a", "b", "c", "d", "e"]
print("Tampilkan element ke-3 :", list1[3])
print("Ambil nilai element 2-4", list1[2:5])
print("Ambil element terakhir :", list[0:4])

print( 45*"=", "\n")

print("================Ubah list==============")
# Ubah list
list2 = [1, 2, 3, 4, 5]
print(list2)
list2[4] = "Element 4"
print(list2)

print()

list3 = ["Satu", "Dua", "Tiga", "Empat", "Lima"]
print("Sebelum di ubah :", list3)
list3[0:6] = [1, 2, 3, 4, 5,]
print("Setelah di ubah :", list3, "\n")

print("================Tambah List Element==================")
# Tambah List Element
# Index 0(-5), 1(-4), 2(-3), 3(-2), 4(-1)
lista = [1, 2, 3, 4, 5]
print("ListA\n", lista)
listb = [6, 7, 8]
print("ListB Sebelum di tambahkan :\n", listb, "\n")

lista = [1, 2, 3, 4, 5]
print("ListA\n", lista)
listb = [6, 7, 8 ]
listb.insert(2, lista[0:2])
print("ListB Sesudah di tambahkan :\n", listb, "\n")

# Menambahkan list B dengan nilai string
listb.append("Timey")
print("ListB :\n", listb, "\n")

# Menambahkan list B dengan 3 nilai
listb.extend([10, 12, 14])
print("Menambahkan ListB dengan 3 nilai :\n", listb, "\n")
# Menggabungkan ListA dan ListB
listN = lista + listb
print("Gabungan listA & ListB: \n", listN)
