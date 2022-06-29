import database as dbd
import remail
import remailanexo
import datetime
import requests
import random
import pandas as pd
import sqlite3


#openpyxl install, pyinstaller, pandas



def split_text(obj, substring = None, start = 0, qtd = None):
    '''
    Função para corte de string.
    Você pode passar apenas o objeto de texto sem especificar nada.
    isso retornará seu objeto por inteiro.
    Agora quando o parâmetro qtd for passado sem
    o parametro start ser passado, retorna uma string na
 quantidade informada.

    Mode de uso.
    passando apenas obj e qtd
    split_text('Seu texto completo aqui', qtd=20)
    sera retornado 20 caracteries apartir do começo da str

    split_text('seu texto aqui',start=16,qtd=7)
    retorma uma string de 7 caracteres começando na pos
    16

    slipt_text('seu texto aqui','texto',qtd=10)
    retorna um string com 10 caracaters apartir da palavra texto

    Lembramdo quando voce passar uma substring não passe o parametro start.
    '''

    qtd = len(obj) if qtd is None else qtd

    if substring:
        inicio = obj.find(substring)
        return obj[inicio:inicio+qtd]
    elif not substring:
        return obj[start:start+qtd]

def puxa_cotacao():

    try:

        requisicao = requests.get("http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL")
        # <Response [200]>
        v_requisicao = split_text(obj=str(requisicao), start=11, qtd=3)
        if int(v_requisicao) == 200:
            print(" Sucesso na requisição, retorno " + str(v_requisicao) + ".")
        elif int(v_requisicao) == 404:
            print(" Problema na requisição, retorno " + str(v_requisicao) + " Moeda especificada não existe.")
        else:
            print(" Problema na requisição, retorno " + str(v_requisicao) + ".")

        print(requisicao.json())

        # criando dicionario
        dic_requisicao = requisicao.json()
        print(dic_requisicao['USDBRL']['bid'])

    except OSError as err:
        print("def_puxa_cotacao {0}".format(err))
    except BaseException as err:
        print(f"def_puxa_cotacao {err=}, {type(err)=}")
    except ValueError:
        print("def_puxa_cotacao Erro conversao de tipos")

def alimenta_base_cep(qtd=1):

    try:

        controle = 1

        #13485054
        #10000000

        while int(controle) <= int(qtd):

            v_requisicao = 1
            while not int(v_requisicao) == 200:

                #gero CEP aleatorio
                rd = random.randint(10000000, 20000000)
                # vou fazer requisicao dos dados
                requisicao = requests.get("https://cep.awesomeapi.com.br/json/" + str(rd))


                #armazeno a resposta
                v_requisicao = split_text(obj=str(requisicao), start=11, qtd=3)

                if int(v_requisicao) == 200:
                    n_busca_cep_IBGE = busca_cep_IBGE(str(rd))
                    dic_requisicao = requisicao.json()
                    n_ins_cep_IBGE = banco.ins_cep_IBGE(cep = dic_requisicao['cep'], tipo=dic_requisicao['address_type'],endereco = dic_requisicao['address'],
                                                        estado=dic_requisicao['state'], bairro = dic_requisicao['district'], latitude= dic_requisicao['lat'],
                                                        longitude=dic_requisicao['lng'], cidade=dic_requisicao['city'],populacao=dic_requisicao['city_ibge'],
                                                        ddd=dic_requisicao['ddd'])
                    controle = int(controle) + 1

                elif int(v_requisicao) == 400:
                    print(" CEP " + str(rd) + " invalido, retorno " + str(v_requisicao) + ".")
                elif int(v_requisicao) == 404:
                    print(" CEP " + str(rd) + " não encontrado, retorno " + str(v_requisicao) + ".")
                else:
                    print(" Problema na requisição, retorno " + str(v_requisicao) + ".")





    except OSError as err:
        print("def_alimenta_base_cep {0}".format(err))
    except BaseException as err:
        print(f"def_alimenta_base_cep {err=}, {type(err)=}")
    except ValueError:
        print("def_alimenta_base_cep Erro conversao de tipos")

