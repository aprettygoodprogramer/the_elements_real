"""
fix the bug that you still have quest when you dont

wall collison

guy put at botom of screen when transion from village to grass land
"""

#imports pygame
import pygame
#imports 
import random
#gets more stuff from pygame
from pygame.locals import *

#inits pygame
pygame.init()
#makes the fonts
smallfont = pygame.font.Font("PixelEmulator-xq08.ttf", 30)
welcome = pygame.font.Font("PixelEmulator-xq08.ttf", 20)
you_got = pygame.font.Font("PixelEmulator-xq08.ttf", 50)
very_small_font = pygame.font.Font("PixelEmulator-xq08.ttf", 7)
running = True
#makes the screen


screen = pygame.display.set_mode((1000, 1000))
#gets all the images
guy = pygame.image.load("wizard_f1.png")
grass = pygame.image.load("grass_right_size.png")
grass = pygame.transform.scale(grass,(100,100))
guy.set_colorkey ("white")
test_enemy = pygame.image.load("test_enemy.png")
test_enemy2 = pygame.image.load("test_enemy_2.png")
fire_good_guy = pygame.image.load("good_fire_monster.png")
fire_good_guy = pygame.transform.scale(fire_good_guy,(100,100))
test_enemy3 = pygame.image.load("grass_monster_right_size.png")
enemy_in_battle_grass = pygame.image.load("grass_monster_battle.png")
guy = pygame.transform.scale(guy,(100,200))
recharge = pygame.image.load("recharge.png")
portal =  pygame.image.load("portal.png")
stone_wall = pygame.image.load("stone.png")
house_im = pygame.image.load("house.png")
recharge = pygame.transform.scale(recharge,(100,100))
old_man = pygame.image.load("old_man.png")
old_man = pygame.transform.scale(old_man,(100,100))
sing = pygame.image.load("sign_right_size.png")
ice_monster = pygame.image.load("ice_monster.png")
sing = pygame.transform.scale(sing, (100, 100))
ice_monster = pygame.transform.scale(ice_monster, (100, 100))
grass_x = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 0, 100, 200, 300, 400, 500, 600, 700, 800, 900]

grass_y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 600, 600, 600, 600, 600, 600, 600, 600, 600, 600, 700, 700, 700, 700, 700, 700, 700, 700, 700, 700, 800, 800, 800, 800, 800, 800, 800, 800, 800, 800, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900]

grass_blocks = []
shop_on_screen = []
#inits the font
pygame.font.init()
#guy = pygame.transform.flip(guy, True, False)
#lots of    varble
#curr player poss 
player_x = 500
player_y = 500
#speed
player_speed = 7

#left = True
#player hp
player_hp = 150
#the enemys on thr map
enemys_on_map = []
in_battle = False 
#player hitbox
player_hitbox = (player_x, player_y, 100, 200)
player_hitbox_rect = pygame.Rect(player_hitbox)
#has the player fliped in the battle
has_fliped = False
#has the enemy been created
enemy_has_create = False
#the objenct in the class that is a enemy in the battle
curr_in_battle_enemy = None
#clock make game run a 60 fps
clock = pygame.time.Clock()
# the players max hp
player_max_hp = 150
#whos turn 
who_turn = "player"

#damage = 10
#if you can attack
can_attack = False
#the amt of heal crytels
heal_crystal = 0
#if your on the start screen
on_start_screen = True
#if your in the welcolm screen
in_welcome = False
#timer var
can_swich = True
#how many lives you have
lives = 5
#if you can heal
can_heal = True
#how much xp you need to level up
xp_needed = 100
#the amt of xp you curr have
xp = 0
#your current level
level = 1
#if the battle is over
battle_over = False
#if you have leveled up
has_added = False
#if you can heal
can_heal_from_get_screen = False
#who won
who_won = None
#the max enemy damage
enemy_max_dam = 25
#the curr world
curr_world = "town"
#what the color of the map subject to change
color_for_map="grey"
#your damage
damage = 10
#charges not used yet
fire_charge = 0
water_charge = 0
grass_charge = 0
charge = 0
#enemys killed
grass_enemy_killed = 0
fire_enemy_killed = 0
water_enemy_killed = 0
#all the doors on you screen
doors_on_screen = []
#if you have compled the quest
quest_1 = True
#if  your in the boss room
boss_room = False
#all the boxes in the boss room
boss_room_boxes = []
#all the cords
boss_room_box_cords_x = [0, 100, 200, 300, 600, 700, 800, 900, 0, 100, 200, 300, 600, 700, 800, 900, 0, 100, 200, 300, 600, 700, 800, 900, 0, 100, 200, 300, 600, 700, 800, 900, 0, 100, 200, 300, 600, 700, 800, 900, 0, 100, 200, 300, 600, 700, 800, 900]
boss_room_box_cords_y = [0, 0, 0, 0, 0, 0, 0, 0, 100, 100, 100, 100, 100, 100, 100, 100, 200, 200, 200, 200, 200, 200, 200, 200, 500, 500, 500, 500, 500, 500, 500, 500, 600, 600, 600, 600, 600, 600, 600, 600, 700, 700, 700, 700, 700, 700, 700, 700,700]
#if you have fliped
flip = True
#if your in quested
in_questes = False
can_swich_quest = True
houses = []
place_for_house_x = [0, 600]
place_for_house_y = [0, 600]
npcs_on_screen = []
enemy_mx_hp = 100
player_items = [] 
gold = 50
has_armor1 = False
has_armor2 = False
enemy_max_dam
#class for the enemy ON THE MAP not in the battle
#its a very basic class with all the basic stuff
class enemy_on_map:
    def __init__(self, x, y, pic):
        self.x = x
        self.y = y 
        self.pic = pic
        self.pic = pygame.transform.scale(self.pic,(100,100))
        self.hitbox = (self.x, self.y, 100, 100)
        self.hitbox_rect = pygame.Rect(self.hitbox)
    def display(self):
        self.hitbox = (self.x, self.y, 100, 100)
        self.hitbox_rect = pygame.Rect(self.hitbox)
        #pygame.draw.rect(screen, (0, 0, 0), self.hitbox_rect, 2)
        screen.blit(self.pic, (self.x, self.y))
    def get_hitbox(self):
        return self.hitbox_rect

