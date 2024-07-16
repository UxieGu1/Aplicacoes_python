import pyqrcode

#coloque seu link aqui
qr_url = 'https://github.com/UxieGu1'

#qrcode será gerado aqui
qr_code = pyqrcode.create(qr_url)

#gerado
qr_code.png(
    file='qr_code.png',
    scale=9,
)
