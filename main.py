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
print("Xボタン:前位置、Bボタン:後位置、Aボタン:EBリセット、警笛1段:HOME、警笛2段:○")
print("終了時はこのウィンドウをそのまま閉じてください。")

time.sleep(0.1)
keyboard.write("s", delay=0.05)

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
        keyboard.write("z", delay=0.05)
    
    minus_knotch = 0
    if P < dengo.accel_knotch:
        minus_knotch = dengo.accel_knotch - P
    if B > dengo.brake_knotch:
        minus_knotch = B - dengo.brake_knotch
    if dengo.brake_knotch == 9:
        keyboard.write("1", delay=0.05)
    else:
        for i in range(minus_knotch):
            keyboard.write("q", delay=0.05)
    
    P = dengo.accel_knotch
    B = dengo.brake_knotch

    if "SW_X" in dengo.buttons:
        keyboard.send("up")
    if "SW_B" in dengo.buttons:
        keyboard.send("down")
    if "SW_A" in dengo.buttons:
        keyboard.write("e", delay=0.05)
    if "SW_HOME" in dengo.buttons:
        keyboard.send("enter")
    if "SW_CIRCLE" in dengo.buttons:
        keyboard.send("backspace")
