### Tarefa 4: Implementar um Endpoint de Upload de Topologia

Nesta tarefa, você criará um endpoint FastAPI que permite aos usuários fazer upload de um arquivo YAML contendo informações de topologia de rede. Esse endpoint analisará o arquivo YAML e armazenará os detalhes dos dispositivos em um dicionário global para uso em outras tarefas.

#### DNS da Topologia
 - clab-bgp_fundamentals-r1
 - clab-bgp_fundamentals-r2
 - clab-bgp_fundamentals-r3

#### Validar acesso aos dispositivos com NAPALM
 - napalm --help
 # Exemplo:
   napalm --user admin --password autonetops --vendor [ios/eos]clab-bgp_fundamentals-r1 call [get_facts,get_interfaces_ip,get_bgp_neighbors]

   [napalm_getters](https://napalm.readthedocs.io/en/latest/support/)



#### Passos
0. **Estrutura**
   - Crie um arquivo chamado main.py
   - Após escrever o código com FastAPI rode o servidor com:
     - (Documentaçao)[https://fastapi.tiangolo.com/]
   - Acesse seu servidor externamete com a seguinte URL:
     - echo $TF_VAR_VPN_CODESPACES_2222
     
1. **Definir o Endpoint**:
   - Um endpoint para o usuário ver qual a topologia e os acessos
   - Crie um endpoint `GET /topology` usando FastAPI.
   - Leia o arquivo `topology.yaml`
   - Retorne as informações para o usuário


#### Código Inicial
```python
from fastapi import FastAPI, HTTPException
import yaml

app = FastAPI()
```

#### Apos o codigo estiver pronto
