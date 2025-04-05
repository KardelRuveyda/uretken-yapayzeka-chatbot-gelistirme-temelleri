# 170421027-İrem Selen
import tkinter as tk
from tkinter import ttk

def encrypt():
    encrypted_text = ""
    user_input = entry.get().lower()  
    num = ""  
    for i in user_input:
        if 'a' <= i <= 'z':  # harfse
            encrypted_text += chr(((ord(i) - 97 + 5) % 26) + 97) 
        elif i.isdigit():  # rakamsa
            num += i  # Rakamları toplar
        else:
            if num:  # rakamlar varsa
                encrypted_text += num[::-1]  # Sayıyı çevirir
                num = ""  
            encrypted_text += i  #boşluk noktalama gibi karakterler olduğu gibi alınır

    if num:  # Eğer devmanında başka bir sayı varsa, text sayı ile bitmişse
        encrypted_text += num[::-1]

    result_label.config(text=encrypted_text)  

def decrypt():
    decrypted_text = ""
    user_input = entry.get().lower()  
    num = "" 
    for i in user_input:
        if 'a' <= i <= 'z':  
            decrypted_text += chr(((ord(i) - 97 - 5) % 26) + 97)  
        elif i.isdigit():  
            num += i  
        else:
            if num:  
                decrypted_text += num[::-1] 
                num = ""  
            decrypted_text += i  

    if num:  
        decrypted_text += num[::-1]

    result_label.config(text=decrypted_text)  

 
# Çıktı label'ını kopyalamak için
def copy_to_clipboard(event):
    root.clipboard_clear()
    root.clipboard_append(result_label.cget("text"))
    root.update()

###################################################        Arayüz        #########################################

root = tk.Tk()
root.title("Şifre Kırıcı")
root.geometry("400x200")
root.configure(bg="#2C3E50")

# Stil ayarları
style = ttk.Style()
style.configure("Decrypt.TButton", font=("Arial", 10), padding=5, relief="flat",  foreground="#2C3E50")
style.configure("Encrypt.TButton", font=("Arial", 10), padding=5, relief="flat", foreground="#2C3E50")
style.map("Decrypt.TButton", background=[("active", "orange")])
style.map("Encrypt.TButton", background=[("active", "orange")])

# Başlık
label = tk.Label(root, text="Şifre Kırıcı", font=("Arial", 14, "bold"), bg="#2C3E50", fg="white")
label.pack(pady=10)

# Input alanı için açıklama
input_label = tk.Label(root, text="Şifrelemek/Çözümlemek istediğiniz metni giriniz:", font=("Arial", 10), bg="#2C3E50", fg="white")
input_label.pack(pady=2)

# Kullanıcı giriş kutusu
entry = ttk.Entry(root, font=("Arial", 12), width=30)
entry.pack(pady=10)

# Butonlar
button_frame = tk.Frame(root, bg="#2C3E50")
button_frame.pack(pady=5)

button1 = ttk.Button(button_frame, text="Şifre Kır", style="Decrypt.TButton", command=decrypt)
button1.pack(side=tk.LEFT, padx=5)

button2 = ttk.Button(button_frame, text="Şifrele", style="Encrypt.TButton", command=encrypt)
button2.pack(side=tk.LEFT, padx=5)

# Şifrelenmiş/Çözümlenmiş metin label'ı 
result_label = tk.Label(root, text="", font=("Arial", 12), bg="#2C3E50", fg="white", cursor="xterm")
result_label.pack(pady=10)
result_label.bind("<Button-1>", copy_to_clipboard)  # Metne tıklayınca kopyalama

root.mainloop()