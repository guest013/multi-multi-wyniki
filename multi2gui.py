import requests
import tkinter as tk
from tkinter import Label

font = 'Verdana 16'

wyniki14 = (requests.get('http://app.lotto.pl/wyniki/?type=mm14').text).split()
wyniki22 = (requests.get('http://app.lotto.pl/wyniki/?type=mm22').text).split()

dat_g14 = wyniki14[0] + '  14:00'
wyniki14 = sorted([int(i) for i in wyniki14[1:]])

dat_g22 = wyniki22[0] + '  21:40'
wyniki22 = sorted([int(i) for i in wyniki22[1:]])

root = tk.Tk()
root.title("Multi v2.0")
root.geometry("510x150+250+150")

label = tk.Label(root).grid(row=0) # free space
label = tk.Label(root, text=dat_g14, font=font).grid(row=1)
label = tk.Label(root, text=wyniki14, font=font, padx=10).grid(row=2)
label = tk.Label(root, text='--------------------------------------------').grid(row=3) # free space
label = tk.Label(root, text=dat_g22, font=font).grid(row=4)
label = tk.Label(root, text=wyniki22, font=font, padx=10).grid(row=5)
label = tk.Label(root).grid(row=6) # free space

root.mainloop()
