#coding: utf-8
import libusb_package
import usb.core
import usb.backend.libusb1
import time

libusb1_backend = usb.backend.libusb1.get_backend(find_library=libusb_package.find_library)

class DENSYA_CON_T01(): 
    BR_LEVEL = {0x79: 0, 0x8A: 1, 0x94: 2, 0x9A: 3, 0xA2: 4, 0xA8: 5, 0xAF: 6, 0xB2: 7, 0xB5: 8, 0xB9: 9}
    MC_LEVEL = {0x81: 0, 0x6D: 1, 0x54: 2, 0x3F: 3, 0x21: 4, 0x00: 5}

    def __init__(self):
        devices = usb.core.find(find_all=True, backend=libusb1_backend, idVendor=0x0ae4, idProduct=0x0004)
        for device in devices:
            self.device = device
        
        # 正しくアサインされたかの検査
        self.device
        
        self.device.reset()
        time.sleep(0.1)
        self.device.reset()
                
    def loadStatus(self):
        self.brake_knotch = None
        self.accel_knotch = None
        self.buttons = []
        
        # 3回試行する
        for i in range(3):
            try:
                # 129: 固定されたエンドポイント
                [_01, BR, MC, PD, HT, BT] = self.device.read(129, 8, 10)
                if BR != 0xFF:
                    self.brake_knotch = self.BR_LEVEL[BR]
                if MC != 0xFF:
                    self.accel_knotch = self.MC_LEVEL[MC]
                
                if PD == 0xFF:
                    self.buttons.append("HONE")
                
                if HT == 0x06:
                    self.buttons.append("TYPE2_LEFT")
                elif HT == 0x02:
                    self.buttons.append("TYPE2_RIGHT")
                elif HT == 0x00:
                    self.buttons.append("TYPE2_UP")
                elif HT == 0x04:
                    self.buttons.append("TYPE2_DOWN")
                    
                if BT == 0x02:
                    self.buttons.append("TYPE2_A")
                elif BT == 0x01:
                    self.buttons.append("TYPE2_B")
                elif BT == 0x04:
                    self.buttons.append("TYPE2_C")
                elif BT == 0x08:
                    self.buttons.append("TYPE2_D")

            except KeyError:
                pass
            
            except usb.core.USBTimeoutError:
                pass

            except usb.core.USBError:
                exit()
                
            finally:
                self.buttons = list(set(self.buttons))

if __name__ == '__main__':
    controller = DENSYA_CON_T01()
    controller.read()
    print(controller.mascon_level, controller.brake_level)
