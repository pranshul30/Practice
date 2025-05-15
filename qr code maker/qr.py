import qrcode
website ='https://www.youtube.com/watch?v=dQw4w9WgXcQ'
qr=qrcode.QRCode(version=1,box_size=5,border=5)
qr.add_data(website)
qr.make()
img=qr.make_image(fill_color='black',back_color='white')
img.save('yt_qr.png')
