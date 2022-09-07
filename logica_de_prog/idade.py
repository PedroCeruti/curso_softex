nome = input("Digite seu nome: ")
ano_certo = False
while(ano_certo == False):
    try: 
        ano_nasc = int(input("Digite o ano do seu nascimento: "))
        if(ano_nasc < 1922) or (ano_nasc > 2021):
            print("Ano Invalido")
        else:
            idade = (2022 - ano_nasc)
            print(f"\n{nome} você têm/terá {idade} anos!")
            ano_certo = True
    except:
        print("Dado Invalido")