#QR Code Generator
import qrcode
print('-='*30)
print('QR Code generator\n')

link = str(input('Enter a link to generate a QR Code:\n'))

generated_code = qrcode.make(link)

generated_code.save('myqrcode.png')

print('QR Code Generated, saved as myqrcode.png\n')
print('-='*30)