import qrcode
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

def generate():
    data = entry_var.get()

    img = qrcode.make(data)

    qr = qrcode.QRCode(version=2, box_size=10, border=4)
    qr.add_data(data.encode('utf-8'))
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')

    if img_directory:
        img_path = f'{img_directory}/qrcode.png'
        img.save(img_path)

        resized_img = img.resize((280, 280), Image.LANCZOS)

        img_tk = ImageTk.PhotoImage(resized_img)
        qr_canvas.create_image(280/2, 280/2, anchor=CENTER, image=img_tk)
        qr_canvas.image = img_tk

        result = f"Imagem salva com sucesso em {img_path}"
        result_text["text"] = result
    else:
        result_text["text"] = "Por favor, escolha um diretório antes de gerar o QR Code."

def choose_directory():
    global img_directory
    img_directory = filedialog.askdirectory()
    directory_label["text"] = f"Diretório escolhido: {img_directory}"

window = Tk()
window.title("Gerador de QRCode")
window.geometry("300x570")

hint_text = Label(window, text="Insira o texto")
hint_text.pack(padx=20, pady=5)

entry_var = StringVar()

input_box = Entry(window, textvariable=entry_var, width=280)
input_box.pack(padx=20, pady=10)

choose_directory_button = Button(window, text="Escolher Diretório", command=choose_directory, width=200, height=1)
choose_directory_button.pack(padx=20, pady=5)

button = Button(window, text="Gerar", command=generate, width=200, height=2)
button.pack(padx=20, pady=5)

directory_label = Label(window, text="Nenhum diretório escolhido ainda.", wraplength=200)
directory_label.pack(padx=20, pady=5)

qr_canvas = Canvas(window, width=280, height=280, background='white')
qr_canvas.pack()

result_text = Label(window, text="", wraplength=200)
result_text.pack(padx=20, pady=10)

img_directory = None

window.mainloop()
