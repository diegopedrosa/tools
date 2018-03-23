from aws import MachinesAWS

if __name__ == '__main__':
    machines = MachinesAWS(sistema='xyz', ambiente='desenvolvimento')

    machines.lista  # lista o id das maquinas
    machines.liga  # liga a lista das listas da maquina
    # noinspection PyStatementEffect
    machines.desliga  # desliga as maquinas