#door class: kind of like a enemy on the map
#if you collide it should put you in a new place
class door:
    def __init__(self, x, y, pic, x_size, y_size):

        self.x = x
        self.y = y
        self.pic = pic
        self.x_size = x_size
        self.y_size = y_size
        self.pic = pygame.transform.scale(self.pic,(self.x_size,self.y_size))
        self.hitbox = (self.x, self.y, self.x_size,self.y_size)
        self.hitbox_rect = pygame.Rect(self.hitbox)
    def display_door(self):
        self.hitbox = (self.x, self.y, self.x_size,self.y_size)
        self.hitbox_rect = pygame.Rect(self.hitbox)
        #pygame.draw.rect(screen, (0, 0, 0), self.hitbox_rect, 2)
        screen.blit(self.pic, (self.x, self.y))
    def get_door_hitbox(self):
        return self.hitbox_rect
#this class is for  THE ENEMYS IN THE BATTLE not on the map
#this class has all the stuff to battle such as damage and hp
class enemy_in_battle:
    def __init__(self, element, damage, pic, max_hp):
        self.element = element
        
        self.damage = damage
        self.pic = pic
        self.pic = pygame.transform.scale(self.pic,(500,500))
        self.max_hp = max_hp
        self.curr_hp = self.max_hp
    def display(self):
        screen.blit(self.pic, (500, 0))
    def get_curr_hp(self):
        return self.curr_hp
    def get_max_hp(self):
        return self.max_hp
    def do_damage(self, damageDone):
        self.curr_hp-=damageDone
    def get_element(self):
        return self.element
    def get_damage(self):
        return self.damage

#a floor tile is a really simpl class
#all irt needs is a x a y and if you can collide then it has a rect
class floor_tile:
    def __init__(self, x, y, can_coilide, tile):
        self.x = x
        self.y = y
        self.can_coilide = can_coilide
        self.box_stats = (self.x, self.y, 100, 100)

        self.box = pygame.Rect(self.box_stats)
        self.tile = tile
        self.tile = pygame.transform.scale(self.tile,(100,100))
    def get_box(self):
        return self.box
    def display_tiles(self):
        self.box_stats = (self.x, self.y, 100, 100)
        pygame.draw.rect(screen, (100, 150, 50), self.box, 2)
        screen.blit(self.tile, (self.x, self.y))
class house:
    def __init__(self, x, y, image, size_x, size_y):
        self.x = x
        self.y = y
        self.image = image
        self.size_x, self.size_y = size_x, size_y
        self.image = pygame.transform.scale(self.image, (self.size_x,self.size_y))
        self.hitbox_stats = (self.x, self.y,self.size_x,self.size_y )
        self.hitbox = pygame.Rect(self.hitbox_stats)
    def display_house(self):
        self.hitbox_stats = (self.x, self.y,self.size_x,self.size_y )
        self.hitbox = pygame.Rect(self.hitbox_stats)
        screen.blit(self.image, (self.x, self.y))
    def get_hitbox(self):
        return self.hitbox
