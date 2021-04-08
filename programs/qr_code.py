import qrcode
def generate(data, img_name):
    img = qrcode.make(data) #generate QRcode
    img.save(img_name)
    return img

data, name = input('Enter text: '), input('Enter img-name: ')
name = name + '.png'
generate(data, name)
