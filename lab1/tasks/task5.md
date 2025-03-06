### Tarefa 5: Modificar o Endpoint `/bgp/neighbors` para Aceitar um IP de Dispositivo

Nesta tarefa, você atualizará o endpoint existente `/bgp/neighbors` para aceitar um parâmetro `device_ip`. Isso permitirá que o endpoint recupere informações de vizinhos BGP de qualquer dispositivo especificado na topologia.

#### Passos
1. **Atualizar o Endpoint**:
   - Adicione um endpoint para `GET /bgp/neighbors/{device_ip}`.
   - Use o parâmetro de caminho `device_name` para especificar de qual dispositivo recuperar os vizinhos BGP.
   - Verifique se o `device_name` existe na topologia. Caso contrário, retorne um erro 404.

2. **Integrar com NAPALM**:
   - Use o tipo e as credenciais do dispositivo para se conectar via NAPALM.
   - Recupere os dados de vizinhos BGP usando o método `get_bgp_neighbors()` do NAPALM.

3. **Retornar os Dados de Vizinhos BGP**:
   - Retorne o IP do dispositivo e suas informações de vizinhos BGP em formato JSON.

#### Código Inicial
```python
from napalm import get_network_driver
from fastapi import HTTPException

@app.get("/bgp/neighbors/{device_name}")
def get_bgp_neighbors(device_name: str):
# Seu código aqui
```