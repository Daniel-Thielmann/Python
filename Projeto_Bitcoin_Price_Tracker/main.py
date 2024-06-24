from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

import requests
import json

cor0 = "#444466"
cor1 = "#feffff"
cor2 = "#6f9fbd"
fundo = "#484f60"

janela = Tk()
janela.title('')
janela.geometry('320x350')
janela.configure(bg=fundo)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=157)

frame_cima = Frame(janela, width=320, height=50, bg=cor1,
                   pady=0, padx=0, relief='flat')
frame_cima.grid(row=1, column=0)

frame_baixo = Frame(janela, width=320, height=300,
                    bg=fundo, pady=0, padx=0, relief='flat')
frame_baixo.grid(row=2, column=0, sticky=NW)

valor_formatado_usd = "$0.000"
valor_formatado_brl = "R$ 0.000,00"


def info():
    api_link = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD%2CBRL'

    response = requests.get(api_link)
    dados = response.json()

    if 'USD' in dados:
        valor_usd = float(dados['USD'])
        global valor_formatado_usd
        valor_formatado_usd = "${:,.3f}".format(valor_usd)
        l_price_usd.config(text=valor_formatado_usd)

    if 'BRL' in dados:
        valor_brl = float(dados['BRL'])
        global valor_formatado_brl
        valor_formatado_brl = "R$ {:,.2f}".format(valor_brl)
        l_price_real.config(text=valor_formatado_brl)

    frame_baixo.after(500, info)


image_path = 'images/icons8-bitcoin.png'
imagem = Image.open(image_path)
imagem = imagem.resize((30, 30), Image.LANCZOS)
imagem = ImageTk.PhotoImage(imagem)

l_icon = Label(frame_cima, image=imagem, compound=LEFT, bg=fundo, relief=FLAT)
l_icon.place(x=10, y=10)

l_nome = Label(frame_cima, text='Bitcoin Price Tracker', bg=cor1,
               fg=cor2, relief=FLAT, anchor='center', font=('Arial 20'))
l_nome.place(x=50, y=5)

l_price_usd = Label(frame_baixo, text=valor_formatado_usd, width=14,
                    bg=fundo, fg=cor1, relief=FLAT, anchor='center', font=('Arial 20'))
l_price_usd.place(x=0, y=50)

l_price_real = Label(frame_baixo, text=valor_formatado_brl, width=14,
                     bg=fundo, fg=cor1, relief=FLAT, anchor='center', font=('Arial 20'))
l_price_real.place(x=0, y=80)

info()

janela.mainloop()
