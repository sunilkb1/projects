"""
author: Sunil K B

description:
Develop a python application for implementing a MINI-Dictionary.
Choose appropriate data structure to store words from each alphabet.
Your data should contain minimum 50 words from first ten alphabets.
Methods to be supported are : Insert_NewWord(), Update_Word(), Search_Word() –


usage:
python3 DSA_5.py
"""

from __future__ import print_function
import re
import json
import sys
import os.path

if sys.version_info < (3, 0, 0):
    print(__file__ + ' requires Python 3, while Python ' + str(sys.version[0] + ' was detected. Terminating. Run - python3 '+__file__))
    sys.exit(1)


meaning=dict()
meaning['Abomasum']= 'the fourth stomach of a ruminant, such as a cow or sheep'
meaning['Absquatulate'] = 'to leave somewhere abruptly'
meaning['Adagio'] = 'to perform in slow tempo '
meaning['Alfresco'] = 'taking place or located in the open air'
meaning['Alcazar'] = 'a Spanish palace or fortress'
meaning['Amok'] = 'an episode of sudden mass assault against people or objects'
meaning['Amphisbaena'] = 'a mythical serpent with a head at each end'
meaning['Antimacassar'] = 'a small covering'
meaning['Bailiwick'] = 'a person’s area of skill, knowledge, authority, or work'
meaning['Ballistic'] = 'having its motion determined or describable by the laws of exterior '
meaning['Calamity'] = 'a great misfortune or disaster'
meaning['Catamaran'] = 'a vessel, usually propelled by sail, formed of two hulls or floats held side by side by a frame above them'
meaning['Convivial'] = 'friendly'
meaning['Cornucopia'] = 'an endless supply'
meaning['Crescendo'] = 'a gradual, steady increase in loudness '
meaning['Cryptozoology'] = 'the study of evidence tending to substantiate the existence of, or the search for, creatures whose reported existence is unproven'
meaning['Demitasse'] = 'a small cup for serving strong black coffee after dinner '
meaning['Doldrums'] = 'a state of inactivity '
meaning['Ephemeral'] = 'lasting a very short time'
meaning['Finagle'] = 'to cheat a person '
meaning['Fez'] = 'a felt cap '
meaning['Gambit'] = 'a device, action, or opening remark '
meaning['Gizmo'] = 'gadget '
meaning['Halcyon'] = 'calm '
meaning['Hooligan'] = 'a ruffian or hoodlum'
meaning['Ignoramus'] = 'an extremely ignorant person'
meaning['Izzard'] = 'the letter Z '
meaning['Jalopy'] = 'an old, decrepit, or unpretentious automobile'
meaning['Juxtaposition'] = 'the state of being close together or side by side'
meaning['Kaput'] = 'ruined; done for; demolished'
meaning['Kvetch'] = 'to complain, especially chronically'
meaning['Limburger'] = 'a variety of soft white cheese of strong odor and flavor '
meaning['Lollapalooza'] = 'an extraordinary or unusual thing, person, or event'
meaning['Machinations'] = 'an act or instance of a plot'
meaning['Maelstrom'] = 'a large, powerful, or violent whirlpool '
meaning['Moocher'] = 'to borrow'
meaning['Mufti'] = 'civilian clothes'
meaning['Nabob'] = 'any very wealthy, influential, or powerful person'
meaning['Noctambulist'] = 'a sleepwalker'
meaning['Operose'] = 'done with or involving much labor '
meaning['Otalgia'] = 'earache'
meaning['Peterman'] = 'a safecracker'
meaning['Pother'] = 'commotion'
meaning['Quibble'] = 'arguments to evade a point at issue'
meaning['Quicksilver'] = 'the metallic element mercury'
meaning['Rendezvous'] = 'an agreement between two or more persons to meet at a certain time and place'
meaning['Ruckus'] = 'a noisy, disorderly disturbance'
meaning['Scofflaw'] = 'a person who flouts the law'
meaning['Sassafras'] = 'an American tree'
meaning['Scatterbrain'] = 'a person incapable of serious, connected thought'


def insert_new_word():
    new_word = ''
    while not re.match(r'^[a-zA-Z]+$', new_word):
        new_word = input('Enter new word to be added: ')
    new_word = new_word.capitalize()
    if search_word(new_word, print_result=False):
        print("\n--------------------------------------\n")
        print("\nWord Already Present\n")
        print("\n--------------------------------------\n\n")
        return 0
    else:
        new_word_meaning = ''
        while not re.match(r'\S+', new_word_meaning):
            new_word_meaning = input('Enter meaning: ')
        meaning[new_word]=new_word_meaning
        print("\n--------------------------------------\n")
        print("\nSuccessfully Added New Word\n")
        print("\n--------------------------------------\n\n")
        return 1


def display_all():
    print("\n-------------------------------------------------------------------------------------------------------\n")
    i=0
    for key in meaning:
        i = i + 1
        print("{}. {}:  {}".format(i, key,meaning[key]))
    print("\n-----------------------------------------------------------------------------------------------------\n\n")


def search_word(word=None, print_result=True):
    if word is None:
        search_word = ''
        while not re.match(r'^[a-zA-Z]+$', search_word):
            search_word = input('Enter word you want to search: ')
        search_word = search_word.capitalize()
    else:
        search_word = word.capitalize()

    if search_word in meaning.keys():
        if print_result:
            print("\n--------------------------------------\n")
            print("\nFound Word\n")
            print("{}:  {}".format(search_word, meaning[search_word]))
            print("\n--------------------------------------\n\n")
        return 1
    else:
        if print_result:
            print("\n--------------------------------------\n")
            print("\nWord Not Found\n")
            print("\n--------------------------------------\n\n")
        return 0


def update_word():
    update_word = ''
    while not re.match(r'^[a-zA-Z]+$', update_word):
        update_word = input('Enter word to be edited: ')
    update_word = update_word.capitalize()

    if not search_word(update_word, print_result=False):
        print("\n--------------------------------------\n")
        print("\nWord Not Present\n")
        print("\n--------------------------------------\n\n")
        return 0
    else:
        update_word_meaning = ''
        while not re.match(r'\S+', update_word_meaning):
            update_word_meaning = input('Enter updated meaning: ')
        meaning[update_word]=update_word_meaning
        print("\n--------------------------------------\n")
        print("\nSuccessfully updated word\n")
        print("\n--------------------------------------\n\n")
        return 1


# Main
if __name__ == '__main__':
    while True:
        response = None
        while response not in {'1', '2', '3', '4', '5'}:
            input_msg = """
Enter your option from the below list of permitted options(1/2/3/4/5)
1. Insert_NewWord 
2. Update_Word
3. Search_Word
4. Display_Dictonary
5. Quit
Your Choice: """
            response = input(input_msg)
        print("Response is {}".format(response))

        if response == "1":
            insert_new_word()
        if response == "2":
            update_word()
        if response == "3":
            search_word()
        if response == "4":
            display_all()
        if response == "5":
            break

