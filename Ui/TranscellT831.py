import serial
import re
import time


r_pun_data = r'\d(?P<data>[\+|-]\d{1,5})'

pattern = re.compile(r_pun_data)
#a_list=np.arange(1)

def dev(i):
    return i/100

if __name__ == '__main__':
    serial = serial.Serial('COM1', 9600)
    print serial
    if serial.isOpen():
       print("open success")
    else:
        print("open failed")


    try:
        while True:
            count = serial.inWaiting()
            if count > 30:
                time.sleep(0.03)
                data = serial.read(count)
                #if
                #print data
                a= pattern.findall(data)
                a=map(float,a)
                a=map(dev,a)
                a=a
                #self.parent.puncual=np.append(self.parent.puncual, [1])

                #a = a.astype(np.float)
                print a
                #print 'ok'
#                if data != b'':
#                    print("receive:", data)
#                    serial.write(data)
#                else:
#                    serial.write(hexsend(data))
    except KeyboardInterrupt:
        if serial != None:
            serial.close()
