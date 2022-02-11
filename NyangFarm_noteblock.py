import os
import pyautogui
import time

def instrument(instrument):
    match instrument:
        case "minecraft:block.note_block.harp":
            return 7
        case "minecraft:block.note_block.bass":
            return 2
        case "minecraft:block.note_block.basedrum":
            return 1
        case "minecraft:block.note_block.snare":
            return 10
        case "minecraft:block.note_block.hat":
            return 8
        case "minecraft:block.note_block.guitar":
            return 6
        case "minecraft:block.note_block.flute":
            return 5
        case "minecraft:block.note_block.bell":
            return 3
        case "minecraft:block.note_block.chime":
            return 4
        case "minecraft:block.note_block.xylophone":
            return 11
        case "minecraft:block.note_block.pling":
            return 9
        case _:
            return 0

def doremi(scale):
    match scale:
        case "0.500000":
            return 1
        case "0.529732":
            return 2
        case "0.561231":
            return 3
        case "0.594604":
            return 4
        case "0.629961":
            return 5
        case "0.667420":
            return 6
        case "0.707107":
            return 7
        case "0.749154":
            return 8
        case "0.793701":
            return 9
        case "0.840896":
            return 10
        case "0.890899":
            return 11
        case "0.943874":
            return 12
        case "1.000000":
            return 13
        case "1.059463":
            return 14
        case "1.122462":
            return 15
        case "1.189207":
            return 16
        case "1.259921":
            return 17
        case "1.334840":
            return 18
        case "1.414214":
            return 19
        case "1.498307":
            return 20
        case "1.587401":
            return 21
        case "1.681793":
            return 22
        case "1.781797":
            return 23
        case "1.887749":
            return 24
        case "2.000000":
            return 25
        case _:
            return 0

def Mmove(inum,rnum): #싹다 미완성
    x = 0
    y = 0

    line = inum % 9
    match line:
        case 0:
            x = 815
        case 1:
            x = 850
        case 2:
            x = 890
        case 3:
            x = 925
        case 4:
            x = 960
        case 5:
            x = 1000
        case 6:
            x = 1030
        case 7:
            x = 1070
        case 8:
            x = 1110
        case _:
            return 0
    
    match rnum:
        case 0:
            y = 360
        case 1:
            y = 400
        case 2:
            y = 430
        case 3:
            y = 470
        case 4:
            y = 505
        case 5:
            y = 540
        case _:
            return 0
    pyautogui.moveTo(x,y)

def PageChange(pcnt):
    pyautogui.moveTo(x=1100,y=720)
    pyautogui.click(clicks=1)
    pcnt = pcnt + 1
    return pcnt

#파일 경로
print("파일의 경로를 입력하세요.\n")
print("경로는 C:/의 드라이브 경로부터 압축해제한 데이터 파일 폴더의 notes/ 까지 입력하셔야 합니다.\n")
print("마지막에 \(또는 '원' 표시 또는 '/'(슬래쉬)꼭 붙여주세요!!!\n")
path = input("경로 : ")
filelists = os.listdir(path)

filenum = []
for num in filelists:
    tmp = num.rstrip('.mcfunction')
    tmp2 = int(tmp)
    filenum.append(tmp2)

filenum.sort()
print(filenum)

fnum = 0 #filenum의 위치인수
pcnt = 1


#파일 변수 
files = []

#파일 경로

atext = []  #모든 텍스트 리스트
ltext = []  #라인 텍스트 리스트



print(filenum)
print("모든 번호가 불러왔는지 확인하세요.\n")
print("마크 창은 1920x1080 기준 창모드 최대화상태이고 악보창을 가리지 않아야 합니다.")
print("비디오 설정에서 GUI비율 -보통-(2)로 설정하세요")
print("10tic/sec의 속도 기준 속도를 2로 설정해주세요.")

null = input("엔터키를 누르면 바로 시작됩니다.")


for num in filenum:
    print(num)
    print((num+1)/pcnt)

    if (num + 1) / pcnt > 9:
        pcnt = PageChange(pcnt)
        print(pcnt)
        
    file = path + str(num) + ".mcfunction"

    f = open(file,'r')
    atext = f.read()
    ltext = atext.split("\n")

    cnt = 0




    for line in ltext:
        if cnt == 6:
            continue
        stext = line.split(" ")
        print(stext)
        if (stext[0] == 'scoreboard' or stext[0] == 'function'):
            continue

        lnum = filenum[fnum]
        Mmove(lnum,cnt)
        inst = instrument(stext[1])
        scale = doremi(stext[8])
        for _ in range(inst):
            pyautogui.click(clicks=1)
            pyautogui.sleep(0.1)
        pyautogui.click(button='right',clicks=(scale-1))
        cnt = cnt + 1
    fnum = fnum + 1
    

