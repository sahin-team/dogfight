import numpy as np
from scipy.spatial import KDTree

def distance(p1,p2):
  return np.sqrt(np.sum(np.square(p1-p2))) 
  
  



    # Kendi İHA'nın Koordinatları
kendi_iha_konum = np.array([[41.508775, 36.118335, 38]])  # Enlem, Boylam, İrtifa

  # Diğer Takımların Konum Bilgileri (Örnek Veri)
konum_bilgileri = [
      {
          "takim_numarasi": 1,
          "iha_enlem": 41.5118256,
          "iha_boylam": 36.11993,
          "iha_irtifa": 36.0,
          "zaman_farki": 467
      },
      {
          "takim_numarasi": 2,
          "iha_enlem": 41.5100365,
          "iha_boylam": 36.11837,
          "iha_irtifa": 44.0,
          "zaman_farki": 248
      }
  ]

  # Rakip İHA Konumlarını Listeye Dönüştürme
rakip_iha_konumlari = np.zeros((1,3))
for iha_bilgisi in konum_bilgileri:
    new = [[
            iha_bilgisi["iha_enlem"], 
            iha_bilgisi["iha_boylam"], 
            iha_bilgisi["iha_irtifa"]
    ]]
  
    rakip_iha_konumlari =np.append(rakip_iha_konumlari,new , axis = 0)


rakip_iha_konumlari = rakip_iha_konumlari[1:]
print(rakip_iha_konumlari)

      
  # KDTree Kullanarak En Yakın Rakip İHA'yı Bulma
kdtree = KDTree(np.array(rakip_iha_konumlari))

  # En Yakın Rakip İHA'nın Mesafesini ve Takım Numarasını Bulma
en_yakin_mesafe, en_yakin_index = kdtree.query(kendi_iha_konum, k=1)
print(en_yakin_mesafe)
print(en_yakin_index)
  # En Yakın Rakip İHA Bilgisini Alma
en_yakin_iha = konum_bilgileri[en_yakin_index[0] - 1 ]

  # Sonuçları Yazdırma
print("En Yakın Rakip İHA:")
print("Takım Numarası:", en_yakin_iha["takim_numarasi"])
print("Mesafe:", en_yakin_mesafe, "metre")



print(distance(p1=kendi_iha_konum,p2=rakip_iha_konumlari[1]))
print(distance(p1=kendi_iha_konum,p2=rakip_iha_konumlari[0]))