class npc:
    def __init__(self, text, pic, x, y, is_quest):
        self.text = text
        self.pic = pic
        self.x = x
        self.y = y
        self.is_quest = is_quest
        self.hitbox_stats = (self.x, self.y, 100 ,100)
        self.hitbox = pygame.Rect(self.hitbox_stats)
        self.text_text = smallfont.render(str(self.text), False,  "black")
        self.main_guy_text = very_small_font.render(str(self.text), False,  "black")
        self.text_box_stats = (0, 800, 1000, 1000)
        self.textbox = pygame.Rect(self.text_box_stats)
    def show_guy(self):
        self.hitbox_stats = (self.x, self.y, 100 ,100)
        self.hitbox = pygame.Rect(self.hitbox_stats)
        screen.blit(self.pic, (self.x, self.y))
        #pygame.draw.rect(screen, (0, 0, 0), self.hitbox, 2)
    def show_text(self):
        pygame.draw.rect(screen, (255, 255, 255), self.textbox)
        self.hitbox_stats = (self.x, self.y, 100 ,100)
        self.hitbox = pygame.Rect(self.hitbox_stats)
        screen.blit(self.pic, (self.x, self.y))
        if self.is_quest == 1:
            screen.blit(self.text_text, [10, 800])
        else:
             screen.blit(self.main_guy_text, [10, 800])

        
    def get_hitbox(self):
        return self.hitbox
    def get_is_quest(self):
        return self.is_quest
class item:
    def __init__(self, name, price, index):
        self.name = name
        self.price = price
        self.text = you_got.render(self.name, False,  "black")
        self.index = index
    def show(self):
        screen.blit(self.text, [50, 500])
    def get_index(self):
        return self.index
    def get_name(self):
        return self.name
    def get_price(self):
        return self.price
class shop:
    def __init__(self, x, y, image, item1, item2, item3):
        self.x = x
        self.y = y
        self.image = image
        self.item1 = item1
        self.item2 = item2
        self.item3 = item3
        self.hitbox = pygame.Rect(self.x, self.y, 100, 100)
        self.text_1 = smallfont.render("shop", False,  "black")
        self.text_2  = smallfont.render("item 1:" + item1.get_name() + " " + str(item1.get_price()) + "$", False,  "black")
        self.text_3  = smallfont.render("item 2:" + item2.get_name() + " " + str(item2.get_price()) + "$", False,  "black")
        self.text_4  = smallfont.render("item 3:" + item3.get_name() + " " + str(item3.get_price()) + "$", False,  "black")
        self.text_5  = smallfont.render("press 1 2 or 3 to buy", False,  "black")
    def show_guy(self):
        screen.blit(self.image, (self.x, self.y))

    def get_hitbox(self):
        return self.hitbox
    def show_shop(self):
        screen.blit(self.image, (self.x, self.y))
        screen.blit(self.text_1, [400, 50])
        screen.blit(self.text_2, [400, 150])
        screen.blit(self.text_3, [400, 250])
        screen.blit(self.text_4, [400, 350])
        screen.blit(self.text_5, [400, 450])
    def get_item1(self):
        return self.item1
    def get_item2(self):
        return self.item2
    def get_item3(self):
        return self.item3
        
npcs_on_screen = [npc("jake: 1+1=11", old_man, 500, 500, 1), npc("old man: 2+2=22", old_man, 700, 300, 2), npc("rando guy: I big brain", old_man, 300, 300, 1)]
#this is for colliding ON THE MAPPPPPPPPPPPP
def collide_on_map():
    for i in enemys_on_map:
        if player_hitbox_rect.colliderect(i.get_hitbox()):
            
            enemys_on_map.remove(i)
            return True
#checks if you collide with a door will return True if collided
def collide_door():
    for i in doors_on_screen:
        if player_hitbox_rect.colliderect(i.get_door_hitbox()):
            #doors_on_screen.remove(i)
            return True
def collion_with_shop():
    for i in shop_on_screen:
        if player_hitbox_rect.colliderect(i.get_hitbox()):
            return True
shop_on_screen = [shop(300, 500, old_man, item("armor tear 1", 10, 3), item("armor tear 2", 30, 4), item("sheild", 50, 5))]
#shows the moves IN THE BATTLE
def show_moves():
    fire_spell_text = smallfont.render("fire spell press 1", False,  "red")


    water_spell_text = smallfont.render("water spell press 2", False,  "blue")

    grass_spell_text = smallfont.render("grass spell press 3", False,  "green")

    screen.blit(fire_spell_text, [20, 900])

    screen.blit(water_spell_text, [20, 800])

    screen.blit(grass_spell_text, [20, 700])
#shows the hp IN THE BATTLE 
def show_hp():
    enemy_curr_hp = curr_in_battle_enemy.get_curr_hp()
    enemy_max_hp = curr_in_battle_enemy.get_max_hp()
    enemy_hp_text = smallfont.render("enemy hp" + str(enemy_curr_hp) + "/" +         str(enemy_max_hp), False,  "black")
    player_hp_text = smallfont.render("player hp" + str(player_hp) + "/" + str(player_max_hp), False,  "black")
    screen.blit(enemy_hp_text, [600, 700])
    screen.blit(player_hp_text, [600, 600])
