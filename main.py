import qrcode

#Welcome message durr
welcome = "Welcome to this QR generator by StephenWilde.net"

#list for file extentions
ext = ["jpg", "png", "gif"]

#Step 1 Txt of QRcode
print(welcome)
print("Enter your QRcode TXT")
qrcodeInput = input()

#Step 2 File Name
print("Enter the name of the image")
qrcodeFName = input()
#replaces all empty strings with _ for a reason! just sayin
qrcodeFName = qrcodeFName.replace(" ", "_")
img = qrcode.make(qrcodeInput)

#Step 3 File extension
print("Please enter a number to your file extension\n1 for jpg\n2 for png\n3 for gif" )
qrcodeFExt = input()
qrcodeFExt = int(qrcodeFExt)

if qrcodeFExt == 1:
    img.save(qrcodeFName + "." + (ext[0]))
    print("Saved as " + qrcodeFName + "." + (ext[0]))

elif qrcodeFExt == 2:
    img.save(qrcodeFName + "." + (ext[1]))
    print("Saved as " + qrcodeFName + "." + (ext[1]))

elif qrcodeFExt == 3:
    img.save(qrcodeFName + "." + (ext[2]))
    print("Saved as " + qrcodeFName + "." + (ext[2]))

else:
    print("can not save as file extension is not valid")

#step 4 its obvious
print("Done")

