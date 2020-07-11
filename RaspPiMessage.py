# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import random
import time
import requests as req

resp = req.get("http://192.168.1.9:15000//local/VehicleCounter/getDiagnostics.cgi")

#print(resp.text)

# Using the Python Device SDK for IoT Hub:
#   https://github.com/Azure/azure-iot-sdk-python
# The sample connects to a device-specific MQTT endpoint on your IoT Hub.
from azure.iot.device import IoTHubDeviceClient, Message

# The device connection string to authenticate the device with your IoT hub.
# Using the Azure CLI:
# az iot hub device-identity show-connection-string --hub-name {YourIoTHubName} --device-id MyNodeDevice --output table
CONNECTION_STRING = "HostName=MQTTMagentaRP.azure-devices.net;DeviceId=magRaspberryPi;SharedAccessKey=m+ix780fsw57DLRK8B2G7BONUhbYRTSQSxe9oGmxD7U="


def iothub_client_init():
    # Create an IoT Hub client
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    return client

def iothub_client_telemetry_sample_run():

    try:
        client = iothub_client_init()
        print ( "IoT Hub device sending periodic messages, press Ctrl-C to exit" )

        while True:
            resp = req.get("http://192.168.1.9:15000//local/VehicleCounter/getDiagnostics.cgi")
            print(resp.text)
            client.send_message(resp.text)
            print ( "Message successfully sent" )
            time.sleep(10)


    except KeyboardInterrupt:
        print ( "IoTHubClient sample stopped" )

if __name__ == '__main__':
    print ( "IoT Hub Quickstart" )
    print ( "Press Ctrl-C to exit" )
    iothub_client_telemetry_sample_run() 
