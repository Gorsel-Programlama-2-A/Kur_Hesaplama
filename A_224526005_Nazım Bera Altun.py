from tkinter import *
from tkinter import ttk

usdKuru =  28
euroKuru = 30

def kurHesapla():
    deger = float(e_miktar_giris.get())
    secili_kur = cmb_kursec.get()
    
    if secili_kur == "$ usd":
        sonuc = deger / usdKuru
    elif secili_kur == "€ euro":
        sonuc = deger / euroKuru
    else:
        sonuc = "Geçersiz Kur"
        
    lbl_hesapsonuc.config(text=str(sonuc))
    
def inputTemizle():
    e_miktar_giris.delete(0, END)
    lbl_hesapsonuc.config(text=".....")

formm = Tk()
formm.title("Kur Hesapla")
formm.geometry("400x600")

lbl_tlmiktar= Label(formm, text="TL Miktarı")

cmb_kursec = ttk.Combobox(formm, values=["$ USD", "€ EURO"])

lbl_kurmiktar = Label(formm, text="Kur Türü")


btn_bos = Button(formm, text="Temzile", command=inputTemizle)
btn_hesapla = ttk.Button(formm, text="Hesapla", command=kurHesapla)

lbl_sonuc = Label(formm, text="Sonuç")
lbl_hesapsonuc = Label(formm, text="........")

e_miktar_giris = ttk.Entry(formm)

    
    
"""
lbl_tlmiktar.pack()
cmb_kursec.pack()
btn_bos.pack()
btn_hesapla.pack()
"""

lbl_tlmiktar.grid(row=0, column=0, padx=5, pady=5)
e_miktar_giris.grid(row=0, column=1, padx=5, pady=5)
lbl_kurmiktar.grid(row=1, column=0, padx=5)
cmb_kursec.grid(row=1, column=1, padx=5, pady=5)
lbl_sonuc.grid(row=2, column=0, padx=5, pady=5)
lbl_hesapsonuc.grid(row=2, column=1, padx=5, pady=5)
btn_bos.grid(row=3, column=0, padx=5, pady=5)
btn_hesapla.grid(row=3, column=1, padx=5, pady=5)



formm.mainloop()