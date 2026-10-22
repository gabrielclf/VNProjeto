# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define narrador = Character(None, what_style="pensamento", callback=name_callback, cb_name=None)
define g = Character("Guilherme", who_color="#ec3700", callback=name_callback, cb_name="guilherme")
define d = Character("Diego", who_color="#8300f6", callback=name_callback, cb_name="diego")
define r = Character("Ramón", who_color="#f4b701", callback=name_callback, cb_name="ramon")
define j = Character("Juliano", who_color="#007171", callback=name_callback, cb_name="juliano")

define caio = Character("Professor Caio", who_color="#0c6300", callback=name_callback, cb_name="caio")
define marcelo = Character("Professor Marcelo", who_color="#0c6300", callback=name_callback, cb_name="marcelo")

# NVL characters are used for the phone texting
# Como o Guilherme é o protagonista, e o celular é dele, só ele recebe o "SendSound"
define g_nvl = Character("Guilherme", kind=nvl, callback=Phone_SendSound)
define d_nvl = Character("Diego", kind=nvl, callback=Phone_ReceiveSound)
define r_nvl = Character("Ramón", kind=nvl, callback=Phone_ReceiveSound)
define j_nvl = Character("Juliano", kind=nvl, callback=Phone_ReceiveSound)

define phone_icons = {
    "Guilherme": "phone/icons/guilherme.png",
    "Diego": "phone/icons/diego.png",
    "Ramón": "phone/icons/ramon.png",
    "Juliano": "phone/icons/juliano.png",
}

define sec = Character("[sec_name]", callback=name_callback, cb_name=None)
default sec_name = "..."

## Posicionamento dos personagens

transform char_leftmost:
    xalign 0.25
    xanchor 0.5
    yalign 1.0
    zoom 0.65

transform char_left:
    xalign 0.40
    xanchor 0.5
    yalign 1.0
    zoom 0.65

transform char_center:
    xalign 0.50
    xanchor 0.5
    yalign 1.0
    zoom 0.65

transform char_right:
    xalign 0.60
    xanchor 0.5
    yalign 1.0
    zoom 0.65

transform char_rightmost:
    xalign 0.75
    xanchor 0.5
    yalign 1.0
    zoom 0.65

transform invert_x:
    xzoom -1

transform smooth_invert_x:
    xzoom 1
    ease 0.4 xzoom -1

transform smooth_uninvert_x:
    xzoom -1
    ease 0.4 xzoom 1

#Definindo estilos para pensamentos, gritos etc
style sussurro:
    italic True
    size 24

style pensamento is say_dialogue:
    italic True
    color "#62626d"

style grito:
    size 40
    bold True
   

# The game starts here.

label start:
    jump main_route.scene_1