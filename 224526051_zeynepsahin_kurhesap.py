from tkinter import *
from tkinter import ttk

usd_kuru = 28
euro_kuru = 30

def kur_hesapla():
    try:
        deger = float(e_miktar_giris.get())
        secili_kur = cmb_kursec.get()

        if secili_kur == "USD":
            sonuc = deger / usd_kuru
        elif secili_kur == "EURO":
            sonuc = deger / euro_kuru
        else:
            sonuc = "Geçersiz Kur"

        lbl_hesapsonuc.config(text=f"Sonuç: {sonuc:.3f}")
    except ValueError:
        lbl_hesapsonuc.config(text="Geçersiz Giriş")

def input_temizle():
    e_miktar_giris.delete(0, END)
    lbl_hesapsonuc.config(text=".....")

anaform = Tk()
anaform.title("Kur Hesaplama")
anaform.geometry("500x600")
anaform.configure(bg="pink")

lbl_tlmiktar = Label(anaform, text="TL Miktarı")
cmb_kursec = ttk.Combobox(anaform, values=["USD", "EURO"])
lbl_kurmiktar = Label(anaform, text="Seçilen Kur")
btn_bos = Button(anaform, text="Temizle", command=input_temizle)
btn_hesapla = ttk.Button(anaform, text="Hesapla", command=kur_hesapla)
lbl_sonuc = Label(anaform, text="Sonuç")
lbl_hesapsonuc = Label(anaform, text="........")
e_miktar_giris = ttk.Entry(anaform)

lbl_tlmiktar.grid(row=0, column=0, padx=5, pady=5)
e_miktar_giris.grid(row=0, column=1, padx=5, pady=5)
lbl_kurmiktar.grid(row=1, column=0, padx=5)
cmb_kursec.grid(row=1, column=1, padx=5, pady=5)
lbl_sonuc.grid(row=2, column=0, padx=5, pady=5)
lbl_hesapsonuc.grid(row=2, column=1, padx=5, pady=5)
btn_bos.grid(row=4, column=0, padx=6, pady=6)
btn_hesapla.grid(row=4, column=1, padx=6, pady=6)

anaform.mainloop()


