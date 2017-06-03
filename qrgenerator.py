import qrcode
def createqr(text):
    img = qrcode.make(text)
    path = './qr/qrcode.png'
    img.save(path)
