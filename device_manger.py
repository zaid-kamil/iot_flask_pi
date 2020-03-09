from gpiozero import OutputDevice, Motor

from time import sleep


DEVICE_1 = 4
DEVICE_2 = 17
DEVICE_3 = 27
DEVICE_4 = 22
device1 = OutputDevice(DEVICE_1, active_high=False, initial_value=False)
device2 = OutputDevice(DEVICE_2, active_high=False, initial_value=False)
device3 = OutputDevice(DEVICE_3, active_high=False, initial_value=False)
device4 = OutputDevice(DEVICE_4, active_high=False, initial_value=False)

def update_device(device='dev1',status='on'):
    if device == 'dev1':return change_status(device1,status)
    elif device == 'dev2':return change_status(device2,status)
    elif device == 'dev3':return change_status(device3,status)
    elif device == 'dev4':return change_status(device4,status)
    else:
        print(f'{device} not a valid device')
        return False


def change_status(device,status):
    try:
        if status=='on':
            print(f"Setting device{device.pin} : ON")
            device.off()
            return True
        else:
            print(f"Setting device{device.pin} : OFF")
            device.on()
            return False
    except Exception as e:
        print('<--- error --->')
        print(e)
        print('<--- end of error msg <---')
        return False

def get_status(device):
    print(device, device1.value)
    if device =='dev1': return 'unchecked' if device1.value else 'checked'
    elif device == 'dev2': return 'unchecked' if device2.value else 'checked'
    elif device == 'dev3': return 'unchecked' if device3.value else 'checked'
    elif device == 'dev4': return 'unchecked' if device4.value else 'checked'
    else: return None
