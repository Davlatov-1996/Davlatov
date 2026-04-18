# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# Mening birinchi kommentim CTRL + / - Kommentga oladi !


# print('Hello world')
# print("Hello world")   # CTRL + D - Dublikat qilib beradi !
#
# print('O`zbekiston')
# print("O'zbekiston")

# 's'
# 7
# 7.2

# print(10 + 5)
# print(10 - 5)
# print(10 * 5)
# print(10 ** 5) # Darajaga kotarish !
# print(10 / 5) # float - Kasr son qaytaradi !
# print(10 // 5) # integer int() - Butun sonni qaytaradi !
# print(10 % 5) # Qoldiqni aniqlash !


# print(5 > 10)  # False
# print(5 < 10)  # True
# boolean - False True


# print('s' + 7)


# name = 'Iskandar'
# last_name = 'Rustamov'
# age = 27
#
# print('Mening simim ' + name + ' familiyam ' + last_name + ' yoshim ' + str(age) + ' da!')
# print(f'Mening ismim {name}! Familiyam {last_name}! Yoshim {age} da!')


# CTRL + ALT + L - KOdni normaga olib keladi !


# name = input('Ismingizni kiriting: ')
# last_name = input('Familiyangizni kiriting: ')
# age = input('Yoshingizni kiriting: ')
#
# print(f'Sizning ismingiz {name}! Familiyangiz {last_name}! Yoshingiz {age} da!')


# a = float(input('Birinchi son kiriting: '))
# b = float(input('Ikkinchi son kiriting: '))
#
# print(a + b)

# print('Hello Bro\n'
#       '\tHello uka')



# =======================================================================================

# if elif else

# num1 = 10
# num2 = 20


# print(num1 == num2) # == - Tenglashtirish !
# print(num1 != num2) # != - Teng Emas !
# print(num1 > num2)
# print(num1 < num2)



# str5 = 'HElLo WorLd'
#
# print(str5)
# print(str5.upper()) # HELLO WORLD
# print(str5.lower()) # hello world
# print(str5.title()) # Hello World
# print(str5.swapcase()) # heLlO wORlD
# print(str5.capitalize()) # Hello world


# num = int(input('Son kiriting: '))
#
# if num >= 0:
#     print('Bu 0 dan katta son !')
# elif num == 0:
#     print('Bu nolku !')
# else:
#     print('Minusli son bu !')


# weather = input('Ob-xavo kiriting: ').lower()
#
# if weather == 'quyosh' or weather == 'anomal issiq':
#     print('Kocha issiq')
# elif weather == 'yomgir':
#     print('Zontik ovol')
# elif weather == 'qor':
#     print('Qor yogvotti')
# else:
#     print('Bu natogri kommanda !')


# Viloyat sonini kiritganda Davlat nomini chiqarsin !

# 12 -- UZB
# 50 -- USA
# 26 -- TKM
# 18 -- GRZ

# country = int(input('Viloyat sonini kiriting: '))
#
# if country == 12:
#     print('UZB')
# elif country == 8:
#     print('KGZ')
# elif country == 27:
#     print('KZ')
# else:
#     print('Xatolik!')


# age = int(input('Yosh kiriting: '))
#
# if 3 <= age <= 7:
#     print('Bolacha')
# elif 8 <= age <= 18:
#     print('Kotta bolacha')
# elif 19 <= age <= 25:
#     print('Student')
# else:
#     print('Xatolik!')

# login = input('Login kiriting: ')
# password = input('Parol kiriting: ')
# phone = input('Tel raqam kiriting: ')
#
# if login == 'admin123' and password == '123456' and phone == '998900070405':
#     print('Xush kelibsiz !')
# else:
#     print('Xush kemabsiz !')


#
# age = int(input('Yosh kiriting: '))
# passport = input('Pasportingiz bormi? ')
#
# if age >= 18 and passport == 'yoq' or passport == 'bor':
#     print('Sayoxat qilishingiz mumkin!')
# else:
#     print('Ruxsat yo`q!')

# age = int(input('Yosh kiriting: '))
# passport = input('Pasportingiz bormi? ').lower()
#
# if age >= 18 and passport == "bor":
#     print('Sayoxat qilishingiz mumkin!')
# else:
#     print('Ruxsat yo‘q!')

