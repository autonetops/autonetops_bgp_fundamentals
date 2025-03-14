# Laboratório: Manipulação de Rotas BGP com o Atributo MED

## Visão Geral
Bem-vindo ao laboratório sobre o atributo BGP **Multi-Exit Discriminator (MED)**! Neste exercício, você aprenderá como usar o MED para influenciar a entrada de tráfego de um AS externo (Autonomous System) em seu AS local. O MED é um atributo opcional do BGP que sugere ao AS vizinho qual caminho preferir ao entrar no seu AS. Quanto menor o valor do MED, maior a preferência. 

Por padrão, o MED é mais eficaz em cenários **multihomed**, onde um AS local se conecta a múltiplos pontos do mesmo AS externo. Para que funcione, o AS externo deve aceitar o MED e não sobrescrevê-lo com atributos de maior prioridade, como o *weight*. Vamos explorar isso passo a passo!

## Contexto
Imagine que temos um **datacenter** operando no AS 200, com roteadores de borda (R2 e R4) conectados a uma filial no AS 100 por meio de dois links distintos. Nosso objetivo é anunciar as redes do datacenter para a filial através desses roteadores de borda e controlar como o tráfego da filial entra no AS 200.

- **Link Principal**: A conexão entre R1 (AS 100) e R2 (AS 200) será usada como o caminho primário para a maioria do tráfego.
- **Link de Backup**: A conexão entre R1 (AS 100) e R4 (AS 200) será reservada como backup e utilizada apenas para redes específicas, conforme configurarmos com o MED.

Neste laboratório, você ajustará o MED para direcionar o tráfego da filial (AS 100) de acordo com essas preferências, simulando um cenário real de controle de entrada em um datacenter.

## Topologia
![Topologia do Laboratório BGP MED](https://ubjpcyfllztpftxqaldu.supabase.co/storage/v1/object/sign/img/labs/lab/md/bgp_path_manipulation_with_med.webp?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJpbWcvbGFicy9sYWIvbWQvYmdwX3BhdGhfbWFuaXB1bGF0aW9uX3dpdGhfbWVkLndlYnAiLCJpYXQiOjE3NDE5NjI4MTMsImV4cCI6MTg5OTY0MjgxM30.X94Qr_6ppmtTa8Hh6n3dlDSMINg0ft_LwcKVOFYw_yo)

Este laboratório utiliza uma topologia com **quatro roteadores** (R1, R2, R3 e R4) para demonstrar a manipulação de rotas com o atributo MED. A estrutura forma um quadrado, permitindo múltiplos caminhos entre os ASs, ideal para testar o controle de tráfego.

### Conexões
- **R1 <-> R2**: Peering eBGP entre AS 100 (R1) e AS 200 (R2).
- **R1 <-> R4**: Peering eBGP entre AS 100 (R1) e AS 200 (R4).
- **R2 <-> R3**: Conexão interna no AS 200 (usaremos OSPF como IGP).
- **R3 <-> R4**: Conexão interna no AS 200 (usaremos OSPF como IGP).

### Endereçamento IP
Cada roteador possui interfaces **Loopback0** e **Loopback1** para identificação e anúncio de rotas no BGP:
- **R1**: Lo0: 1.1.1.1/32, Lo1: 11.1.1.1/32
- **R2**: Lo0: 2.2.2.2/32, Lo1: 22.2.2.2/32
- **R3**: Lo0: 3.3.3.3/32, Lo1: 33.3.3.3/32
- **R4**: Lo0: 4.4.4.4/32, Lo1: 44.4.4.4/32

### Objetivo
Você configurará sessões BGP e usará o MED para direcionar o tráfego do AS 100 (R1) para prefixos específicos no AS 200 (R2, R3, R4). Prepare-se para explorar o poder da manipulação de rotas!

Boa sorte e bons estudos!