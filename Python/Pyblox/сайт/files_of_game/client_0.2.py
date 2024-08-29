
#------------ИМПОРТ БИБЛИОТЕК------------
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursinanetworking import *
import threading
import random

#from tkinter import Tk
#from tkinter.filedialog import askopenfilename
#import os
#from tkinter import *
#from tkinter import ttk
#------------ИМПОРТ БИБЛИОТЕК------------


#root = Tk() # Иницилизируем ткинтер
#root.title("Pyblox V0.2") # Название окна
#root.geometry("250x150") # Пвзмер окна
#
#def click(): # Выбор карты
#    global filename #
#
#    #------------ОТКРЫТИЕ КАРТЫ------------
#    filename = askopenfilename()
#    path = filename
#    filename = os.path.basename(path)
#    root.destroy()
#    #------------ОТКРЫТИЕ КАРТЫ------------
#
#nick_text = ttk.Label(text="Ваш никнейм: ").pack(anchor=CENTER)
#settings_button = ttk.Button(text="Настройки").pack(anchor=CENTER)
#
#change_map_button = ttk.Button(text="Выбрать карту", command=click).pack(anchor=CENTER, expand=1)
#
#root.mainloop() # Делаем так чтобы окно работало

App = Ursina() # Иницилизируем 3д движок

Client = UrsinaNetworkingClient("localhost", 25565)

#------------ПЕРЕМЕННЫЕ------------
fallspeed = 0 # Скорость падения
isGround = 0 # На земле ли мы

ID = random.randint(0, 100) # Айди игрока

MessagesToSend = [] # Сообщения на отправку

cam = FirstPersonController() # Создаем камеру
cam.gravity = 0 # Отключаем физику (сделал свою)
#------------ПЕРЕМЕННЫЕ------------

print(" ") # Пустота
print(" ") # Пустота
print(" ") # Пустота
print(" ") # Пустота
print(" ") # Пустота
print(" ") # Пустота
print(" ") # Пустота

print("⡆⣐⢕⢕⢕⢕⢕⢕⢕⢕⠅⢗⢕⢕⢕⢕⢕⢕⢕⠕⠕⢕⢕⢕⢕⢕⢕⢕⢕⢕") # аниме тянка
print("⢐⢕⢕⢕⢕⢕⣕⢕⢕⠕⠁⢕⢕⢕⢕⢕⢕⢕⢕⠅⡄⢕⢕⢕⢕⢕⢕⢕⢕⢕") # аниме тянка
print("⢕⢕⢕⢕⢕⠅⢗⢕⠕⣠⠄⣗⢕⢕⠕⢕⢕⢕⠕⢠⣿⠐⢕⢕⢕⠑⢕⢕⠵⢕") # аниме тянка
print("⢕⢕⢕⢕⠁⢜⠕⢁⣴⣿⡇⢓⢕⢵⢐⢕⢕⠕⢁⣾⢿⣧⠑⢕⢕⠄⢑⢕⠅⢕") # аниме тянка
print("⢕⢕⠵⢁⠔⢁⣤⣤⣶⣶⣶⡐⣕⢽⠐⢕⠕⣡⣾⣶⣶⣶⣤⡁⢓⢕⠄⢑⢅⢑") # аниме тянка
print("⠍⣧⠄⣶⣾⣿⣿⣿⣿⣿⣿⣷⣔⢕⢄⢡⣾⣿⣿⣿⣿⣿⣿⣿⣦⡑⢕⢤⠱⢐") # аниме тянка
print("⢠⢕⠅⣾⣿⠋⢿⣿⣿⣿⠉⣿⣿⣷⣦⣶⣽⣿⣿⠈⣿⣿⣿⣿⠏⢹⣷⣷⡅⢐") # аниме тянка
print("⣔⢕⢥⢻⣿⡀⠈⠛⠛⠁⢠⣿⣿⣿⣿⣿⣿⣿⣿⡀⠈⠛⠛⠁⠄⣼⣿⣿⡇⢔") # аниме тянка
print("⢕⢕⢽⢸⢟⢟⢖⢖⢤⣶⡟⢻⣿⡿⠻⣿⣿⡟⢀⣿⣦⢤⢤⢔⢞⢿⢿⣿⠁⢕") # аниме тянка
print("⢕⢕⠅⣐⢕⢕⢕⢕⢕⣿⣿⡄⠛⢀⣦⠈⠛⢁⣼⣿⢗⢕⢕⢕⢕⢕⢕⡏⣘⢕") # аниме тянка
print("⢕⢕⠅⢓⣕⣕⣕⣕⣵⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣷⣕⢕⢕⢕⢕⡵⢀⢕⢕") # аниме тянка
print("⢑⢕⠃⡈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢃⢕⢕⢕") # аниме тянка
print("⣆⢕⠄⢱⣄⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢁⢕⢕⠕⢁") # аниме тянка
print("⣿⣦⡀⣿⣿⣷⣶⣬⣍⣛⣛⣛⡛⠿⠿⠿⠛⠛⢛⣛⣉⣭⣤⣂⢜⠕⢑⣡⣴⣿") # аниме тянка

