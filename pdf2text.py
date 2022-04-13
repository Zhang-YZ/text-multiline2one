import tkinter as tk
import os
from tkinter import scrolledtext


def main_deal(origin_text, target_ele):
    data = origin_text.split("\n")
    print(origin_text)
    print("-"*30)
    print(data)
    result = ""
    flag = False
    for line in data:
        if line == "":
            continue
        # if line[-1] == "\n":
        #     line = line[:-1]
        if flag:
            result += line
            flag = False
        else:
            result += " " + line
        if line[-1] == "-":
            flag = True
            result = result[:-1]
    result = result.strip()
    target_ele.delete("0.0","end")
    target_ele.insert("0.0",result)
    


def finish():
    os._exit(0)


if __name__ == "__main__":
    window_start_pos = [500, 200]
    space = 20
    start_pos = [20, 20]
    box_size = [300, 800] # height width
    label_size = [30, 100]
    button_size = [30, 100]
    window_size = [start_pos[1]*2+2*box_size[0]+button_size[0]+space*2, start_pos[0]*2+label_size[1]+box_size[1]+space]
    position_origin = [start_pos[0], start_pos[1]] # x y
    position_target = [position_origin[0], position_origin[1]+box_size[0]+space]
    position_text_origin = [position_origin[0]+label_size[1]+space, position_origin[1]]
    position_text_target = [position_target[0]+label_size[1]+space, position_target[1]]
    position_button_start = [window_size[1]/2-space-button_size[1], position_text_target[1]+box_size[0]+space]
    position_button_finish = [window_size[1]/2+space, position_text_target[1]+box_size[0]+space]
    
    root = tk.Tk()
    root.title("pdftext2text")
    root.geometry(str(window_size[1])+"x"+str(window_size[0])+"+"+str(window_start_pos[0])+"+"+str(window_start_pos[1]))
    root.config(bg='#a3a3a3')
    label_target = tk.Label(root, text="Original Text:")
    label_result = tk.Label(root, text="Dealed Text:")
    label_target.place(x=position_origin[0], y=position_origin[1],height=label_size[0],width=label_size[1])
    label_result.place(x=position_target[0], y=position_target[1],height=label_size[0],width=label_size[1])
    text_origin = scrolledtext.ScrolledText(root)
    text_target = scrolledtext.ScrolledText(root)  
    text_origin.place(x=position_text_origin[0], y=position_text_origin[1], height=box_size[0], width=box_size[1])
    text_target.place(x=position_text_target[0], y=position_text_target[1], height=box_size[0], width=box_size[1])
    button_start = tk.Button(root, text="DEAL",width=10,command=lambda: main_deal(text_origin.get("1.0","end"),text_target))
    button_finish = tk.Button(root, text="CLOSE",width=10,command=finish)
    button_start.place(x=position_button_start[0],y=position_button_start[1],height=button_size[0], width=button_size[1])
    button_finish.place(x=position_button_finish[0],y=position_button_finish[1],height=button_size[0], width=button_size[1])
    
    tk.mainloop()        
