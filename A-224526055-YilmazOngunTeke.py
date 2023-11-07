from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Kur")
window.geometry("400x400")
window.configure(background="gray")


kurlar = {
    'USD': 0.035,
    'EURO': 0.033,
    'GBP': 0.028
    }

def hesapla():
    lbl_sonuc.configure(text=kurlar[kur.get()]*int(money.get()))

kur = StringVar()
money = StringVar()

lbl_tlmik = Label(window, text="Tl Miktarı: ")
lbl_tlmik.grid(row=0, column=0, padx="10")

money_entry = Entry(window, textvariable = money, font=('calibre',10,'normal'))
money_entry.grid(row=0, column=1, padx="10")

cmb_kursec = ttk.Combobox(window, values=['USD', 'EURO', 'GBP'], textvariable=kur, state="readonly")
cmb_kursec.grid(row=1, column=1, padx="10")

label2 = Label(window, text="Dönüştürülecek kuru seç: ")
label2.grid(row=1, column=0, padx="10", pady="15")

btn_hes = ttk.Button(window, text="Hesapla", command=hesapla)
btn_hes.grid(row=3, column=1, padx="10", pady="15")

lbl1 = Label(window, text="Dönüştürülmüş paranız --> ")
lbl1.grid(row=2, column=0)

lbl_sonuc = Label(window, text="0")
lbl_sonuc.grid(row=2, column=1, padx="10")

btn1 = ttk.Button(window, text="Exit", command=window.destroy)
btn1.grid(row=4, column=1, pady="30")

window.mainloop()