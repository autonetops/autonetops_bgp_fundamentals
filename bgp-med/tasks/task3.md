# Tarefa 3: Controle Granular de Rotas com MED

## Objetivo
Configurar o AS 200 para que o AS 100 (R1) use:
- **R2 como link principal** para todas as redes, exceto uma exceção específica.
- **R4** para alcançar a rede 33.3.3.3/32 (Loopback1 de R3).

Você deve usar o atributo MED para direcionar o tráfego de forma granular, refletindo o cenário onde R1-R2 é o caminho primário e R1-R4 é o backup com exceções.

## Instruções
1. **Em R2**:
   - Configure uma *route-map* para definir MED 100 especificamente para a rede 33.3.3.3/32.
   - Deixe o MED padrão (0) para todas as outras redes, tornando R2 o caminho preferido por padrão.
   - Aplique a *route-map* na sessão eBGP com R1.
2. **Em R4**:
   - Configure um MED padrão de 200 para todos os anúncios, tornando R4 menos preferido por padrão.
   - Crie uma exceção com MED 50 para a rede 33.3.3.3/32, tornando R4 o caminho preferido apenas para essa rede.
   - Aplique a *route-map* na sessão eBGP com R1.



## Validação
- Em R2 e R4:
  - `show ip prefix-list`: Confirme que a *prefix-list* NET33 referencia 33.3.3.3/32.
- Em R1:
  - `traceroute 3.3.3.3 source 1.1.1.1`: Deve passar por R2 (192.168.12.2), pois MED 0 (R2) < MED 200 (R4).
  - `traceroute 33.3.3.3 source 1.1.1.1`: Deve passar por R4 (192.168.14.4), pois MED 50 (R4) < MED 100 (R2).
  - `show ip bgp`: Verifique os valores de MED para cada prefixo:
    - 3.3.3.3/32: MED 100 (R2), MED 200 (R4).
    - 33.3.3.3/32: MED 100 (R2), MED 50 (R4).