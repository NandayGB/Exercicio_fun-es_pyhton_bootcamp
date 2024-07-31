"""Vamos construir um jogo de forca. O programa escolherá
aleatoriamente uma palavra secreta de uma lista predefinida. A palavra
secreta será representada por espaços em branco, um para cada letra
da palavra. O jogador terá um número limitado de 6 tentativas. Em cada
tentativa, o jogador pode fornecer uma letra. Se a letra estiver presente
na palavra secreta, ela será revelada nas posições correspondentes. Se
a letra não estiver na palavra, uma mensagem de erro deverá ser
informada. Após um número máximo de erros, o jogador perde. O jogo
continua até que o jogador adivinhe a palavra ou exceda o número
máximo de tentativas.

Dica: Você precisará importar uma biblioteca para resolver esse
exercício"""


import random

def escolher_palavra():
    palavras = ['python', 'desenvolvimento', 'programacao', 'inteligencia', 'artificial']
    return random.choice(palavras)

def mostrar_palavra(palavra, letras_certas):
    return ' '.join([letra if letra in letras_certas else '_' for letra in palavra])

def jogo_forca():
    palavra_secreta = escolher_palavra()
    letras_certas = set()
    letras_erradas = set()
    tentativas = 6
    
    print("Bem-vindo ao jogo da Forca!")
    
    while tentativas > 0:
        print("\nPalavra:", mostrar_palavra(palavra_secreta, letras_certas))
        print(f"Tentativas restantes: {tentativas}")
        
        tentativa = input("Digite uma letra: ").lower()
        
        if len(tentativa) != 1 or not tentativa.isalpha():
            print("Por favor, digite apenas uma letra.")
            continue
        
        if tentativa in letras_certas or tentativa in letras_erradas:
            print("Você já tentou essa letra.")
            continue
        
        if tentativa in palavra_secreta:
            letras_certas.add(tentativa)
            if all(letra in letras_certas for letra in palavra_secreta):
                print(f"\nParabéns! Você adivinhou a palavra: {palavra_secreta}")
                break
        else:
            letras_erradas.add(tentativa)
            tentativas -= 1
            print(f"Letra errada! Você tem {tentativas} tentativas restantes.")
    
    if tentativas == 0:
        print(f"\nVocê perdeu! A palavra era: {palavra_secreta}")

if __name__ == "__main__":
    jogo_forca()