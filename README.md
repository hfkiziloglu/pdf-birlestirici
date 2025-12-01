# PDF Birleştirici

Birden fazla PDF dosyasını tek bir PDF dosyasında birleştiren basit bir Python programı

## Özellikler

- Birden fazla PDF dosyasını alfabetik sıraya göre birleştirir
- Kullanımı kolay ve basit arayüz
- Otomatik klasör oluşturma

## Gereksinimler

- Python 3.x
- PyPDF2 kütüphanesi

## Kurulum

1. Projeyi klonlayın:
```bash
git clone https://github.com/hfkiziloglu/pdf-birlestirici.git
cd pdf-birlestirici
```

2. Gerekli kütüphaneyi yükleyin:
```bash
pip install PyPDF2
```

## Kullanım

1. Birleştirmek istediğiniz PDF dosyalarını `birlestirilecekler` klasörüne koyun.

2. Programı çalıştırın:
```bash
python pdf_birlestir.py
```

3. Birleştirilmiş PDF dosyası `birlesik.pdf` adıyla ana klasörde oluşturulacaktır.

## Örnek Çıktı

```
3 adet PDF dosyası bulundu:
  1. dosya1.pdf
  2. dosya2.pdf
  3. dosya3.pdf

Ekleniyor: dosya1.pdf
Ekleniyor: dosya2.pdf
Ekleniyor: dosya3.pdf

PDF'ler başarıyla birleştirildi: birlesik.pdf
```

## Lisans

MIT License
