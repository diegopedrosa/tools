__author__ = "Diego Pedrosa"
__copyright__ = "MIT"

import boto3
import os


class MachinesAWS:

    def __init__(self, ambiente, sistema, nome=None):
        self.ec2 = boto3.resource('ec2', region_name=os.environ['aws_region_name'])

        self.sistema = sistema
        self.ambiente = ambiente
        self.nome = nome

    def filter(self, state=None):
        filters = [{
            'Name': 'tag:Sistema',
            'Values': [self.sistema]
        },
            {
                'Name': 'tag:Ambiente',
                'Values': [self.ambiente]
            }
        ]
        if state:
            print("OK")
            filters.append({
                'Name': 'instance-state-name',
                'Values': [state]
            })

        if self.nome:
            filters.append({
                'Name': 'tag:Name',
                'Values': [self.nome]
            })

        return filters

    @property
    def liga(self):

        instances = self.ec2.instances.filter(Filters=self.filter('stopped'))

        startinstances = [instance.id for instance in instances]

        if len(startinstances) > 0:
            return self.ec2.instances.filter(InstanceIds=startinstances).start()

    @property
    def desliga(self):

        instances = self.ec2.instances.filter(Filters=self.filter(state='running'))

        startinstances = [instance.id for instance in instances]

        if len(startinstances) > 0:
            return self.ec2.instances.filter(InstanceIds=startinstances).stop()

    @property
    def lista(self):

        instances = self.ec2.instances.filter(Filters=self.filter())

        for instance in instances:
            print('%s' % instance.id)
