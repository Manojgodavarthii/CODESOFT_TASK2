import random

def generate_password(length):
  characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'
  password = ''
  for i in range(length):
    password += random.choice(characters)
  return password

def main():
  length = int(input('Enter the desired length of the password: '))

  password = generate_password(length)

  print('The generated password is:', password)


if __name__ == '__main__':
  main()