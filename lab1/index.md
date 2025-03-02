## Visão Geral
Este laboratório introduz os alunos ao Border Gateway Protocol (BGP), um protocolo crítico para o roteamento entre domínios na internet. Usando imagens Cisco IOL (IOS on Linux) em um ambiente Containerlab, os alunos configurarão uma topologia de múltiplos roteadores para explorar o BGP externo (eBGP), o BGP interno (iBGP) e conceitos chave do BGP, como o atributo next-hop-self.

O laboratório inclui um desafio de solução de problemas para reforçar o aprendizado e uma tarefa de automação de rede usando FastAPI e NAPALM para recuperar informações de vizinhos BGP, demonstrando práticas modernas de rede. O laboratório é projetado para ser envolvente, prático e um excelente exemplo para seus propósitos de divulgação.

## Topologia
O laboratório utiliza uma topologia de três roteadores para demonstrar interações de eBGP e iBGP:

    R1 (AS 100): Um roteador Cisco IOL atuando como o gateway entre AS 100 e AS 200.
    R2 (AS 100): Um roteador Cisco IOL interno ao AS 100, conectado apenas ao R1.
    R3 (AS 200): Um roteador Cisco IOL em um sistema autônomo diferente, conectado ao R1.

### Conexões
    R1 eth1 <-> R3 eth1: Peering eBGP entre AS 100 e AS 200.
    R1 eth2 <-> R2 eth1: Peering iBGP dentro do AS 100.

### Endereçamento IP
Cada roteador possui uma interface loopback0 para identificação e anúncio de rotas:

    R1: 1.1.1.1/32 (Loopback0), 10.1.0.1/32 (Loopback1)
    R2: 2.2.2.2/32 (Loopback0), 10.2.0.1/32 (Loopback2)
    R3: 3.3.3.3/32 (Loopback0)

As interfaces físicas usarão os seguintes endereços IP:

    R1 eth1: 192.168.13.1/24
    R3 eth1: 192.168.13.3/24
    R1 eth2: 192.168.12.1/24
    R2 eth1: 192.168.12.2/24

Esta topologia permite que os alunos explorem como as rotas se propagam através de limites de AS (eBGP) e dentro de um AS (iBGP), com foco no atributo next-hop-self para garantir a alcançabilidade das rotas.