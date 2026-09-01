import pygame as pg
from textwrap import wrap
from settings import *
from buildings.astronomican import Astronomican
from action_menu import Action_menu_HUD
from buildings.farm import Farm
from label import Label
from message import Messages
from button import Buttons
from map import Map
import os
import sys

sc = pg.display.set_mode((WIDTH, HEIGHT))
scene = "Menu"
map = Map(sc)
clock = pg.time.Clock()
label = Label(sc)
btn = Buttons(sc)
msg = Messages(sc)
action_menu = Action_menu_HUD(sc)
astronomican = Astronomican(sc)

def menu():
    global scene, sc
    events = pg.event.get()   
    clock.tick(FPS)
    for event in events:
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    pg.display.set_caption(f'{TITLE}    FPS: {round(clock.get_fps())}')
    sc.fill(GRAY)

    if btn.create_btn((WIDTH//2, HEIGHT//2-75), 200, 60, "Старт", 60, events):
        scene = "Main"
        
    if btn.create_btn((WIDTH//2, HEIGHT//2+75), 200, 60, "Выход", 60, events):
        pg.quit()
        sys.exit()

    if btn.create_btn((40, 15), 80, 30, 'Помощь', 20, events):
        scene = 'Help'

    sc.blit(pg.font.Font(None, 30).render(CURR_VERSION, True, WHITE), (5, HEIGHT-20))

    pg.display.flip()

def main():
    global scene, sc
    while 1:
        events = pg.event.get()
        mouse_pos = pg.mouse.get_pos()
        clock.tick(FPS)
        for event in events:
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        pg.display.set_caption(f'{TITLE}    FPS: {round(clock.get_fps())}')
        sc.fill(GRASS)  
        action_menu.check_open(events, mouse_pos)  
        map.update_map()
        map.draw_map()

        msg.draw_msg(events)

        if not msg.msg_queue:
            astronomican.build(map.not_free_tiles, events, mouse_pos)

        astronomican.draw_build()
        action_menu.draw_hud()
        
        pg.display.flip()

def main_tips():
    global scene, sc
    events = pg.event.get()   
    clock.tick(FPS)
    for event in events:
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    pg.display.set_caption(f'{TITLE}    FPS: {round(clock.get_fps())}')
    sc.fill(GRAY)   

    if btn.create_btn((75, 50), 100, 30, 'Здания', 30, events):
        scene = "Building_tips"

    if btn.create_btn((WIDTH//2, HEIGHT-100), 100, 40, 'Обратно', 30, events):
        scene = "Menu"

    sc.blit(pg.font.Font(None, 30).render(CURR_VERSION, True, WHITE), (5, HEIGHT-20))
    pg.display.flip()

def bulding_tips():
    global scene, sc
    events = pg.event.get()
    clock.tick(FPS)
    for event in events:
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    pg.display.set_caption(f'{TITLE}    FPS: {round(clock.get_fps())}')
    sc.fill(GRAY) 

    text_1_1 = 'Астрономикон - сердце и оплот города. Строиться в первую очередь и нуждается в сильнейшей обороне. Уничтожен Астрономикон = уничтожен город. ' \
               'Запас ХП составляет 1000 единиц.'
    text_1_2 = 'Ферма - здание, производящее еду для вашего поселения. Производит 12 единиц еды, но потребляет 3 единицы энергии и требует минимум 1 человека. ' \
               'Запас ХП составляет 500 единиц.'

    label.draw_text(10, 10, text_1_1)
    label.draw_text(10, 125, text_1_2)
    
    if btn.create_btn((WIDTH//2, HEIGHT-100), 100, 40, 'Обратно', 30, events):
        scene = "Help"

    sc.blit(pg.font.Font(None, 30).render(CURR_VERSION, True, WHITE), (5, HEIGHT-20))
    pg.display.flip()

if __name__ == "__main__":
    pg.init()
    os.system('cls')
    
    msg.add_to_queue('Добро пожаловать!')
    msg.add_to_queue('Перед тобой карта мира, с расположенными на ней ресурсами: камнем, водой, песком и так далее.')
    msg.add_to_queue('Чтобы начать игру тебе нужно выбрать место и построить Астрономикон, используя ЛКМ.')

    while 1:
        if scene == "Menu":
            menu()
        elif scene == "Main":
            break
        elif scene == "Help":
            main_tips()
        elif scene == "Building_tips":
            bulding_tips()
    main()