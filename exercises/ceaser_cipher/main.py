import art
alphabet = ["a",'b','c','ç','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def ceaser(original_text, shift_amount,encode_or_decode):
    cipher_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter not in alphabet:
            cipher_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]
    print(f'Here is the {encode_or_decode}d text: {cipher_text}')
should_continue = True
print(art.logo)
while should_continue:
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n ").lower()
    text = input("Type your message:\n ").lower()
    shift = int(input("Type the shift number:\n "))
    ceaser(original_text=text, shift_amount=shift, encode_or_decode=direction)
    restart = input("If you want to start the process again, type 'yes'. If you want to stop, type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Thank you for using this program. Stay in shadows...")