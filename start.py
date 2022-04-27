import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

ec2 = boto3.resource('ec2')
def lambda_handler(event, context):

    filters = [{'Name': 'tag:AutoTermination', 'Values': ['True']}, {'Name': 'instance-state-name', 'Values': ['stopped']}]
    instances = ec2.instances.filter(Filters=filters)
    RunningInstances = [instance.id for instance in instances]
    
    if len(RunningInstances) > 0:
        shuttingDown = ec2.instances.filter(InstanceIds=RunningInstances).start()
        print("Starting")
    else:
        print("Nothing to see here")
