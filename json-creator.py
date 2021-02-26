import json
import pandas as pd

data = pd.read_excel('C:\\Users\\marco\\PycharmProjects\\jsoncreator\\teste-ip.xlsx')

lista_colunas = data.columns
colunas = []

for item in range(len(lista_colunas)):
    #print(lista_colunas[item])
    colunas.append(lista_colunas[item])

nome = []
matricula = []
email = []
celular = []
dthrvoto = []
key = []
ip = []

for linha in data["Matricula"]:
    matricula.append(linha)
for linha in data["Nome"]:
    nome.append(linha)
for linha in data["E-mail"]:
    email.append(linha)
for linha in data["Celular"]:
    celular.append(linha)
for linha in data["Data/Hora do voto"]:
    dthrvoto.append(linha)
for linha in data["KEY"]:
    key.append(linha)
for linha in data["IP"]:
    ip.append(linha)

for i in range(len(nome)):
    json_data = {colunas[0]: matricula[i], colunas[1]: nome[i], colunas[2]: email[i], colunas[3]: celular[i], colunas[4]: str(dthrvoto[i]),
                 colunas[5]: key[i], colunas[6]: ip[i]}
    compile_json_data = json.dumps(json_data)

    j_out = json.loads(compile_json_data)
    print(j_out)
    # print(compile_json_data)
