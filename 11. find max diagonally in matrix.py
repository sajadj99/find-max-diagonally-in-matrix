import numpy as np

strMatrix ='08022297381500400075040507785212507791084949994017811857608717409843694804566200814931735579142993714067538830034913366552709523046011426924685601325671370236912231167151676389419236542240402866331380244732609903450244753353783684203517125032988128 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48'
strMatrix = strMatrix.replace(' ' , '')
listDiagonally =[]

for i in range(0 , len(strMatrix) , 2 ):
    listDiagonally.append(int(strMatrix[i:i+2]))

arr = np.zeros((20, 20))
for i in range(20):
    for j in range(20):
        arr[i][j] = listDiagonally[i*20+j]

lst = []       
for i in range(20):
    for j in range(20):
        diagonal_right = 1
        diagonal_left = 1
        horizontal = 1
        vertical = 1
        for n in range(4):
            if (i <= 16 and j <= 16):
                diagonal_right *= arr[i+n][j+n]
            if j <= 16:
                horizontal *= arr[i][j+n]
            if i <= 16:
                vertical *= arr[i+n][j]
            if i <= 16 and j >= 3:
                diagonal_left *= arr[i+n][j-n]
        if (i <= 16 and j <= 16):
           lst.append(diagonal_right)
        if j <= 16:
            lst.append(horizontal)
        if i <= 16:
            lst.append(vertical)
        if i <= 16 and j >= 3:
            lst.append(diagonal_left)

print(max(lst))

