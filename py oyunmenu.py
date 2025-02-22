import random
import sys

def oyun_menusu():
    while True:
        print("\n🎮 Oyun Menüsüne Hoş Geldiniz! 🎮")
        print("1. Sayı Tahmin Oyunu")
        print("2. Taş-Kağıt-Makas")
        print("3. Matematik Quiz")
        print("4. Çıkış")

        secim = input("Seçiminizi yapın (1-4): ")

        if secim == "1":
            sayi_tahmin_oyunu()
        elif secim == "2":
            tas_kagit_makas()
        elif secim == "3":
            matematik_quiz()
        elif secim == "4":
            print("Oyundan çıkılıyor... Görüşmek üzere!")
            sys.exit()
        else:
            print("Geçersiz seçim, lütfen 1-4 arasında bir seçenek girin!")

def sayi_tahmin_oyunu():
    print("\n🎯 Sayı Tahmin Oyununa Hoş Geldiniz! 🎯")
    rastgele_sayi = random.randint(1, 100)
    tahmin = 0

    while tahmin != rastgele_sayi:
        tahmin = int(input("1 ile 100 arasında bir sayı tahmin edin: "))
        if tahmin < rastgele_sayi:
            print("Daha büyük bir sayı girin.")
        elif tahmin > rastgele_sayi:
            print("Daha küçük bir sayı girin.")
        else:
            print("Tebrikler, doğru tahmin! 🎉")

def tas_kagit_makas():
    print("\n✊✋✌️ Taş-Kağıt-Makas Oyununa Hoş Geldiniz! ✊✋✌️")
    secenekler = ["Taş", "Kağıt", "Makas"]
    
    while True:
        bilgisayar_secimi = random.choice(secenekler)
        oyuncu_secimi = input("Seçiminiz (Taş/Kağıt/Makas): ").capitalize()

        if oyuncu_secimi not in secenekler:
            print("Geçerli bir seçim yapın!")
            continue
        
        print(f"Bilgisayarın seçimi: {bilgisayar_secimi}")
        
        if oyuncu_secimi == bilgisayar_secimi:
            print("Berabere!")
        elif (oyuncu_secimi == "Taş" and bilgisayar_secimi == "Makas") or \
             (oyuncu_secimi == "Kağıt" and bilgisayar_secimi == "Taş") or \
             (oyuncu_secimi == "Makas" and bilgisayar_secimi == "Kağı"):
            print("Kazandınız! 🎉")
        else:
            print("Kaybettiniz! 😢")

        devam = input("Tekrar oynamak ister misiniz? (E/H): ").lower()
        if devam != "e":
            break

def matematik_quiz():
    print("\n🧮 Matematik Quizine Hoş Geldiniz! 🧮")
    puan = 0

    for _ in range(3):
        a, b = random.randint(1, 10), random.randint(1, 10)
        sonuc = a + b
        cevap = int(input(f"{a} + {b} = ? "))

        if cevap == sonuc:
            print("Doğru! ✅")
            puan += 1
        else:
            print(f"Yanlış! Doğru cevap: {sonuc}")

    print(f"Toplam puanınız: {puan}/3")

# Oyun menüsünü başlat
oyun_menusu()
