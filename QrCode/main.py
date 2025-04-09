import qrcode

linkdin_acount_link = "https://www.linkedin.com/in/tayyeba-ali-71a66029a/"

img = qrcode.make(linkdin_acount_link)

img.save('E:/Giaic/QUATER 3/class assigment/QrCode/myqrcode.png')