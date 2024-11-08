from osdefs import *
import os

while True:
    while True:
        try:
            escolha = menu()
            break

        except Exception as e:
            print("Ops, parece que você digitou algo errado...\nTente novamente")
            os.system("pause")
            os.system("cls")

    match escolha:
        case 1:
            os.system("cls")
            cliente_logado = login()
            if cliente_logado:
                while True:
                    menu_cliente(cliente_logado)
                    break

            else:
                os.system("pause")
                os.system("cls")

        case 2:
            os.system("cls")
            cliente = cadastrar()
        case 3:
            os.system("cls")
            menu_adm()
        case 4:
            os.system("cls")
            print("Saindo")
            break
        case _:
            print("Ops, parece que você digitou algo errado...\nTente novamente")
            os.system("pause")
            os.system("cls")
