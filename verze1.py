#-*- coding: utf-8 -*-
from psychopy.visual import Window, TextStim, Rect
from psychopy.core import wait, Clock, quit, getTime
from psychopy.event import waitKeys, getKeys, clearEvents
from psychopy import prefs
prefs.hardware['audioLib'] = ['PTB']
from psychopy import sound
from psychopy import gui
from pickle import dump
import time
import random 
from psychopy.hardware import keyboard
from psychopy import core
from stimuly_lenovo import *

myDlg = gui.Dlg(title=u'Časový experiment')
myDlg.addText('Informace o participantovi: ')
participant_number=myDlg.addField("ID participanta: ")
participant_age=myDlg.addField(u"Věk participanta: ")
participant_gender=myDlg.addField(u"Pohlaví participanta: ")
date=myDlg.addField(u"Datum: ")
time=myDlg.addField(u"Čas: ")
variant=myDlg.addField(u"Verze: ")
ok_data = myDlg.show()
ok_data=str(ok_data)
if myDlg.OK:
    print(ok_data)
    datalog=open('C:/Users/Lenovo/Documents/NUDZ/mylogfile.txt', "at")
    datalog.write("\n" + ok_data +"\n")
    datalog.close()
    datalog=open('C:/Users/Lenovo/Documents/NUDZ/all_ver.txt', "at")
    datalog.write("\n" + ok_data)
    datalog.close()
    
else:
    print(u'user log out')
    quit()

    

my_time=Clock()
my_time.reset()

def display_text(text):
    intro=TextStim(my_win, text = text)
    intro.draw()
    my_win.flip()


#acu_intro:
my_win= Window([1000, 600], color="black", fullscr=False)
display_text(u"Vítejte v našem experimentu.")
t_hello = my_time.getTime()
wait(3)
display_text(u"V experimentu uslyšíte krátké zvukové nahrávky.\n\nPro pokračování stiskněte mezerník nebo tlačítko 2.")
waitKeys(keyList = ["space","b"])
t_two_parts=my_time.getTime()
display_text(u"Vaším úkolem je reprodukovat nahrávku, kterou uslyšíte.\n\n<mezerník/2>")
t_after=my_time.getTime()
waitKeys(keyList = ["space","b"])
display_text(u"Po každém stimulu se objeví symbol otazníku:\n\n?\n\nPro reprodukci použijte tlačítko 1.\nStiskněte tlačítko na tak dlouho, jak si myslíte, že stimul trval.\n\n<mezerník/2>")
t_for_reproduction=my_time.getTime()
waitKeys(keyList = ["space","b"])
display_text(u"Nahrávky mohou obsahovat:\n\n- jeden dlouhý tón, nebo \n- ticho ohraničené tónem na začátku a na konci (tzv. prázdný interval).\n\n<mezerník>")
waitKeys(keyList = ["space","b"])
display_text(u"Prosíme, reprodukujte celou délku trvání stimulu (včetně ticha). \n\n<mezerník/2>")
t_whole=my_time.getTime()
waitKeys(keyList = ["space","b"])
#display_text(u"Až dokončíte reprodukci, stiskněte tlačítko 2 pro spuštění/zobrazení dalšího stimulu.\n\n<mezerník/2>")
#t_next=my_time.getTime()
#waitKeys(keyList = ["space","b"])
display_text(u"Prosíme, soustřeďte se a nepočítejte si délku trvání stimulů.\n\n<mezerník/2>")
t_not_count=my_time.getTime()
waitKeys(keyList = ["space","b"])
display_text(u"Pokud rozumíte instrukcím a nemáte žádné další otázky, stiskněte mezerník nebo tlačítko 2 pro pokračování.")
t_if=my_time.getTime()
waitKeys(keyList = ["space","b"])
kb = keyboard.Keyboard()

datalog=open('C:/Users/Lenovo/Documents/NUDZ/mylogfile.txt', "at")
datalog.write(u"intro:"+ "\n" + u"t_hello:\t" + str(t_hello) + u"\nt_two_parts:\t" + str(t_two_parts) + u"\nt_after:\t" + str(t_after) + u"\nt_for_reproduction:\t" + str(t_for_reproduction) + u"\nt_whole:\t" + str(t_whole) + u"\nt_not_count:\t" + str(t_not_count)+u"\nt_if:\t"+str(t_if))
datalog.close()

