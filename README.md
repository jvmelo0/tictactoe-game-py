<h1 align="center"> :joystick: Tic Tac Toe / Jogo da Velha :joystick: </h1>

## :pencil: Description / Descrição
<p align="left"> 
  Tic Tac Toe Game developed in Python in the first semester of 2025 as a project for the Information Security course of the Computer Science program at Unifaj college.
  The project has its own RSA encryption, uses public andprivate keys for both players and use Sockets for network connection
</p>
<p align="left">
  Jogo da Velha desenvolvido em Python no primeiro semestre de 2025 como projeto para a disciplina de Segurança da Informação do curso de Ciência da Computação da Unifaj.
  O projeto conta com uma criptografia RSA própria, faz o uso de chaves públicas e privadas para ambos os jogadores e o uso de Socket para conexão de rede
</p>

## :computer: Technology / Tecnologia
<img src="https://github.com/user-attachments/assets/2647d29f-c87e-4a98-ad3b-19dc7c9e97d5" alt="Python-logo svg" align="right" width="40" height="50"/>
<p align="left"> The technology used for the development of this project was the Python language with Google Collab environment </p>
<p align="left"> A tecnologia usada para o desenvolvimento desse projeto foi a linguagem Python no ambiente do Google Collab. </p>

## :running: How to Run / Como Executar
<ol align="left"> 
  <li> One player must have the server on their machine. <br>
    Um dos jogadores precisa estar com o servidor em sua máquina. </li> <br>
  <li> The other player must have the client on their machine. <br>
    O outro jogador precisa estar com o cliente em sua máquina. </li> <br>
  <li> Both players must be connected to the same Internet network. <br>
    Ambos precisam estar conectados na mesma rede de Internet. </li> <br>
  <li> The player with the client must enter the other player's IP address into their program while it is running. <br>
    O jogador com o cliente precisa informar o endereço de IP do outro em seu programa enquanto excecutar. </li>
</ol>

```
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_servidor = input('Digite o IP do servidor: ')
cliente.connect((ip_servidor, 5000))
```
<img width="349" height="26" alt="image" src="https://github.com/user-attachments/assets/f5e31627-032c-417e-aee1-cb96b52dd59d" />

## :bust_in_silhouette:	Collaborators / Colaboradores
<p align="left"> João Vitor Melo </p>
<p align="left"> Lucas Stafochi </p>
