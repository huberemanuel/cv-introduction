import os

user_name = input()
user_age = input()
filename = input()

# Verifica se o arquivo existe na pasta atual

print(f"{user_name}, {user_age}")

if os.path.isfile(filename):
    full_path = os.path.abspath(filename)
    print(f"O arquivo existe em: {full_path}")
else:
    print("O arquivo não foi encontrado, tente novamente.")