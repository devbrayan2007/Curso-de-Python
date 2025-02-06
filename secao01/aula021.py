# VARIÁVEIS, CONSTANTES E COMPLEXIDADE DE CÓDIGO

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

velocidade = 50
local_carro = 90

if velocidade > RADAR_1:
    print(f'Carro com velocidade {velocidade}km/h passou do radar')
    
if local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE) and velocidade > RADAR_1:
    print('Carro multado em radar 1')