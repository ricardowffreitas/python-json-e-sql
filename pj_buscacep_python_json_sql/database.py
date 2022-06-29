import sqlite3

class BancoDeDados:
    """Classe que representa o banco de dados (database) da aplicação"""

    def __init__(self, nome='bdadosjson.db'):
        """Inicializa o banco de dados"""
        self.nome, self.conexao = nome, None

    def conecta(self):
        """Conecta passando o nome do arquivo"""
        self.conexao = sqlite3.connect(self.nome)

    def desconecta(self):
        """Desconecta do banco"""
        try:
            self.conexao.close()
        except AttributeError:
            pass

    def criar_tabelas(self):
        """Cria as tabelas do banco"""
        try:
            # definindo um cursor
            # o cursor permite navegar e manipular os registros do banco de dados
            cursor = self.conexao.cursor()

            # cria a tabela clientes (se ela não existir) utilizando um comando SQL
            # tipos de dados do SQlite3: http://www.sqlite.org/datatype3.html
            # o execute lê e executa comandos SQL diretamente no banco de dados
            cursor.execute("""
			CREATE TABLE IF NOT EXISTS logp (
					id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
					evento TEXT NOT NULL,
					datahora DATETIME NOT NULL					
			);
			""")
            cursor.execute("""
                        			CREATE TABLE IF NOT EXISTS cep_IBGE (
                        					id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        					cep TEXT NOT NULL,
                        					tipo TEXT NOT NULL,
                        					endereco TEXT NOT NULL,  
                        					estado TEXT NOT NULL,
                        					bairro TEXT NOT NULL,
                        					latitude TEXT NOT NULL,
                        					longitude TEXT NOT NULL,
                        					cidade TEXT NOT NULL,
                        					populacao TEXT NOT NULL,
                        					ddd TEXT NOT NULL            					            										
                        			);
                        			""")

            cursor.execute("""
            			CREATE TABLE IF NOT EXISTS imgbin (
            					id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            					nome TEXT NOT NULL,
            					arquivo BLOB NOT NULL,
            					resolucao TEXT NOT NULL            					            										
            			);
            			""")

            cursor.execute("""
                        			CREATE TABLE IF NOT EXISTS pwindows (
                        					id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        					pid TEXT NOT NULL,
                        					exec TEXT NOT NULL            										
                        			);
                        			""")

            cursor.execute("""
                                    			CREATE TABLE IF NOT EXISTS usuarios (
                                    					id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                    					usuario TEXT NOT NULL,
                                    					senha TEXT NOT NULL,
                                    					ativo INTEGER NOT NULL            										
                                    			);
                                    			""")




        except AttributeError:
            print('Faça a conexão do banco antes de criar as tabelas.')

    def ins_usuario(self, usuario, senha, ativo=1):
        """Insere cliente no banco"""
        try:
            cursor = self.conexao.cursor()

            try:
                # insere o cliente na tabela
                cursor.execute("""
				INSERT INTO usuarios (usuario, senha, ativo) VALUES (?,?,?)
				""", (usuario, senha, ativo))

                # o commit grava de fato as alterações na tabela
                # pode-se fazer alterações na tabela com as instruções INSERT, UPDATE, DELETE
                self.conexao.commit()
            except sqlite3.IntegrityError:
                print("Houston we have a problem!")
        except AttributeError:
            print('Faça a conexão do banco antes de inserir clientes.')

    def ins_cep_IBGE(self, cep, tipo, endereco, estado, bairro, latitude, longitude, cidade, populacao, ddd):
        """Insere cliente no banco"""
        try:
            cursor = self.conexao.cursor()

            try:
                # insere o cliente na tabela
                cursor.execute("""
                INSERT INTO cep_IBGE (cep, tipo, endereco, estado, bairro, latitude, longitude, cidade, populacao, ddd) VALUES (?,?,?,?,?,?,?,?,?,?)
                """, (str(cep), str(tipo), str(endereco),str(estado),str(bairro),str(latitude),str(longitude),str(cidade),str(populacao),str(ddd)))

                # o commit grava de fato as alterações na tabela
                # pode-se fazer alterações na tabela com as instruções INSERT, UPDATE, DELETE
                self.conexao.commit()
            except sqlite3.IntegrityError:
                print("Houston we have a problem!")
        except AttributeError:
            print('Faça a conexão do banco antes de inserir cep.')



    def buscar_usuario(self, usuario):

        try:
            cursor = self.conexao.cursor()
            # obtém todos os dados
            cursor.execute("""SELECT * FROM usuarios WHERE ativo = 1 """)

            # o fetchall retorna o resultado do select
            # o retorno é uma lista, um iterável
            for linha in cursor.fetchall():
                # print(linha)
                if linha[1] == usuario:
                    # print('Imagem %s encontrada.' % linha[1])
                    return linha[2]

        except:
            print("Houston we have a problem!")

    def buscar_img(self, imagem):
        """Busca uma imagem pelo nome"""
        try:
            cursor = self.conexao.cursor()


            # obtém todos os dados
            cursor.execute("""SELECT * FROM imgbin """)


            # o fetchall retorna o resultado do select
            # o retorno é uma lista, um iterável
            for linha in cursor.fetchall():
                #print(linha)
                if linha[1] == imagem:
                    #print('Imagem %s encontrada.' % linha[1])
                    return linha[2]

        except AttributeError:
            print('Faça a conexão do banco antes de buscar clientes.')

    def ins_pwindows(self,pid,exec):
        """Insere log no banco"""
        try:
            cursor = self.conexao.cursor()
            try:
                # insere o log  na tabela
                cursor.execute("""
        				INSERT INTO pwindows (pid, exec) VALUES (?,?)
        				""", ([pid],[exec]))

                # o commit grava de fato as alterações na tabela
                # pode-se fazer alterações na tabela com as instruções INSERT, UPDATE, DELETE
                self.conexao.commit()
            except sqlite3.IntegrityError:
                print('Deu merda')
        except AttributeError:
            print('Faça a conexão do banco antes de inserir log.')

    def ins_logp(self,evento):
        """Insere log no banco"""
        try:
            cursor = self.conexao.cursor()



            try:
                # insere o log  na tabela
                cursor.execute("""
        				INSERT INTO logp (evento, datahora) VALUES (?, date('now'))
        				""", ([evento]))

                # o commit grava de fato as alterações na tabela
                # pode-se fazer alterações na tabela com as instruções INSERT, UPDATE, DELETE
                self.conexao.commit()
            except sqlite3.IntegrityError:
                print('Deu merda')
        except AttributeError:
            print('Faça a conexão do banco antes de inserir log.')

    def dropa_tabela(self,tabela):
        """Apaga dados das tabelas"""
        try:
            cursor = self.conexao.cursor()

            # obtém todos os dados
            cursor.execute("DROP TABLE IF EXISTS " + tabela)

            #crava alterações
            self.conexao.commit()


        except AttributeError:
            print('Faça a conexão do banco antes de tentar limpar o log.')


    def sel_tabela(self, tabela):
        """Exibe log completo"""
        try:
            cursor = self.conexao.cursor()

            # obtém todos os dados
            cursor.execute("SELECT * FROM " + tabela + " ORDER BY ID ASC")

            # o fetchall retorna o resultado do select
            # o retorno é uma lista, um iterável
            for linha in cursor.fetchall():
                print(linha)

        except AttributeError:
            print('Faça a conexão do banco antes de tentar trazer o log.')


    def ins_imgbin(self,tupla):
        """Insere log no banco"""
        try:
            cursor = self.conexao.cursor()
            try:
                # insere o log  na tabela

                cursor.execute("""
        				INSERT INTO imgbin (nome, arquivo, resolucao) VALUES (?,?,?)
        				""", (tupla))

                # o commit grava de fato as alterações na tabela
                # pode-se fazer alterações na tabela com as instruções INSERT, UPDATE, DELETE
                self.conexao.commit()
            except sqlite3.IntegrityError:
                print('Deu merda')
        except AttributeError:
            print('Faça a conexão do banco antes de inserir log.')
