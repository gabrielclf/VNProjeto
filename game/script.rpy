# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define narrador = Character(None, callback=name_callback, cb_name=None)
define g = Character ("Guilherme", who_color="#ec3700", callback=name_callback, cb_name="guilherme")
define d = Character("Diego", who_color="#8300f6", callback=name_callback, cb_name="diego")
define r = Character("Ramón", who_color="#f4b701", callback=name_callback, cb_name="ramon")
define j = Character("Juliano", who_color="#007171", callback=name_callback, cb_name="juliano")

define sec = Character("[sec_name]", callback=name_callback, cb_name=None)
default sec_name = "..."
#Essas cores estão claras de mais para visualizar na caixa de texto

## Script auxiliar pra fazer um personagem secundário com nome falar algo, removendo o highlight de todos.
init python:
    def secondary_say(name, text):
        renpy.say(
            Character(name, callback=name_callback, cb_name=None),
            text
        )

## Posicionamento dos personagens

transform char_leftmost:
    xalign -0.05
    yalign 1.0
    zoom 0.65

transform char_left:
    xalign 0.30
    yalign 1.0
    zoom 0.65

transform char_center:
    xalign 0.50
    yalign 1.0
    zoom 0.65

transform char_right:
    xalign 0.70
    yalign 1.0
    zoom 0.65

transform char_rightmost:
    xalign 1.05
    yalign 1.0
    zoom 0.65


#Definindo estilos para pensamentos, gritos etc
style sussurro:
    italic True
    size 24

style pensamento:
    italic True
    color "#62626d"

style grito:
    size 40
    bold True
   

# The game starts here.

label start:

jump main_route.scene_1
    
