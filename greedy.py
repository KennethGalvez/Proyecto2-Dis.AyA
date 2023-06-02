def longestCommonSubsequenceGreedy(seq1, seq2):
    lcs = []

    for element in seq1:
        if element in seq2:
            lcs.append(element)

    return lcs, len(lcs)

def test_longestCommonSubsequenceGreedy():
    seq1 = "AGGTAB"
    seq2 = "GXTXAYB"
    lcs, lcs_length = longestCommonSubsequenceGreedy(seq1, seq2)
    print("Secuencia 1:", seq1)
    print("Secuencia 2:", seq2)
    print("Subsecuencia común más larga:", lcs)
    print("Longitud de la subsecuencia común más larga:", lcs_length)

test_longestCommonSubsequenceGreedy()
