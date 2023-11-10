from tkinter import *
from tkinter import ttk

anaform = Tk()

anaform.title("Kur Hesapla")
anaform.geometry("300x300")

def doviz_kuru_hesapla():
    miktar = float(e_miktar_giris.get())
    secilen_kur = cmb_kursec.get()
    sonuc = 0

    if secilen_kur == "USD":
        sonuc = miktar / usdkur
    elif secilen_kur == "EURO":
        sonuc = miktar / eurokur

    lbl_sonuc.config(text=f"{miktar} TL, {sonuc:.2f} {secilen_kur} ")
    
def inputSifirla():
    e_miktar_giris.delete(0, END)
    lbl_sonuc.config(text="Sonuç")
    

lbl_tlmiktar = Label(anaform, text="TL MİKTARI:")
cmb_kursec = ttk.Combobox(anaform, values=["USD", "EURO"])

usdkur = 28
eurokur = 30
btn_hesapla = ttk.Button(anaform,
                         text="Hesapla", command=doviz_kuru_hesapla)
btn_sifirla = ttk.Button(anaform,
                     text="Sıfırla", command=inputSifirla)

e_miktar_giris = ttk.Entry(anaform)

lbl_kurtur = ttk.Label(anaform,
                       text="Kur Turunu Seç")
lbl_sonuc = ttk.Label(anaform,
                      text="Sonuç")



lbl_tlmiktar.grid(row=0, column=0, padx=5, pady=5)
e_miktar_giris.grid(row=0, column=1, padx=5, pady=5)
lbl_kurtur.grid(row=1, column=0, padx=5, pady=5)
cmb_kursec.grid(row=1, column=1, padx=5, pady=5)
lbl_sonuc.grid(row=2, column=0, padx=5, pady=5)

btn_hesapla.grid(row=3, column=0, padx=5, pady=5)
btn_sifirla.grid(row=4, column=0, padx=5, pady=5)

anaform.mainloop()
