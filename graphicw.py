import tkinter as tk
# grafické rozhraní překladače je vytvořené pomocí knihovny tkinter
import main
#importování souboru main - soubor, který se stará o překlad textu zadaného do grafického okna

#třída pro grafické okno
class Window:

    #funkce tlačítka 1 - spustí se překlad do morseovky
   def t_czech(self):
        text = self.t.get("1.0", 'end-1c')
        self.labelText.set(main.t_funkce(text))

    #funkce tlačítka 2 - spustí se překlad do češtiny
   def t_morse(self):
        text2 = self.t.get("1.0", 'end-1c')
        self.labelText.set(main.m_funkce(text2))

    #grafické okno - definování tlačítek a textových boxů
   def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack()
        self.button = tk.Button(frame, text= "Translate to Morse",command= self.t_czech,width=20,bg="#00BFFF", relief="ridge")
        self.labelText=tk.StringVar(frame)
        self.t = tk.Text(frame,width = 50, height= 15)
        self.t2 = tk.Label(frame,width = 57, height= 17, textvariable=self.labelText, anchor="nw",justify="left",wraplength=350,relief="groove")
        self.button2 = tk.Button(frame, text= "Translate to Czech",command= self.t_morse,width=20,bg="#00FF7F",relief="ridge")
        self.t.pack()
        self.button.pack()
        self.button2.pack()
        self.t2.pack()



w = tk.Tk()
app = Window(w)
w.title("Translator")


w.mainloop()