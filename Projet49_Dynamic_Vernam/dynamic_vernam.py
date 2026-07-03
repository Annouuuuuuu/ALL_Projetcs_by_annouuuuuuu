import secrets
import hashlib

def text_to_bits(text):
    """Convertit un texte en chaîne binaire (ASCII/Unicode sur 8 bits)."""
    return ''.join(f'{ord(c):08b}' for c in text)

def bits_to_text(bits):
    """Convertit une chaîne binaire en texte."""
    return ''.join(chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8))

def generate_initial_key(length, seed=None):
    """Génère une chaîne binaire de longueur spécifiée."""
    if seed is None:
        # Version optimisée pour la génération aléatoire
        return ''.join(str(secrets.randbits(1)) for _ in range(length))
    
    # Version déterministe avec seed
    bits = []
    counter = 0
    
    while len(bits) < length:
        # Utiliser directement l'encodage bytes pour l'efficacité
        data = f"{seed}{counter}".encode()
        hash_bytes = hashlib.sha256(data).digest()
        
        for byte in hash_bytes:
            bits.append(f'{byte:08b}')
            if len(''.join(bits)) >= length:
                break
        counter += 1
    
    return ''.join(bits)[:length]

def xor_bits(bits1, bits2):
    """XOR bit à bit entre deux chaînes binaires de même longueur."""
    return ''.join('1' if b1 != b2 else '0' for b1, b2 in zip(bits1, bits2))

def encrypt(message, seed):
    """Chiffre un message avec Vernam dynamique mot par mot."""
    if not message:
        return [], []
    
    words = message.split(" ")
    bits_list = [text_to_bits(w) for w in words if w]  # Ignorer les mots vides
    
    # Si tous les mots sont vides (que des espaces)
    if not bits_list:
        return [""] * len(words), []
    
    # Longueur du mot le plus long en bits
    max_len = max(len(b) for b in bits_list)
    
    # Générer la clé initiale K0
    K0 = generate_initial_key(max_len, seed if seed else None)
    prev_key = K0
    keys = [K0]
    cipher_words = []
    
    for word_bits in bits_list:
        # Pour les mots vides d'origine (espaces multiples)
        if not word_bits:
            cipher_words.append("")
            keys.append(prev_key)
            continue
        
        # Chiffrement du mot
        key_prefix = prev_key[:len(word_bits)]
        cipher_word = xor_bits(word_bits, key_prefix)
        cipher_words.append(cipher_word)
        
        # Mise à jour de la clé pour le mot suivant
        padded_word = word_bits.ljust(max_len, '0')
        new_key = xor_bits(prev_key, padded_word)
        keys.append(new_key)
        prev_key = new_key
    
    # Gérer les espaces multiples à la fin
    while len(cipher_words) < len(words):
        cipher_words.append("")
        keys.append(prev_key)
    
    return cipher_words, keys

def decrypt(cipher_words, K0):
    """Déchiffre un message avec Vernam dynamique mot par mot."""
    plain_words = []
    prev_key = K0
    max_len = len(K0)
    
    for Ci in cipher_words:
        if not Ci:  # Mot vide (espace)
            plain_words.append("")
            continue
        
        # Déchiffrement du mot
        key_prefix = prev_key[:len(Ci)]
        Mi = xor_bits(Ci, key_prefix)
        plain_words.append(bits_to_text(Mi))
        
        # Mise à jour de la clé (identique à l'encryption)
        padded_word = Mi.ljust(max_len, '0')
        new_key = xor_bits(prev_key, padded_word)
        prev_key = new_key
    
    return " ".join(plain_words)

def main():
    """Fonction principale"""
    print("╔══════════════════════════════════════╗")
    print("║  CHIFFREMENT VERNAM DYNAMIQUE        ║")
    print("╚══════════════════════════════════════╝\n")
    
    while True:
        message = input("Entrez le message à chiffrer : ")
        
        if not message:
            print("Aucun message fourni. Fin.")
            break
        
        seed = input("Entrez une graine (optionnel, laissez vide pour aléatoire) : ")
        seed = seed if seed.strip() else None
        
        print("\n" + "=" * 50)
        
        # Chiffrement
        cipher, keys = encrypt(message, seed)
        
        print(f"Message clair : '{message}'")
        words = message.split(" ")
        print(f"Nombre de mots : {len(words)}")
        print(f"Longueur max en bits : {len(keys[0]) if keys else 0}")
        
        print("\nMots originaux avec longueurs (en bits) :")
        for i, w in enumerate(words):
            if w:
                word_bits = text_to_bits(w)
                print(f"  Mot {i} : '{w}' ({len(word_bits)} bits)")
            else:
                print(f"  Mot {i} : (espace)")

        
        print("\nClés générées :")
        if not keys:
            print("  (aucune clé générée)")
        else:
            # Afficher toutes les clés en entier
            for i, key in enumerate(keys):
                print(f"  K{i} : {key}")
        
        print("\nMessage chiffré (en binaire) avec longueurs :")
        total_cipher_bits = 0
        for i, cipher_word in enumerate(cipher):
            if cipher_word:
                total_cipher_bits += len(cipher_word)
                print(f"  Mot {i} : {cipher_word} ({len(cipher_word)} bits)")
            else:
                print(f"  Mot {i} : (espace)")
        print(f"Longueur totale du message chiffré : {total_cipher_bits} bits")
        
        # Déchiffrement
        decrypted = decrypt(cipher, keys[0])
        
        print(f"\nMessage déchiffré : '{decrypted}'")
        print(f"Correspondance : {'✓' if message == decrypted else '✗'}")
        
        # Option pour recommencer
        print("\n" + "=" * 50)
        again = input("\nVoulez-vous chiffrer un autre message ? (o/n) : ")
        if again.lower() != 'o':
            print("Fin du processus.")
            break
        print("\n")

if __name__ == "__main__":
    main()