#
# age = int(input('Yosh kiriting: '))
# passport = input('Pasportingiz bormi? ').lower()
#
# if age >= 18 and passport == "bor":
#     print('Sayoxat qilishingiz mumkin!')
# else:
#     print('Ruxsat yo‘q!')



# age = int(input('Yosh: '))
# ticket = input('Bilet bormi? ').lower()
#
# if age >= 16 and ticket == 'bor':
#     print('Kirish mumkin')
# else:
#     print('Kirish mumkin emas')


# score = int(input("Ball: "))
#
# if score >= 60:
#     print("O‘tdingiz")
# else:
#     print("Yiqildingiz")


# status = input("Status (talaba/pensioner/oddiy): ").lower()
#
# if status == "talaba" or status == "pensioner":
#     print("Chegirma bor")
# else:
#     print("Chegirma yo‘q")


# score = int(input("Ball: "))
#
# if score >= 60:
#     print("O‘tdingiz")
# else:
#     print("Yiqildingiz")



# login = input("Login: ")
# password = input("Parol: ")
#
# if login == "admin" and password == "1234":
#     print("Kirish muvaffaqiyatli")
# else:
#     print("Xato login yoki parol")


# age = int(input("Yosh: "))
# license = input("Guvohnoma bormi? ").lower()
#
# if age >= 18 and license == "bor":
#     print("Haydash mumkin")
# else:
#     print("Haydash mumkin emas")


# score = int(input("Ball: "))
# english = input("Sertifikat bormi? ").lower()
#
# if (score >= 70 and english == "bor") or score >= 90:
#     print("Qabul qilindingiz")
# else:
#     print("Qabul qilinmadingiz")


# age = int(input("Yosh: "))
# exp = int(input("Tajriba (yil): "))
# eng = input("English bormi? ").lower()
# rus = input("Russian bormi? ").lower()
#
# if 20 <= age <= 35 and exp >= 2 and (eng == "bor" or rus == "bor"):
#     print("Ishga qabul qilindingiz")
# else:
#     print("Rad etildingiz")



# money = int(input("Pul: "))
# delivery = input("Delivery bormi? ").lower()
# pickup = input("O‘zi olib ketadimi? ").lower()
#
# if money >= 50 and (delivery == "bor" or pickup == "ha"):
#     print("Buyurtma qabul qilindi")
# else:
#     print("Buyurtma rad etildi")


# score = int(input("Ball: "))
#
# if score >= 85:
#     print("A’lo")
# elif score >= 60:
#     print("Yaxshi")
# else:
#     print("Yiqildingiz")


# vip = input("VIPmisiz? ").lower()
# age = int(input("Yosh: "))
# card = input("Karta bormi? ").lower()
#
# if vip == "ha":
#     print("Xush kelibsiz VIP!")
# elif age >= 18 and card == "bor":
#     print("Kirish mumkin")
# else:
#     print("Kirish taqiqlangan")


# pin = input("PIN kod: ")
#
# if pin == "1234":
#     balance = 1000
#     amount = int(input("Qancha pul yechmoqchisiz: "))
#
#     if amount <= balance:
#         print("Pul yechildi")
#     else:
#         print("Balans yetarli emas")
# else:
#     print("PIN xato")



# money = int(input("Pul: "))
# card = input("Karta bormi? ").lower()
# cash = input("Naqd bormi? ").lower()
# vip = input("VIPmisiz? ").lower()
#
# if money >= 100 and (card == "bor" or cash == "bor"):
#     if vip == "ha":
#         print("Sotib oldingiz (20% chegirma bilan)")
#     else:
#         print("Sotib oldingiz")
# else:
#     print("Sotib olish mumkin emas")


# age = int(input("Yosh: "))
# license = input("Guvohnoma bormi? ").lower()
# deposit = int(input("Depozit: "))
# vip = input("VIPmisiz? ").lower()
#
# if age >= 21 and license == "bor" and (deposit >= 500 or vip == "ha"):
#     print("Mashina ijaraga berildi")
# else:
#     print("Rad etildi")



