import time
import sys
import ibmiotf.application
import ibmiotf.device
import random


organization = "mq4pvv"
deviceType="raspberrypi"
deviceId='123456'
authMethod="token"
authToken="12345678"

def myCommandCallback(cmd):
    print('Command received: %s' %cmd.data)


try:
    deviceOptions={'org':organization, 'type':deviceType, 'id':deviceId, 'auth-method':authMethod, 'auth-token':authToken}
    deviceCli=ibmiotf.device.Client(deviceOptions)


except Exception as e:
    print('caught exception conneting device:%s'%str(e))
    
    sys.exit()

deviceCli.connect()



while True:
    hum=random.randint(1,90)
    temp=random.randint(1,90)
    data={'temperature':temp, 'humidity':hum}
    def myOnPublishCallback():
        print('temperature=%s C' %temp, 'humidity=%s %%' %hum, 'to IBM Watsion')

    success = deviceCli.publishEvent('DHT11','json',data,qos=0,on_publish=myOnPublishCallback)
    if not success:
        print('Not connected to IOTF')

    time.sleep(2)

    deviceCli.commandCallBack=myCommandCallback

deviceCli.disconnect()
