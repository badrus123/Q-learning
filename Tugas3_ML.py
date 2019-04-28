import pandas as pd
import random
import matplotlib.pyplot as plt
import numpy as np 

Lbar = np.zeros((15,15))
def petunjuk_jalan(baris,kolom):
    arah = ['A','B','Ki','Ka']
    if (baris == 0):
        arah.remove('A')
    if (baris == len(Lbar)-1):
        arah.remove('B')
    if (kolom == 0):
        arah.remove('Ki')
    if (kolom == len(Lbar)-1):
        arah.remove('Ka')

    return arah
#syarat untuk menentukan posisi
def langkah_lanjut(baris,kolom, arah):
    if (arah == 'A'):
        baris = baris - 1
    if (arah == 'Ka'):
        kolom = kolom + 1
    if (arah == 'B'):
        baris= baris + 1
    if (arah == 'Ki'):
        kolom = kolom - 1

    return [baris, kolom]

Ldata = np.genfromtxt(fname = 'Tugas3_ML.txt')
print(Ldata)
Ome = 1
x   = 1
done = [0,14]

#Rumus yang digunakan untuk menentukan langkah terbaik
def data(mulai):
    return random.choice(petunjuk_jalan(mulai[0],mulai[1])) 

def state(langkah,i):
    return langkah_lanjut(langkah[0],langkah[1],i)

def jState(mulai,BM):
    return langkah_lanjut(mulai[0],mulai[1],BM)
#Sampai di sini


for n in range(100):
    mulai = [14,0]
    while mulai != done :
        dat = data(mulai)
        langkah = langkah_lanjut(mulai[0],mulai[1],dat)
        has = Ldata[langkah[0], langkah[1]]
        jb = []
        for i in petunjuk_jalan(langkah[0],langkah[1]):
            stt = state(langkah,i)
            jb.append(Lbar[stt[0],stt[1]])
        Lbar[langkah[0],langkah[1]] = Lbar[langkah[0],langkah[1]] + Ome * (has+( x * max(jb))- Lbar[langkah[0],langkah[1]])
        mulai = [langkah[0],langkah[1]]

print(Lbar)   
angk = []
hasil_akhir = []
mulai = [14,0]

while mulai != done:
    listD = {}
    bergerak = petunjuk_jalan(mulai[0], mulai[1])
    for i in bergerak :
        State = langkah_lanjut(mulai[0],mulai[1],i)
        listD[i] = Lbar[State[0],State[1]]
    BM = max(listD, key=listD.get)
    tstate = jState(mulai,BM)
    angk.append(Ldata[tstate[0],tstate[1]])
    hasil_akhir.append(Lbar[tstate[0],tstate[1]])
    plt.scatter(x=mulai[0], y=mulai[1], c = 'b')
    mulai = [tstate[0], tstate[1]]

print(sum(hasil_akhir))
print(sum(angk))
plt.show()
      
        
        
        
        
        