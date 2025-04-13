### Tarefa 2: Configurar iBGP com Next-Hop-Self

Agora, configure o BGP interno (iBGP) entre R1 e R2 dentro do AS 100. Como o R2 não está diretamente conectado ao R3, o R1 deve compartilhar as rotas do AS 200 com o R2. Você usará o recurso *next-hop-self* para fazer isso funcionar.

#### Passos
1. No R1:
   - Adicione o R2 (2.2.2.2) como vizinho iBGP usando endereços *loopback* para estabilidade.
   - Habilite o `next-hop-self` para o vizinho R2.
   - Atualize a tabela de roteamento para incluir o *loopback* do R2 (rota estática ou IGP).
2. No R2:
   - Configure o BGP com o AS 100.
   - Adicione o R1 (1.1.1.1) como vizinho iBGP usando endereços *loopback*.
   - Anuncie o *loopback0* (2.2.2.2/32) e o *loopback2* (10.2.0.1/32).
   - Adicione uma rota estática para alcançar 1.1.1.1 via 192.168.12.1.
3. Verifique com `show ip bgp` no R2 que ele enxerga 3.3.3.3/32 vindo do R1.
4. Teste fazendo um *ping* de 3.3.3.3 a partir do R2.

#### Dica
Sem o `next-hop-self`, o R2 não saberá como alcançar o IP de próximo salto do R3 (192.168.13.3). Esse é um conceito chave do BGP!

#### Entregáveis
- O iBGP está ativo entre R1 e R2.