#acu_stimuli:
sounds = { 'emptint_1s': emptint_1s,
            'emptint_1_5s':emptint_1_5s,
            'emptint_2s':emptint_2s, 
            'emptint_2_5s':emptint_2_5s, 
            'emptint_2_75s':emptint_2_75s, 
            'emptint_3s':emptint_3s, 
            'emptint_3_5s':emptint_3_5s, 
            'emptint_4s':emptint_4s,
            'fullint_1s':fullint_1s,
            'fullint_1_5s':fullint_1_5s,
            'fullint_2s':fullint_2s, 
            'fullint_2_5s':fullint_2_5s, 
            'fullint_2_75s':fullint_2_75s, 
            'fullint_3s':fullint_3s, 
            'fullint_3_5s':fullint_3_5s, 
            'fullint_4s':fullint_4s} 
soundsList = list(sounds.keys())
sounds_practise = {'emptint_1_5s':emptint_1_5s,'emptint_3s':emptint_3s,'fullint_1_5s':fullint_1_5s, 'fullint_3s':fullint_3s}
soundsList_practise = list(sounds_practise.keys())

#acu_functions: 


def practise_acu():
    choiceList_practise = list("")
    n_trials=0
    display_text(u"Nyní začneme zácvikem.\n\n<mezerník/2>")
    waitKeys(keyList = ["space","b"])
    display_text(u"V zácviku vždy před přehráním nahrávky dostanete instrukci, o jaký druh nahrávky se bude jednat.\n\n<mezerník/2>")
    waitKeys(keyList = ["space","b"])
    display_text("Stisknutím mezerníku nebo tlačítka 2 IHNED spustíte první zkušební nahrávku.\n\n<mezerník/2>")
    waitKeys(keyList = ["space","b"])
    for i in range (4):
        n_trials +=1
        while True:
            choice_practise=random.choice(soundsList_practise)
            if choice_practise in choiceList_practise:
                continue
            else:
                choiceList_practise.append(choice_practise)
                print(choiceList_practise)
                break
        choice_practise_sound=sound.Sound(sounds_practise[choice_practise])
        clearEvents()
        while True:
            t_practise_begin = my_time.getTime()
            experiment=TextStim(my_win, text=u"",bold=True, units='pix',height=80)
            my_win.flip()
            if choice_practise == 'fullint_1_5s' or choice_practise == 'fullint_3s':
                display_text(u"Nyní bude přehráván jeden dlouhý tón.")
                wait(3)
            elif choice_practise == 'emptint_1_5s' or choice_practise == 'emptint_3s':
                display_text(u"Nyní bude přehráván prázdný interval.")
                wait(3)
            clearEvents()
            experiment.text = ""
            experiment.draw()
            my_win.flip()
            choice_practise_sound.play()
            if choice_practise == 'emptint_1_5s' or choice_practise == 'fullint_1_5s':
                wait(3.5)
            if choice_practise == 'emptint_3s' or choice_practise == 'fullint_3s':
                wait(5)
            clearEvents()
            t_repro_begin = my_time.getTime()
            kb.clock.reset()
            experiment.text = "?"
            experiment.draw()
            my_win.flip()
            keys=kb.waitKeys(keyList = ["space","c","b","right","q"], waitRelease=True)
            if 'q' in keys:
                core.quit()
            for key in keys:
                print(key.name, key.duration, key.rt)
            break
        t_trial_end=my_time.getTime()
        print(choice_practise)
        datalog=open('C:/Users/Lenovo/Documents/NUDZ/mylogfile.txt', "at")
        datalog.write(u"\nTrial number:\t"+str(n_trials))
        datalog.write(u"\nTrial begin:\t" + str(t_practise_begin) + u"\nReproduction begin:\t" + str(t_repro_begin) + u"\nCondition:\t"+str(choice_practise) + u"\nKey name:\t"+str(key.name)+u"\nReproduction:\t"+str(key.duration)+u"\nRT:\t"+ str(key.rt) + u"\nTrial end:\t" + str(t_trial_end))
        datalog.close()
        wait(0.5)
        

