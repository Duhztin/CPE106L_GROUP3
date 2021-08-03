import cv2
import numpy as np
from pyzbar.pyzbar import decode


#sampleQrCode = cv2.imread('Kian_QR.png')
capture = cv2.VideoCapture(0)
capture.set(3, 640)
capture.set(4, 480)

with open('authenticate') as out:
    authen = out.read().splitlines()
while True:
    success, sampleQrCode = capture.read()
    for barcode in decode(sampleQrCode):
        #print(barcode.data)
        sample = barcode.data.decode('utf-8')
        print(sample)

        if sample in authen:
            authorized = 'THIS IS A MAPUAN'
            bgcolor = (0, 255, 0)
        else:
            authorized = 'THIS IS NOT A MAPUAN'
            bgcolor = (0, 0, 255)
        size = np.array([barcode.polygon], np.int32)
        size = size.reshape((-1, 1, 2))
        cv2.polylines(sampleQrCode, [size], True, bgcolor)

        size2 = barcode.rect
        cv2.putText(sampleQrCode, authorized, (size2[0],size2[1]),cv2.FONT_HERSHEY_SIMPLEX, 0.9, bgcolor,3)

    cv2.imshow('Result', sampleQrCode)
    cv2.waitKey(1)