print(" ") # Пустота
print(" ") # Пустота


print("---------------------ID--------------------") # Мой айди
print(" ") # Мой айди
print("<<<<<<<<<<<<<<<<<<<< " + str(ID) + " >>>>>>>>>>>>>>>>>>>>") # Мой айди
print(" ") # Мой айди
print("---------------------ID--------------------") # Мой айди

print(" ") # Пустота
print(" ") # Пустота
print(" ") # Пустота
print(" ") # Пустота
print(" ") # Пустота
print(" ") # Пустота
print(" ") # Пустота
#------------СОЗДАНИЕ ИГРОКА------------
playerHead = Entity(model="cube", color=color.yellow, scale=0.6, collider='mesh', parent = cam)
playerTorso = Entity(model="cube", color=color.blue, scale=(1, 1, 0.5), collider='box', parent = cam)
playerHandL = Entity(model='cube', color=color.yellow, scale=(1, 0.5, 0.5), collider='box', parent = cam)
playerHandR = Entity(model='cube', color=color.yellow, scale=(1, 0.5, 0.5), collider='box', parent = cam)
playerLegL = Entity(model='cube', color=color.green, scale=(1, 0.5, 0.5), collider='box', parent = cam)
playerLegR = Entity(model='cube', color=color.green, scale=(1, 0.5, 0.5), collider='box', parent = cam)
playerCheckGround = Entity(model="cube", color=color.green, scale=(1, 0.1, 0.5), collider='box', parent = cam)
worldGround = Entity(model='plane', scale=(25, 0.1, 25), collider='mesh')
#------------СОЗДАНИЕ ИГРОКА------------

Sky() # Небо

playerTorso.position = (0, -0.75, 0) # тело, позиция

camera.position = (0, 2, -15)

worldGround.position = (0, -2.25, 0) # земля, позиция

playerCheckGround.position = (0, -2.2, 0)

playerHandL.position = (-0.75, -0.75, 0) # левая рука, позиция
playerHandL.rotation = (0, 0, 90) # левая рука, поворот
playerHandR.position = (0.75, -0.75, 0) # правая рука, позиция
playerHandR.rotation = (0, 0, 90) # правая рука, поворот

playerLegL.position = (-0.25, -1.75, 0) # левая нога, позиция
playerLegL.rotation = (0, 0, 90) # левая нога, поворот
playerLegR.position = (0.25, -1.75, 0) # правая нога, позиция
playerLegR.rotation = (0, 0, 90) # правая нога, поворот

def update(): # Все повторяется:
    playerController()

def playerController(): # логика игрока
    global fallspeed # обьявлянем переменную

    #------------ФИЗИКА------------
    if playerCheckGround.intersects(worldGround).hit: # Если мы на земле то:
        fallspeed = 0
        isGround = 1
    if not playerCheckGround.intersects(worldGround).hit: # Если мы не на земле то:
        fallspeed += 0.01
        cam.position -= (0, fallspeed, 0)
        isGround = 0
    #------------ФИЗИКА------------


    #------------ПРЫЖОК------------
    if held_keys['space'] and isGround == 1: # Когда мы на земле и нажали на пробел:
        fallspeed -= 0.15
        cam.position -= (0, fallspeed, 0)

#    if held_keys['c']: # Когда мы нажали на "с":
#        createOBJ('test', 'sphere', 1, 'sphere', True)
    #------------ПРЫЖОК------------

    if cam.position.y <= -10: #
        cam.position = (0, 0, 0)

#def createOBJ(name, model_name, size_name, collider_name, fiz):
#    name = Entity(model=model_name, scale=size_name, collider=collider_name)
#    fallspeedOBJ = name
#
#    print(fallspeedOBJ) # Проверяем имя работает ли функция
#    
#    if fiz == True:
#        if name.intersects(worldGround).hit:
#                fallspeedOBJ = 0
#        elif not name.intersects(worldGround).hit:
#            fallspeedOBJ += 0.01
#            name.position -= (0, fallspeed, 0)

App.run() # иницилизируем игру



def sendMessageThread():
    while True:
        MessagesToSend.append("Моя позиция: " + str(cam.position)) # Отправка сообщений

@Client.event
def onConnectionEtablished():
    Client.send_message("changeName", ID) # Имя игркоа
    threading.Thread(target = sendMessageThread).start()

@Client.event
def messageReceveid(message):
    print(message)

while True:
    for message in MessagesToSend:
        Client.send_message("message", message)
    MessagesToSend.clear()

    Client.process_net_events()