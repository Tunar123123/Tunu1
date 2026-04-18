import time

def tunarin_dunyasi():
    ad = "Tunar"
    print("🚀 Sistem yüklənir...")
    time.sleep(1)
    muellim_adi = input("Hörmətli müəllim, adınızı yazın: ")
    print(f"\n🌟 XOŞ GƏLDİNİZ, {muellim_adi.upper()} MÜƏLLİM! 🌟")
    hobbilər = ["📚 Kitab oxumaq", "🎮 Oyun oynamaq", "⚽ Futbol oynamaq", "💻 Kod yazmaq"]
    print("\nHobbilərim:")
    for hobi in hobbilər:
        print(hobi)
    print("\nGələcəyin proqramçısından sizə salamlar! 👋")

if __name__ == "__main__":
    tunarin_dunyasi()
