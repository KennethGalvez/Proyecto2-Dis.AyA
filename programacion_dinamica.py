import time

def longestCommonSubsequenceDP(seq1, seq2):
    start_time = time.time()
    m = len(seq1)
    n = len(seq2)
    dp = [[0] * (n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if seq1[i-1] == seq2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    lcs_length = dp[m][n]
    lcs = []

    while m > 0 and n > 0:
        if seq1[m-1] == seq2[n-1]:
            lcs.insert(0, seq1[m-1])
            m -= 1
            n -= 1
        elif dp[m-1][n] > dp[m][n-1]:
            m -= 1
        else:
            n -= 1

    end_time = time.time()
    execution_time = end_time - start_time

    return lcs, lcs_length, execution_time

def test_longestCommonSubsequenceDP():
    seq1 = "yyuueruhufdafudufnsdfuidsnifnsdfodsfdsfinsdiofnoidsfyyuueruhufdafudufnsdfuidsnifnsdfodsfdsfinsdiofnoidsfyyuueruhufdafudufnsdfuidsnifnsdfodsfdsfinsdiofnoidsfyyuueruhufdafudufnsdfuidsnifnsdfodsfdsfinsdiofnoidsf"
    seq2 = "sdunaufniasfndaufnuiadnfuidafuinadfuinaudifndausdunaufniasfndaufnuiadnfuidafuinadfuinaudifndausdunaufniasfndaufnuiadnfuidafuinadfuinaudifndausdunaufniasfndaufnuiadnfuidafuinadfuinaudifndau"
    lcs, lcs_length, execution_time = longestCommonSubsequenceDP(seq1, seq2)
    print("Secuencia 1:", seq1, len(seq1))
    print("Secuencia 2:", seq2, len(seq2))
    print("Subsecuencia común más larga:", lcs)
    print("Longitud de la subsecuencia común más larga:", lcs_length)
    print("Tiempo de ejecución:", execution_time, "segundos")

test_longestCommonSubsequenceDP()
