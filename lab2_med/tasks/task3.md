# Tarefa 3: Controle Granular de Rotas com MED

## Objetivo
Configurar o AS 200 para que o AS 100 (R1) use:
- R4 para alcançar a rede 33.3.3.3/32 (Loopback1 de R3).
- R2 para alcançar a rede 3.3.3.3/32 (Loopback0 de R3).

Você deve usar o MED para direcionar o tráfego de forma granular.

## Instruções
1. Em R2:
   - Crie *prefix-lists* para identificar 3.3.3.3/32 e 33.3.3.3/32.
   - Use uma *route-map* para definir MED 50 para 33.3.3.3/32 e MED 10 para 3.3.3.3/32.
   - Aplique na sessão com R1.
2. Em R4:
   - Configure MED 10 para 33.3.3.3/32 e MED 50 para 3.3.3.3/32 (inverso de R2).
   - Aplique na sessão com R1.


## Validação
- `show ip prefix-list`: Confirme as *prefix-lists* em R2 e R4.
- Em R1:
  - `traceroute 3.3.3.3 source 1.1.1.1`: Deve passar por R2 (192.168.12.2).
  - `traceroute 33.3.3.3 source 1.1.1.1`: Deve passar por R4 (192.168.14.4).
- `show ip bgp`: Verifique os valores de MED para cada prefixo.