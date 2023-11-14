from tkinter import * 
from tkinter import ttk

Kur_Hesaplayıcı = Tk()
Kur_Hesaplayıcı.title("Kur Hesaplayıcı")
Kur_Hesaplayıcı.geometry("250x100")
kuroran = {"USD":0.035,"EURO":0.033,"GBP":0.028}
def hesapla():
    x = int(ent_miktar.get())*kuroran[cmb_kursec.get()]
    lbl_hesap_sonuc.configure(text=str(x))
lbl_tlmiktar = Label(
    Kur_Hesaplayıcı,
    text="Türk Lirası :")

lbl_kursec = Label(Kur_Hesaplayıcı,
    text="Kur Seçiniz :",)

ent_miktar = Entry()

btn_hesapla = ttk.Button(Kur_Hesaplayıcı,
                         text="HESAPLA",command=hesapla,)

lbl_sonuc = Label(Kur_Hesaplayıcı,
                  text="SONUÇ: ")

lbl_hesap_sonuc = Label(Kur_Hesaplayıcı,
                        text="....")

cmb_kursec = ttk.Combobox(Kur_Hesaplayıcı,
                          values=["USD","EURO","GBP"])
                        
"""lbl_tlmiktar.pack(expand=YES)
ent_miktar.pack(expand=YES)"""

lbl_tlmiktar.grid(row=0,column=0)
lbl_hesap_sonuc.grid(row=2,column=1)
btn_hesapla.grid( row=3 , column=1)
ent_miktar.grid(row=0,column=1)
lbl_kursec.grid(row=1,column=0)
cmb_kursec.grid(row=1,column=1)
lbl_sonuc.grid(row=2,column=0)

Kur_Hesaplayıcı.mainloop()