# 1. PERKALIAN MATRIX 2x2
def perkalian_matrix_2x2(A, B):
    hasil = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                hasil[i][j] += A[i][k] * B[k][j]

    print("Perkalian Matrix 2x2:")
    print(f"  A = {A[0]}    B = {B[0]}")
    print(f"      {A[1]}        {B[1]}")
    print("  Hasil:")
    for baris in hasil:
        print(f"    {baris}")
    print()
    return hasil



# 2. PERKALIAN MATRIX 3x3
def perkalian_matrix_3x3(A, B):
    hasil = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                hasil[i][j] += A[i][k] * B[k][j]

    print("Perkalian Matrix 3x3:")
    for i in range(3):
        print(f"  A = {A[i]}    B = {B[i]}")
    print("  Hasil:")
    for baris in hasil:
        print(f"    {baris}")
    print()
    return hasil



# 3. TRANSPOSE VEKTOR
def transpose_vektor(v):
    hasil = [[elemen] for elemen in v]

    print("Transpose Vektor:")
    print(f"  Vektor asal  : {v}")
    print(f"  Hasil (kolom):")
    for baris in hasil:
        print(f"    {baris}")
    print()
    return hasil



# 4. TRANSPOSE MATRIX
def transpose_matrix(A):
    baris = len(A)
    kolom = len(A[0])
    hasil = [[0] * baris for _ in range(kolom)]
    for i in range(baris):
        for j in range(kolom):
            hasil[j][i] = A[i][j]

    print("Transpose Matrix:")
    print("  Matrix asal:")
    for b in A:
        print(f"    {b}")
    print("  Hasil Transpose:")
    for b in hasil:
        print(f"    {b}")
    print()
    return hasil



# 5. DOT PRODUCT
def dot_product(a, b):
    if len(a) != len(b):
        raise ValueError("Panjang kedua vektor harus sama.")
    hasil = sum(a[i] * b[i] for i in range(len(a)))

    perhitungan = " + ".join(f"{a[i]}×{b[i]}" for i in range(len(a)))
    print("Dot Product:")
    print(f"  a = {a}")
    print(f"  b = {b}")
    print(f"  a · b = {perhitungan} = {hasil}")
    print()
    return hasil



# 6. HADAMARD PRODUCT
def hadamard_product(A, B):
    baris = len(A)
    kolom = len(A[0])
    if baris != len(B) or kolom != len(B[0]):
        raise ValueError("Ukuran kedua matrix harus sama.")
    hasil = [[A[i][j] * B[i][j] for j in range(kolom)] for i in range(baris)]

    print("Hadamard Product (elemen per elemen):")
    print("  Matrix A:")
    for b in A:
        print(f"    {b}")
    print("  Matrix B:")
    for b in B:
        print(f"    {b}")
    print("  Hasil (A ⊙ B):")
    for b in hasil:
        print(f"    {b}")
    print()
    return hasil



# 7. FROBENIUS NORM
def frobenius_norm(A):
    total = 0
    for baris in A:
        for elemen in baris:
            total += elemen ** 2
    hasil = total ** 0.5

    semua_elemen = [A[i][j] for i in range(len(A)) for j in range(len(A[0]))]
    kuadrat = [f"{e}²" for e in semua_elemen]
    print("Frobenius Norm:")
    print("  Matrix A:")
    for b in A:
        print(f"    {b}")
    print(f"  ||A||_F = sqrt({' + '.join(kuadrat)})")
    print(f"         = sqrt({total})")
    print(f"         = {hasil:.6f}")
    print()
    return hasil



# 8. PENJUMLAHAN MATRIX
def penjumlahan_matrix(A, B):
    baris = len(A)
    kolom = len(A[0])
    if baris != len(B) or kolom != len(B[0]):
        raise ValueError("Ukuran kedua matrix harus sama.")
    hasil = [[A[i][j] + B[i][j] for j in range(kolom)] for i in range(baris)]

    print("Penjumlahan Matrix (A + B):")
    print("  Matrix A:")
    for b in A:
        print(f"    {b}")
    print("  Matrix B:")
    for b in B:
        print(f"    {b}")
    print("  Hasil:")
    for b in hasil:
        print(f"    {b}")
    print()
    return hasil


