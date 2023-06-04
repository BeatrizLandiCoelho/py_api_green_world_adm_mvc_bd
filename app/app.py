#python -m venv venv
#.\venv\Scripts\activate


from flask import Flask,make_response, jsonify, request

from amd_controller import update_adm,activation_adm,add_adm
app = Flask(__name__)

print(activation_adm("2"))
#__________________________________BY ID ___________________________________

@app.route("/v1/greens-world/adm-by-id", methods=['POST'])
def change_adm_status():

    id =request.json['adm_id']

    operarion_status,adm = activation_adm(id)

    return make_response(
             jsonify(
                status = operarion_status,
                data = adm
               
            )
        )

#__________________________________________________________________________________________
@app.route("/v1/greens-world/update_adm-by-id", methods=['POST'])
def update_adm():

    id =request.json['adm_id']
    nome_completo =request.json['adm_name']
    data_nascimento =request.json['adm_nascimento']
    rg =request.json['adm_rg']
    cpf=request.json['adm_cpf']
    telefone =request.json['adm_telefone']
    ativo =request.json['adm_status']
    email =request.json['adm_email']
    senha =request.json['adm_senha']
    experiencia =request.json['adm_experiencia']


    operarion_status,adm = update_adm(id, nome_completo, data_nascimento, rg, cpf, telefone, ativo, email, senha, experiencia)

    return make_response(
             jsonify(
                status = operarion_status,
                data = adm
               
            )
        )
#______________________________________________________________________________________________________________________________
@app.route("/v1/greens-world/add_adm", methods=['POST'])
def add_adm_route():
    nome_completo = request.json['adm_name']
    data_nascimento = request.json['adm_nascimento']
    rg = request.json['adm_rg']
    cpf = request.json['adm_cpf']
    telefone = request.json['adm_telefone']
    email = request.json['adm_email']
    senha = request.json['adm_senha']
    experiencia = request.json['adm_experiencia']

    operarion_status,adm = add_adm(nome_completo, data_nascimento, rg, cpf, telefone, email, senha, experiencia)
    
    return make_response(
             jsonify(
                status = operarion_status,
                data = adm
               
            )
        )


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
app.run(debug=True, port=8282)

