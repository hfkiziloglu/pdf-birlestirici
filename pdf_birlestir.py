import os
from pathlib import Path
from PyPDF2 import PdfMerger

def pdf_birlestir():
    # Klasör yolu
    klasor = "birlestirilecekler"
    cikti_dosyasi = "birlesik.pdf"

    # Klasör yoksa oluştur
    if not os.path.exists(klasor):
        os.makedirs(klasor)
        print(f"'{klasor}' klasörü oluşturuldu.")
        print(f"Lütfen birleştirilecek PDF dosyalarını bu klasöre koyun.")
        return

    # PDF dosyalarını bul
    pdf_dosyalari = sorted([
        f for f in os.listdir(klasor)
        if f.lower().endswith('.pdf')
    ])

    if not pdf_dosyalari:
        print(f"'{klasor}' klasöründe PDF dosyası bulunamadı.")
        return

    print(f"{len(pdf_dosyalari)} adet PDF dosyası bulundu:")
    for i, dosya in enumerate(pdf_dosyalari, 1):
        print(f"  {i}. {dosya}")

    # PDF'leri birleştir
    merger = PdfMerger()

    try:
        for dosya in pdf_dosyalari:
            dosya_yolu = os.path.join(klasor, dosya)
            print(f"\nEkleniyor: {dosya}")
            merger.append(dosya_yolu)

        # Çıktı dosyasını kaydet
        merger.write(cikti_dosyasi)
        merger.close()

        print(f"\nPDF'ler başarıyla birleştirildi: {cikti_dosyasi}")

    except Exception as e:
        print(f"\nHata oluştu: {str(e)}")
        merger.close()

if __name__ == "__main__":
    pdf_birlestir()
