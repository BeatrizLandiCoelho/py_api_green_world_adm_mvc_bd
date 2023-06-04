from admDAO import inserir_administrador,atualizar_administrador,desativar_administrador

#pip install validate_email
#pip install py3dns
#nao ultilizar
#pip install cpf_check
#pip install phonenumbers
from tools import ERROR_INTERNAL,ERROR_DATA_NOT_FULLFILL, DELETED,NOT_FOUND
from datetime import date
#import phonenumbers
from validate_email import validate_email

#____________________VALIDA CPF_______________________________________________________________________________#

#validate_email("beatriz.landi.celho@gmail.com")

def validar_cpf(cpf):
    # Remove caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))
    
    # Verifica se o CPF possui 11 dígitos
    if len(cpf) != 11:
        return False
    
    # Verifica se todos os dígitos são iguais (CPF inválido)
    if cpf == cpf[0] * 11:
        return False
    
    # Calcula o primeiro dígito verificador
    def calcular_digito_verificador(digitos):
        soma = sum(int(digitos[i]) * (len(digitos) + 1 - i) for i in range(len(digitos)))
        resto = soma % 11
        if resto < 2:
            return 0
        else:
            return 11 - resto
    
    digito_verificador_1 = calcular_digito_verificador(cpf[:9])
    if int(cpf[9]) != digito_verificador_1:
        return False
    
    # Calcula o segundo dígito verificador
    digito_verificador_2 = calcular_digito_verificador(cpf[:10])
    if int(cpf[10]) != digito_verificador_2:
        return False
    
    return True

#cpf = "49346696800"  # CPF a ser verificado
#print(validar_cpf(cpf))  

#____________________VALIDA RG_______________________________________________________________________________#
def validar_rg(rg):
    # Remove caracteres não numéricos
    rg = ''.join(filter(str.isdigit, rg))
    
    # Verifica se o RG possui 9 dígitos
    if len(rg) != 9:
        return False
    
    # Verifica se todos os dígitos são iguais (RG inválido)
    if rg == rg[0] * 9:
        return False
    
    # Verifica a validade do RG usando o cálculo do dígito verificador
    soma = 0
    
    for i in range(8):
        soma += int(rg[i]) * (2 + i)
    
    resto = soma % 11
    digito_calculado = 11 - resto if resto <= 9 else 0
    
    digito_verificador = int(rg[8])
    
    if digito_verificador != digito_calculado:
        return False
    
    return True

rg = "595361274"  # RG a ser verificado
#print(validar_rg(rg))


#_______________________________________________TELEFONE__________________________________


#numpye

#________________________________DATA_______________________________________________

#d#ef dividir_data(data):
  #  partes = data.split('-')
  #  ano = int(partes[0])
  #  mes = int(partes[1])
  #  dia = int(partes[2])
  #  return ano, mes, dia

# Exemplo de uso da função
#data = '1990-01-01'
##ano, mes, dia = dividir_data(data)
#print(ano, mes, dia)


#def verificar_data_passada(data):
   # data_atual = date.today()
   # if data < data_atual:
   # elif data == data_atual:
   #     return "Hoje é a data."
   # else:
   #     return "A data ainda está por vir."

# Exemplo de uso da função
#data_futura = date(2023, 12, 31)
#resultado = verificar_data_passada(data_futura)
#print(resultado)

#___________________________ADD ADM____________________________________________________
def add_adm(nome_completo, data_nascimento, rg, cpf, telefone, email, senha, experiencia):

 cpf = ''.join(filter(str.isdigit, cpf))

 if(
    nome_completo ==''
    or data_nascimento ==''
    or rg ==''
    or cpf == ''
    or telefone == ''
    or email == ''
    or senha == ''
    
    or len(nome_completo) < 3
    or len(nome_completo) > 149
    or len(experiencia)>50
    or len(senha)>79
    or len(email)>255
    or len(rg)>12
    or len(cpf)>14
    or len(telefone)>15

    or rg.isdigit() == False
    or cpf.isdigit() == False
   # or telefone.isdigit() == False
    
 ):
    return 400, ERROR_DATA_NOT_FULLFILL
 
 if(validate_email(email) == False):
    return 400, 'invalid email'
 
 if(validar_cpf(cpf)==False):
    return 400, 'invalid cpf'
 
 if(validar_rg(rg) == False):
    return 400, 'invalid rg'
       
 else:

    try:
       #deixa em lowercase
       nome_completo = nome_completo.lower()
       experiencia = experiencia.lower()
       
       data = inserir_administrador(nome_completo, data_nascimento, rg, cpf, telefone, True, email, senha, experiencia)

       if(data == None):
        return 404, NOT_FOUND
       
       elif(data == False):
          return 500, ERROR_INTERNAL
       
       return 201,data

    except Exception as e:
        return 500, ERROR_INTERNAL


#dados_administrador = inserir_administrador(
   # 'caio palermo cogh lemos',
   # '1990-01-01',
   # '123456789',
  #  '987654321',
  #  '1234567890',
  #  True,
  #  'admin@example.com',
 #   'senha123',
 #   'Experiência do administrador'
#)


#print(add_adm(   
   #'camila pinho',
    #'1990-01-01',
    #'595361274',
    #'49346696800',
    #'595361274',
    #'admin@example.com',
   # 'senha123',
   # 'Experiência do administrador'))

def activation_adm (id):
   
    if( id.isdigit() ==False):
      return 404,ERROR_DATA_NOT_FULLFILL

    try:
        data = desativar_administrador(id)
        return 200, data
   
    except Exception as e:
      return 500, ERROR_INTERNAL
     
#print(activation_adm("3"))


def update_adm(administrador_id, nome_completo, data_nascimento, rg, cpf, telefone, ativo, email, senha, experiencia):
  
  
 cpf = ''.join(filter(str.isdigit, cpf))

 if(
    nome_completo ==''
    or data_nascimento ==''
    or rg ==''
    or cpf == ''
    or telefone == ''
    or email == ''
    or senha == ''
    
    or len(nome_completo) < 3
    or len(nome_completo) > 149
    or len(experiencia)>50
    or len(senha)>79
    or len(email)>255
    or len(rg)>12
    or len(cpf)>14
    or len(telefone)>15

    or rg.isdigit() == False
    or cpf.isdigit() == False
   # or telefone.isdigit() == False
    
 ):
    return 400, ERROR_DATA_NOT_FULLFILL
 
 if(validate_email(email) == False):
    return 400, 'invalid email'
 
 if(validar_cpf(cpf)==False):
    return 400, 'invalid cpf'
 
 if(validar_rg(rg) == False):
    return 400, 'invalid rg'
 
 try:

      data = atualizar_administrador(administrador_id, nome_completo, data_nascimento, rg, cpf, telefone, ativo, email, senha, experiencia)

      if(data != False):
        return 200, data
      else:
         return 404, ERROR_DATA_NOT_FULLFILL


 except Exception as e:
     return 500, ERROR_INTERNAL
 
#______________________________________________________ADD___________________________________________________


# Chamar a função atualizar_administrador com os valores desejados
#print(update_adm(
 #   administrador_id=1,  # ID do administrador que deseja atualizar
 #   nome_completo='camila p3nheiro',
  #  data_nascimento='1990-01-01',
 #   rg='595361274',
 #   cpf='49346696800',
 #   telefone='0987654321',
  #  ativo=True,
  #  email='novo_admin@example.com',
  #  senha='nova_senha123',
  #  experiencia='Nova Experiência do administrador'
#))
#__________________________________________EXISTE NO SISTEMA OU N_____________________
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



