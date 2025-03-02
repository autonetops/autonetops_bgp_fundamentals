### Tarefa 4: Implementar um Endpoint de Upload de Topologia

Nesta tarefa, você criará um endpoint FastAPI que permite aos usuários fazer upload de um arquivo YAML contendo informações de topologia de rede. Esse endpoint analisará o arquivo YAML e armazenará os detalhes dos dispositivos em um dicionário global para uso em outras tarefas.

#### Passos
1. **Definir o Endpoint**:
   - Crie um endpoint `POST /topology` usando FastAPI.
   - Use o `UploadFile` do FastAPI para aceitar um arquivo YAML.
   - Valide que o arquivo enviado é um YAML (termina em `.yaml` ou `.yml`).
   - Analise o conteúdo YAML e garanta que ele contém uma lista `devices`.
   - Armazene os detalhes de cada dispositivo (IP, tipo, usuário, senha) em um dicionário global chamado `topology`.

2. **Lidar com Erros**:
   - Se o arquivo não for YAML, retorne um erro 400 com a mensagem "Apenas arquivos YAML são permitidos".
   - Se o YAML for inválido ou não contiver uma lista `devices`, retorne um erro 400 com uma mensagem apropriada.

3. **Retornar uma Mensagem de Sucesso**:
   - Após um upload bem-sucedido, retorne uma mensagem confirmando o upload e liste os IPs dos dispositivos.

#### Código Inicial
```python
from fastapi import FastAPI, UploadFile, HTTPException
import yaml

app = FastAPI()
topology = {}  # Dicionário global para armazenar dados da topologia