# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define g = Character ("Guilherme", who_color="#ec3700")
define d = Character("Diego", who_color="#8300f6")
define r = Character("Ramón", who_color="#f4b701")
define j = Character("Juliano", who_color="#007171")
#Essas cores estão claras de mais para visualizar na caixa de texto


#Definindo estilos para pensamentos, gritos etc
style sussuro:
    italic True
style grito:
    size 40
    bold True
   

# The game starts here.

label start:

jump parte_14
    
