### Tarefa 1: Configurar Peering eBGP

* Configure os roteadores R2, R3 e R4 no AS 200; esses roteadores devem ter uma sessão de peer full-mesh entre eles. R2 e R4 devem ter uma sessão de peer eBGP com R1 no AS 100.
* Os roteadores BGP devem anunciar apenas suas interfaces loopback no BGP.

#### Validacao

sh ip bgp summary
sh ip bgp