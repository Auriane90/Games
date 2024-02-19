from random import randint
import emoji
computador = randint(1, 20)
print('-=-' * 20)
print('Olá')
print('Sou seu computador... Acabei de pensar em um número entre 0 e 20.')
print('Será que você consegue adivinhar qual foi? ')
print('-=-' * 20)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print(emoji.emojize('PENSEI QUE VOCÊ FOSSE MAIS ESPERTO :laughing:, Mais... Tente mais uma vez.', use_aliases=True))
        elif jogador > computador:
            print(emoji.emojize('PENSEI QUE VOCÊ FOSSE MAIS ESPERTO :laughing:, Menos... Tente mais uma vez.', use_aliases=True))
print('Acertou com {} tentativas. Parabéns'.format(palpites))
