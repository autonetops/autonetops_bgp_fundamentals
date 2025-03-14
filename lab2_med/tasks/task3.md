### Tarefa 3

Configure o(s) roteador(es) apropriado(s) no AS 200 para que o AS 100 passe pelo R4 para alcançar a rede 33.3.3.3/32 e pelo R2 para alcançar a rede 3.3.3.3/32.
Você deve utilizar o MED para realizar essa tarefa.

#### Sugestoes
No R2, configure as seguintes duas prefix lists (NET3 e NET33), que fazem referência às redes 3.3.3.3/32 e 33.3.3.3/32, respectivamente:

Nota: É muito fácil lembrar que a prefix list NET3 faz referência à rede 3.3.3.3/32 e a prefix list NET33 faz referência à rede 33.3.3.3/32. No entanto, sempre que possível, você deve escolher um nome significativo.

#### Verificacao
show ip prefix-list
A partir do R1:
    traceroute 3.3.3.3 source 1.1.1.1 
    traceroute 33.3.3.3 source 1.1.1.1