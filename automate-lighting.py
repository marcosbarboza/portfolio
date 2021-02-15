import getmac
from yeelight import Bulb
from datetime import datetime
from time import sleep

bulb = Bulb('192.168.0.112')
# print(bulb.get_properties())
# bulb.set_brightness(100)
# bulb.set_color_temp(6500)


counter_break = 0
counter_continue = 0
state_power = str(bulb.get_properties()["power"])

# """
while True:
    now = datetime.now()
    hour = int(now.hour)
    minute = now.minute
    second = now.second
    if hour >= 17 or hour <= 2:
        adders_mac = str(getmac.get_mac_address(ip='192.168.0.108'))
        time.sleep(1)
        if adders_mac == 'None':
            counter_break = counter_break + 1
            if counter_break > 5:
                if state_power == 'on':
                    bulb.turn_off()
                    counter_continue = 0
                    print('Waiting for the return!')
                else:
                    print('Waiting for the return!')

            else:
                print(f'{counter_break} loss')
        else:
            counter_break = 0
            counter_continue = counter_continue+1

            if counter_continue == 1:
                state_power = str(bulb.get_properties()["power"])
                if state_power == 'off':
                    bulb.turn_on(effect="sudden")
                    bulb.set_brightness(100)
                    bulb.set_rgb(255, 255, 255)
                    bulb.set_color_temp(6500)
                elif state_power == 'on':
                    print(f'Bulb is {state_power}')

            elif counter_continue == 30:
                counter_continue = 0
            print(f'Cont: {counter_continue} MAC: {adders_mac} Time: {hour}:{minute}:{second}')
    else:
        time.sleep(1)
        print(f'Morning is here! {hour}:{minute}:{second}')
# """
