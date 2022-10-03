import pygame
import time

class SwitchDenGo(Joystick):
    ACCEL_KNOTCH_NUM = 5
    BRAKE_KNOTCH_NUM = 9
    
    def loadStatus(self):
        self.buttons = []
        pygame.event.get()
        
        # 前後左右ボタン
        hat_x, hat_y = self.joy.get_hat(0)
        
        # Xボタン
        if self.joy.get_button(3):
            self.buttons.append("SW_X")
        # Yボタン
        if self.joy.get_button(0):
            self.buttons.append("SW_Y")
        # Aボタン
        if self.joy.get_button(2):
            self.buttons.append("SW_A")
        # Bボタン
        if self.joy.get_button(1):
            self.buttons.append("SW_B")
        # ホームボタン
        if self.joy.get_button(12):
            self.buttons.append("SW_HOME")
        # ○ボタン
        if self.joy.get_button(13):
            self.buttons.append("SW_CIRCLE")
        # Lボタン
        if self.joy.get_button(4):
            self.buttons.append("SW_L")
        # ZLボタン
        if self.joy.get_button(6):
            self.buttons.append("SW_ZL")
        # Rボタン
        if self.joy.get_button(5):
            self.buttons.append("SW_R")
        # ZRボタン
        if self.joy.get_button(7):
            self.buttons.append("SW_ZR")
        # +ボタン
        if self.joy.get_button(9):
            self.buttons.append("SW_PLUS")
        # -ボタン
        if self.joy.get_button(8):
            self.buttons.append("SW_MINUS")
        
        # B9
        if self.joy.get_button(6):
            self.brake_knotch = 9
        
        knotch_level = self.joy.get_axis(1)
        
        if knotch_level > 0.95:
            self.accel_knotch = 5
        elif knotch_level > 0.85:
            self.accel_knotch = 4
        elif knotch_level > 0.5:
            self.accel_knotch = 3
        elif knotch_level > 0.3:
            self.accel_knotch = 2
        elif knotch_level > 0:
            self.accel_knotch = 1
        elif knotch_level > -0.05:
            self.accel_knotch = 0
            self.brake_knotch = 0
        elif knotch_level > -0.2:
            self.brake_knotch = 1
        elif knotch_level > -0.3:
            self.brake_knotch = 2
        elif knotch_level > -0.45:
            self.brake_knotch = 3
        elif knotch_level > -0.6:
            self.brake_knotch = 4
        elif knotch_level > -0.75:
            self.brake_knotch = 5
        elif knotch_level > -0.85:
            self.brake_knotch = 6
        elif knotch_level > -0.97:
            self.brake_knotch = 7
        elif knotch_level >= -1.0:
            self.brake_knotch = 8
            
        if self.brake_knotch > 0:
            self.accel_knotch = 0
