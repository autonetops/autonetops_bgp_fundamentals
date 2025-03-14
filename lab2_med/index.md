## Visão Geral
Outro atributo BGP que podemos usar para manipular como um AS externo entrará em nosso AS local é o discriminador de saída múltipla (MED), que é muito útil nesse cenário. No entanto, para que isso funcione, o AS externo deve ser configurado para aceitar o atributo MED. Além disso, por padrão, o MED só funcionará em cenários onde o AS local está multihomed para o mesmo AS externo, conforme ilustrado.


## Topologia
![bgp_fundamentals_lab2_med](https://ubjpcyfllztpftxqaldu.supabase.co/storage/v1/object/sign/img/labs/lab/md/bgp_path_manipulation_with_med.webp?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJpbWcvbGFicy9sYWIvbWQvYmdwX3BhdGhfbWFuaXB1bGF0aW9uX3dpdGhfbWVkLndlYnAiLCJpYXQiOjE3NDE5NjI4MTMsImV4cCI6MTg5OTY0MjgxM30.X94Qr_6ppmtTa8Hh6n3dlDSMINg0ft_LwcKVOFYw_yo)

O laboratório utiliza uma topologia de três roteadores para demonstrar manipulação de rotas com MED:


### Conexões
    R1 <-> R2: Peering eBGP entre AS 100 e AS 200.
    R1 <-> R4: Peering eBGP entre AS 100 e AS 200.
    R2 <-> R3: Peering eBGP entre AS 200 e AS 200.
    R3 <-> R4: Peering eBGP entre AS 200 e AS 200.


### Endereçamento IP
Cada roteador possui uma interface loopback0 para identificação e anúncio de rotas:

    R1: 1.1.1.1/32 (Loopback0)
    R2: 2.2.2.2/32 (Loopback0)
    R3: 3.3.3.3/32 (Loopback0)
    R4: 4.4.4.4/32 (Loopback0)

Boa sorte e bons estudos!