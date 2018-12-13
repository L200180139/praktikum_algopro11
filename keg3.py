from Tkinter import *
bgeo = Tk(className="Bangun Geometri")

judul = Label(bgeo, text="Bangun Geometri", font="Times, 24", padx=10, pady=10)
judul.grid(row=0)

des = Label(bgeo, font="Times, 12", justify=CENTER, text="""Dalam geometri, prisma adalah bangun ruang tiga dimensi yang dibatasi oleh alas dan tutup identik berbentuk segi-n dan sisi-sisi tegak berbentuk persegi atau persegi panjang.
Dengan kata lain prisma adalah bangun ruang yang mempunyai penampang melintang yang selalu sama dalam bentuk dan ukuran.
Prisma segi-n memiliki n + 2 sisi, 3n rusuk dan 2n titik sudut. adalah bangun ruang tiga.
Contoh benda yang berbentuk bola antara lain:
Tenda Perkemahan, Atap Rumah, Teropong Binokuler, Kotak Tisu dan Bungkus Kemasan Makanan.""", padx=10)
des.grid(row=1)

L1 = Label(bgeo, font="Times, 12", text="Luas :", padx=10)
L1.place(x=85, y=170)

E = Entry(bgeo, font="Times, 12")
E.place(x=175, y=170, height=30)

def hitung():
    r = float(E.get())
    hasil = L = 2 * LuasAlas + LuasSelimut
    luas.config(text=hasil)
    
B = Button(bgeo, text="Hitung Luas", command=hitung, font="Times 14", justify=CENTER)
B.place(x=85, y=210)

L2 = Label(bgeo, text="Luas = ", font="Times 14 bold")
L2.place(x=200, y=215)

luas = Label(bgeo, font="Times 14 bold")
luas.place(x=265, y=215)

bgeo.mainloop()
