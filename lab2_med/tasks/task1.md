# Tarefa 1: Configurar Sessões eBGP

## Objetivo
Configurar o BGP básico para estabelecer conectividade entre os ASs. O AS 200 (R2, R3, R4) deve formar um *full-mesh* interno (OSPF já foi configurado como IGP), enquanto R2 e R4 estabelecem sessões eBGP com R1 (AS 100). Os roteadores devem anunciar suas interfaces **Loopback0** no BGP.

## Instruções
1. No AS 200:
   - Configure R2, R3 e R4 no AS 200.
   - Certifique-se de que o OSPF (já pré-configurado) mantém a conectividade interna.
   - Não é necessário iBGP *full-mesh* entre R2, R3 e R4, pois o OSPF já distribui as rotas internas.
2. Configure as sessões eBGP:
   - R2 <-> R1: AS 200 para AS 100.
   - R4 <-> R1: AS 200 para AS 100.
3. Anuncie apenas as interfaces **Loopback0** (e.g., 1.1.1.1/32 em R1) no BGP usando o comando `network`.


## Validação
Execute os seguintes comandos:
- `show ip bgp summary`: Verifique se as sessões estão ativas (estado "Established").
- `show ip bgp`: Confirme que as rotas Loopback0 estão sendo anunciadas e recebidas.