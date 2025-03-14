### Tarefa 2: Configurar MED

Configure o AS 200 de modo que R1, no AS 100, utilize R4 para alcançar qualquer prefixo anunciado no AS 200. Você deve manipular o MED para realizar essa tarefa.

O MED é usado como uma sugestão para um AS externo sobre o caminho preferido para entrar no AS que está anunciando a métrica. Essa sugestão é utilizada aqui porque o AS que recebe o atributo MED pode usar outro atributo, como weight, que sobrescreve o atributo MED. No que diz respeito ao MED, valores mais baixos têm maior preferência.

### Sugestao
Crie uma route-map e

### NOTA
Observe que o R1 recebe um valor de MED de 100 para todos os prefixos vindos do R2, pois o R1 não recebe um valor de MED do R4. O R1 considera o valor de MED vindo do R4 como zero.

Quando o R1 compara os dois valores de MED vindos do mesmo AS, ele escolhe o caminho com o menor valor de MED, que é o R4.