def block_acu():
    choiceList = list("")
    n_trials_e=0
    for i in range (16):
        n_trials_e+=1
        while True:
            choice=random.choice(soundsList)
            if choice in choiceList:
                continue
            else:
                choiceList.append(choice)
                print(choiceList)
                break
        choice_sound=sound.Sound(sounds[choice])
        clearEvents()
        while True:
            t_begin_e = my_time.getTime()
            experiment=TextStim(my_win, text=u"",bold=True, units='pix', height=80)
            experiment.draw()
            my_win.flip()
            clearEvents()
            choice_sound.play()
            if choice == 'emptint_1s' or choice == 'fullint_1s':
                wait(3)
            if choice == 'emptint_1_5s' or choice == 'fullint_1_5s':
                wait(3.5)
            if choice == 'emptint_2s' or choice == 'fullint_2s':
                wait(4)
            if choice == 'emptint_2_5s' or choice == 'fullint_2_5s':
                wait(4.5)
            if choice == 'emptint_2_75s' or choice == 'fullint_2_75s':
                wait(4.75)    
            if choice == 'emptint_3s' or choice == 'fullint_3s':
                wait(5)
            if choice == 'emptint_3_5s' or choice == 'fullint_3_5s':
                wait(5.5)
            if choice == 'emptint_4s' or choice == 'fullint_4s':
                wait(6)
            clearEvents()
            t_repro_begin_e = my_time.getTime()
            kb.clock.reset()
            experiment.text= u"?"
            experiment.draw()
            my_win.flip()
            keys=kb.waitKeys(keyList = ["space","c","b","right","q"], waitRelease=True)
            if 'q' in keys:
                core.quit()
            for key in keys:
                print(key.name, key.duration, key.rt)
            break
        t_trial_end=my_time.getTime()
        print(choice)
        datalog=open('C:/Users/Lenovo/Documents/NUDZ/mylogfile.txt', "at")
        datalog.write(u"\nTrial number:\t"+str(n_trials_e))
        datalog.write(u"\nTrial begin:\t" + str(t_begin_e) + u"\nReproduction begin:\t" + str(t_repro_begin_e)+u"\nCondition:\t" + str(choice) + u"\nReproduction:\t" + str(key.duration) +u"\nKey name:\t"+ str(key.name) + u"\nRT:\t" + str(key.rt) + u"\nTrial end:\t" + str(t_trial_end)) 
        datalog.close()
        datalog=open('C:/Users/Lenovo/Documents/NUDZ/all_ver.txt', "at")
        datalog.write("\n" + str(choice)+","+str(key.duration)+","+str(key.rt))
        datalog.close()
        wait(0.5)
        
#code_execution:

#practise_acu:
datalog=open('C:/Users/Lenovo/Documents/NUDZ/mylogfile.txt', "at")
datalog.write(u"\npractise:")
datalog.close()
practise_acu()
t_practise_end_1 = my_time.getTime()
display_text(u"Zácvik je u konce. Nyní bude experimentální část.\n\n<mezerník/2>")
waitKeys(keyList = ["space","b"])
display_text(u"Stisknutím mezerníku nebo tlačítka 2 IHNED spustíte první experimentální nahrávku.")
waitKeys(keyList = ["space","b"])

#1st_block_acu:

t_begin_b1 = my_time.getTime()
datalog=open('C:/Users/Lenovo/Documents/NUDZ/mylogfile.txt', "at")
datalog.write(u"\nPractise end 1:\t" + str(t_practise_end_1) + u"\n\nBlock 1 begin:" + str(t_begin_b1))
datalog.close()
block_acu()
t_end_b1 = my_time.getTime()
display_text(u"První blok je u konce. Můžete si dát krátkou pauzu. Stiskněte mezerník/tlačítko 2, až budete připraveni pokračovat.")
waitKeys(keyList = ["space","b"])

#2nd_block_acu:

t_begin_b2=my_time.getTime()
datalog=open('C:/Users/Lenovo/Documents/NUDZ/mylogfile.txt', "at")
datalog.write(u"\nBlock 1 end:\t" + str(t_end_b1) + u"\nPause length" + str(t_begin_b2-t_end_b1)+u"\n\nBlock 2 begin:"+str(t_begin_b2))
datalog.close()
datalog=open('C:/Users/Lenovo/Documents/NUDZ/all_ver.txt', "at")
datalog.write("\nblock break")
datalog.close()
block_acu()
t_end_b2 = my_time.getTime()
display_text(u"Druhý blok je u konce. Můžete si dát krátkou pauzu. Stiskněte mezerník/tlačítko 2, až budete připraveni pokračovat.")
waitKeys(keyList = ["space","b"])

#3rd_block_acu:

t_begin_b3=my_time.getTime()
datalog=open('C:/Users/Lenovo/Documents/NUDZ/mylogfile.txt', "at")
datalog.write(u"\nBlock 2 end:\t" + str(t_end_b2) + u"\nPause length" + str(t_begin_b3-t_end_b2)+u"\n\nBlock 3 begin:"+str(t_begin_b3))
datalog.close()
datalog=open('C:/Users/Lenovo/Documents/NUDZ/all_ver.txt', "at")
datalog.write("\nblock break")
datalog.close()
block_acu()
t_end_b3 = my_time.getTime()
    
#end

display_text(u"Experiment je u konce.Děkujeme Vám za účast.")
waitKeys(keyList = ["q"])