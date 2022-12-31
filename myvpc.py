#myami = 'ami-0de07eb85c12b8dbb'

myvpc = '192.168.10.0/24'
#mysub 192.168.10.0/28 and 192.168.10.16/28

import boto3
myclient = boto3.client('ec2')
myami = 'ami-0de07eb85c12b8dbb'
myvpc = '192.168.10.0/24'
myvpcid = myclient.create_vpc(CidrBlock=myvpc)['Vpc']['VpcId']
myclient.create_subnet(CidrBlock='192.168.10.0/28', VpcId=myvpcid)
mysub = myclient.create_subnet(CidrBlock='172.31.16.0/20', VpcId=myvpcid)['Subnet']['SubnetId']
myclient.run_instances(
    ImageId=myami,
    InstanceType='t2.micro',
    SubnetId=mysub,
    MinCount=1,
    MaxCount=1
)
