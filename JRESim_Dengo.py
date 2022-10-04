#coding: utf-8

import SwitchDenGo
import keyboard
import time

print("このソフトウェアは、JR東日本トレインシミュレータ(JR EAST Train Simulator)を")
print("ゲーム向けマスコンで操作できるようにするための、同人ソフトウェアです。")
print("JR東日本およびその関連会社、また音楽館とは一切関係がありません。")
print("製作者Twitter: @mipsparc , GitHub: https://github.com/mipsparc")
print("現在はZUIKIの1ハンSwitchマスコンとタイトーのPS2 Type2 2ハンドルマスコンに対応しています")
print()
print("JRESim_Dengo Version1.1")
print("使い方: シミュレータ起動前にこのプログラムを起動するだけです。")
print("運転画面になったら、一旦非常ブレーキ(EB)に入れてください。")
print("Xボタン:前位置、Bボタン:後位置、Aボタン:EBリセット")
print("終了時はこのウィンドウをそのまま閉じてください。")

dengo = SwitchDenGo.SwitchDenGo()
P = 0
B = 0
while True:
    dengo.loadStatus()
    
    plus_knotch = 0
    if P > dengo.accel_knotch:
        plus_knotch = P - dengo.accel_knotch
    if B < dengo.brake_knotch:
        plus_knotch = dengo.brake_knotch - B
    for i in range(plus_knotch):
        keyboard.press_and_release("q")
    
    minus_knotch = 0
    if P < dengo.accel_knotch:
        minus_knotch = dengo.accel_knotch - P
    if B > dengo.brake_knotch:
        minus_knotch = B - dengo.brake_knotch
    if dengo.brake_knotch == 9:
        keyboard.press_and_release("1")
        time.sleep(0.5)
    else:
        for i in range(minus_knotch):
            keyboard.press_and_release("z")
    
    P = dengo.accel_knotch
    B = dengo.brake_knotch

    if "SW_X" in dengo.buttons:
        keyboard.send("up")
    if "SW_B" in dengo.buttons:
        keyboard.send("down")
    if "SW_A" in dengo.buttons:
        keyboard.press_and_release("e")
    if "SW_HOME" in dengo.buttons:
        keyboard.send("enter")
    if "SW_CIRCLE" in dengo.buttons:
        keyboard.send("backspace")
        
    time.sleep(0.05)
