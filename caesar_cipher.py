"""
Caesar Cipher Program
=====================


def caesar_cipher(text: str, shift: int, mode: str = "encrypt") -> str:
    """
    Encrypt or decrypt text using the Caesar Cipher algorithm.

    Args:
        text  : The message to process.
        shift : Number of positions to shift (1–25).
        mode  : 'encrypt' to encode, 'decrypt' to decode.

    Returns:
        The processed message as a string.
    """
    result = []

    # Decryption is just encryption with the opposite shift direction
    if mode == "decrypt":
        shift = -shift

    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            # Shift with wraparound using modulo 26
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            result.append(shifted_char)
        else:
            # Digits, spaces, punctuation — pass through unchanged
            result.append(char)

    return "".join(result)


def brute_force_decrypt(text: str) -> list[tuple[int, str]]:
    """
    Try all 25 possible shifts to decrypt a message.

    Returns:
        A list of (shift, decrypted_text) tuples.
    """
    return [(shift, caesar_cipher(text, shift, mode="decrypt")) for shift in range(1, 26)]


# ─────────────────────────── CLI helpers ─────────────────────────────────────

DIVIDER = "─" * 52


def banner() -> None:
    print()
    print("═" * 52)
    print("          🔐  CAESAR CIPHER PROGRAM  🔐")
    print("═" * 52)
    print()


def prompt_shift() -> int:
    """Keep asking until the user enters a valid shift (1–25)."""
    while True:
        try:
            shift = int(input("  Enter shift value (1–25): "))
            if 1 <= shift <= 25:
                return shift
            print("  ⚠  Shift must be between 1 and 25. Try again.\n")
        except ValueError:
            print("  ⚠  Please enter a whole number.\n")


def menu() -> None:
    print("  Options:")
    print("    [1]  Encrypt a message")
    print("    [2]  Decrypt a message")
    print("    [3]  Brute-force decrypt (try all 25 shifts)")
    print("    [4]  Exit")
    print()


# ───────────────────────────── Main loop ─────────────────────────────────────

def main() -> None:
    banner()

    while True:
        menu()
        choice = input("  Choose an option (1–4): ").strip()
        print()

        if choice == "1":
            # ── Encrypt ──────────────────────────────────────────────────────
            message = input("  Enter the message to encrypt:\n  > ")
            shift   = prompt_shift()
            encrypted = caesar_cipher(message, shift, mode="encrypt")

            print(f"\n  {DIVIDER}")
            print(f"  📝  Original  : {message}")
            print(f"  🔒  Encrypted : {encrypted}")
            print(f"  🔑  Shift key : {shift}")
            print(f"  {DIVIDER}")

        elif choice == "2":
            # ── Decrypt ──────────────────────────────────────────────────────
            message = input("  Enter the message to decrypt:\n  > ")
            shift   = prompt_shift()
            decrypted = caesar_cipher(message, shift, mode="decrypt")

            print(f"\n  {DIVIDER}")
            print(f"  🔒  Encrypted : {message}")
            print(f"  🔓  Decrypted : {decrypted}")
            print(f"  🔑  Shift key : {shift}")
            print(f"  {DIVIDER}")

        elif choice == "3":
            # ── Brute-force ──────────────────────────────────────────────────
            message = input("  Enter the message to brute-force:\n  > ")
            results = brute_force_decrypt(message)

            print(f"\n  {DIVIDER}")
            print(f"  🔍  All 25 possible decryptions of: \"{message}\"")
            print(f"  {DIVIDER}")
            for shift, text in results:
                print(f"  Shift {shift:2d} → {text}")
            print(f"  {DIVIDER}")

        elif choice == "4":
            print("  👋  Goodbye! Keep your messages secret.\n")
            break

        else:
            print("  ⚠  Invalid choice. Please enter 1, 2, 3, or 4.")

        print()


if __name__ == "__main__":
    main()
