import requests
import re
import operator
import tkinter as tk
from tkinter import *


Height = 650
Width = 500

items_poetics = {
     19961: 10,
     16733: 25,
     19960: 10,
     19992: 10,
     14153: 5,
     14156: 5,
     14150: 5,
     14147: 5,
     20005: 10,
     14164: 5,
     16731: 10,
     16732: 10,
     22421: 10,
     24245: 20,
     24248: 20,
     16730: 10,
     24249: 20,
     16729: 10,
     24244: 20,
     19935: 10,
     16728: 10,
     24247: 20,
     24246: 20,
     22413: 10,
     22416: 10,
     22415: 10,
     22414: 10,
     22412: 10,
     16727: 10
}
items_seals = {
    4567: 1710,
    4568: 1010,
    15855: 500,
    15856: 500,
    4566: 290,
    5598: 230,
    5597: 138,
    4564: 120,
    5596: 70,
    5595: 34,
    5594: 12,
    5357: 200,
    5358: 200,
    5558: 200,
    16911: 500,
    7621: 200,
    21800: 200,
    6470: 6800,
    6526: 5050,
    6538: 8300,
    7102: 1100,
    4720: 500,
    4715: 500,
    12849: 550,
    13743: 550,
    12858: 600,
    12847: 700,
    12854: 800,
    13595: 5000,
    13591: 5000,
    13589: 5000,
    13593: 5000,
    12844: 900,
    7095: 19150,
    15649: 7000,
    9356: 2300,
    9371: 250,
    9372: 250,
    9368: 2250,
    9367: 2250,
    9369: 250,
    9370: 2250,
    9366: 250,
    7605: 30,
    7603: 30,
    7604: 30,
    7602: 30,
    7601: 1500,
    7600: 1500,
    7599: 1500,
    7806: 450,
    6151: 20,
    5119: 200,
    5261: 200,
    5501: 200,
    5502: 200,
    6153: 20,
    6154: 20,
    9357: 2500,
    10386: 345,
    17837: 575,
    5531: 200,
    7597: 1500,
    5532: 200,
    7598: 1500,
    7596: 1500,
    5530: 200,
    5274: 200,
    18021: 800,
    18028: 800,
    18029: 800,
    18019: 800,
    18020: 800,
    18011: 800,
    18018: 800,
}


for key in items_poetics.keys():

    key_list_poetics = list(items_poetics)

for key in items_poetics.keys():

    key_list_poetics_price = list(items_poetics.values())


for key in items_seals.keys():

    key_list_seals = list(items_seals)

for key in items_seals.keys():

    key_list_seals_price = list(items_seals.values())
    


item_list = {
}
item_list2 = {
}

def closer():
    exit()

def api_grab(item_num):
    api_url = ("https://universalis.app/api/Aether/" + str(item_num))
    page = requests.get(api_url)
    page_data = page.json()
    refine1 = {key: page_data[key] for key in page_data.keys()
           & {"listings"}}

    for pro in refine1:
        new_dict = refine1[pro][4]
        refine2 = {key: new_dict[key] for key in new_dict.keys()
                & {"pricePerUnit"}}
    new1_entry = str(refine2)
    new2_entry = list(map(int, re.findall(r'\d+', new1_entry)))
    new3_entry = new2_entry[0]
    return new3_entry

def search_best_seals():
    i = 0
    while i < len(key_list_seals):
         item_num = (key_list_seals[i])
         world_price = api_grab(item_num)
         item_list2[int(item_num)] = int(world_price / key_list_seals_price[i])
         i = i + 1
    i = 0



    sorted_b = dict(sorted(item_list2.items(), reverse=True, key=operator.itemgetter(1)))
    best_prices1 = list(sorted_b.items())[:15]
    T.insert(tk.END, ("\nThe best value items in order: "))

    T.insert(tk.END, ("\nuniversalis.app/market/" + str(best_prices1[0]).replace('(', '').replace(')', '').replace(',', '').replace(' ', '  PricePer: ')) + \
            ("\nuniversalis.app/market/" + str(best_prices1[1]).replace('(', '').replace(')', '').replace(',', '').replace(' ', '  PricePer: ')) + \
            ("\nuniversalis.app/market/" + str(best_prices1[2]).replace('(', '').replace(')', '').replace(',', '').replace(' ', '  PricePer: ')) + \
            ("\nuniversalis.app/market/" + str(best_prices1[3]).replace('(', '').replace(')', '').replace(',', '').replace(' ', '  PricePer: ')) + \
            ("\nuniversalis.app/market/" + str(best_prices1[4]).replace('(', '').replace(')', '').replace(',', '').replace(' ', '  PricePer: '))+ \
            ("\nuniversalis.app/market/" + str(best_prices1[5]).replace('(', '').replace(')', '').replace(',', '').replace(' ', '  PricePer: '))+ \
            ("\nuniversalis.app/market/" + str(best_prices1[6]).replace('(', '').replace(')', '').replace(',', '').replace(' ', '  PricePer: '))+ \
            ("\nuniversalis.app/market/" + str(best_prices1[7]).replace('(', '').replace(')', '').replace(',', '').replace(' ', '  PricePer: '))+ \
            ("\nuniversalis.app/market/" + str(best_prices1[8]).replace('(', '').replace(')', '').replace(',', '').replace(' ', '  PricePer: '))+ \
            ("\nuniversalis.app/market/" + str(best_prices1[9]).replace('(', '').replace(')', '').replace(',', '').replace(' ', '  PricePer: '))+ \
            ("\nuniversalis.app/market/" + str(best_prices1[10]).replace('(', '').replace(')', '').replace(',', '').replace(' ', '  PricePer: '))+ \
            ("\nuniversalis.app/market/" + str(best_prices1[11]).replace('(', '').replace(')', '').replace(',', '').replace(' ', '  PricePer: '))+ \
            ("\nuniversalis.app/market/" + str(best_prices1[12]).replace('(', '').replace(')', '').replace(',', '').replace(' ', '  PricePer: '))+ \
            ("\nuniversalis.app/market/" + str(best_prices1[13]).replace('(', '').replace(')', '').replace(',', '').replace(' ', '  PricePer: '))+ \
            ("\nuniversalis.app/market/" + str(best_prices1[14]).replace('(', '').replace(')', '').replace(',', '').replace(' ', '  PricePer: '))
             )