#shows all the stuff on the map
def show_stuff_on_map():
    show_lives_left = smallfont.render("lives: "+ str(lives), False,  "black")
    player_hp_text = smallfont.render("player hp" + str(player_max_hp) + "/" + str(player_hp), False,  "black")
    show_heal = smallfont.render("crytels: " + str(heal_crystal), False, "black")
    show_xp = smallfont.render("xp: " + str(xp) + "/" + str(xp_needed), False, "black")
    show_level = smallfont.render("level " + str(level), False, "black")
    show_gold = smallfont.render("gold " + str(gold), False, "black")
    screen.blit(player_hp_text, [0, 0])
    screen.blit(show_lives_left, [0, 50])
    screen.blit(show_heal, [0, 100])
    screen.blit(show_xp, [0, 150])
    screen.blit(show_level, [0, 200])
    screen.blit(show_gold, [0, 250])
#makes all the blocks
def creat_boss_room():
    for i in range(len(boss_room_box_cords_x)):
        boss_room_boxes.append(floor_tile(boss_room_box_cords_x[i], boss_room_box_cords_y[i], True, stone_wall))


creat_boss_room()
def make_grass():
    for i in range(len(grass_x)):
        grass_blocks.append(floor_tile(grass_x[i], grass_y[i], False, grass))
make_grass()
def show_grass():
    for i in grass_blocks:
        i.display_tiles()
def make_house():
    for i in range(len(place_for_house_x)):
        houses.append(house(place_for_house_x[i], place_for_house_y[i], house_im, 400, 400))
make_house()
def show_collide_house():
    for i in houses:
        i.display_house()

#draws the blocks
def show_boss_room():
    for i in boss_room_boxes:
        i.display_tiles()
#make a collison func and a draw func
def draw_npc():
    for i in npcs_on_screen:
        if player_hitbox_rect.colliderect(i.get_hitbox()):
            i.show_text()
        else:
            i.show_guy()
def qust_give_npc():
    for i in npcs_on_screen:
        if player_hitbox_rect.colliderect(i.get_hitbox()) and i.get_is_quest() == 2:
            return 1
        if player_hitbox_rect.colliderect(i.get_hitbox()) and i.get_is_quest() == 3:
            return 2
#will check if your collideing if you are
#it will check what side it does that by checking if 2 opsite side subtracked by eachother is less then 10 if it is its the amt we subtacted
def collide_boss_room():
    for i in boss_room_boxes:
        if i.get_box().colliderect(player_hitbox):
            if abs(player_hitbox_rect.bottom - i.get_box().top) < 10:
                print("you collided on the top")
                return 1
            if abs(player_hitbox_rect.top - i.get_box().bottom) < 10:
                print("you collided on the bottom")
                return 2
            if abs(player_hitbox_rect.right - i.get_box().left) < 10:
                print("you collided on the left")
                return 3
            if abs(player_hitbox_rect.left - i.get_box().right) < 10:
                print("you collided on the left")
                return 4   
#shows your quest
def show_quest():
    if quest_1 == False:
        show_name_q1 = smallfont.render("kill 20 fire water and grass monsters", False,  "black")
        show_complete_q1_f = smallfont.render(str(fire_enemy_killed) + " /20" + " fire monsters killed", False,  "black")
        show_complete_q1_w = smallfont.render(str(water_enemy_killed) + " /20" + " water monsters killed", False,  "black")
        show_complete_q1_g = smallfont.render(str(grass_enemy_killed) + " /20" + " grass monsters killed", False,  "black")
        screen.blit(show_name_q1, [100, 400])
        screen.blit(show_complete_q1_f, [100, 600])
        screen.blit(show_complete_q1_w, [100,500])
        screen.blit(show_complete_q1_g, [100, 700])