# login = input("Login: ")
# password = input("Parol: ")
# age = int(input("Yosh: "))
#
# if login == "admin" and password == "11":
#     print("Admin panelga xush kelibsiz")
# elif login == "user" and password == "123":
#     if age >= 18:
#         print("User sifatida kirdingiz")
#     else:
#         print("Yosh yetarli emas")
# else:
#     print("Login yoki parol xato")



# passport = input("Pasport bormi? ").lower()
#
# if not passport == "bor":
#     print("Pasport yo‘q")


# password = ""
#
# while password != "1234":
#     password = input("Parol kiriting: ")
#
# print("Tizimga kirdingiz")


# def tekshir(age):
#     if age >= 18:
#         return "Mumkin"
#     else:
#         return "Mumkin emas"
#
# print(tekshir(18))


# text = '"Ali", "Vali", "Sardor"'
#
# names = text.replace('"', '').split(', ')
#
# for name in names:
#     print(name)


# import pandas as pd
#
# text = '"Ali", "Vali", "Sardor"'
# names = text.replace('"', '').split(', ')
#
# df = pd.DataFrame(names, columns=["Names"])
# df.to_excel("names.xlsx", index=False)



# import pandas as pd
#
# text = 'Ali, Vali, Sardor'
# names = text.replace('"', '').split(', ')
#
# df = pd.DataFrame(names, columns=["Names"])
#
# df.to_excel("names.xlsx", index=False)



# score = int(input("Ball: "))
#
# if score >= 85:
#     print("A’lo")
# elif score >= 60:
#     print("Yaxshi")
# else:
#     print("Yiqildingiz")


# print("Salom, Dunyo!")

# print('Davlatov Dilshodjon')
#
# name = "Ali"
# age = 25
# print('age')

# a = 2
# b = 3
# print(a ++ b)   # 15
# print(a ** b)   # 50
# # print(a/b)
#
# age = 17
#
# if age >= 18:
#     print("Kirish mumkin")
# else:
#     print("Kirish mumkin emas")

# for i in range(5):
#     print(i)

# price = 100
# discount = 0.2
#
# final_price = price * (1 - discount)
# print(final_price)

# ism = "Ali"
# yosh = 20
#
# print(ism)
# print(yosh)

# ism = input("Ismingni yoz: ")
# yosh = int(input("Yoshingni yoz: "))
#
# print(f"Salom, {ism}! Sen {yosh} yoshdasan.")


# ism = input("Ismingni yoz: ")
# yosh = int(input("Yoshingni yoz: "))
#
# kelasi_yil = yosh + 1   # FORMULA
#
# print(f"Salom, {ism}!")
# print(f"Kelasi yili sen {kelasi_yil} yoshda bo‘lasan.")


# ism = input("Ismingni yoz: ")
# yosh = int(input("Yoshingni yoz: "))
#
# hozirgi_yil = 2026
# tugilgan_yil = hozirgi_yil - yosh   # FORMULA
#
# print(f"{ism}, sen {tugilgan_yil}-yilda tug‘ilgansan.")

#
# yosh = int(input("Yoshingni yoz: "))
#
# if yosh >= 18:
#     print("Sen katta odamsan")
# else:
#     print("Sen hali yoshsan")

# a = int(input("1-sonni yoz: "))
# b = int(input("2-sonni yoz: "))
#
# print("Yig‘indi:", a + b)
# print("Ayirma:", a - b)
# print("Ko‘paytma:", a * b)
# print("Bo‘lish:", a / b)


# ism = "Davlatov"
# yosh = 20
#
# print(ism)
# print(yosh)

# ism = input("Ismingni yoz: ")
# yosh = input("Yoshingni yoz: ")
#
# print("Salom", ism)
# print("Sen", yosh, "yoshdasan")

# ism = input("Ismingni yoz: ")
# yosh = int(input("Yoshingni yoz: "))
#
# kelasi_yil = yosh + 1
#
# print(f"Salom, {ism}!")
# print(f"Kelasi yili sen {kelasi_yil} yoshda bo‘lasan.")
#
# import random
#
# son = random.randint(1, 10)
#
# while True:
#     taxmin = int(input("1 dan 10 gacha son o‘yla: "))
#
#     if taxmin == son:
#         print("🎉 To‘g‘ri topding!")
#         break
#     elif taxmin > son:
#         print("📉 Kichikroq son ayt")
#     else:
#         print("📈 Kattaroq son ayt")


