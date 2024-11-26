import tkinter as tk
from tkinter import messagebox
import unicodedata

# Polski alfabet
POLISH_ALPHABET = "aąbcćdeęfghijklłmnńoóprsśtuwyzźż"


def normalize_text(text):
    """
    Normalizuje tekst: usuwa znaki białe, nieobsługiwane znaki i zamienia na małe litery.
    """
    return ''.join([c for c in text.lower() if c in POLISH_ALPHABET])


def vigenere_encrypt(text, key):
    """
    Szyfruje tekst za pomocą szyfru Vigenère.
    """
    text = normalize_text(text)
    key = normalize_text(key)

    if not key:
        raise ValueError("Klucz nie może być pusty!")

    encrypted_text = []
    key_length = len(key)
    alphabet_length = len(POLISH_ALPHABET)
    key_index = 0  # Licznik dla klucza

    for char in text:
        if char in POLISH_ALPHABET:
            text_index = POLISH_ALPHABET.index(char)
            key_char_index = POLISH_ALPHABET.index(key[key_index % key_length])
            encrypted_char = POLISH_ALPHABET[(text_index + key_char_index) % alphabet_length]
            encrypted_text.append(encrypted_char)
            key_index += 1  # Przesuwaj klucz tylko dla liter

    return ''.join(encrypted_text)


def vigenere_decrypt(text, key):
    """
    Dekoduje tekst za pomocą szyfru Vigenère.
    """
    text = normalize_text(text)
    key = normalize_text(key)

    if not key:
        raise ValueError("Klucz nie może być pusty!")

    decrypted_text = []
    key_length = len(key)
    alphabet_length = len(POLISH_ALPHABET)
    key_index = 0  # Licznik dla klucza

    for char in text:
        if char in POLISH_ALPHABET:
            text_index = POLISH_ALPHABET.index(char)
            key_char_index = POLISH_ALPHABET.index(key[key_index % key_length])
            decrypted_char = POLISH_ALPHABET[(text_index - key_char_index) % alphabet_length]
            decrypted_text.append(decrypted_char)
            key_index += 1  # Przesuwaj klucz tylko dla liter

    return ''.join(decrypted_text)


def encrypt_action():
    try:
        text = text_entry.get("1.0", tk.END).strip()
        key = key_entry.get().strip()
        encrypted_text = vigenere_encrypt(text, key)
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, encrypted_text)
    except Exception as e:
        messagebox.showerror("Błąd", str(e))


def decrypt_action():
    try:
        text = text_entry.get("1.0", tk.END).strip()
        key = key_entry.get().strip()
        decrypted_text = vigenere_decrypt(text, key)
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, decrypted_text)
    except Exception as e:
        messagebox.showerror("Błąd", str(e))


# Tworzenie GUI
root = tk.Tk()
root.title("Szyfr Vigenère - Polski Alfabet")

# Etykiety i pola tekstowe
tk.Label(root, text="Tekst do przetworzenia:").grid(row=0, column=0, sticky="w")
text_entry = tk.Text(root, height=5, width=50)
text_entry.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

tk.Label(root, text="Klucz:").grid(row=2, column=0, sticky="w")
key_entry = tk.Entry(root, width=30)
key_entry.grid(row=2, column=1, padx=10, pady=5)

# Pole na wynik
tk.Label(root, text="Wynik:").grid(row=3, column=0, sticky="w")
result_text = tk.Text(root, height=5, width=50)
result_text.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

# Przyciski
encrypt_button = tk.Button(root, text="Szyfruj", command=encrypt_action, width=20)
encrypt_button.grid(row=5, column=0, pady=10)

decrypt_button = tk.Button(root, text="Deszyfruj", command=decrypt_action, width=20)
decrypt_button.grid(row=5, column=1, pady=10)

# Uruchomienie aplikacji
root.mainloop()
