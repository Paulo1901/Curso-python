"""
CONSTANTES = "Variaveis" que não vão mudar
muitas condições no mesmo if (ruin)
    <- contagem de complexidade (ruin)

"""

velocidade = 61 # A velocidade atual do corro
local_carro = 100 # O local que o carro esta na estrada

RADAR_1 = 60 # Volocidade máxima do rodar 1
LOCAL_1 = 100 # Local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o rodar pega

velocidade_carro_paddou_radar_1 =  velocidade > RADAR_1

if velocidade_carro_paddou_radar_1:
    print('Velocidade do carro passou do radar 1')

if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE) and \
        velocidade_carro_paddou_radar_1:
    print('carro multado em radar 1') 