# import random
#
# print("🎮 Son topish o‘yini")
#
# # difficulty tanlash
# daraja = input("Daraja tanla (easy / medium / hard): ")
#
# if daraja == "easy":
#     max_son = 10
# elif daraja == "medium":
#     max_son = 50
# else:
#     max_son = 100
#
# son = random.randint(1, max_son)
#
# urinishlar = 0
#
# while True:
#     taxmin = int(input(f"1 dan {max_son} gacha son o‘yla: "))
#     urinishlar += 1
#
#     if taxmin == son:
#         print(f"🎉 To‘g‘ri topding! {urinishlar} urinishda")
#         break
#     elif taxmin > son:
#         print("📉 Kichikroq son ayt")
#     else:
#         print("📈 Kattaroq son ayt")


# import random
#
# print("🎮 Son topish o‘yini (PRO)")
#
# umumiy_score = 0
#
# while True:
#     # difficulty
#     daraja = input("\nDaraja tanla (easy / medium / hard): ").lower()
#
#     if daraja == "easy":
#         max_son = 10
#     elif daraja == "medium":
#         max_son = 50
#     elif daraja == "hard":
#         max_son = 100
#     else:
#         print("❗ Noto‘g‘ri daraja, default = easy")
#         max_son = 10
#
#     son = random.randint(1, max_son)
#     urinishlar = 0
#
#     while True:
#         try:
#             taxmin = int(input(f"1 dan {max_son} gacha son o‘yla: "))
#         except:
#             print("❗ Iltimos faqat son kiriting")
#             continue
#
#         urinishlar += 1
#
#         if taxmin == son:
#             print(f"🎉 To‘g‘ri topding! {urinishlar} urinishda")
#
#             # score logika
#             score = max(0, (max_son * 2) - urinishlar)
#             umumiy_score += score
#
#             print(f"⭐ Bu o‘yindan score: {score}")
#             print(f"🏆 Umumiy score: {umumiy_score}")
#             break
#
#         elif taxmin > son:
#             print("📉 Kichikroq son ayt")
#         else:
#             print("📈 Kattaroq son ayt")
#
#     # qayta o‘ynash
#     yana = input("\nYana o‘ynaysanmi? (ha / yo‘q): ").lower()
#     if yana != "ha":
#         print("👋 O‘yin tugadi")
#         break


#
# import random
# import tkinter as tk
# from tkinter import messagebox
#
# son = random.randint(1, 100)
# urinish = 0
#
# def tekshir():
#     global urinish, son
#
#     try:
#         taxmin = int(entry.get())
#     except:
#         messagebox.showerror("Xato", "Faqat son kiriting")
#         return
#
#     urinish += 1
#
#     if taxmin == son:
#         messagebox.showinfo("Yutding!", f"{urinish} urinishda topding!")
#         son = random.randint(1, 100)
#         urinish = 0
#         entry.delete(0, tk.END)
#     elif taxmin > son:
#         label.config(text="📉 Kichikroq son ayt")
#     else:
#         label.config(text="📈 Kattaroq son ayt")
#
# # UI
# root = tk.Tk()
# root.title("Son topish o‘yini")
#
# label = tk.Label(root, text="1-100 oralig‘ida son top")
# label.pack()
#
# entry = tk.Entry(root)
# entry.pack()
#
# btn = tk.Button(root, text="Tekshir", command=tekshir)
# btn.pack()
#
# root.mainloop()





# from telegram.ext import ApplicationBuilder
#
# app = ApplicationBuilder().token("8779554312:AAF_lQ-BdInhfq_eAZYxUzi5Ap2W_ioY-RQ").build()
#
# app.run_polling()



# from telegram import Update
# from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
#
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text("Salom! Bot ishlayapti 🚀")
#
# app = ApplicationBuilder().token("8779554312:AAF_lQ-BdInhfq_eAZYxUzi5Ap2W_ioY-RQ").build()
#
# app.add_handler(CommandHandler("start", start))
#
# app.run_polling()



