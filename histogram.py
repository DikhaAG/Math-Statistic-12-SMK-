import pandas as pd
import matplotlib.pylab as plt
import numpy as np
import math
import time


#Mengambil banyak kelas
banyak_kelas = int(input("Input banyak kelas : "))

print("Input batas bawah [ex: xx xx xx]")
get_bb = input("")
batas_bawah = get_bb.split()
for i in range(len(batas_bawah)):
  batas_bawah[i] = int(batas_bawah[i])

print("Input batas atas")
get_ba = input("")
batas_atas = get_ba.split()
for i in range(len(batas_atas)):
  batas_atas[i] = int(batas_atas[i])
  
tepi_bb = []
for i in batas_bawah:
  rumus = i - 0.5
  tepi_bb.append(rumus)
  
tepi_ba = []
for i in batas_atas:
  rumus = i + 0.5
  tepi_ba.append(rumus)
  
print("Input frekuensi")
get_f = input("")
frekuensi = get_f.split()
for i in range(len(frekuensi)):
  frekuensi[i] = int(frekuensi[i])
  
tabel = {
  'batas bawah': batas_bawah,
  'batas atas': batas_atas,
  'tepi batas bawah': tepi_bb,
  'tepi batas atas': tepi_ba,
  'frekuensi': frekuensi
}

class HistnPoli():
  def __init__(self, table):
    self.table = table
    self.tbb = self.table['tepi batas bawah']
    self.tba = self.table['tepi batas atas']
    last = max(self.tba)
    self.xp = []
    for i in self.tbb:
      self.xp.append(i)
    self.xp.append(last)

    self.get_f = self.table['frekuensi']
    self.f = []
    for i in self.get_f:
      self.f.append(i)
    ln = len(self.get_f)
    last_index = ln - 1
    self.f.append(self.get_f[last_index])

  def show_histo(self):
    self.bins = self.xp
    self.frek = []
    for i in range(len(self.f)):
      for j in range(self.f[i]):
        self.frek.append(self.bins[i])
    self.grafik = plt.hist(self.frek, self.bins)
    plt.title("Histogram & Poligon")
    plt.grid()
    plt.ylabel("Frekuensi")
    return self.grafik

  def show_poli(self):
    #Find Middle Value
    mid_value = []
    interval_range = self.tbb[1] - self.tbb[0]
    mid_value.append(((self.tbb[0] - interval_range) + self.tbb[0]) / 2)
    for i in range(len(self.tbb)):
      mid = mid_value[i] + 5
      mid_value.append(mid)
    last_i = len(mid_value) - 1
    mid_value.append(mid_value[last_i] + 5)
    
    #Find Frekuency
    self.frek = []
    self.frek.append(0)
    for i in range(len(self.f)):
      for j in range(self.f[i]):
        self.frek.append(mid_value[i])
    self.frek.append(0)

    middle_f = []
    middle_f.append(0)
    for i in range(len(self.f)-1):
      middle_f.append(self.f[i])
    middle_f.append(0)

    #show plot
    self.grafik = plt.plot(mid_value, middle_f, marker="o")
    return self.grafik
    plt.title("Poligon")

  def ogiveN(self):
    self.xpoint = self.xp
    fcum = []
    sumlist = sum(self.get_f)
    cum = sumlist
    for i in range(len(self.get_f)):
      fcum.append(cum)
      cum = cum - self.get_f[i]
    fcum.append(0)
    plt.plot(self.xpoint, fcum, marker="o")

  def ogiveP(self):
    fcum = [0]
    for i in range(len(self.get_f)):
      fcum.append(self.get_f[i] + fcum[i])
    plt.plot(self.xpoint, fcum, marker="o")
