import time
import struct


class Slicing:
    def __init__(self, msg):
        self.msg = msg

    def temp(self, correction=0):
        temp = struct.unpack('!f', bytes.fromhex(self.msg[26:34]))[0]
        print(temp)
        print('수온 : ', temp + correction, '°C')

    def oxygen(self, correction=0):
        # percent = struct.unpack('!f', bytes.fromhex(self.msg[34:42]))[0]
        milligram_per_liter = struct.unpack(
            '!f', bytes.fromhex(self.msg[42:50]))[0]
        print(milligram_per_liter)
        # ppm = struct.unpack('!f', bytes.fromhex(self.msg[50:58]))[0]
        # print('용존산소 : ', percent, '%')
        print('용존산소 : ', milligram_per_liter + correction, 'mg/l')
        # print('용존산소 : ', ppm, 'ppm')

    def ph(self, correction=0):
        ph = struct.unpack('!f', bytes.fromhex(self.msg[66:74]))[0]
        print(ph)
        # redox = struct.unpack('!f', bytes.fromhex(self.msg[74:82]))[0]
        # meter = struct.unpack('!f', bytes.fromhex(self.msg[82:90]))[0]
        print('pH : ', ph + correction, 'pH')
        # print('redox: ', redox, 'mV')
        # print('pH_meter : ', meter, 'mV')

    def conductivity(self, correction=0):
        # electrical_conductivity = struct.unpack(
        #     '!f', bytes.fromhex(self.msg[98:106]))[0]
        salinity = struct.unpack('!f', bytes.fromhex(self.msg[106:114]))[0]
        print(salinity)
        # total_dissolved_solids = struct.unpack(
        #     '!f', bytes.fromhex(self.msg[114:122]))[0]
        print('염도: ', salinity + correction, 'ppt')