# from telegram import Update
# from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
# import random
#
# user_son = {}
# user_urinish = {}
#
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user_id = update.effective_user.id
#     user_son[user_id] = random.randint(1, 10)
#     user_urinish[user_id] = 0
#
#     await update.message.reply_text("🎮 O‘yin boshlandi! 1 dan 10 gacha son top!")
#
# async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user_id = update.effective_user.id
#
#     if user_id not in user_son:
#         user_son[user_id] = random.randint(1, 10)
#         user_urinish[user_id] = 0
#
#     try:
#         taxmin = int(update.message.text)
#     except:
#         await update.message.reply_text("❗ Faqat son yoz")
#         return
#
#     user_urinish[user_id] += 1
#     son = user_son[user_id]
#
#     if taxmin == son:
#         urinish = user_urinish[user_id]
#         await update.message.reply_text(f"🎉 To‘g‘ri! {urinish} urinishda topding!")
#
#         # yangi o‘yin
#         user_son[user_id] = random.randint(1, 10)
#         user_urinish[user_id] = 0
#         await update.message.reply_text("🔁 Yangi son o‘yladim! Yana top!")
#
#     elif taxmin > son:
#         await update.message.reply_text("📉 Kichikroq son ayt")
#     else:
#         await update.message.reply_text("📈 Kattaroq son ayt")
#
#
# app = ApplicationBuilder().token("8779554312:AAF_lQ-BdInhfq_eAZYxUzi5Ap2W_ioY-RQ").build()
#
# app.add_handler(CommandHandler("start", start))
# app.add_handler(MessageHandler(filters.TEXT, handle))
#
# app.run_polling()



#
#
# from telegram import Update, ReplyKeyboardMarkup
# from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
# import random
#
# # user data
# user_data = {}
#
# # 🔘 tugmalar
# menu = [["Level tanlash"], ["Score"], ["Leaderboard"]]
# keyboard = ReplyKeyboardMarkup(menu, resize_keyboard=True)
#
# # 🎮 start
# user_id = update.effective_user.id
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#
#     user_data[user_id] = {
#         "max": 10,
#         "son": random.randint(1, 10),
#         "urinish": 0,
#         "score": 0
#     }
#
#     await update.message.reply_text(
#         "🎮 O‘yin boshlandi!\n1 dan 10 gacha son top!",
#         reply_markup=keyboard
#     )
#
# # 🎯 handle (asosiy logika)
# async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user_id = update.effective_user.id
#     text = update.message.text
#
#     if user_id not in user_data:
#         await start(update, context)
#         return
#
#     data = user_data[user_id]
#
#     # 🔘 LEVEL TANLASH
#     if text == "Level tanlash":
#         await update.message.reply_text("Level tanla: easy / medium / hard")
#         return
#
#     if text.lower() == "easy":
#         data["max"] = 10
#     elif text.lower() == "medium":
#         data["max"] = 50
#     elif text.lower() == "hard":
#         data["max"] = 100
#     elif text == "Score":
#         await update.message.reply_text(f"⭐ Score: {data['score']}")
#         return
#     elif text == "Leaderboard":
#         sorted_users = sorted(user_data.items(), key=lambda x: x[1]["score"], reverse=True)
#         text_lb = "🏆 Leaderboard:\n"
#         for i, (uid, d) in enumerate(sorted_users[:5], start=1):
#             text_lb += f"{i}. User {uid} — {d['score']}\n"
#         await update.message.reply_text(text_lb)
#         return
#     else:
#         # 🎯 sonni tekshirish
#         try:
#             taxmin = int(text)
#         except:
#             await update.message.reply_text("❗ Son yoz yoki tugmani bos")
#             return
#
#         data["urinish"] += 1
#
#         if taxmin == data["son"]:
#             urinish = data["urinish"]
#             score = max(0, (data["max"] * 2) - urinish)
#             data["score"] += score
#
#             await update.message.reply_text(
#                 f"🎉 To‘g‘ri! {urinish} urinishda\n⭐ +{score} ball\n🏆 Umumiy: {data['score']}"
#             )
#
#             # reset
#             data["son"] = random.randint(1, data["max"])
#             data["urinish"] = 0
#             return
#
#         elif taxmin > data["son"]:
#             await update.message.reply_text("📉 Kichikroq")
#         else:
#             await update.message.reply_text("📈 Kattaroq")
#
#         return
#
#     # level o‘zgarsa yangi o‘yin
#     data["son"] = random.randint(1, data["max"])
#     data["urinish"] = 0
#
#     await update.message.reply_text(f"✅ Level o‘zgardi! 1 dan {data['max']} gacha top!")
#
# # 🚀 run
# app = ApplicationBuilder().token("8779554312:AAF_lQ-BdInhfq_eAZYxUzi5Ap2W_ioY-RQ").build()
#
# app.add_handler(CommandHandler("start", start))
# app.add_handler(MessageHandler(filters.TEXT, handle))
#
# app.run_polling()