def busca_cep_IBGE(cep):

    try:

        # vou fazer requisicao dos dados
        requisicao = requests.get("https://cep.awesomeapi.com.br/json/" + str(cep))

        # <Response [200]>
        v_requisicao = split_text(obj=str(requisicao), start=11, qtd=3)
        if int(v_requisicao) == 200:
            print(" CEP " + str(cep) + " encontrado, retorno " + str(v_requisicao) + ".")
        elif int(v_requisicao) == 400:
            print(" CEP " + str(cep) + " invalido, retorno " + str(v_requisicao) + ".")
        elif int(v_requisicao) == 404:
            print(" CEP " + str(cep) + " não encontrado, retorno " + str(v_requisicao) + " Moeda especificada não existe.")
        else:
            print(" Problema na requisição, retorno " + str(v_requisicao) + ".")

        # criando dicionario
        dic_requisicao = requisicao.json()

        print(dic_requisicao)

    except OSError as err:
        print("def_busca_cep_IBGE {0}".format(err))
    except BaseException as err:
        print(f"def_busca_cep_IBGE {err=}, {type(err)=}")
    except ValueError:
        print("def_busca_cep_IBGE Erro conversao de tipos")

def excel_file ():

    cnx = sqlite3.connect('bdadosjson.db')
    result = pd.read_sql_query("SELECT DISTINCT * FROM cep_IBGE", cnx)

    result.to_excel("Relacao_CEP_base.xlsx", sheet_name='Notas', index=False )

    #msg = QMessageBox()
    #msg.setIcon(QMessageBox.Information)
    #msg.setWindowTitle("Relação de CEP'S na base de dados")
    #msg.setText("Relatório gerado com sucesso")
    #msg.exec_()

    print("Relatório gerado com sucesso !")




#inicio main
minicial = 0


try:

    #crio a conexao
    banco = dbd.BancoDeDados()
    sqlexe = banco.conecta()

    #starto e trabalho a base
    sqlexe = banco.dropa_tabela('logp')
    sqlexe = banco.dropa_tabela("imgbin")
    sqlexe = banco.dropa_tabela("usuarios")
    sqlexe = banco.criar_tabelas()

    #agora armazeno o CEP
    #https://cep.awesomeapi.com.br/json/05424020






    while not minicial == 9:

        minicial = int(input("\n \n O que deseja fazer? \n 1.Buscar CEP base IBGE \n 2.Alimentar base de dados com novo CEP \n 3.Buscar dados na base \n 4.Gerar o relatório da base \n 9.Sair do sistema \n :"))

        if minicial == 1:

            #teste busca cep IBGE

            n_cep = int(input("Digite o cep, só numeros, exemplo 13485054: "))

            n_busca_cep_IBGE = busca_cep_IBGE(str(n_cep))

        elif minicial == 2:


            n_qtd = int(input("Deseja alimentar a base com quantos CEP's novos ? "))

            # gera aleatorio
            n_alimenta_base_cep = alimenta_base_cep(qtd=int(n_qtd))

        elif minicial == 3:

            print("Buscando dados... ")
            #trazer a tabela completa
            n_sel_tabela = banco.sel_tabela("cep_IBGE")

        elif minicial == 4:

            print("Gerando relatorio...")
            #imprimindo relatorio
            n_excel_file = excel_file()

        elif minicial == 9:
            print("Saindo...")

        else:

            print("Opcao invalida!")















    #no final do codigo encerro a conexao
    sqlexe = banco.desconecta()


except OSError as err:
    print("Geral Erro OS! {0}".format(err))
except BaseException as err:
    print(f"Geral Erro Inesperado {err=}, {type(err)=}")
except ValueError:
    print("Geral Erro conversao de tipos")


