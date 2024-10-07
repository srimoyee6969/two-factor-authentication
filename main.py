import time
import pyotp  # type: ignore
import qrcode

key = "twofactor-2FA"

uri = pyotp.totp.TOTP(key).provisioning_uri(name="Himanshushetty", issuer_name="2FA-APP")

print(uri)

qrcode.make(uri).save("totp.png")

totp = pyotp.TOTP(key)


while True:
    print(totp.verify(input("Enter code")))