                                         #QR Code Generator

import qrcode
data = 'https://www.linkedin.com/in/tayyeba-ali-71a66029a/'
img = qrcode.make(data)
img.save('qrcode.png')