# 9. PENGURANGAN MATRIX
def pengurangan_matrix(A, B):
    baris = len(A)
    kolom = len(A[0])
    if baris != len(B) or kolom != len(B[0]):
        raise ValueError("Ukuran kedua matrix harus sama.")
    hasil = [[A[i][j] - B[i][j] for j in range(kolom)] for i in range(baris)]

    print("Pengurangan Matrix (A - B):")
    print("  Matrix A:")
    for b in A:
        print(f"    {b}")
    print("  Matrix B:")
    for b in B:
        print(f"    {b}")
    print("  Hasil:")
    for b in hasil:
        print(f"    {b}")
    print()
    return hasil



# 10. DETERMINAN MATRIX 2x2
def determinan_2x2(A):
    a, b = A[0][0], A[0][1]
    c, d = A[1][0], A[1][1]
    hasil = a * d - b * c

    print("Determinan Matrix 2x2:")
    print(f"  | {a}  {b} |")
    print(f"  | {c}  {d} |")
    print(f"  det(A) = ({a}×{d}) - ({b}×{c})")
    print(f"         = {a*d} - {b*c}")
    print(f"         = {hasil}")
    print()
    return hasil



# 11. DETERMINAN MATRIX 3x3 (Sarrus)
def determinan_3x3(A):
    p1 = A[0][0] * A[1][1] * A[2][2]
    p2 = A[0][1] * A[1][2] * A[2][0]
    p3 = A[0][2] * A[1][0] * A[2][1]
    n1 = A[0][2] * A[1][1] * A[2][0]
    n2 = A[0][0] * A[1][2] * A[2][1]
    n3 = A[0][1] * A[1][0] * A[2][2]
    hasil = (p1 + p2 + p3) - (n1 + n2 + n3)

    print("Determinan Matrix 3x3 (Aturan Sarrus):")
    for b in A:
        print(f"  {b}")
    print(f"  Diagonal positif : ({A[0][0]}×{A[1][1]}×{A[2][2]}) + ({A[0][1]}×{A[1][2]}×{A[2][0]}) + ({A[0][2]}×{A[1][0]}×{A[2][1]})")
    print(f"                   = {p1} + {p2} + {p3} = {p1+p2+p3}")
    print(f"  Diagonal negatif : ({A[0][2]}×{A[1][1]}×{A[2][0]}) + ({A[0][0]}×{A[1][2]}×{A[2][1]}) + ({A[0][1]}×{A[1][0]}×{A[2][2]})")
    print(f"                   = {n1} + {n2} + {n3} = {n1+n2+n3}")
    print(f"  det(A) = {p1+p2+p3} - {n1+n2+n3} = {hasil}")
    print()
    return hasil



# 12. INVERS MATRIX 2x2
def invers_matrix_2x2(A):
    a, b = A[0][0], A[0][1]
    c, d = A[1][0], A[1][1]
    det = a * d - b * c
    if det == 0:
        raise ValueError("Matrix singular, invers tidak ada (determinan = 0).")
    hasil = [[ d / det, -b / det],
             [-c / det,  a / det]]

    print("Invers Matrix 2x2:")
    print(f"  Matrix A:")
    print(f"    | {a}  {b} |")
    print(f"    | {c}  {d} |")
    print(f"  det(A) = {det}")
    print(f"  A⁻¹ = (1/{det}) × | {d}  {-b} |")
    print(f"                     | {-c}  {a} |")
    print("  Hasil:")
    for baris in hasil:
        print(f"    [{', '.join(f'{x:.4f}' for x in baris)}]")
    print()
    return hasil