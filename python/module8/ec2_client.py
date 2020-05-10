import boto3

def change_instance_state(region, current_state, action):
    ec2 = boto3.client('ec2', region_name=region)
    for instance in ec2.describe_instances()['Reservations']:

        print(f"Current instance is {instance['Instances'][0]['InstanceId']}")

        if instance['Instances'][0]['State']['Name'] == current_state:
            if action == 'start':
                print(f"Starting instance {instance['Instances'][0]['InstanceId']}")
                ec2.start_instances(InstanceIds=[instance['Instances'][0]['InstanceId']])
                waiter = ec2.get_waiter('instance_started')
                waiter.wait(InstanceIds=[instance['Instances'][0]['InstanceId']])
                print('Completed')
            elif action == 'stop':
                print(f"Stopping instance {instance['Instances'][0]['InstanceId']}")
                ec2.stop_instances(InstanceIds=[instance['Instances'][0]['InstanceId']])
                waiter = ec2.get_waiter('instance_stopped')
                waiter.wait(InstanceIds=[instance['Instances'][0]['InstanceId']])
                print('Completed')
            elif action == 'reboot':
                print(f"Rebooting instance {instance['Instances'][0]['InstanceId']}")
                ec2.reboot_instances(InstanceIds=[instance['Instances'][0]['InstanceId']])
                waiter = ec2.get_waiter('instance_started')
                waiter.wait(InstanceIds=[instance['Instances'][0]['InstanceId']])
                print('Completed')
            elif action == 'terminate':
                print(f"Terminating instance {instance['Instances'][0]['InstanceId']}")
                ec2.terminate_instances(InstanceIds=[instance['Instances'][0]['InstanceId']])
                waiter = ec2.get_waiter('instance_terminated')
                waiter.wait(InstanceIds=[instance['Instances'][0]['InstanceId']])
                print('Completed')
            else:
                print(
                    f"State of the instance {instance['Instances'][0]['InstanceId']} is {instance['Instances'][0]['State']['Name']} but you inputed unknown action....")
        else:
            print(f"State of the instance {instance['Instances'][0]['InstanceId']} is {instance['Instances'][0]['State']['Name']}, not any action required")


if __name__ == '__main__':
    change_instance_state('us-east-1', 'stopped', 'start')