# from telegram import Update, ReplyKeyboardMarkup
# from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
# import random
#
# user_data = {}
#
# menu = [["Level tanlash"], ["Score"], ["Leaderboard"]]
# keyboard = ReplyKeyboardMarkup(menu, resize_keyboard=True)
#
# # 🚀 START
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user_id = update.effective_user.id
#
#     user_data[user_id] = {
#         "name": None,
#         "max": 10,
#         "son": random.randint(1, 10),
#         "urinish": 0,
#         "score": 0
#     }
#
#     await update.message.reply_text("Ismingni yoz:")
#
# # 🎯 HANDLE
# async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user_id = update.effective_user.id
#     text = update.message.text
#
#     if user_id not in user_data:
#         await start(update, context)
#         return
#
#     data = user_data[user_id]
#
#     # 🧑 ISM YOZISH
#     if data["name"] is None:
#         data["name"] = text
#         await update.message.reply_text(
#             f"Salom, {data['name']}! 🎮 O‘yin boshlandi!\n1 dan 10 gacha son top!",
#             reply_markup=keyboard
#         )
#         return
#
#     # 🔘 BUTTONLAR
#     if text == "Level tanlash":
#         await update.message.reply_text("Level tanla: easy / medium / hard")
#         return
#
#     if text.lower() == "easy":
#         data["max"] = 10
#     elif text.lower() == "medium":
#         data["max"] = 50
#     elif text.lower() == "hard":
#         data["max"] = 100
#     elif text == "Score":
#         await update.message.reply_text(f"⭐ Score: {data['score']}")
#         return
#     elif text == "Leaderboard":
#         sorted_users = sorted(user_data.items(), key=lambda x: x[1]["score"], reverse=True)
#         text_lb = "🏆 Leaderboard:\n"
#         for i, (uid, d) in enumerate(sorted_users[:5], start=1):
#             name = d["name"] if d["name"] else "NoName"
#             text_lb += f"{i}. {name} — {d['score']}\n"
#         await update.message.reply_text(text_lb)
#         return
#     else:
#         # 🎯 O‘YIN LOGIKA
#         try:
#             taxmin = int(text)
#         except:
#             await update.message.reply_text("❗ Son yoz yoki tugmani bos")
#             return
#
#         data["urinish"] += 1
#
#         if taxmin == data["son"]:
#             urinish = data["urinish"]
#             score = max(0, (data["max"] * 2) - urinish)
#             data["score"] += score
#
#             await update.message.reply_text(
#                 f"🎉 To‘g‘ri, {data['name']}! {urinish} urinishda\n⭐ +{score} ball\n🏆 Umumiy: {data['score']}"
#             )
#
#             data["son"] = random.randint(1, data["max"])
#             data["urinish"] = 0
#             return
#
#         elif taxmin > data["son"]:
#             await update.message.reply_text("📉 Kichikroq")
#         else:
#             await update.message.reply_text("📈 Kattaroq")
#
#         return
#
#     # level change
#     data["son"] = random.randint(1, data["max"])
#     data["urinish"] = 0
#
#     await update.message.reply_text(f"✅ Level o‘zgardi! 1 dan {data['max']} gacha top!")
#
# # ▶️ RUN
# app = ApplicationBuilder().token("8779554312:AAF_lQ-BdInhfq_eAZYxUzi5Ap2W_ioY-RQ").build()
#
# app.add_handler(CommandHandler("start", start))
# app.add_handler(MessageHandler(filters.TEXT, handle))
#
# app.run_polling()
#
#
#
#
# from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
# from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes
# import random
#
# user_data = {}
#
# menu = [["Level tanlash"], ["Score"], ["Leaderboard"]]
# keyboard = ReplyKeyboardMarkup(menu, resize_keyboard=True)
#
# level_buttons = InlineKeyboardMarkup([
#     [InlineKeyboardButton("Easy (1-10)", callback_data="easy")],
#     [InlineKeyboardButton("Medium (1-50)", callback_data="medium")],
#     [InlineKeyboardButton("Hard (1-100)", callback_data="hard")]
# ])
#
# # START
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user_id = update.effective_user.id
#
#     user_data[user_id] = {
#         "name": None,
#         "max": 10,
#         "son": random.randint(1, 10),
#         "urinish": 0,
#         "score": 0
#     }
#
#     await update.message.reply_text("Ismingni yoz:")
#
# # BUTTON HANDLER
# async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     query = update.callback_query
#     await query.answer()
#
#     user_id = query.from_user.id
#     data = user_data[user_id]
#
#     choice = query.data
#
#     if choice == "easy":
#         data["max"] = 10
#     elif choice == "medium":
#         data["max"] = 50
#     elif choice == "hard":
#         data["max"] = 100
#
#     data["son"] = random.randint(1, data["max"])
#     data["urinish"] = 0
#
#     await query.edit_message_text(f"✅ Level: {choice.upper()} | 1 dan {data['max']} gacha top!")
#
# # MAIN HANDLE
# async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user_id = update.effective_user.id
#     text = update.message.text
#
#     if user_id not in user_data:
#         await start(update, context)
#         return
#
#     data = user_data[user_id]
#
#     # NAME
#     if data["name"] is None:
#         data["name"] = text
#         await update.message.reply_text(
#             f"Salom, {data['name']}!\n1 dan 10 gacha son top!",
#             reply_markup=keyboard
#         )
#         return
#
#     # BUTTON MENU
#     if text == "Level tanlash":
#         await update.message.reply_text("Level tanla:", reply_markup=level_buttons)
#         return
#
#     if text == "Score":
#         await update.message.reply_text(f"⭐ Score: {data['score']}")
#         return
#
#     if text == "Leaderboard":
#         sorted_users = sorted(user_data.items(), key=lambda x: x[1]["score"], reverse=True)
#         text_lb = "🏆 Leaderboard:\n"
#         for i, (uid, d) in enumerate(sorted_users[:5], start=1):
#             name = d["name"] if d["name"] else "NoName"
#             text_lb += f"{i}. {name} — {d['score']}\n"
#         await update.message.reply_text(text_lb)
#         return
#
#     # GAME
#     try:
#         taxmin = int(text)
#     except:
#         await update.message.reply_text("❗ Son yoz yoki tugmani bos")
#         return
#
#     data["urinish"] += 1
#
#     if taxmin == data["son"]:
#         urinish = data["urinish"]
#         score = max(0, (data["max"] * 2) - urinish)
#         data["score"] += score
#
#         await update.message.reply_text(
#             f"🎉 To‘g‘ri, {data['name']}!\n{urinish} urinish\n⭐ +{score} ball\n🏆 {data['score']}"
#         )
#
#         data["son"] = random.randint(1, data["max"])
#         data["urinish"] = 0
#
#     elif taxmin > data["son"]:
#         await update.message.reply_text("📉 Kichikroq")
#     else:
#         await update.message.reply_text("📈 Kattaroq")
#
# # RUN
# app = ApplicationBuilder().token("8779554312:AAF_lQ-BdInhfq_eAZYxUzi5Ap2W_ioY-RQ").build()
#
# app.add_handler(CommandHandler("start", start))
# app.add_handler(CallbackQueryHandler(button_handler))
# app.add_handler(MessageHandler(filters.TEXT, handle))
#
# app.run_polling()


