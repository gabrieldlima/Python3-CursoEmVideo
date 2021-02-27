# DESAFIO 004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informacões
# possíveis sobre ele.

x = input('Digite algo para ser analizado: ')

print('- É um número?       {}\n'
      '- É uma letra?       {}\n'
      '- É alfanumérico?    {}\n'
      '- Só tem espaços?    {}\n'
      '- Está em maiúculo?  {}\n'
      '- Está em minúsculo? {}\n    '
      ''.format(x.isnumeric(), x.isalpha(), x.isalnum(), x.isspace(), x.isupper(), x.islower()))
