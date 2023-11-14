import tkinter as tk
from tkinter import ttk
import requests

def get_currency_list():
    try:
        api_url = "https://open.er-api.com/v6/latest/USD"
        response = requests.get(api_url)
        data = response.json()
        return {"USD": 1.0, "EUR": data['rates']['EUR'], "TRY": data['rates']['TRY']}
    except requests.RequestException as e:
        print(f"Hata: {e}")
        return None

def convert_currency():
    try:
        miktar = float(entry_miktar.get())
        giris_kuru = combo_giris_kuru.get()
        hedef_kuru = combo_hedef_kuru.get()

        currency_list = get_currency_list()

        if currency_list:
            giris_kuru_oran = currency_list.get(giris_kuru, 1.0)
            hedef_kuru_oran = currency_list.get(hedef_kuru, 1.0)

            sonuc = (miktar / giris_kuru_oran) * hedef_kuru_oran
            label_sonuc["text"] = f"{miktar:.2f} {giris_kuru} = {sonuc:.2f} {hedef_kuru}"
        else:
            label_sonuc["text"] = "Geçerli kur bilgileri bulunamadı."

    except ValueError:
        label_sonuc["text"] = "Geçersiz giriş! Miktarı kontrol edin."

def update_conversion(*args):
    convert_currency()

root = tk.Tk()
root.title("Güncel Kur Çevirici")

currency_list = get_currency_list()
if currency_list:
    currency_names = list(currency_list.keys())
else:
    currency_names = []

label_miktar = tk.Label(root, text="Miktar:")
label_miktar.grid(row=0, column=0, padx=10, pady=10)

entry_miktar = tk.Entry(root)
entry_miktar.grid(row=0, column=1, padx=10, pady=10)
entry_miktar.bind("<FocusOut>", update_conversion)

label_giris_kuru = tk.Label(root, text="Giriş Kur:")
label_giris_kuru.grid(row=1, column=0, padx=10, pady=10)

combo_giris_kuru = ttk.Combobox(root, values=currency_names)
combo_giris_kuru.grid(row=1, column=1, padx=10, pady=10)
combo_giris_kuru.bind("<<ComboboxSelected>>", update_conversion)

label_hedef_kuru = tk.Label(root, text="Hedef Kur:")
label_hedef_kuru.grid(row=2, column=0, padx=10, pady=10)

combo_hedef_kuru = ttk.Combobox(root, values=currency_names)
combo_hedef_kuru.grid(row=2, column=1, padx=10, pady=10)
combo_hedef_kuru.bind("<<ComboboxSelected>>", update_conversion)

label_sonuc = tk.Label(root, text="")
label_sonuc.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
