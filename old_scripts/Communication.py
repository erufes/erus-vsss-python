import array
import math
import time
import serial


class Communication:
    def __init__(self, port='COM0', bauds=4800):
        self.ser = serial.Serial(port, bauds, timeout=1)
        time.sleep(1)
        self.ser.flush()

    def send_message(self, msg):
        self.ser.write(msg.tostring())	

    def sendCommand(self, robotId, cmdId, value):
        print ('\0', robotId, cmdId, value)
        self.ser.write('\0')
        self.ser.write(robotId)
        self.ser.write(cmdId)
        self.ser.write(value)

    def set_speed_right(self, rid, speed):
        if speed > 255:
            speed = 255
        if speed < -255:
            speed = -255

        self.sendCommand(rid, 'r', chr(speed/2 + 128))

    def set_pwm_right(self, rid, speed):
        if speed > 255:
            speed = 255
        if speed < -255:
            speed = -255

        self.sendCommand(rid, 'R', chr(speed/2 + 128))

    def set_speed_left(self, rid, speed):
        if speed > 255:
            speed = 255
        if speed < -255:
            speed = -255

        self.sendCommand(rid, 'l', chr(speed/2 + 128))

    def set_pwm_left(self, rid, speed):
        if speed > 255:
            speed = 255
        if speed < -255:
            speed = -255

        self.sendCommand(rid, 'L', chr(speed/2 + 128))

    def set_speed(self, rid, left, right):
        b = rid
        b << 1

        if left > 255:
            left = 255
            b &= 0x01
        elif left < -255:
            left = -255
            b |= 0x01

        b << 1

        if right > 255:
            right = 255
            b &= 0x01
        elif right < -255:
            right = -255
            b |= 0x01

        cmd = chr(b)+chr(left)+chr(right)
        serial.write(cmd)

    def stop(self, rid):
        #self.sendCommand(rid, 'l', chr(128))
        #self.sendCommand(rid, 'r', chr(128))
        self.sendCommand(rid, 's', chr(128))
        self.sendCommand(rid, 's', chr(128))

class Message:
    def __init__(self):
        self.vector = []

    def add_new_param(self, vl, vr):
        self.vector.append(vl)
        self.vector.append(vr)

    def tostring(self):
        return array.array('B', self.vector).tostring()

    def create_header(self):
        header = 0
        for x in self.vector:
            header <<= 1
            if x < 0:
                header |= 0x01
        return header

    def generate_message(self):
        header = self.create_header()
        self.vector = [header] + [abs(x) for x in self.vector]
