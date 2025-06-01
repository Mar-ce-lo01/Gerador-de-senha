import string
import random

def gerador_de_senha():
    resposta = input('Quer gerar senha aleatória? (S) ou (N): ').strip().lower()
    if resposta == 's':
        print("Gerando senha...")
        try:
            tamanho = int(input('Digite o tamanho da senha que você desejá: '))
        except ValueError:
            print('Entrada ínvalid. Use apenas números.')
            return

        cararteres = string.ascii_letters + string.digits + string.punctuation
        senha = ''.join(random.choice(cararteres) for _ in range(tamanho))
        print(f'Sua senha gerada: {senha}')
    elif resposta == 'n':
        print('Operação cancelada. Encerrado o programa.') 
    else:
        print('Operação Invalida. Tente novemente.')

if __name__ == '__main__':
    gerador_de_senha()
