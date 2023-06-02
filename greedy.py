import time

def longestCommonSubsequenceGreedy(seq1, seq2):
    start_time = time.time()
    lcs = []

    for element in seq1:
        if element in seq2:
            lcs.append(element)

    end_time = time.time()
    execution_time = end_time - start_time

    return lcs, len(lcs), execution_time

def test_longestCommonSubsequenceGreedy():
    seq1 = "yyuueruhufdafudufnsdfuidsnifnsdfodsfdsfinsdiofnoidsfyyuueruhufdafudufnsdfuidsnifnsdfodsfdsfinsdiofnoidsfyyuueruhufdafudufnsdfuidsnifnsdfodsfdsfinsdiofnoidsfyyuueruhufdafudufnsdfuidsnifnsdfodsfdsfinsdiofnoidsf"
    seq2 = "sdunaufniasfndaufnuiadnfuidafuinadfuinaudifndausdunaufniasfndaufnuiadnfuidafuinadfuinaudifndausdunaufniasfndaufnuiadnfuidafuinadfuinaudifndausdunaufniasfndaufnuiadnfuidafuinadfuinaudifndau"
    lcs, lcs_length, execution_time = longestCommonSubsequenceGreedy(seq1, seq2)
    print("Secuencia 1:", seq1, len(seq1))
    print("Secuencia 2:", seq2, len(seq2))
    print("Subsecuencia común más larga:", lcs)
    print("Longitud de la subsecuencia común más larga:", lcs_length)
    print("Tiempo de ejecución:", execution_time, "segundos")

test_longestCommonSubsequenceGreedy()
