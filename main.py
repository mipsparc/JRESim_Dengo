#coding: utf-8

import SwitchDenGo
import keyboard
import time

print("このソフトウェアは、JR東日本トレインシミュレータ(JR EAST Train Simulator)を")
print("ゲーム向けマスコンで操作できるようにするための、同人ソフトウェアです。")
print("JR東日本およびその関連会社、また音楽館とは一切関係がありません。")
print("製作者Twitter: @mipsparc , GitHub: https://github.com/mipsparc")
print("現在はZUIKIの1ハンSwitchマスコンにのみ対応していますが、")
print("随時アップデート(PS2 2ハン対応など)も予定していますので、ご期待ください")
print()
print("JRESim_Dengo Version0.1")
print("使い方: プレイ画面まで移動した後、このプログラムを起動するだけです。")
print("↑ボタン:前位置、↓ボタン:後位置、Aボタン:EBリセット、警笛1段:HOME、警笛2段:○")
print("終了時はこのウィンドウをそのまま閉じてください。")

keyboard.press_and_release("S")

dengo = SwitchDenGo()
P = 0
B = 0
while True:
    dengo.loadStatus()
    if P > dengo.accel_knotch:
        plus_knotch = P - dengo.accel_knotch
    if B < dengo.brake_knotch:
        plus_knotch = dengo.brake_knotch - B
    for i in range(plus_knotch):
        keyboard.press_and_release("Z")
        time.sleep(0.05)
    
    time.sleep(0.05)
    
    if P < dengo.accel_knotch:
        minus_knotch = dengo.accel_knotch - P
    if B > dengo.brake_knotch:
        minus_knotch = B - dengo.brake_knotch
    if dengo.brake_knotch == 9:
        keyboard.press_and_release("1")
    else:
        for i in range(minus_knotch):
            keyboard.press_and_release("Q")
            time.sleep(0.05)
    
    P = dengo.accel_knotch
    B = dengo.brake_knotch

    if "SW_PLUS" in dengo.buttons:
        keyboard.press_and_release("up arrow")
    elif "SW_MINUS" in dengo.buttons:
        keyboard.press_and_release("down arrow")
    elif "SW_A" in dengo.buttons:
        keyboard.press_and_release("E")
    elif "SW_HOME" in dengo.buttons:
        keyboard.press_and_release("enter")
    elif "SW_CIRCLE" in dengo.buttons:
        keyboard.press_and_release("backspace")

    time.sleep(0.01)
