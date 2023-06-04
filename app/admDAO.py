from sqlalchemy import create_engine, Column, String, Integer, Text, Date, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import date


from Adm import Administrador
# Cria a conexão com o banco de dados
engine = create_engine('mysql+mysqldb://root:ubermensch@localhost/db_green_world?charset=utf8mb4&local_infile=1')

# Cria uma sessão
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# Cria a tabela no banco de dados
Base.metadata.create_all(bind=engine)

#_____________________________________________INSERT ADM______________________________________________________

def inserir_administrador(nome_completo, data_nascimento, rg, cpf, telefone, ativo, email, senha, experiencia):
    try:
        administrador = Administrador(
            nome_completo=nome_completo,
            data_nascimento=data_nascimento,
            rg=rg,
            cpf=cpf,
            telefone=telefone,
            ativo=ativo,
            email=email,
            senha=senha,
            experiencia=experiencia
        )
        session.add(administrador)
        session.commit()
        #print("Inserção de administrador concluída com sucesso!")
        # Retorna dict
        return {
            'id': administrador.id,
            'nome_completo': administrador.nome_completo,
            'data_nascimento': administrador.data_nascimento,
            'rg': administrador.rg,
            'cpf': administrador.cpf,
            'telefone': administrador.telefone,
            'ativo': administrador.ativo,
            'email': administrador.email,
            'senha': administrador.senha,
            'experiencia': administrador.experiencia
        }
    except Exception as e:

        return False

#________________________________________________UPDATE______________________________
#def atualizar_administrador(administrador_id, nome_completo, data_nascimento, rg, cpf, telefone, ativo, email, senha, experiencia):
   # try:
    #    # Busca o administrador pelo ID
       # administrador = session.query(Administrador).get(administrador_id)
        
      #  if administrador:
         #   # Atualiza os dados do administrador
          #  administrador.nome_completo = nome_completo
       #     administrador.data_nascimento = data_nascimento
        #   administrador.rg = rg
        #    administrador.cpf = cpf
         #   administrador.telefone = telefone
       #     administrador.ativo = ativo
       #    administrador.email = email
       #     administrador.senha = senha
       #     administrador.experiencia = experiencia

         #   session.commit()
          #  print("Atualização de administrador concluída com sucesso!")
        #    # Retorna um dicionário com as novas informações
        #    return {
        #        'id': administrador.id,
        #        'nome_completo': administrador.nome_completo,
        #        'data_nascimento': administrador.data_nascimento,
       #         'rg': administrador.rg,
       #         'cpf': administrador.cpf,
       #         'telefone': administrador.telefone,
       #         'ativo': administrador.ativo,
     #           'email': administrador.email,
     #           'senha': administrador.senha,
       #         'experiencia': administrador.experiencia
     #       }
   #     else:
  #          print("Administrador não encontrado.")
  #          return None
   # except Exception as e:
  #      print(f"Erro ao atualizar administrador: {str(e)}")
    #    return None

# Exemplo de chamada da função para atualizar um administrador
#novos_dados_administrador = atualizar_administrador(
  #  administrador_id=1,
   # nome_completo='Novo Nome do Administrador',
    #data_nascimento=date(1995, 5, 15),
   # rg='987654321',
  #  cpf='123456789',
  #  telefone='0987654321',
 #   ativo=True,
  #  email='novo_admin@example.com',
  #  senha='nova_senha123',
  #  experiencia='Nova Experiência do administrador'
#)

#if novos_dados_administrador:
   # print(novos_dados_administrador)
#______________________________________________________________________________________________________________________________________

def atualizar_administrador(
        administrador_id, nome_completo, data_nascimento, rg, cpf, telefone, ativo, email, senha, experiencia):
    
    try:
        # Busca o administrador pelo ID
        administrador = session.query(Administrador).filter_by(id=administrador_id).first()
        
        if administrador:
            # Atualiza os dados do administrador
            administrador.nome_completo = nome_completo
            administrador.data_nascimento = data_nascimento
            administrador.rg = rg
            administrador.cpf = cpf
            administrador.telefone = telefone
            administrador.ativo = ativo
            administrador.email = email
            administrador.senha = senha
            administrador.experiencia = experiencia

            session.commit()
            print("Atualização de administrador concluída com sucesso!")
            # Retorna um dict
            return {
                'id': administrador.id,
                'nome_completo': administrador.nome_completo,
                'data_nascimento': administrador.data_nascimento,
                'rg': administrador.rg,
                'cpf': administrador.cpf,
                'telefone': administrador.telefone,
                'ativo': administrador.ativo,
                'email': administrador.email,
                'senha': administrador.senha,
                'experiencia': administrador.experiencia
            }
        else:
            return None
        
    except Exception as e:
        return False
    
#___________________________DESATIVA POR ID________________________________________
def desativar_administrador(administrador_id):
    try:
        # Busca o administrador pelo ID
        administrador = session.query(Administrador).filter_by(id=administrador_id).first()

        if administrador:
            # Define o status de ativo como False (desativado)
            if(administrador.ativo == False):
                administrador.ativo = True
            elif(administrador.ativo == True):
                administrador.ativo = False
            session.commit()
            #print("Desativação de administrador concluída com sucesso!")
            # Retorna um dicionário com as informações atualizadas do administrador
            return {
                'id': administrador.id,
                'nome_completo': administrador.nome_completo,
                'data_nascimento': administrador.data_nascimento,
                'rg': administrador.rg,
                'cpf': administrador.cpf,
                'telefone': administrador.telefone,
                'ativo': administrador.ativo,
                'email': administrador.email,
                'senha': administrador.senha,
                'experiencia': administrador.experiencia
            }
        else:
            
            return None
    except Exception as e:
      
        return False
    
#print(desativar_administrador(1) ) # Passando o ID do administrador que deseja desativar

#if administrador_desativado:
    #print(administrador_desativado)

    #______________________EXISTE NO SITEMA OU N__________________
def verificar_administrador(email, senha):
    try:
        # Busca o administrador pelo email e senha
        administrador = session.query(Administrador).filter_by(email=email, senha=senha).first()

        if administrador:
            # O administrador existe no sistema
            return True
        else:
            # O administrador não existe no sistema
            return False
    except Exception as e:
        # Ocorreu um erro durante a verificação do administrador
        return False
    
#email = 'admin@example.com'
#senha = 'senha123'