#
# import sqlite3
#
# conn = sqlite3.connect("game.db", check_same_thread=False)
# cursor = conn.cursor()
#
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS users (
#     user_id INTEGER PRIMARY KEY,
#     name TEXT,
#     score INTEGER DEFAULT 0
# )
# """)
# conn.commit()
#
# def save_user(user_id, name):
#     cursor.execute("INSERT OR IGNORE INTO users (user_id, name) VALUES (?, ?)", (user_id, name))
#     conn.commit()
#
# def update_score(user_id, score):
#     cursor.execute("UPDATE users SET score = score + ? WHERE user_id = ?", (score, user_id))
#     conn.commit()
#
# def update_name(user_id, name):
#     cursor.execute("UPDATE users SET name = ? WHERE user_id = ?", (name, user_id))
#     conn.commit()
#
# def get_top():
#     cursor.execute("SELECT name, score FROM users ORDER BY score DESC LIMIT 5")
#     return cursor.fetchall()



from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes
import random

from db import save_user, update_score, get_top, update_name

user_data = {}

menu = [["Level tanlash"], ["Score"], ["Leaderboard"]]
keyboard = ReplyKeyboardMarkup(menu, resize_keyboard=True)

level_buttons = InlineKeyboardMarkup([
    [InlineKeyboardButton("Easy (1-10)", callback_data="easy")],
    [InlineKeyboardButton("Medium (1-50)", callback_data="medium")],
    [InlineKeyboardButton("Hard (1-100)", callback_data="hard")]
])

# START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    user_data[user_id] = {
        "name": None,
        "max": 10,
        "son": random.randint(1, 10),
        "urinish": 0
    }

    await update.message.reply_text("Ismingni yoz:")

