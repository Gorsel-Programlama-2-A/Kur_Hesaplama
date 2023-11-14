import tkinter as tk
from tkinter import ttk


kurlar = {
    "USD": 1.0,
    "EUR": 0.93,
    "TRY": 28,
}

def kur_hesapla(*args):
    miktar = float(miktar_entry.get())
    baslangic_kur = kurlar[baslangic_cb.get()]
    hedef_kur = kurlar[hedef_cb.get()]
    sonuc = miktar * (hedef_kur / baslangic_kur)
    sonuc_label["text"] = f"{miktar} {baslangic_cb.get()} = {sonuc:.2f} {hedef_cb.get()}"

root = tk.Tk()
root.title("Döviz")

miktar_entry = ttk.Entry(root)
miktar_entry.grid(column=0, row=0)

baslangic_cb = ttk.Combobox(root, values=list(kurlar.keys()))
baslangic_cb.grid(column=1, row=0)
baslangic_cb.current(0)

hedef_cb = ttk.Combobox(root, values=list(kurlar.keys()))
hedef_cb.grid(column=2, row=0)
hedef_cb.current(1)

sonuc_label = ttk.Label(root, text="")
sonuc_label.grid(column=0, row=1, columnspan=3)

hesapla_button = ttk.Button(root, text="Hesapla", command=kur_hesapla)
hesapla_button.grid(column=0, row=2, columnspan=3)

root.mainloop()