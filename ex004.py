#Faça um programa que leia algo pelo teclado e seu tipo primitivo e todas as informações sobre ela
msg = input('Digite algo:')
print('O tipo dessa mensagem é:',type(msg))
print('Essa mensagem é somente espaços?:',msg.isspace())
print('Essa mensagem é numérica?:',msg.isnumeric())
print('Essa mensagem é alfabética?:',msg.isalpha())
print('Essa mensagem é alfanumérica?:',msg.isalnum())
print('Essa mensagem está toda em letras minúsculas?:',msg.islower())
print('Essa mensagem está toda em letras maiúsculas?:',msg.isupper())
print('Essa mensagem está capitalizada?:',msg.istitle())