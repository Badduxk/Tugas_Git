print("perubahan branch baru bang")
print("konflik")

data_panen = {
    'lokasi1':{
        'nama_lokasi': 'kebun a',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai':500
        }
    },
    'lokasi2':{
        'nama_lokasi': 'kebun b',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai':450
        }
    },
    'lokasi3':{
        'nama_lokasi': 'kebun c',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai':600
        }
    },
    'lokasi4':{
        'nama_lokasi': 'kebun d',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai':550
        }
    },
    'lokasi5':{
        'nama_lokasi': 'kebun e',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai':480
        }
    }
}

print("DATA PANEN PAK")
for i,a in data_panen.items():
    print(f"{a['nama_lokasi']}:{a['hasil_panen']}")
    
print("\nJumlah panen Jagung tiap lokasi")
for i,a in data_panen.items():
    print(f"{a['nama_lokasi']}:{a['hasil_panen']['jagung']} ton jagung")
    
print("\nNama Lokasi3")
print(f"{data_panen['lokasi3']['nama_lokasi']}\n")

jumlah_padi = {}
jumlah_kedelai = {}

for i,a in data_panen.items():
     jumlah_padi[i] = a['hasil_panen']['padi']
     jumlah_kedelai[i] = a['hasil_panen']['kedelai']
    
print("jumlah hasil panen padi setiap daerah\n",jumlah_padi)
print("jumlah hasil panen kedelai setiap daerah\n",jumlah_kedelai,"\n")


for i, a in data_panen.items():
    if a['hasil_panen']['padi'] > 1300 or a['hasil_panen']['jagung'] > 800:
        print(f"{a['nama_lokasi']}: memerlukan perhatian khusus") 
    else:
        print(f"{a['nama_lokasi']}: dalam kondisi aman")
