import qrcode

inp_text = input("Enter text or URL: ").strip()
filename = input("Enter file name: ").strip()
qr = qrcode.make(box_size=10,border=4,data=inp_text)
qr.save(filename)
