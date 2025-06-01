import string
import random

def gerador_de_senha():
    resposta = input('Quer gerar senha aleatória? (S) ou (N): ').strip().lower()
    if resposta == 's':
        print("Gerando senha...")

        cararteres = string.ascii_letters + string.digits + string.punctuation
        senha = ''.join(random.choice(cararteres) for _ in range(12))
        print(f'Sua senha gerada: {senha}')
    elif resposta == 'n':
        print('Operação cancelada. Encerrado o programa.') 
    else:
        print('Operação Invalida. Tente novemente.')

gerador_de_senha()       
