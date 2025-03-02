### Tarefa 5: Modificar o Endpoint `/bgp/neighbors` para Aceitar um IP de Dispositivo

Nesta tarefa, você atualizará o endpoint existente `/bgp/neighbors` para aceitar um parâmetro `device_ip`. Isso permitirá que o endpoint recupere informações de vizinhos BGP de qualquer dispositivo especificado na topologia.

#### Passos
1. **Atualizar o Endpoint**:
   - Modifique o endpoint para `GET /bgp/neighbors/{device_ip}`.
   - Use o parâmetro de caminho `device_ip` para especificar de qual dispositivo recuperar os vizinhos BGP.
   - Verifique se o `device_ip` existe no dicionário `topology`. Caso contrário, retorne um erro 404.

2. **Integrar com NAPALM**:
   - Use o tipo e as credenciais do dispositivo do dicionário `topology` para se conectar via NAPALM.
   - Recupere os dados de vizinhos BGP usando o método `get_bgp_neighbors()` do NAPALM.
   - Armazene os dados recuperados de vizinhos BGP no dicionário `topology` sob uma nova chave, `"bgp_neighbors"`.

3. **Retornar os Dados de Vizinhos BGP**:
   - Retorne o IP do dispositivo e suas informações de vizinhos BGP em formato JSON.

#### Código Inicial
```python
from napalm import get_network_driver
from fastapi import HTTPException

# Seu código aqui