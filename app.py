# Load dataset dan lihat isi dari kolom
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
import streamlit as st
st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_page_config(page_title ='Jumlah Pendonor Darah', layout ='wide')

st.markdown(
    """
    <style>
    .title {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown("<h1 class='title'>Jumlah Pendonor Darah Berdasarkan Golongan Darah dan Jenis Kelamin di PMI Kota Tasikmalaya Dari Tahun 2022 s.d 2023.</h1>", unsafe_allow_html=True)

st.write(
   '\n\n'
)

st.write('Dataset ini berisi data jumlah pendonor darah berdasarkan golongan darah dan jenis kelamin di PMI Kota Tasikmalaya dari tahun 2022 s.d 2023. Dataset terkait topik kesehatan ini dihasilkan oleh Palang Merah Indonesia (PMI) Kota Tasikmalaya yang dikeluarkan dalam periode 1 tahun')


df= pd.read_csv('jumlah_pendonor_darah_berdasarkan_golongan_darah_dan_jenis_kelamin_di_tasikmalaya.csv')
#st.write(df)

# Filter data untuk tahun 2022
df_2022 = df[df['tahun'] == 2022]

# Menghitung jumlah pendonor darah berdasarkan golongan darah
jumlah_pendonor_per_golongan = df_2022.groupby('golongan_darah')['jumlah_pendonor_darah'].sum()
st.write(
   '\n\n'
)
# Membuat plot
col_1,col_2,col_3 = st.columns(3)
with col_1:
  plt.figure(figsize=(8, 6))
  jumlah_pendonor_per_golongan.plot(kind='bar', color='skyblue')
  plt.title('Jumlah Pendonor Darah Berdasarkan Golongan Darah Tahun 2022')
  plt.xlabel('Golongan Darah')
  plt.ylabel('Jumlah Pendonor Darah')
  plt.xticks(rotation=0)
  #plt.grid(axis='y', linestyle='--', alpha=0.7)
  # Menambahkan teks langsung di atas setiap balok kolom
  for i, jumlah in enumerate(jumlah_pendonor_per_golongan):
      plt.text(i, jumlah, str(jumlah), ha='center', va='bottom')

  plt.tight_layout()

  # Menampilkan plot
  st.pyplot()

# Filter data untuk tahun 2023
df_2023 = df[df['tahun'] == 2023]

# Menghitung jumlah pendonor darah berdasarkan golongan darah
jumlah_pendonor_per_golongan = df_2023.groupby('golongan_darah')['jumlah_pendonor_darah'].sum()

with col_2:
  plt.figure(figsize=(8, 6))
  jumlah_pendonor_per_golongan.plot(kind='bar', color='lightgreen')
  plt.title('Jumlah Pendonor Darah Berdasarkan Golongan Darah Tahun 2023')
  plt.xlabel('Golongan Darah')
  plt.ylabel('Jumlah Pendonor Darah')
  plt.xticks(rotation=0)
  #plt.grid(axis='y', linestyle='--', alpha=0.7)

  # Menambahkan teks langsung di atas setiap balok kolom
  for i, jumlah in enumerate(jumlah_pendonor_per_golongan):
      plt.text(i, jumlah, str(jumlah), ha='center', va='bottom')

  plt.tight_layout()

  # Menampilkan plot
  st.pyplot()

# Menghitung jumlah pendonor darah berdasarkan golongan darah untuk tahun 2022
jumlah_pendonor_per_golongan_2022 = df_2022.groupby('golongan_darah')['jumlah_pendonor_darah'].sum()
# Menghitung jumlah pendonor darah berdasarkan golongan darah untuk tahun 2023
jumlah_pendonor_per_golongan_2023 = df_2023.groupby('golongan_darah')['jumlah_pendonor_darah'].sum()
kategori = df['golongan_darah'].unique()
x = np.arange(len(kategori))
with col_3:
 st.write(
  '\n\n'
)
 plt.figure(figsize=(10, 6))
 # Plot untuk tahun 2022
 plt.bar(x= x- 0.2, height = jumlah_pendonor_per_golongan_2022, width=0.4, color='skyblue', label='2022')
 # Plot untuk tahun 2023
 plt.bar(x= x + 0.2, height = jumlah_pendonor_per_golongan_2023, width=0.4, color='lightgreen', label='2023')
 plt.title('Perbandingan Jumlah Pendonor Darah Berdasarkan Golongan Darah dan Tahun (2022-2023)')
 plt.xlabel('Golongan Darah')
 plt.ylabel('Jumlah Pendonor Darah')
 plt.xticks(x, kategori)
 plt.legend()
#plt.grid(axis='y', linestyle='--', alpha=0.7)
 for i, jumlah_pendonor_per_golongan_2022 in enumerate(jumlah_pendonor_per_golongan_2022):
    plt.text(i - 0.2, jumlah_pendonor_per_golongan_2022 +1, str(jumlah_pendonor_per_golongan_2022), ha = 'center', va = 'bottom')
 for i, jumlah_pendonor_per_golongan_2023 in enumerate(jumlah_pendonor_per_golongan_2023):
       plt.text(i + 0.2, jumlah_pendonor_per_golongan_2023 +1, str(jumlah_pendonor_per_golongan_2023), ha = 'center', va = 'bottom')
       plt.tight_layout()
       # Menampilkan plot
 st.pyplot()

st.write(
   '\n\n'
)

st.write('Visualisasi grafik batang diatas menunjukkan jumlah pendonor darah berdasarkan golongan darah tahun 2022 dan tahun 2023 ini mengalami kenaikan jumlah pendonor. Pada grafik diatas terlihat perbandingan jumlah pendonor yang meningkat dari tahun 2022 sampai 2023 dengan peningkatan yang signifikan terlihat pada grafik Perbandingan Jumlah Pendonor Darah Berdasarkan Golongan Darah dan Tahun (2022-2023) ada pada golongan darah O yaitu sebanyak 1.206 pendonor. Sedangkan pendonor darah dengan golongan darah B hanya mengalami peningkatan yang sedikit yaitu hanya sebanyak 204 pendonor. ')
st.write(
   '\n\n'
)
st.write(
   '\n\n'
)
st.write(
   '\n\n'
)

# Filter data untuk tahun 2022
df_2022 = df[df['tahun'] == 2022]

# Menghitung jumlah pendonor darah berdasarkan golongan darah dan jenis kelamin
jumlah_pendonor = df_2022.groupby(['golongan_darah', 'jenis_kelamin'])['jumlah_pendonor_darah'].sum().unstack()
col_1,col_2,col_3 = st.columns(3)
with col_1:
 plt.figure(figsize=(10, 6))
 jumlah_pendonor.plot(kind='bar', stacked=True, color=['lightblue', 'pink'])
 plt.title('Jumlah Pendonor Darah Berdasarkan Golongan Darah dan Jenis Kelamin Tahun 2022')
 plt.xlabel('Golongan Darah')
 plt.ylabel('Jumlah Pendonor Darah')
 plt.xticks(rotation=0)
 #plt.grid(axis='y',linestyle='--', alpha=0.7)
 plt.legend(title='Jenis Kelamin')
 plt.legend(loc='upper left')
 # Menambahkan teks langsung di atas setiap balok kolom
 for i, (index, row) in enumerate(jumlah_pendonor.iterrows()):
    for jenis_kelamin, jumlah in row.items():
       plt.text(i, row[:jenis_kelamin].sum(), str(jumlah), ha='center', va='bottom')
 plt.tight_layout()
 st.pyplot()


# Filter data untuk tahun 2022
df_2023 = df[df['tahun'] == 2023]

# Menghitung jumlah pendonor darah berdasarkan golongan darah dan jenis kelamin
jumlah_pendonor = df_2023.groupby(['golongan_darah', 'jenis_kelamin'])['jumlah_pendonor_darah'].sum().unstack()
with col_2:
# Membuat plot dengan warna yang berbeda untuk laki-laki dan perempuan
 plt.figure(figsize=(10, 6))
 jumlah_pendonor.plot(kind='bar', stacked=True, color=['grey', 'Violet'])
 plt.title('Jumlah Pendonor Darah Berdasarkan Golongan Darah dan Jenis Kelamin Tahun 2023')
 plt.xlabel('Golongan Darah')
 plt.ylabel('Jumlah Pendonor Darah')
 plt.xticks(rotation=0)
 #plt.grid(axis='y', linestyle='--', alpha=0.7)
 plt.legend(title='Jenis Kelamin')

# Menambahkan teks langsung di atas setiap balok kolom
 for i, (index, row) in enumerate(jumlah_pendonor.iterrows()):
    for jenis_kelamin, jumlah in row.items():
       plt.text(i, row[:jenis_kelamin].sum(), str(jumlah), ha='center', va='bottom')
       plt.tight_layout()

# Menampilkan plot
 plt.show()
 st.pyplot()

with col_3:
 st.write(
   '\n\n'
)
 st.write('Pada grafik disamping ini terlihat kenaikan jumlah pendonor laki-laki dan perempuan dari tahun 2022 ke tahun 2023. Jumlah pendonor laki-laki naik sebanyak 1.729 pendonor dan perempuan naik sebanyak 1.179 pendonor. Pertambahan yang paling sedikit yaitu terjadi pada golongan darah AB. Dalam banyak populasi di seluruh dunia, golongan darah AB hanya ditemukan pada sekitar 1% hingga 5% dari total populasi. Karena itu, golongan darah ini dianggap langka dibandingkan dengan golongan darah lainnya..')

st.write(
   '\n\n'
)

st.write(
   '\n\n'
)

st.write(
   '\n\n'
)
# Menghitung jumlah pendonor darah berdasarkan golongan darah dan jenis kelamin
jumlah_pendonor_jk_2022 = df_2022.groupby('jenis_kelamin')['jumlah_pendonor_darah'].sum()
jumlah_pendonor_jk_2023 = df_2023.groupby('jenis_kelamin')['jumlah_pendonor_darah'].sum()

# Membuat plot dengan warna yang berbeda untuk laki-laki dan perempuan
col_1,col_2,col_3 = st.columns(3)
with col_1:
 plt.figure(figsize=(10, 6))
 plt.bar(x = '2022', height = jumlah_pendonor_jk_2022['LAKI-LAKI'], width=0.4, color='skyblue', label='LAKI-LAKI')
 plt.bar(x = '2022', height = jumlah_pendonor_jk_2022['PEREMPUAN'], bottom = jumlah_pendonor_jk_2022['LAKI-LAKI'], width=0.4, color='pink', label='PEREMPUAN')
 plt.bar(x = '2023', height = jumlah_pendonor_jk_2023['LAKI-LAKI'], width=0.4, color='skyblue')
 plt.bar(x = '2023', height = jumlah_pendonor_jk_2023['PEREMPUAN'], bottom = jumlah_pendonor_jk_2023['LAKI-LAKI'],  width=0.4, color='pink')
 plt.title('Perbandingan Jumlah Pendonor Darah Berdasarkan Jenis Kelamin dan Tahun (2022 - 2023)')
 plt.xlabel('Tahun')
 plt.ylabel('Jumlah Pendonor Darah')
 plt.xticks(rotation=0)
 plt.legend(title='Jenis Kelamin')
 total_sementara = 0
 for isi in (jumlah_pendonor_jk_2022):
   total_sementara = isi + total_sementara
   plt.text(0, total_sementara + 1, str(isi), ha = 'center', va = 'bottom')
 total_sementara = 0
 for isi in (jumlah_pendonor_jk_2023):
   total_sementara = isi + total_sementara
   plt.text(1, total_sementara + 1, str(isi), ha = 'center', va = 'bottom')
 plt.tight_layout()
 plt.show()
 st.pyplot()

# Filter data untuk tahun 2022 dan 2023
df_2022 = df[df['tahun'] == 2022]
df_2023 = df[df['tahun'] == 2023]

# Menghitung jumlah pendonor darah berdasarkan golongan darah untuk tahun 2022
jumlah_pendonor_per_golongan_2022 = df_2022['jumlah_pendonor_darah'].sum()

# Menghitung jumlah pendonor darah berdasarkan golongan darah untuk tahun 2023
jumlah_pendonor_per_golongan_2023 = df_2023['jumlah_pendonor_darah'].sum()
with col_2:
 plt.figure(figsize=(10, 6))

 # Plot untuk tahun 2022
 plt.bar(x='2022', height = jumlah_pendonor_per_golongan_2022, width=0.4, color='skyblue', label='2022')
 # Plot untuk tahun 2023
 plt.bar(x='2023', height = jumlah_pendonor_per_golongan_2023, width=0.4, color='lightgreen', label='2023')
 plt.title('Perbandingan Jumlah Pendonor Darah (2022-2023)')
 plt.xlabel('Tahun')
 plt.ylabel('Jumlah Pendonor Darah')
 plt.xticks(rotation=0)
 plt.legend()
 #plt.grid(axis='y', linestyle='--', alpha=0.7)

 # Menambahkan label nilai di atas setiap balok kolom
 plt.text(x = 0, y = jumlah_pendonor_per_golongan_2022 , s = str(jumlah_pendonor_per_golongan_2022), ha='center', va='bottom')
 plt.text(x = 1, y = jumlah_pendonor_per_golongan_2023 , s = str(jumlah_pendonor_per_golongan_2023), ha='center', va='bottom')

 plt.tight_layout()

 # Menampilkan plot
 plt.show() 
 st.pyplot()
with col_3:
 st.write(
   '\n\n'
)
 st.write('Pada grafik disamping ini terlihat kenaikan jumlah pendonor dari tahun 2022-2023. Jumlah kenaikan pendonor dari tahun 2022-2023 sebanyak 2908 pendonor.Jumlah pendonor laki-laki naik sebanyak 1.729 pendonor dan perempuan naik sebanyak 1.179 pendonor.')

st.write('Insight Analysis:')
st.write(
   '\n\n'
)
st.write('1. Peningkatan jumlah pendonor dari tahun 2022 ke 2023 menunjukkan adanya peningkatan kesadaran masyarakat akan pentingnya donor darah. Hal ini bisa disebabkan oleh kampanye yang lebih efektif, perbaikan infrastruktur PMI, atau peristiwa khusus seperti bencana alam yang meningkatkan kebutuhan akan darah.')
st.write('2. Meskipun jumlah pendonor golongan darah O masih yang paling banyak, namun perlu diperhatikan bahwa pendonor golongan darah A dan B memiliki peningkatan yang signifikan dari tahun 2022 ke 2023. Hal ini bisa menjadi fokus untuk menggali alasan di balik peningkatan tersebut dan memperluas upaya pemasaran atau kampanye untuk golongan darah A dan golongan darah B.')
st.write('3. Terdapat pola yang menarik dalam perbandingan antara golongan darah dan jenis kelamin pendonor. pada golongan darah A, jumlah pendonor perempuan  lebih banyak daripada pendonor perempuan golongan darah B  pada tahun 2022 hingga 2023. Hal ini bisa menjadi titik awal untuk analisis lebih lanjut tentang faktor-faktor yang mempengaruhi partisipasi donor darah berdasarkan jenis kelamin.')
st.write('4. Terlihat bahwa baik laki-laki maupun perempuan mengalami peningkatan dalam partisipasi donor darah. Ini menunjukkan bahwa upaya untuk meningkatkan kesadaran dan motivasi donor darah dapat mencapai kedua jenis kelamin dengan efektif.')