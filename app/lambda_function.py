import boto3

def get_bootstrap():
   return '''
#!/bin/bash
aws_instance_id = `curl -s http://169.254.169.254/latest/meta-data/instance-id`
yum install python3
echo "
import os
id = os.getenv('aws_instance_id')
session = boto3.Session()
ec2= boto3.resoure('ec2')
instance = ec2.Instance(id)
instance.terminate()
"

shutdown -h now
'''


def create ec2(region):
   tags = [{'Key'}: 'Name', 'Value':'adsfads']
   sg_list= ["id","",""]
   subnet = "id"
   proxies = ""
   boto3_resource = boto3.resource('ec2', region_name= region)
   create_instance_repsonse = boto3_resoruce.create_instance(
   ImageId=api,
   MinCount=1
   MaxCount=2
   InstanceType=..
   SubnetId=
   SecurityGroupIds=
   CreditSpecification={'CpuCredits': 'unlimited'})
   TagSpecifications=[{'ResourceType'}: 'instance', 'Tags': tags]
   InstanceInitiatedShutdownBehavior="terminate"
   UserData=get_bootstrap()
   )
   return create_instance_repsonse[0].id
   
def lambda_handler(event,context):
   id = create_ec2()
   print(id)
