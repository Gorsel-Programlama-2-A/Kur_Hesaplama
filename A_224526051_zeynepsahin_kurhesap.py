import tkinter as tk
from tkinter import *
import tkinter.messagebox
from forex_python.converter import CurrencyRates

def kur_cevir():
    c = CurrencyRates()

    kur1 = variable1.get()
    kur2 = variable2.get()

    if (kur1Alan.get() == ""):
        tkinter.messagebox.showinfo("Hata !!", "Tutar Girilmedi.\n Lütfen geçerli bir tutar girin.")

    elif (kur1 == "kur" or kur2 == "kur"):
        tkinter.messagebox.showinfo("Hata !!", "Para Birimi Seçilmedi.")

    else:
        yeni_fark = c.convert(kur1, kur2, float(kur1Alan.get()))
        yeni_fiyat = float("{:.4f}".format(yeni_fark))
        kur2Alan.insert(0, str(yeni_fiyat))

def temizle():
    kur1Alan.delete(0, tk.END)
    kur2Alan.delete(0, tk.END)

anapano = tk.Tk()

anapano.title("Kur Hesaplama")

baslikAlan = Frame(anapano, bg='#264729', pady=2, width=1850, height=100, relief="ridge")
baslikAlan.grid(row=0, column=0)

baslik = tk.Label(baslikAlan, font=('arial', 19, 'bold'), text='Kur Hesaplama', bg='#264729', fg='black')
baslik.grid(row=1, column=0, sticky=W)

variable1 = tk.StringVar(anapano)
variable2 = tk.StringVar(anapano)

variable1.set("kur")
variable2.set("kur")

kur_listesi = ["USD", "EUR"]

anapano.configure(background='#264729')
anapano.geometry("400x400")

Label_1 = Label(anapano, font=('arial', 27, 'bold'), text="", padx=2, pady=2, bg="#264729", fg="black")
Label_1.grid(row=1, column=0, sticky=W)

label1 = tk.Label(anapano, font=('arial', 15, 'bold'), text="\t Tutar : ", bg="#264729", fg="black")
label1.grid(row=2, column=0, sticky=W)

label1 = tk.Label(anapano, font=('arial', 15, 'bold'), text="\t 1. Kur : ", bg="#264729", fg="black")
label1.grid(row=3, column=0, sticky=W)

label1 = tk.Label(anapano, font=('arial', 15, 'bold'), text="\t 2. Kur : ", bg="#264729", fg="black")
label1.grid(row=4, column=0, sticky=W)

label1 = tk.Label(anapano, font=('arial', 15, 'bold'), text="\t Hesaplanmış Kur : ", bg="#264729", fg="black")
label1.grid(row=8, column=0, sticky=W)

Label_1 = Label(anapano, font=('arial', 7, 'bold'), text="", padx=2, pady=2, bg="#264729", fg="black")
Label_1.grid(row=5, column=0, sticky=W)

Label_1 = Label(anapano, font=('arial', 7, 'bold'), text="", padx=2, pady=2, bg="#264729", fg="black")
Label_1.grid(row=7, column=0, sticky=W)

kur1_secenek = tk.OptionMenu(anapano, variable1, *kur_listesi)
kur2_secenek = tk.OptionMenu(anapano, variable2, *kur_listesi)

kur1_secenek.grid(row=3, column=0, ipadx=45, sticky=E)
kur2_secenek.grid(row=4, column=0, ipadx=45, sticky=E)

kur1Alan = tk.Entry(anapano)
kur1Alan.grid(row=2, column=0, ipadx=28, sticky=E)

kur2Alan = tk.Entry(anapano)
kur2Alan.grid(row=8, column=0, ipadx=31, sticky=E)

Label_9 = Button(anapano, font=('arial', 15, 'bold'), text=" Hesapla ", padx=2, pady=2, bg="lightblue", fg="white", command=kur_cevir)
Label_9.grid(row=6, column=0)

Label_1 = Label(anapano, font=('arial', 7, 'bold'), text="", padx=2, pady=2, bg="#264729", fg="black")
Label_1.grid(row=9, column=0, sticky=W)

Label_9 = Button(anapano, font=('arial', 15, 'bold'), text="Temizle ", padx=2, pady=2, bg="lightblue", fg="white", command=temizle)
Label_9.grid(row=10, column=0)

anapano.mainloop()
