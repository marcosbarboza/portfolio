import pyvda
from datetime import datetime
import time

# -----Gerando Logs-----  #
data = datetime.now()
nome_arquivos = str(input("Insira a Data: "))

# -----Projetos----- #
cmrvpi = 1
infraprev = 2
eleicaonet = 3

# -----Contador----- #
counter_crmvpi = 0
counter_infraprev = 0
counter_eleicaonet = 0
counter_extra = 0
hora_extra_prevista = 5

# -----Função-----  #
while True:
    desktops = pyvda.GetCurrentDesktopNumber()
    if desktops == cmrvpi:
        print(f'CRMVPI ->> T+ {counter_crmvpi}')
        counter_crmvpi += 1
        time.sleep(1)
    elif desktops == infraprev:
        print(f'INFRAPREV ->> T+ {counter_infraprev}')
        counter_infraprev += 1
        time.sleep(1)
    elif desktops == eleicaonet:
        print(f'EleicaoNet ->> T+ {counter_eleicaonet}')
        counter_eleicaonet += 1
        time.sleep(1)

        # ----- Validation de Tempo----- #
    if counter_crmvpi + counter_infraprev + counter_eleicaonet == 28800:
        arquivo_project = open("Log de Projeto - "+nome_arquivos, "a")
        projetos = list()
        projetos.append('CRMVPI: '+str(counter_crmvpi)+"\n")
        projetos.append('INFRAPREV: '+str(counter_infraprev)+"\n")
        projetos.append('ELEICAONET: ' + str(counter_eleicaonet) + "\n")
        print(projetos)
        arquivo_project.writelines(projetos)

        print("Inicio de Hora Extra")
        tem_extra = str(input('Haverá Horas Extras ? '))

        if tem_extra == 'sim':
            hora_extra_projeto = input('Insira o nome do projeto extra: ')
            hora_extra_prevista = int(input('Insira o tempo previsto em segundos: '))
            log_hora_extra = open('Log de Horas Extras - ' + nome_arquivos, 'a')
            while counter_extra <= hora_extra_prevista:
                log_hora_extra.write('HORA EXTRA: '+str(hora_extra_projeto)+' '+str(counter_extra)+'\n')
                print('HORA EXTRA: '+str(hora_extra_projeto)+' '+str(counter_extra))
                counter_extra += 1
                time.sleep(1)
            else:
                break

        elif tem_extra == 'nao':
            print('Expediente Encerrado!')
            print('Sistema Finalizado \n Logs Gerados')
            break

# current_window_handle = win32gui.GetForegroundWindow()
# pyvda.MoveWindowToDesktopNumber(current_window_handle, 1)
# pyvda.GoToDesktopNumber(2)
# pyvda.GoToDesktopNumber(1)
# window_move_to = pyvda.GetWindowDesktopNumber(current_window_handle)
# print(window_move_to)