def search_best_poetics():
    i = 0
    while i < len(key_list_poetics):
        item_num = (key_list_poetics[i])
        world_price = api_grab(item_num)
        item_list[int(item_num)] = int(world_price / key_list_poetics_price[i])
        i = i + 1
    i = 0



    sorted_d = dict(sorted(item_list.items(), reverse=True, key=operator.itemgetter(1)))
    best_prices = list(sorted_d.items())[:15]
    T.insert(tk.END, ("\nThe best value items in order: "))

    T.insert(tk.END, ("\nuniversalis.app/market/" + str(best_prices[0]).replace('(', '').replace(')', '').replace(',', '').replace(' ', '  PricePer: ')) + \
            ("\nuniversalis.app/market/" + str(best_prices[1]).replace('(', '').replace(')', '').replace(',', '').replace(' ', '  PricePer: ')) + \
            ("\nuniversalis.app/market/" + str(best_prices[2]).replace('(', '').replace(')', '').replace(',', '').replace(' ', '  PricePer: ')) + \
            ("\nuniversalis.app/market/" + str(best_prices[3]).replace('(', '').replace(')', '').replace(',', '').replace(' ', '  PricePer: ')) + \
            ("\nuniversalis.app/market/" + str(best_prices[4]).replace('(', '').replace(')', '').replace(',', '').replace(' ', '  PricePer: '))+ \
            ("\nuniversalis.app/market/" + str(best_prices[5]).replace('(', '').replace(')', '').replace(',', '').replace(' ', '  PricePer: '))+ \
            ("\nuniversalis.app/market/" + str(best_prices[6]).replace('(', '').replace(')', '').replace(',', '').replace(' ', '  PricePer: '))+ \
            ("\nuniversalis.app/market/" + str(best_prices[7]).replace('(', '').replace(')', '').replace(',', '').replace(' ', '  PricePer: '))+ \
            ("\nuniversalis.app/market/" + str(best_prices[8]).replace('(', '').replace(')', '').replace(',', '').replace(' ', '  PricePer: '))+ \
            ("\nuniversalis.app/market/" + str(best_prices[9]).replace('(', '').replace(')', '').replace(',', '').replace(' ', '  PricePer: '))+ \
            ("\nuniversalis.app/market/" + str(best_prices[10]).replace('(', '').replace(')', '').replace(',', '').replace(' ', '  PricePer: '))+ \
            ("\nuniversalis.app/market/" + str(best_prices[11]).replace('(', '').replace(')', '').replace(',', '').replace(' ', '  PricePer: '))+ \
            ("\nuniversalis.app/market/" + str(best_prices[12]).replace('(', '').replace(')', '').replace(',', '').replace(' ', '  PricePer: '))+ \
            ("\nuniversalis.app/market/" + str(best_prices[13]).replace('(', '').replace(')', '').replace(',', '').replace(' ', '  PricePer: '))+ \
            ("\nuniversalis.app/market/" + str(best_prices[14]).replace('(', '').replace(')', '').replace(',', '').replace(' ', '  PricePer: '))
             )


root = tk.Tk()

root.title("                                    Seals & Poetics Converter")

canvas = tk.Canvas(root, height=Height, width=Width)
canvas.pack()


frame2 = tk.Frame(root)
frame2.place(relx=0.7, rely=0.008, relwidth=0.2, relheight=0.05)

frame1 = tk.Frame(root)
frame1.place(relx=0.1, rely=0.008, relwidth=0.2, relheight=0.05)

frame = tk.Frame(root)
frame.place(relx=0.4, rely=0.008, relwidth=0.2, relheight=0.05)

S = tk.Scrollbar(root)
T = tk.Text(root, height=10, width=50)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
T.place(relx=0.01, rely=0.07, relwidth=0.98, relheight=0.92)


T.insert(tk.END, "After clicking the button, please be patient\nit may take some time to search items:")

button = tk.Button(frame1, text="Show Best \nPoetics", command=search_best_poetics)
button.pack(expand=True, fill="both")

button = tk.Button(frame, text="Show Best \nSeals", command=search_best_seals)
button.pack(expand=True, fill="both")

button = tk.Button(frame2, text="Close\nApp", command=closer)
button.pack(expand=True, fill="both")

root.mainloop()
