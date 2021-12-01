elemen1 = [0, 1, 2, 3, 4, 5]

print ("elemen 3 : ", elemen1 [2])
print ("elemen 2 dan 4 : ", elemen1[1:4])
print ("elemen terakhir : ", elemen1[5])

print(elemen1)
elemen1[3] = 4

print(elemen1)
elemen1[3:] = ["satu","dua","tiga","empat"]

print(elemen1)

elemenA = [0, 1, 2]
print(elemenA)

elemenB = [3, 4, 5]
print(elemenB)

elemenB.insert(0, 'Manggis')
print(elemenB)

elemenB.insert(0, [12, 13, 14])
print(elemenB)

elemenbaru = elemenB + elemenA
print(elemenbaru)