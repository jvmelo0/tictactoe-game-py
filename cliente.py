import socket
from random import randint

def gerar_chaves():
    p = 59
    q = 47
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 17
    d = modinv(e, phi)
    return (e, n), (d, n)

def mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def criptografar(mensagem, chave):
    e, n = chave
    return [pow(ord(c), e, n) for c in mensagem]

def descriptografar(cifra, chave):
    d, n = chave
    return ''.join([chr(pow(c, d, n)) for c in cifra])

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_servidor = input('Digite o IP do servidor: ')
cliente.connect((ip_servidor, 5000))

chave_publica, chave_privada = gerar_chaves()

chave_publica_servidor = eval(cliente.recv(1024).decode())

cliente.send(str(chave_publica).encode())

print(f'Chave pública do servidor recebida: {chave_publica_servidor}')

def enviar_mensagem(msg):
    cifrada = criptografar(msg, chave_publica_servidor)
    cliente.send(str(cifrada).encode())

def receber_mensagem():
    cifra = eval(cliente.recv(1024).decode())
    mensagem = descriptografar(cifra, chave_privada)
    return mensagem

tabuleiro = [' ']*9

def mostrar_tabuleiro():
    print()
    print(f' {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} ')
    print('-----------')
    print(f' {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ')
    print('-----------')
    print(f' {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ')
    print()

def verificar_vitoria(simbolo):
    combinacoes = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    return any(all(tabuleiro[i] == simbolo for i in c) for c in combinacoes)

while True:
    mostrar_tabuleiro()
    
    print('Aguardando jogada do jogador 1 (X)...')
    jogada = int(receber_mensagem())
    if tabuleiro[jogada] == ' ':
        tabuleiro[jogada] = 'X'

    mostrar_tabuleiro()

    if verificar_vitoria('X'):
        print('Jogador 1 (X) venceu!')
        break
    if ' ' not in tabuleiro:
        print('Empate!')
        break

    while True:
        try:
            jogada = int(input('Jogador 2 (O) - sua jogada (1-9): ')) -1
            if tabuleiro[jogada] == ' ':
                tabuleiro[jogada] = 'O'
                enviar_mensagem(str(jogada))
                break
            else:
                print('Posição ocupada!')
        except:
            print('Entrada inválida!')

    if verificar_vitoria('O'):
        mostrar_tabuleiro()
        print('Jogador 2 (O) venceu!')
        break
    if ' ' not in tabuleiro:
        mostrar_tabuleiro()
        print('Empate!')
        break

cliente.close()
