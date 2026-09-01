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
        curr_action = action_menu.check_pressed(events)

        map.update_map()
        map.draw_map()

        if not msg.msg_queue:
            astronomican.build(map.not_free_tiles, events, mouse_pos)

        if astronomican.position:
            map.edit_map(astronomican.position, 'A')
            msg.add_to_queue('Вот и твой первый город!')
            msg.add_to_queue('Конечно, пока что вы не можете строить заводы по производству оружия и уничтожать соседние поселения. Но, всегда можно продолжать развиваться.')
            msg.add_to_queue('Постройте вашу первую ферму, чтобы ваше поселение не погибло с голоду и не предало вас.')

        astronomican.draw_build()
        action_menu.draw_hud()
        msg.draw_msg(events)
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

    if btn.create_btn((200, 50), 125, 30, 'Действия', 30, events):
        scene = "Actions_tips"

    if btn.create_btn((325, 50), 90, 30, 'Блоки', 30, events):
        scene = "Block_tips"

    if btn.create_btn((WIDTH//2, HEIGHT-100), 100, 40, 'Обратно', 30, events):
        scene = "Menu"

    sc.blit(pg.font.Font(None, 30).render(CURR_VERSION, True, WHITE), (5, HEIGHT-20))
    pg.display.flip()

def actions_tips():
    global scene, sc
    events = pg.event.get()
    clock.tick(FPS)
    for event in events:
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    pg.display.set_caption(f'{TITLE}    FPS: {round(clock.get_fps())}')
    sc.fill(GRAY) 

    text_1_1 = 'Построить - действие, позволяющее возвести здание в выбранной клетке. Здание можно возвести только на земле.'
    text_1_2 = 'Инфо - действие, отображающее информацию об здании и/или клетке на выбранной клетке.'
    text_1_3 = 'Разобрать - действие, разбирающее здание в выбранной клетке, разборка требует ресурсов. Данное действие не может разобрать Астрономикон.'

    label.draw_text(10, 10, text_1_1)
    label.draw_text(10, 100, text_1_2)
    label.draw_text(10, 166, text_1_3)
    
    if btn.create_btn((WIDTH//2, HEIGHT-100), 100, 40, 'Обратно', 30, events):
        scene = "Help"

    sc.blit(pg.font.Font(None, 30).render(CURR_VERSION, True, WHITE), (5, HEIGHT-20))
    pg.display.flip()

def block_tips():
    global scene, sc
    events = pg.event.get()
    clock.tick(FPS)
    for event in events:
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    pg.display.set_caption(f'{TITLE}    FPS: {round(clock.get_fps())}')
    sc.fill(GRAY) 

    pg.draw.rect(sc, GRASS, (10, 50, TILE_SIZE, TILE_SIZE))
    text_1_1 = 'Земля - обычный блок, на котором можно возвести здание. Ничего не даёт.'

    pg.draw.rect(sc, SAND, (10, 125, TILE_SIZE, TILE_SIZE))
    text_1_2 = 'Песок - блок песка, на нём нельзя возводить здания из за неустойчивости материала. На смежных блоках земли можно разместить карьер.'

    pg.draw.rect(sc, FOREST, (10, 210, TILE_SIZE, TILE_SIZE))
    text_1_3 = 'Лес - блок земли с деревьями, разместите на смежных блоках земли лесопилку чтобы получать древесину. Постройка зданий в лесу невозможна'

    pg.draw.rect(sc, STONE, (10, 295, TILE_SIZE, TILE_SIZE))
    text_1_4 = 'Камень - блок твёрдого камня, чтобы добыть его, постройте каменоломню на смежных блоках земли. Постройка на блоке камня невозможна.'

    pg.draw.rect(sc, WATER, (10, 390, TILE_SIZE, TILE_SIZE))
    text_1_5 = 'Вода - блок заполненный водой, вместе с водой, так же может выдавать рыбу при постройке рядом рыбоводного предприятия.'

    label.draw_text(70, 45, text_1_1)
    label.draw_text(70, 115, text_1_2)
    label.draw_text(70, 200, text_1_3)
    label.draw_text(70, 290, text_1_4)
    label.draw_text(70, 385, text_1_5)
    
    if btn.create_btn((WIDTH//2, HEIGHT-100), 100, 40, 'Обратно', 30, events):
        scene = "Help"

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
    text_1_2 = 'Ферма - здание, производящее еду для вашего поселения. Производит 12 единиц еды, но потребляет 3 единицы энергии и требует минимум 1 человека. Может быть установлена только на клетке с землёй. ' \
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
    msg.add_to_queue('Так же ты можешь открыть меню действий, нажав ПКМ. Чтобы применить действие, нажми на клавиатуре нужный номер действия.')

    while 1:
        if scene == "Menu":
            menu()
        elif scene == "Main":
            break
        elif scene == "Help":
            main_tips()
        elif scene == "Building_tips":
            bulding_tips()
        elif scene == 'Actions_tips':
            actions_tips()
        elif scene == 'Block_tips':
            block_tips()
    main()