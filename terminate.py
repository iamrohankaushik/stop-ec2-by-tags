import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

ec2 = boto3.resource('ec2')
def lambda_handler(event, context):

    filters = [{'Name': 'tag:AutoOff', 'Values': ['yes']}, {'Name': 'instance-state-name', 'Values': ['running']}]
    instances = ec2.instances.filter(Filters=filters)
    RunningInstances = [instance.id for instance in instances]
    
    if len(RunningInstances) > 0:
        shuttingDown = ec2.instances.filter(InstanceIds=RunningInstances).terminate()
        print("ShuttingDown")
    else:
        print("Nothing to see here")
