#coding: utf-8

import DENSYA_CON_T01
import keyboard
import time

print("このソフトウェアは、JR東日本トレインシミュレータ(JR EAST Train Simulator)を")
print("ゲーム向けマスコンで操作できるようにするための、同人ソフトウェアです。")
print("JR東日本およびその関連会社、また音楽館とは一切関係がありません。")
print("製作者Twitter: @mipsparc , GitHub: https://github.com/mipsparc")
print("現在はZUIKIの1ハンSwitchマスコンとタイトーのPS2 Type2 2ハンドルマスコンに対応しています")
print()
print("JRESim_Type2 Version1.1")
print("使い方: シミュレータ起動前にこのプログラムを起動するだけです。")
print("運転画面になったら、一旦マスコンは切、ブレーキは非常ブレーキに入れてください。")
print("上ボタン:前位置、下ボタン:後位置、Aボタン:EBリセット、Bボタンまたはペダル:ホーン")
print("終了時はこのウィンドウをそのまま閉じてください。")

dengo = DENSYA_CON_T01.DENSYA_CON_T01()
P = 0
B = 0
while True:
    dengo.loadStatus()
    
    if dengo.accel_knotch > 0:
        plus_p = 0
        minus_p = 0
        if P > dengo.accel_knotch:
            plus_p = P - dengo.accel_knotch
        if P < dengo.accel_knotch:
            minus_p = dengo.accel_knotch - P
        for i in range(plus_p):
            keyboard.press_and_release("z")
        for i in range(minus_p):
            keyboard.press_and_release("a")
      
    if dengo.brake_knotch == 9:
        keyboard.press_and_release("/")
        time.sleep(0.5)
    elif dengo.brake_knotch > 0:
        plus_b = 0
        minus_b = 0
        if B > dengo.accel_knotch:
            plus_b = B - dengo.brake_knotch
        if B < dengo.accel_knotch:
            minus_b = dengo.brake_knotch - B
        for i in range(plus_b):
            keyboard.press_and_release(".")
        for i in range(minus_p):
            keyboard.press_and_release(",")
    
    P = dengo.accel_knotch
    B = dengo.brake_knotch

    if "TYPE2_UP" in dengo.buttons:
        keyboard.send("up")
    if "TYPE2_DOWN" in dengo.buttons:
        keyboard.send("down")
    if "TYPE2_A" in dengo.buttons:
        keyboard.press_and_release("e")
    if "HONE" in dengo.buttons or "TYPE2_B" in dengo.buttons:
        keyboard.send("backspace")
        
    time.sleep(0.02)
