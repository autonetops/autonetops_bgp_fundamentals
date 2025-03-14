## Visão Geral
Outro atributo BGP que podemos usar para manipular como um AS externo entrará em nosso AS local é o discriminador de saída múltipla (MED), que é muito útil nesse cenário. No entanto, para que isso funcione, o AS externo deve ser configurado para aceitar o atributo MED. Além disso, por padrão, o MED só funcionará em cenários onde o AS local está multihomed para o mesmo AS externo, conforme ilustrado.


## Topologia
![bgp_fundamentals_lab2_med](https://ubjpcyfllztpftxqaldu.supabase.co/storage/v1/object/sign/img/labs/lab/md/bgp_fundamentals_diagram.webp?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJpbWcvbGFicy9sYWIvbWQvYmdwX2Z1bmRhbWVudGFsc19kaWFncmFtLndlYnAiLCJpYXQiOjE3NDA5NDA5NTUsImV4cCI6MTg5ODYyMDk1NX0.Eun52MyKJbWMVVXHM9eDiwCbHkVYKaLv1ZH1aSSOGLg)

O laboratório utiliza uma topologia de três roteadores para demonstrar interações de eBGP e iBGP:


### Conexões
    R1 eth1 <-> R3 eth1: Peering eBGP entre AS 100 e AS 200.


### Endereçamento IP
Cada roteador possui uma interface loopback0 para identificação e anúncio de rotas:

    R1: 1.1.1.1/32 (Loopback0)
    R2: 2.2.2.2/32 (Loopback0)
    R3: 3.3.3.3/32 (Loopback0)
    R4: 4.4.4.4/32 (Loopback0)

Boa sorte e bons estudos!