# BUTTON HANDLER
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id
    data = user_data[user_id]

    choice = query.data

    if choice == "easy":
        data["max"] = 10
    elif choice == "medium":
        data["max"] = 50
    elif choice == "hard":
        data["max"] = 100

    data["son"] = random.randint(1, data["max"])
    data["urinish"] = 0

    await query.edit_message_text(f"✅ Level: {choice.upper()} | 1 dan {data['max']} gacha top!")

# CHANGE NAME
async def change_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    new_name = " ".join(context.args)

    if not new_name:
        await update.message.reply_text("Ism yoz: /name Ali")
        return

    user_data[user_id]["name"] = new_name
    update_name(user_id, new_name)

    await update.message.reply_text(f"✅ Ism o‘zgardi: {new_name}")

# MAIN HANDLE
async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    text = update.message.text

    if user_id not in user_data:
        await start(update, context)
        return

    data = user_data[user_id]

    # NAME
    if data["name"] is None:
        data["name"] = text
        save_user(user_id, text)

        await update.message.reply_text(
            f"Salom, {data['name']}!\n1 dan 10 gacha son top!",
            reply_markup=keyboard
        )
        return

    # MENU
    if text == "Level tanlash":
        await update.message.reply_text("Level tanla:", reply_markup=level_buttons)
        return

    if text == "Score":
        await update.message.reply_text("Score DB’da saqlanadi 👍")
        return

    if text == "Leaderboard":
        top = get_top()
        text_lb = "🏆 Leaderboard:\n"

        for i, (name, score) in enumerate(top, start=1):
            text_lb += f"{i}. {name} — {score}\n"

        await update.message.reply_text(text_lb)
        return

    # GAME
    try:
        taxmin = int(text)
    except:
        await update.message.reply_text("❗ Son yoz yoki tugmani bos")
        return

    data["urinish"] += 1

    if taxmin == data["son"]:
        urinish = data["urinish"]
        score = max(0, (data["max"] * 2) - urinish)

        update_score(user_id, score)

        await update.message.reply_text(
            f"🎉 To‘g‘ri, {data['name']}!\n{urinish} urinish\n⭐ +{score} ball"
        )

        data["son"] = random.randint(1, data["max"])
        data["urinish"] = 0

    elif taxmin > data["son"]:
        await update.message.reply_text("📉 Kichikroq")
    else:
        await update.message.reply_text("📈 Kattaroq")


# RUN
app = ApplicationBuilder().token("8779554312:AAF_lQ-BdInhfq_eAZYxUzi5Ap2W_ioY-RQ").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("name", change_name))
app.add_handler(CallbackQueryHandler(button_handler))
app.add_handler(MessageHandler(filters.TEXT, handle))

app.run_polling()


