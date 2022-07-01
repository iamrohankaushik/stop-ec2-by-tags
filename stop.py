import boto3

from datetime import datetime 

ec2 = boto3.resource('ec2', region_name='ap-south-1')
def lambda_handler(event, context):

    now = datetime.now() 
    current_time = now.strftime("%H") 
    print("Current Time is :", current_time)
    
    tagfilter = [{'Name': 'tag:Schedule_On_Off', 'Values': ['Yes']}, {'Name': 'instance-state-name', 'Values': ['running']}, {'Name': 'tag:StopHrs', 'Values': [current_time]}]
    RunningInstances = ec2.instances.filter(Filters=tagfilter)
    ScheduledInstances = [instance.id for instance in RunningInstances]
    print(ScheduledInstances)
    
    if len(ScheduledInstances) > 0:
        ec2.instances.filter(InstanceIds=ScheduledInstances).stop()
        print("Shutting Down" + str(ScheduledInstances))
    else:
        print("Nothing to see here")
