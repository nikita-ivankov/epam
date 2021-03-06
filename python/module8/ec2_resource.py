import boto3

def change_instance_state(region, current_state, action):
    ec2 = boto3.resource('ec2', region_name=region)
    instances = ec2.instances.all()

    for instance in instances:
        print(f'Curren instance is {instance.id}')

        if instance.state['Name'] == current_state:
            if action == 'start':
                print(f'Starting instance {instance.id}')
                ec2.Instance(instance.id).start()
                print('Completed')
            elif action == 'stop':
                print(f'Stopping instance {instance.id}')
                ec2.Instance(instance.id).stop()
                print('Completed')
            elif action == 'reboot':
                print(f'Rebooting instance {instance.id}')
                ec2.Instance(instance.id).reboot()
                print('Completed')
            elif action == 'terminate':
                print(f'Terminating instance {instance.id}')
                ec2.Instance(instance.id).terminate()
                print('Completed')
            else:
                print(f"State of the instance {instance.id} is {instance.state['Name']} but you inputed unknown action....")
        else:
            print(f"State of the instance {instance.id} is {instance.state['Name']}, not additional action required")


if __name__ == '__main__':
    pass
