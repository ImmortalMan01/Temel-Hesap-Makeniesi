# Python GUI Hesap Makinesi

Bu depo, kullanım kolaylığı için Tkinter ile oluşturulmuş **Grafiksel Kullanıcı Arayüzüne (GUI)** sahip Python tabanlı bir hesap makinesi içerir.
Uygulama, `HesapMakinesi/calculator.py` içinde bulunan temel bir hesap makinesi mantık motorunu kullanır.

---

## GUI Hesap Makinesi

GUI hesap makinesi, hesaplamaları gerçekleştirmek için kullanıcı dostu, görsel bir yol sağlar. Python'un standart Tkinter kütüphanesi kullanılarak oluşturulmuştur.

### Hesap Makinesini Çalıştırma

GUI hesap makinesini çalıştırmak için terminalinizde projenin kök dizinine gidin ve şunu çalıştırın:

```bash
python HesapMakinesi/gui_calculator.py
```

### GUI Düzeni ve Kullanımı

GUI, üstte bir ekran alanı ve ardından çeşitli işlemler için düğme sıraları ile düzenlenmiştir.

-   **Ekran Alanı:** Üstteki geniş bir giriş alanı, oluşturulmakta olan mevcut ifadeyi ve hesaplamaların sonuçlarını gösterir.

-   **Hafıza Düğmeleri (Üst Sıra):**
    -   `MC` (Hafızayı Temizle): Hafızada saklanan değeri 0'a sıfırlar.
    -   `MR` (Hafızadan Çağır): Mevcut hafıza değerini ifadeye ekler. Hesaplamalarınızda bir sayı olarak kullanılabilir.
    -   `MS` (Hafızaya Kaydet): Ekrandaki mevcut ifadeyi değerlendirir ve sonucu hafızaya kaydeder.
    -   `M+` (Hafızaya Ekle): Mevcut ifadeyi değerlendirir ve sonucu hafızadaki mevcut değere ekler.
    -   `M-` (Hafızadan Çıkar): Mevcut ifadeyi değerlendirir ve sonucu hafızadaki mevcut değerden çıkarır.
    *Hafıza fonksiyonları, ara sonuçları veya sık kullanılan sayıları saklamak için kullanışlıdır.*

-   **Kontrol ve Temel Fonksiyon/Operatör Düğmeleri (Üstten İkinci Sıra):**
    -   `C` (Temizle): Mevcut ifadenin tamamını temizler ve ekranı sıfırlar.
    -   `CE` (Girişi Temizle): İfadeye girilen son karakteri temizler (basitleştirilmiş versiyon).
    -   `sqrt`: Karekök fonksiyonu.
    -   `pow`: Üs alma operatörü (`sayı pow üs` olarak kullanın).

-   **Sayı Düğmeleri (0-9, .):** Tipik bir tuş takımı düzeninde düzenlenmiş standart sayısal giriş ve ondalık nokta.

-   **Operatör Düğmeleri:**
    -   Temel Aritmetik: `+`, `-`, `*`, `/` (genellikle sayı sıralarının yanında bulunur).

-   **Gelişmiş Fonksiyon Düğmeleri (Özel Sıralar):**
    -   `log`: Doğal Logaritma (e tabanında).
    -   `log10`: 10 Tabanında Logaritma.
    -   `sin`, `cos`, `tan`: Trigonometrik fonksiyonlar (giriş açıları radyan cinsinden).

-   **Parantez ve Bilimsel Sabitler Düğmeleri (Alt Sıralar):**
    -   `(` ve `)`: İfadeleri gruplamak için.
    -   **Bilimsel Sabitler:**
        -   `π` (Pi): Pi değerini ekler (yaklaşık 3.14159).
        -   `e`: Euler sayısını ekler (yaklaşık 2.71828).
        -   `c`: Vakumdaki ışık hızını ekler (yaklaşık 2.998e8 m/s).
        -   `h`: Planck sabitini ekler (yaklaşık 6.626e-34 J*s).
        -   `G`: Kütleçekim sabitini ekler (yaklaşık 6.674e-11 N*m²/kg²).
    *Bir sabit düğmesine basmak, sembolünü (örneğin, "pi", "e", "c_isik") ifadeye ekler ve bu daha sonra tanımlanmış değeri kullanılarak değerlendirilir.*

-   **Eşittir Düğmesi (`=`):** Görüntülenen mevcut ifadeyi değerlendirir.

**Nasıl Kullanılır (Genel):**
1.  Ekran alanında matematiksel ifadenizi oluşturmak için düğmelere tıklayın.
2.  `sqrt` veya `log` gibi fonksiyonlar `sqrt(` veya `log(` olarak görünecek ve argümanı girmenizi isteyecektir.
3.  İfadenizin bölümlerini gerektiği gibi gruplamak için parantezleri `(` `)` kullanın.
4.  Sonucu görmek için `=` düğmesine basın.
5.  Bir hesaplamanın sonucu, bir sonraki hesaplama için başlangıç noktası olarak kullanılabilir.
6.  Mevcut ifadeyi temizlemek ve baştan başlamak için `C` düğmesine basın.

### Hata Yönetimi
Geçersiz bir ifade girerseniz veya bir hesaplama matematiksel bir hatayla sonuçlanırsa (örneğin, sıfıra bölme, negatif bir sayının karekökü):
-   Ekran tipik olarak "Hata" gösterecektir.
-   Daha spesifik bir hata mesajı içeren bir açılır iletişim kutusu görünecektir.
Bir hatadan sonra ifade genellikle temizlenir veya sıfırlanır, bu da yeni bir hesaplama başlatmanıza olanak tanır.

---

## Birim Testleri

Temel hesap makinesi mantığı (GUI tarafından kullanılır) Python'un `unittest` modülü kullanılarak birim testine tabi tutulur. Testler `HesapMakinesi/test_calculator.py` konumunda bulunur. `HesapMakinesi` dizinine gidin ve testleri çalıştırmak için şunu çalıştırın:
```bash
python -m unittest test_calculator.py
```

---
*Tarihsel Not: Bu proje başlangıçta çok temel bir C++ hesap makinesi olarak başladı. Daha sonra komut satırı arayüzüne (CLI) sahip bir Python projesine dönüştü. Yakın zamanda, CLI mevcut, daha kullanıcı dostu GUI hesap makinesi ile değiştirildi, ancak hala aynı temel Python tabanlı hesaplama mantığını kullanıyor.*
