import math

def bit_frequencies(bits):
    """Calcule la fréquence des bits 0 et 1"""
    N = len(bits)
    N1 = bits.count('1')
    N0 = N - N1
    p0 = N0 / N
    p1 = N1 / N
    return N0, N1, p0, p1

def chi_squared_test(N0, N1):
    """Test du chi-carré pour l’équiprobabilité"""
    N = N0 + N1
    expected = N / 2
    chi2 = ((N0 - expected) ** 2) / expected + ((N1 - expected) ** 2) / expected
    return chi2

def shannon_entropy(p0, p1):
    """Entropie de Shannon par bit"""
    if p0 == 0 or p1 == 0:
        return 0.0
    return -(p0 * math.log2(p0) + p1 * math.log2(p1))

def autocorrelation(bits, max_lag=10):
    """Autocorrélation pour différents décalages (lags)"""
    N = len(bits)
    Y = [1 if b == '1' else -1 for b in bits]
    results = {}
    for h in range(1, max_lag + 1):
        if h >= N:
            results[h] = None
        else:
            s = sum(Y[i] * Y[i + h] for i in range(N - h))
            results[h] = s / (N - h)
    return results

def avalanche_ratio(bits1, bits2):
    """Distance de Hamming et ratio de bits modifiés"""
    assert len(bits1) == len(bits2), "Les deux chaînes doivent avoir la même longueur"
    N = len(bits1)
    diff = sum(b1 != b2 for b1, b2 in zip(bits1, bits2))
    ratio = diff / N
    ic95 = (0.5 - 0.98 / math.sqrt(N), 0.5 + 0.98 / math.sqrt(N))
    return diff, ratio, ic95

def analyse_message_chiffre(bits, bits2=None):
    print("Analyse statistique du message chiffré :")
    print(f"Longueur du message : {len(bits)} bits")

    # 1. Fréquences
    N0, N1, p0, p1 = bit_frequencies(bits)
    print(f"Fréquence des 0 : {p0:.4f}, des 1 : {p1:.4f}")

    # 2. Chi-carré
    chi2 = chi_squared_test(N0, N1)
    print(f"Statistique du test chi-carré : {chi2:.4f} (seuil 95% ≈ 3.84)")

    # 3. Entropie
    H1 = shannon_entropy(p0, p1)
    H_total = H1 * len(bits)
    print(f"Entropie de Shannon par bit : {H1:.4f}, totale : {H_total:.2f} bits")

    # 4. Autocorrélation
    autocorrs = autocorrelation(bits)
    print("Autocorrélations (lags 1 à 10) :")
    for h, val in autocorrs.items():
        if val is not None:
            print(f"  Lag {h} : {val:.4f}")

    # 5. Avalanche (si second message fourni)
    if bits2:
        diff, ratio, ic = avalanche_ratio(bits, bits2)
        print(f"Distance de Hamming : {diff} bits modifiés sur {len(bits)}")
        print(f"Ratio de bits modifiés : {ratio:.4f}")
        print(f"Intervalle de confiance 95% attendu : [{ic[0]:.4f}, {ic[1]:.4f}]")

# Exemple d'utilisation avec deux messages binaires
message1 = '10100100010000100101010010010010110111011111001100101101001001101111111010111001'
message2 = '11011100000010011010110111110100111010011000101101100110110111111001100010001101'

analyse_message_chiffre(message1, message2)