#the main loop
while running == True:
    #checks for all key presses
    keys = pygame.key.get_pressed()
    #checks if you hit the X

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    #makes run at 60 fps
    clock.tick(60)
    
    #makes the screen in the loop
    
    screen = pygame.display.set_mode((1000, 1000))
    fps_counter = smallfont.render(str(round(clock.get_fps())), False,  "black")
    screen.blit(fps_counter, [500, 500])
    
    #checks if you are in a battle 
    if on_start_screen == False:
        if in_battle == False:
            #scales the player size
            guy = pygame.transform.scale(guy,(100,100))
            if curr_world == "grass1" or curr_world == "grass2" or curr_world == "grass3":
                show_grass()
                if curr_world == "grass1":
                    npcs_on_screen=[ npc("water <--", sing, 200, 500, 1),npc("fire -->", sing, 700, 500,1)]
            else:
                screen.fill((color_for_map))
            fps_counter = smallfont.render("fps:" + str(round(clock.get_fps())), False,  "black")
            screen.blit(fps_counter, [850, 50])
            #player movement
            #keys = pygame.key.get_pressed()

            if keys[pygame.K_w]:
                player_y-=player_speed
            if keys[pygame.K_s]:
                player_y+=player_speed
            if keys[pygame.K_d]:
                player_x+=player_speed
                if flip == True:
                    guy = pygame.transform.flip(guy, True, False)
                    flip = False
            if keys[pygame.K_a]:
                player_x-=player_speed
                if flip == False:
                    guy = pygame.transform.flip(guy, True, False)
                    flip = True
                    print("test")
            else:

                pass
            if curr_world == "town":
                show_collide_house()
            #if you press q then it will show the quest
            if  keys[pygame.K_q] and can_swich_quest == True:
                in_questes = not in_questes
                can_swich_quest = False
                can_swich_quest_ticks = pygame.time.get_ticks()
            if can_swich_quest == False and pygame.time.get_ticks() - can_swich_quest_ticks >= 500:
                can_swich_quest = True
            if in_questes == True:
                show_quest()
            #if you press space and you can heal heal your self with a healing crystal
            if keys[pygame.K_SPACE] and can_heal == True:
                if heal_crystal != 0:
                    player_hp+=10
                    heal_crystal-=1
                    can_heal = False
                    can_test = pygame.time.get_ticks()
            #checks the amt of time you have         
            if can_heal == False and pygame.time.get_ticks() - can_test >= 500:
                can_heal    = True
            if fire_enemy_killed >= 20 and water_enemy_killed >= 20 and grass_enemy_killed >= 20 and quest_1 == False:
                    doors_on_screen.append(door(600, 500, portal, 150, 150))
                    quest_1 = True
            #displays the doors
            for i in doors_on_screen:
                i.display_door()
            #checks if you collide with the boss room door

            if collide_door() == True:
                boss_room = True
            #if your in the boss room check for collison with the tiles
            if boss_room == True:
                show_boss_room()
                output = collide_boss_room()
                if output == 1:
                    player_y-=player_speed
                if output == 2:
                    player_y+=player_speed
                if output == 3:
                    player_x-=player_speed
                if output == 4:
                    player_x+=player_speed
  
            #collison_with_boss_room()
            for i in player_items:
                if i.get_index() == 1:
                    player_speed = 12
                elif i.get_index() == 2:
                    i.show()
                    player_items.remove(i)
                elif i.get_index() == 3 and has_armor1 == False:
                    player_max_hp+=50
                    has_armor1 = True
                elif i.get_index() == 4 and has_armor2 == False:
                    if has_armor1 == True:
                        player_max_hp+=50
                    else:
                        player_max_hp+=100
                    has_armor2 = True
            

            #right grass
            if boss_room == False:
                #this is the loject for swichiing worlds
                if player_x >= 900 and curr_world == "grass1":
                    color_for_map = "dark green"
                    curr_world = "grass3"
                    player_x = 100
                    enemys_on_map = []
                    shop_on_screen = []
                    npcs_on_screen = []
                    
                #left grass
                if player_x <= 0 and curr_world == "grass1":
                    curr_world = "grass2"
                    color_for_map = "dark green"
                    player_x = 850
                    enemys_on_map = []
                    npcs_on_screen = []
                    shop_on_screen = []
                #right water
                if player_x >= 900 and curr_world == "grass2":
                    curr_world = "grass1"
                    color_for_map = "dark green"
                    player_x = 100
                    enemys_on_map = []
                    npcs_on_screen = []
                    shop_on_screen = []
                #left water
                if player_x <= 0 and curr_world == "grass2" and curr_world != "endlesswoods":
                    player_x+=player_speed
                #left fire
                if player_x >= 900 and curr_world == "grass3" and curr_world != "endlesswoods":
                    player_x-=player_speed
                if player_x <= 0 and curr_world == "grass3":
                    curr_world = "grass1"
                    color_for_map = "dark green"
                    player_x = 850
                    enemys_on_map = []
                    npcs_on_screen = []
                    shop_on_screen = []
                if player_y >= 900 and curr_world!="town" and curr_world!= "fire":
                        player_y-=player_speed
                        print("down")
                if player_y >= 900 and curr_world == "town":
                    curr_world = "grass1"
                    color_for_map = "dark green"
                    player_y = 900
                    enemys_on_map = []
                    npcs_on_screen = []
                    shop_on_screen = []
                    #up
                if player_y <= 0 and curr_world!="grass3" and curr_world!="grass1"  and curr_world!= "grass2":
                        player_y+=player_speed
                        print("up !@#$%")

                if curr_world!="grass" and curr_world!= "town" and curr_world!="grass3" and curr_world!="grass1" and curr_world!= "grass2":
                    if player_y <= 0:
                            player_y+=player_speed
                            print("up 245345-")

                if curr_world == "grass3" and player_y <= 0:
                    curr_world = "fire"
                    color_for_map = "red"
                    print("fire time")
                    enemys_on_map = []
                    npcs_on_screen = [npc("fire monster:   dont kill me pls take this", fire_good_guy, 850, 50 , 3) ]
                    shop_on_screen = []
                if curr_world == "grass2" and player_y <= 0:
                    curr_world = "water"
                    color_for_map = "blue"
                    print("fire time")
                    enemys_on_map = []
                    npcs_on_screen = []
                    shop_on_screen = []
                    player_x = 500
                    player_y = 500

                if curr_world == "fire" and player_y >= 900:
                    curr_world = "grass3"
                    color_for_map = "dark green"
                    print("It SHOULD WORK")
                    player_y = 800
                    enemys_on_map = []
                    npcs_on_screen = []
                    shop_on_screen = []
                if curr_world == "water" and player_y >= 890:
                    curr_world = "grass2" 
                    enemys_on_map = []
                    npcs_on_screen = []
                    shop_on_screen = []
                if curr_world == "grass2" and player_x <= 50:
                    curr_world = "endlesswoods"
                    color_for_map = "dark green"
                    enemys_on_map = []
                    npcs_on_screen = []
                    shop_on_screen = []
                    player_x = 500
                if curr_world == "endlesswoods" and player_x >= 1000:
                    curr_world = "grass2" 
                    enemys_on_map = []
                    npcs_on_screen = []
                    shop_on_screen = []
                    player_x = 500
                if curr_world == "grass3" and player_y >= 890:
                    curr_world = "moutain"
                    color_for_map = "white"
                    enemys_on_map = []
                    npcs_on_screen = []
                    shop_on_screen = []
                    player_x = 500
                    player_y = 500
                    print("as;dlkfhaslkdj fhasd")
                if curr_world == "moutain" and player_y <= 100:
                    curr_world = "grass3"
                    color_for_map = "dark green"
                    player_y = 500
                    player_x = 500
                    enemys_on_map = []
                    npcs_on_screen = []
                    shop_on_screen = []
                    print("ooookkkkkkkkkkkkkkkkkkkkkkkkkkke")
                else:
                    if player_y <= 0 and curr_world!="fire":
                            #player_y+=player_speed
                            #print("up")
                            curr_world  = "town"
                            color_for_map = "grey"
                            enemys_on_map = []
                            shop_on_screen = [shop(300, 500, old_man, item("armor tear 1", 10, 3), item("armor tear 2", 30, 4), item("sheild", 50, 5))]
                            npcs_on_screen = [npc("jake: 1+1=11", old_man, 500, 500, 1), npc("old man: Hi you must kill the 3 headed hydra that destroyed this village you can do that by killing all three dragons kill all the types to get the dragons take this staff to kill them", old_man, 700, 300, 2), npc("rando guy: I big brain", old_man, 300, 300, 1)]
                            player_y = 500
                    

                #right fire
                #down
            #if your in the boss room  you should not be able to move off the screen
            #this does it
            else:
                if player_y >= 900:
                        player_y-=player_speed
                        print("down")
                    #up
                if player_y <= 0 and curr_world!="grass3":
                        player_y+=player_speed
                        print("up 1+1=11")
                if player_x >= 900:
                    player_x-=player_speed
                if player_x <= 0:
                    player_x+=player_speed

            #displayers the player
            screen.blit(guy, (player_x, player_y))
            #shows all the enemys on the map

            for i in enemys_on_map:
                    i.display()
            #player hitbox
            player_hitbox = (player_x, player_y, 100, 100)
            player_hitbox_rect = pygame.Rect(player_hitbox)
            #pygame.draw.rect(screen, (0, 0, 0), player_hitbox_rect, 2)
            #if you collide go into battle
            if collide_on_map() == True:
                in_battle = True
            #checks if it should spwan enemy
            if boss_room == False and quest_1 == False:
                spawn_enemy = random.randint(1, 150)
                if spawn_enemy == 1 and len(enemys_on_map) < 5:
                    enemy_x = random.randint(1, 900)

                    enemy_y = random.randint(1, 900)
                    if curr_world == "water":
                        enemys_on_map.append(enemy_on_map(enemy_x, enemy_y, test_enemy2))
                    
                    elif curr_world == "grass1" or curr_world == "grass2" or curr_world == "grass3":
                        enemys_on_map.append(enemy_on_map(enemy_x, enemy_y, test_enemy3))
                    elif curr_world == "fire":
                        enemys_on_map.append(enemy_on_map(enemy_x, enemy_y, test_enemy))
                    elif curr_world == "endlesswoods":
                        enemys_on_map.append(enemy_on_map(enemy_x, enemy_y, test_enemy3))
                    elif curr_world == "moutain":
                        enemys_on_map.append(enemy_on_map(enemy_x, enemy_y, ice_monster))
            #check if you should level up
            if xp >= xp_needed:
                xp = 0
                player_max_hp+=10
                level+=1
                lives = 5
                player_hp = player_max_hp
                damage+=10
                if level%2==0:
                    enemy_max_dam+=15
                    enemy_mx_hp += 50
                    
                xp_needed+=10
                has_armor1 = False
            if player_hp > player_max_hp:
                player_hp = player_max_hp

            #shows the enemy on the map
            show_stuff_on_map()
            if player_hp <= 0:
                lives-=1
                player_hp = player_max_hp
            if lives == 0:
                print("YOU DIED")

                show_boss_room()

            draw_npc()
            qust_give_npc_out_put = qust_give_npc()
            if  qust_give_npc_out_put  == 1:
                print("this is a quest giver")
                player_items.append(item("you got a nutall staff", 1, 2))
                quest_1 = False
            elif qust_give_npc_out_put == 2:

                player_items.append(item("you got a speed boots!!!", 1, 1))
                for i in player_items:
                    if i.get_index() == 1:
                        i.show()
            



            for i in shop_on_screen:
                i.show_guy()
                if collion_with_shop() == True:
                    i.show_shop()
                    if keys[pygame.K_1] and gold >= i.get_item1().get_price() :

                        player_items.append(i.get_item1())
                        gold -= i.get_item1().get_price()
                    if keys[pygame.K_2] and gold >= i.get_item2().get_price() :
                        player_items.append(i.get_item2())
                        gold -= i.get_item2().get_price()
                    if keys[pygame.K_3] and gold >= i.get_item3().get_price() :
                        player_items.append(i.get_item3())
                        gold -= i.get_item3().get_price()
        #if else its in the battle
        
        else:
            if battle_over == False:
                #flipes the player
                if has_fliped == False:

                    guy = pygame.transform.flip(guy, True, False)
            
                    has_fliped = True
                #makes the enemy
                if enemy_has_create == False:
                    if curr_world == "water":
                        curr_in_battle_enemy = enemy_in_battle("water", 15, test_enemy2, 250)
                    elif curr_world == "fire":
                        curr_in_battle_enemy = enemy_in_battle("fire",  20, test_enemy, 500)
                    elif curr_world == "grass1" or curr_world == "grass2" or curr_world == "grass3":
                        curr_in_battle_enemy = enemy_in_battle("grass", 10, test_enemy3, 100)
                    elif curr_world == "endlesswoods":
                        curr_in_battle_enemy = enemy_in_battle("grass", enemy_max_dam, test_enemy3, enemy_mx_hp)
                    elif curr_world == "moutain":
                        curr_in_battle_enemy = enemy_in_battle("grass", 13, ice_monster, 300)
                    enemy_has_create = True
                #changes the size
                guy = pygame.transform.scale(guy,(500,500))
                screen.fill((255, 255, 255))
                #shows the moves
                show_moves()
                #draws the guy
                screen.blit(guy, (0, 0))
                #draws hp
                show_hp()
                #displays the enemy
                curr_in_battle_enemy.display()
                
                #all the attacks and when you press attack
                #keys=pygame.key.get_pressed()
                #fire
                if keys[pygame.K_1] and who_turn == "player" and can_attack == False :
                    #damge_done = random.randint(5, 10)
                    if curr_in_battle_enemy.get_element() == "grass":
                        curr_in_battle_enemy.do_damage(damage*2)

                    elif curr_in_battle_enemy.get_element() == "fire":
                        curr_in_battle_enemy.do_damage(damage)
                    elif curr_in_battle_enemy.get_element() == "water":
                        damage_done = damage/2
                        damage_done = round(damage_done)
                        curr_in_battle_enemy.do_damage(damage_done)
                    who_turn = "enemy"
                    can_attack = True
                    starttime = pygame.time.get_ticks()

                    fire_charge+=1

                #water
                if keys[pygame.K_2] and who_turn == "player" and can_attack == False :

                    who_turn = "enemy"
                    can_attack = True
                    starttime = pygame.time.get_ticks()
                    if curr_in_battle_enemy.get_element() == "fire":
                        curr_in_battle_enemy.do_damage(damage*2)

                    elif curr_in_battle_enemy.get_element() == "water":
                        curr_in_battle_enemy.do_damage(damage)
                    elif curr_in_battle_enemy.get_element() == "grass":
                        damage_done = damage/2
                        damage_done = round(damage_done)
                        curr_in_battle_enemy.do_damage(damage_done)
                #grass
                if keys[pygame.K_3] and who_turn == "player" and can_attack == False :
                    damge_done = 7
                    curr_in_battle_enemy.do_damage(damge_done)
                    who_turn = "enemy"
                    can_attack = True

                    starttime = pygame.time.get_ticks()
                    if curr_in_battle_enemy.get_element() == "water":
                        curr_in_battle_enemy.do_damage(damage*2)
                    elif curr_in_battle_enemy.get_element() == "grass":
                        curr_in_battle_enemy.do_damage(damage)
                    elif curr_in_battle_enemy.get_element() == "fire":
                        damage_done = damage/2
                        damage_done = round(damage_done)
                        curr_in_battle_enemy.do_damage(damage_done)
                #enemy attack
                if who_turn == "enemy" and can_attack == False:
                    damage_done = random.randint(5, curr_in_battle_enemy.get_damage())
                    print("fhlsadkfjhsadlkjfh asld kfjh")
                    for i in player_items:
                        if i.get_index() == 5 and random.randint(1, 10) == 1:
                            damage_done = 0
                            print("we are deduseing damage")
                    who_turn = "player"
                    player_hp-=damage_done
                    charge+=1
                #makes so you cant spam
                if can_attack == True and pygame.time.get_ticks() - starttime >= 1000:
                    can_attack = False
                #if you die exist battle or the enemy
                if curr_in_battle_enemy.get_curr_hp() <= 0:
                    battle_over = True
                    who_turn = "enemy"
                    enemy_has_create = False
                    who_won = "player"
                #if you die
                if player_hp <= 0:
                    battle_over = True
                    who_turn = "enemy"
                    enemy_has_create = False
                    lives-=1
                    player_hp = player_max_hp
                    who_won = "enemy"

                print(charge)

            elif battle_over == True:
                    if who_won == "player":
                        screen.fill((255, 255, 255))
                        # added the xp and heal stuff
                        if has_added == False:
                            crsysels_added = random.randint(2, 10)
                            heal_crystal+=crsysels_added
                    

                            xp_added = random.randint(20, 30)
                            gold_added = random.randint(1, 15)
                            xp+=xp_added
                            gold += gold_added
                            has_added = True
                        #all the texts
                        press_space_to_contin = smallfont.render("press space to continue", False,  "black")
                        you_got_crystals  = smallfont.render("crstles got "+str(crsysels_added-1), False,  "black")
                        you_got_xp = smallfont.render("xp got "+str(xp_added), False,  "black")
                        you_got_gold = smallfont.render("gold got" + str(gold_added), False, "black")
                        screen.blit(you_got_crystals, [300, 600])
                        screen.blit(you_got_xp, [300, 700])
                        screen.blit(press_space_to_contin, [300, 900])
                        screen.blit(you_got_gold, [300, 800])
                        if keys[pygame.K_SPACE]:
                            in_battle = False
                            has_added = False
                            battle_over = False
                            if curr_in_battle_enemy.get_element() == "fire":
                                fire_enemy_killed+=1
                            elif curr_in_battle_enemy.get_element() == "grass":
                                grass_enemy_killed+=1
                            elif curr_in_battle_enemy.get_element() == "water":
                                water_enemy_killed+=1
                    elif who_won == "enemy":
                        screen.fill((255,255,255))
                        you_lost =smallfont.render("you lost press space to continue", False,  "black")
                        screen.blit(you_lost, [200,500])
                        if keys[pygame.K_SPACE]:

                            heal_crystal=0
                            in_battle = False
                            has_added = False
                            battle_over = False
    #####################################################################################################################
    else:
        #the  menu
        screen.fill((255, 255, 255))
        #show the main screen
        
        if in_welcome == False:
            press_space = smallfont.render("press space to start", False,  "green")
            press_a = smallfont.render("press a for help", False,  "green")
            screen.blit(press_space, [300, 500])
            screen.blit(press_a, [300, 600])
            play_button = (500, 500, 300, 300)
        #check if you are hitting space and if you are yyour not on the start screeb
        if keys[pygame.K_SPACE] and in_welcome == False:
            on_start_screen = False
        #sends you to the welcolme screen
        if keys[pygame.K_a] and can_swich == True:
            in_welcome = not in_welcome
            can_swich = False
            starttime = pygame.time.get_ticks()
        #checks the time  if you can press a again
        if can_swich == False:
            if pygame.time.get_ticks() - starttime >= 500:
                can_swich = True
        #all the text in the welcome screen
        if in_welcome == True:
            welcome_to = welcome.render("welcome to the unamed game im making in this game you are a wiz", False,  "green")
            welcome_to_2 = welcome.render("ard that fights stuff you can use healing crysles from monters ", False,  "green")
            welcome_to_3 = welcome.render("to heal and you have 5 lives", False,  "green")
            keys = pygame.key.get_pressed()
            screen.blit(welcome_to, [0, 500])
            screen.blit(welcome_to_2, [0, 550])
            screen.blit(welcome_to_3, [0, 600])
            in_welcome = True
    #updates the screen
    pygame.display.update()
pygame.quit()

