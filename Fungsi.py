def hitung_kecepatan_akhir(kecepatan_awal, percepatan, waktu):
    kecepatan_akhir = kecepatan_awal + (percepatan * waktu)
    return kecepatan_akhir

def hitung_jarak_ditempuh(kecepatan_awal, percepatan, waktu):
    jarak = (kecepatan_awal * waktu) + (0.5 * percepatan * waktu**2)
    return jarak

def tampilkan_output(n, input_data):
    print("---------------------------------------------------------------------------")
    print("| No. | Kecepatan Awal | Percepatan | Waktu | Kecepatan Akhir | Jarak |")
    print("---------------------------------------------------------------------------")
    for i in range(n):
        kecepatan_awal, percepatan, waktu = input_data[i]
        kecepatan_akhir = hitung_kecepatan_akhir(kecepatan_awal, percepatan, waktu)
        jarak = hitung_jarak_ditempuh(kecepatan_awal, percepatan, waktu)
        print(f"| {i+1:<3} | {kecepatan_awal:<14} | {percepatan:<10} | {waktu:<5} | {kecepatan_akhir:<15.2f} | {jarak:<9.2f} |")
    print("---------------------------------------------------------------------------")
    return tampilkan_output

n = int(input("Masukkan jumlah data: "))
input_data = []
for i in range(n):
    data = i + 1
    kecepatan_awal, percepatan, waktu = map(float, input(f"Masukkan data {data} (kecepatan awal, percepatan, dan waktu, pisahkan dengan spasi): ").split())
    input_data.append((kecepatan_awal, percepatan, waktu))

    
tampilkan_output(n, input_data)