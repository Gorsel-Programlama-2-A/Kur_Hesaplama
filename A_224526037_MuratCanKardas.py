from tkinter import *
from tkinter import ttk

usd =  28
euroKuru = 30

anaform = Tk()

anaform.title("Kur Hesapla")
anaform.geometry("400x600")

lbl_tlmiktar = Label(anaform, text="TL Miktarını Yazınız: ")
lbl_kurtur = ttk.Label(anaform, text="Kur Türünü Seçiniz: ")
lbl_sonuc = ttk.Label(anaform, text="Sonuç: ")
lbl_hesapsonuc = ttk.Label(anaform, text="...........")
cmb_kursec = ttk.Combobox(anaform, values=["USD", "EURO"])

btn_1 = Button(anaform, text="Boş")
btn_hesapla = ttk.Button(anaform, text="Hesapla")

e_miktar_giris = ttk.Entry(anaform)
lbl_tlmiktar.grid(row=0, column=0)
e_miktar_giris.grid(row=0, column=1, padx=20)
cmb_kursec.grid(row=1, column=1, padx=20)
lbl_kurtur.grid(row=1, column=0, pady=20)
btn_1.grid(row=3, column=0, padx=20, pady=20)
btn_hesapla.grid(row=3, column=1, padx=20, pady=20)
lbl_sonuc.grid(row=2, column= 0)
lbl_hesapsonuc.grid(row=2, column= 1)


def hesapla():
    miktar = int(e_miktar_giris.get())
    kur = cmb_kursec.get()

    if kur == "USD":
        sonuc = miktar / usd
    elif kur == "EURO":
        sonuc = miktar / euroKuru

    #yuvarlama
    sonuc = round(sonuc, 2)

    lbl_hesapsonuc.config(text=str(sonuc))


btn_hesapla.config(command=hesapla)


anaform.mainloop()
