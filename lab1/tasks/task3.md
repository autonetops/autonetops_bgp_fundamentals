### Tarefa 3: Solucionar Problemas no BGP

Algo está errado! O R2 não consegue ver o prefixo 10.1.0.0/24 do R1, mesmo que o R1 esteja anunciando para o R3. Investigue e corrija o problema.

#### Passos
1. Verifique a tabela BGP no R2 (`show ip bgp`)—o 10.1.0.1/32 está presente?
2. No R1, examine a configuração BGP (`show run | section bgp`).
3. Procure por filtros, políticas ou comandos ausentes que possam estar bloqueando o anúncio para o R2.
4. Corrija o problema e confirme que o R2 agora vê o 10.1.0.1/32.
5. Teste fazendo um *ping* de 10.1.0.1 a partir do R2.

#### Dica
Compare o que o R3 vê com o que o R2 vê. O R1 está tratando seus vizinhos de forma diferente?

#### Entregáveis
- A tabela BGP do R2 inclui 10.1.0.1/32.
- *Ping* bem-sucedido de R2 para 10.1.0.1.