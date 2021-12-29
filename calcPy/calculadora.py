while(True):
    print('Bem-vindo à Calculadora em Python\n\n')
    
    print('Aperte "Q" no OPERADOR para SAIR!\n')

    numberA = int(input('Digite o PRIMEIRO valor:\n'))
    
    operator = input('Informe a operação [+ - * /]:\n')
    if (operator == "Q" or operator == "q"):
        print('Aplicação ENCERRADA!')
        break

    numberB = int(input('Digite o SEGUNDO valor:\n'))

    def operation(numberA, operator, numberB):

        if(operator == "+"): return numberA + numberB

        elif(operator == "-"): return numberA - numberB

        elif(operator == "*"): return numberA * numberB

        elif(operator == "/"): return numberA / numberB

        else: 
            print('Algo deu errado! Por favor, entre com os valores novamente!')
    
    result = print('RESULTADO: ', operation(numberA, operator, numberB), '\n')