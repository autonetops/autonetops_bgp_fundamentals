# Tarefa 2: Configurar o Atributo MED

## Objetivo
Manipular o tráfego do AS 100 (R1) para que ele prefira o caminho via R4 (AS 200) ao alcançar qualquer prefixo anunciado pelo AS 200, usando o atributo MED.

## Contexto
O MED (*Multi-Exit Discriminator*) é uma métrica que o AS 200 envia ao AS 100 para sugerir o caminho preferido de entrada. Valores menores de MED têm maior prioridade. Por padrão, se nenhum MED for especificado, o valor é assumido como 0. Aqui, R1 escolherá R4 se o MED de R4 for menor que o de R2.

## Instruções
1. Em R2:
   - Crie uma *route-map* para definir o MED como 100 para todos os prefixos anunciados a R1.
   - Aplique a *route-map* na sessão eBGP com R1.
2. Em R4:
   - Não configure MED (ou defina como 0 explicitamente), permitindo que R1 o prefira.

## Exemplo de Configuração
Em R2:
```
route-map SET_MED permit 10
set metric 100
!
router bgp 200
neighbor 192.168.12.1 route-map SET_MED out
```


## Validação
Em R1:
- `show ip bgp`: Verifique que os prefixos do AS 200 via R4 têm MED 0 e via R2 têm MED 100.
- `traceroute 2.2.2.2 source 1.1.1.1`: Confirme que o caminho passa por R4 (192.168.14.4).