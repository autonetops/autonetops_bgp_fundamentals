### Tarefa 1: Configurar Peering eBGP

Nesta tarefa, você configurará o BGP externo (eBGP) entre o R1 no AS 100 e o R3 no AS 200. Seu objetivo é estabelecer uma relação de vizinhança BGP e anunciar interfaces *loopback* para que cada roteador possa alcançar as redes do outro.

#### Passos
1. No R1:
   - Configure o BGP com o AS 100.
   - Adicione o R3 (192.168.13.3) como vizinho eBGP.
   - Anuncie o *loopback0* (1.1.1.1/32) e o *loopback1* (10.1.0.1/32) usando um comando *network*.
2. No R3:
   - Configure o BGP com o AS 200.
   - Adicione o R1 (192.168.13.1) como vizinho eBGP.
   - Anuncie o *loopback0* (3.3.3.3/32).
3. Verifique o status dos vizinhos BGP usando `show ip bgp summary`.
4. Verifique a tabela BGP com `show ip bgp` para garantir que as rotas foram trocadas.
5. Teste a conectividade fazendo um *ping* de 3.3.3.3 a partir do R1 e de 1.1.1.1 a partir do R3.

#### Entregáveis
- O BGP está ativo entre R1 e R3.
- O R1 pode fazer *ping* em 3.3.3.3, e o R3 pode fazer *ping* em 1.1.1.1 e 10.1.0.1.

Execute `autonetops task 1` para configurar o estado inicial, se necessário.