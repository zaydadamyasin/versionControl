# Zayd Yasin
def encode(password):
  encoded_password = ''
  for digit in password:
      encoded_password += str((int(digit) + 3) % 10)
  return encoded_password


def decode(password):
  decoded_password = ''
  for digit in password:
      decoded_password += str((int(digit) - 3) % 10)
  return decoded_password


def main():
  while True:
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    option = int(input("Please enter an option: "))
    if option == 1:
      password = input("Please enter your password to encode: ")
      encoded_password = encode(password)
      print("Your password has been encoded and stored!")
    elif option == 2:
      pass
      original_password = decode(encoded_password)
      print("The encoded password is " + encoded_password + ", and the original password is " + original_password + ".")
    elif option == 3:
      break

main()