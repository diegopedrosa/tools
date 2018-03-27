# Tools
Ferramentas para facilitar a o desenvolvimento e automatizar tratamento de incidentes.

* **`checkip`**: Checar geolocalização do endereço ip.

           checkip 8.8.8.8
           checkip ips.txt

* **`aws`**: ligar, listar e desligar maquinas na aws.

           machines = MachinesAWS(sistema='xyz', ambiente='poc')
           machines.lista  # lista o id das maquinas
           machines.liga  # liga a lista das listas da maquina
           machines.desliga  # desliga as maquinas

* **`finddomains`**: Achar domínios por string.
   
           finddomains google

* **`findgithub`**: Fazer buscas no github.

           findgithub poker
           findgithub "poker com amigos"


