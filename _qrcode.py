import qrcode


def generate_code(description):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.ERROR_CORRECT_L,
        box_size=10,
        border=2
    )

    qr.add_data(description)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')
    img.save('code1.png')


generate_code('https://bbc.com')