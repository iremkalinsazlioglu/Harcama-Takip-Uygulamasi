import json

def verileri_yukle():
    try:
        with open("harcamalar.json", "r", encoding="utf-8") as dosya:
            return json.load(dosya)
    except FileNotFoundError:
       
        return []

def verileri_kaydet(harcama_listesi):

    with open("harcamalar.json", "w", encoding="utf-8") as dosya:
        json.dump(harcama_listesi, dosya, ensure_ascii=False, indent=4)


expenses = verileri_yukle()

while True:
    print("----işlemler----")
    print("1.Harcama Ekle")
    print("2.Harcamaları Listele")
    print("3.Harcama Düzenle")
    print("4.Harcama Sil")
    print("5.İstatistikleri Göster")
    print("6.Harcama Ara")
    print("7.Çıkış")

    choice = input("Lütfen yapmak istediğiniz işlemi seçin (1-7): ")

    if choice == "1":
        title = input("Harcama başlığı: ")
        category = input("Kategori: ")
        
        try:
            amount = float(input("Tutar: "))
            
            expense = {"title": title, "category": category, "amount": amount}
            expenses.append(expense)
            print("Harcama başarıyla eklendi!")
            verileri_kaydet(expenses)

        except ValueError:
            print("Hata: Lütfen tutar kısmına sadece sayı giriniz! (Örn: 150 veya 150.5)")

    elif choice == "2":
     print("Harcamaları listeleme işlemi başlatılıyor...")
     if len(expenses) == 0:
      print("Henüz harcama eklemediniz! Lütfen harcama ekleyip tekrar deneyin.")

     else:
      for expense in expenses:
       print(f"Başlık: {expense['title']} | Kategori: {expense['category']} | Tutar: {expense['amount']} TL")

    
    elif choice == "3":
     print("Harcama düzenleme işlemi başlatılıyor...")
     if len(expenses) == 0:
            print("Düzenlenebilir bir harcama bulunamadı! Lütfen harcama ekleyip tekrar deneyin.")
     else:
            i = 1
            for expense in expenses:
                print(f"{i}. Başlık: {expense['title']} | Kategori: {expense['category']} | Tutar: {expense['amount']} TL")
                i += 1
            
            try:
                selection = int(input("Düzenlemek istediğiniz harcamanın numarasını girin: "))
                index = selection - 1
                
                new_title = input("Yeni başlığı girin: ")
                new_category = input("Yeni kategoriyi girin: ")
                new_amount = float(input("Yeni tutarı girin: "))
                
                expenses[index]["title"] = new_title
                expenses[index]["category"] = new_category
                expenses[index]["amount"] = new_amount
                
                print("Harcama başarıyla güncellendi!")
                verileri_kaydet(expenses)

            except ValueError:
                print("Hata: Numara veya tutar seçimi yaparken lütfen sadece sayı giriniz!")
            except IndexError:
                print("Hata: Girdiğiniz numarada bir harcama listede bulunmuyor!")
            
    elif choice == "4":
        print("Harcama silme işlemi başlatılıyor...")
        if len(expenses) == 0:
            print("Silinecek bir harcama bulunamadı! Lütfen önce harcama ekleyin.")
        else:
            i = 1
            for expense in expenses:
                print(f"{i}. Başlık: {expense['title']} | Kategori: {expense['category']} | Tutar: {expense['amount']} TL")
                i += 1
            
            selection = int(input("Silmek istediğiniz harcamanın numarasını girin: "))
            index = selection - 1
            
            expenses.pop(index)
            
            print("Harcama başarıyla silindi!")
            verileri_kaydet(expenses)

    elif choice == "5":
        print("İstatistikler hesaplanıyor...")
        if len(expenses) == 0:
            print("Henüz istatistik hesaplanacak bir harcama yok!")
        else:
            total_amount = 0
            max_expense = expenses[0] 

            for expense in expenses:
                total_amount += expense["amount"]
                
                if expense["amount"] > max_expense["amount"]:
                    max_expense = expense
            
            average = total_amount / len(expenses)
            
            print("-" * 20)
            print(f"Toplam Harcama: {total_amount} TL")
            print(f"Ortalama Harcama: {average} TL")
            print(f"En Yüksek Harcama: {max_expense['title']} ({max_expense['amount']} TL)")
            print("-" * 20)


    elif choice == "6":
        search_term = input("Aranacak başlığı girin: ")
        found = False 
        for expense in expenses:
            if search_term.lower() in expense["title"].lower():
                print(f"Bulunan Harcama -> Başlık: {expense['title']} | Kategori: {expense['category']} | Tutar: {expense['amount']} TL")
                
                found = True 
                
        if not found:
            print("Bu başlıkta bir harcama bulunamadı.")

    elif choice == "7":
        print("Programdan çıkılıyor. İyi günler!")
        break

    else:
     print("Hatalı giriş! Lütfen 1-7 arasında bir değer tuşlayın.")