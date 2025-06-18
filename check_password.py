# check_password.py

import sys
from password_validator import PasswordValidator

if len(sys.argv) != 2:
    print("Uso: python check_password.py <senha>")
    sys.exit(1)

senha = sys.argv[1]

validator = PasswordValidator(blacklist=['123456', 'password', 'admin'])
resultado, mensagem = validator.validate(senha)

print(f"Resultado: {'✔️ Válida' if resultado else '❌ Inválida'}")
print(f"Mensagem: {mensagem}")
