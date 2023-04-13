from tkinter import * 
from tkinter import ttk 
from poke_api import fetch_pokemon_info

#creating window 
root = Tk()
root.title("Pokemon info viewer")

#adding frames to window
frm_top = ttk.Frame(root)
frm_top.grid(row=0, column=0, columnspan=2)

frm_btm_left = ttk.LabelFrame(root,text= 'Information')
frm_btm_left.grid(row=0, column=2, padx=(20,10), pady=(10,20)) 

frm_btm_right = ttk.LabelFrame(root,text= 'statistics')
frm_btm_right.grid(row=1, column=1, padx=(10,20), pady=(10,20))

#adding widgets to top frames
lbl_name = ttk.Label(frm_top, text='Pokemon name:')
lbl_name.grid(row=0, column=0, padx=(10,5), pady=10)

ent_name = ttk.Entry(frm_top)
ent_name.grid(row=0, column=1)

def handle_get_info():
    #get pokemon name entered by user
    poke_name = ent_name.get()
    
    #get pokemon info from PokeAPI
    poke_info = fetch_pokemon_info(poke_name)

    #populating info values
    lbl_height_value['text'] = f"{poke_info['height']} dm"

    bar_hp['value'] = poke_info['statistics'][0]['base_statistics']
    bar_attack['value'] = poke_info['statistics'][1]['base_statistics']
    bar_defense['value'] = poke_info['statistics'][2]['base_statistics']
   
    return 


btn_get_info = ttk.Button(frm_btm_left, text='Get info', command=handle_get_info)
btn_get_info.grid(row=0, column=2, padx=10, pady=5)

#populate widgets in the info frame
lbl_height = ttk.Label(frm_btm_left, text='Height:')
lbl_height.grid(row=0, column=7)

lbl_height_value = ttk.Label(frm_btm_left, text='TBD')
lbl_height_value.grid(row=0, column=8)

#add weight and type 


#populate widget in the statistics frame
lbl_hp = ttk.Label(frm_btm_right, text='HP:')
lbl_hp.grid(row=0, column=0)
bar_hp = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_hp.grid(row=0, column=1) 

lbl_attack = ttk.Label(frm_btm_right, text='Attack:')
lbl_attack.grid(row=1, column=0)
bar_attack = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_attack.grid(row=1, column=1)

lbl_defense = ttk.Label(frm_btm_right, text='Defense:')
lbl_defense.grid(row=2, column=0)
bar_defense = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_defense.grid(row=2, column=1)

lbl_special_attack = ttk.Label(frm_btm_right, text='Special Attack:')
lbl_special_attack.grid(row=3, column=0)
bar_special_attack = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_special_attack.grid(row=3, column=1)

lbl_special_defence = ttk.Label(frm_btm_right, text='Special Defense:')
lbl_special_defence.grid(row=4, column=0)
bar_special_defence = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_special_defence.grid(row=4, column=1)

lbl_speed = ttk.Label(frm_btm_right, text='Speed:')
lbl_speed.grid(row=5, column=0)
bar_speed = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_speed.grid(row=5, column=1)





#Loop until window closes
root.mainloop()