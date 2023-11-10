import tkinter as tk
from tkinter import ttk

def hesapla():
    girilen_miktar = e_miktar_giris.get()

    if not girilen_miktar.replace(".", "", 1).isdigit():
        lbl_hesapsonuc.config(text="Hatalı miktar girişi")
        return

    miktar = float(girilen_miktar)
    secilen_kur = cmb_kursec.get()
    
    if secilen_kur == "USD":
        sonuc = miktar / 28  
    elif secilen_kur == "EURO":
        sonuc = miktar / 30  
    else:
        sonuc = "Hatalı kur seçimi"
    
    lbl_hesapsonuc.config(text=f"Sonuç: {sonuc} {secilen_kur}")

anaform = tk.Tk()
anaform.title("Kur Hesapla")
anaform.geometry("400x600")

lbl_tlmiktar = tk.Label(anaform, text="TL Miktarı:")
e_miktar_giris = ttk.Entry(anaform)
cmb_kursec = ttk.Combobox(anaform, values=["USD", "EURO"])

btn_hesapla = ttk.Button(anaform, text="Hesapla", command=hesapla)

lbl_tlmiktar.grid(row=0, column=0, padx=50)
e_miktar_giris.grid(row=0, column=1, padx=5)
cmb_kursec.grid(row=1, column=1, padx=5, pady=5)
btn_hesapla.grid(row=2, column=1, padx=5, pady=5)

lbl_kurtur = ttk.Label(anaform, text="Kur Türünü Seçiniz")
lbl_hesapsonuc = ttk.Label(anaform, text="")
lbl_kurtur.grid(row=1, column=0, padx=5, pady=5)
lbl_hesapsonuc.grid(row=2, column=1, padx=5, pady=5)
anaform.mainloop()
