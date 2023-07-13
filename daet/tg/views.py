from telegram import KeyboardButton, ReplyKeyboardMarkup

contact = ReplyKeyboardMarkup([
    [KeyboardButton("Contact", request_contact=True)]
], resize_keyboard=True)

log = {"state": 0}


def button(type=None):
    btn = []
    if type == "til":
        btn = [
            [KeyboardButton('uz🇺🇿')]
        ]
    elif type == "location":
        btn = [
            [KeyboardButton("Toshkent"), KeyboardButton("Toshkent viloyati"), KeyboardButton("Andijon viloyati"), ],
            [KeyboardButton("Fargʻona viloyati"), KeyboardButton("Buxoro viloyati"), KeyboardButton("Xorazm viloyati")],
            [KeyboardButton("Namangan viloyati"), KeyboardButton("Jizzax viloyati"), KeyboardButton("Navoiy viloyati")],
            [KeyboardButton("Qashqadaryo viloyati"), KeyboardButton("Qoraqalpogʻiston viloyati"),
             KeyboardButton("Sirdaryo viloyati")],
            [KeyboardButton("Samarqand  viloyati"), KeyboardButton("Surxondaryo viloyati")],
            [KeyboardButton("◀️Ortga")],
        ]
    elif type == "menu":
        btn = [
            [KeyboardButton("🍴 Menyu")],
            [KeyboardButton("🛍 Mening buyurtmalarim")],
            [KeyboardButton("✍ Fikr bildirish"), KeyboardButton("⚙ Sozlamalar")],
            [KeyboardButton("◀️Ortga")],
        ]

    elif type == "menu_ctg":
        btn = [
            [KeyboardButton("🍱 Set"), KeyboardButton("🫔 lavash")],
            [KeyboardButton("🥙 Shaurma"), KeyboardButton("🥙 Donar")],
            [KeyboardButton("🍔 Burger"), KeyboardButton("🌭 Hot Dog")],
            [KeyboardButton("🍰 Cake & Bakery"), KeyboardButton("☕ Ichimliklar")],
            [KeyboardButton("◀️Ortga")],
        ]

    elif type == "🫔 lavash":
        btn = [
            [KeyboardButton("Tovuq goʼshtli qalampirli lavash"), KeyboardButton("Tovuq goʼshtli pishloqli lavash")],
            [KeyboardButton("Mol goʼshtidan qalampirli lavash"), KeyboardButton("Mol goʼshtidan lavash")],
            [KeyboardButton("FITTER")],
            [KeyboardButton("◀️Ortga")],
        ]

    elif type == "🍱 Set":
        btn = [
            [KeyboardButton("COMBO+"), KeyboardButton("Kids COMBO")],
            [KeyboardButton("◀️Ortga")],
        ]

    elif type == "🥙 Shaurma":
        btn = [
            [KeyboardButton("Tovuq goʼshtidan taʼmi oʼtkir shaurma"), KeyboardButton("Tovuq goʼshtidan shaurma")],
            [KeyboardButton("Mol goʼshtidan shaurma"), KeyboardButton("Mol goʼshtidan taʼmi oʼtkir shaurma")],
            [KeyboardButton("◀️Ortga")],
        ]

    elif type == "🥙 Donar":
        btn = [
            [KeyboardButton("Mol goʼshtidan donar"), KeyboardButton("Tovuq goʼshtidan donar")],
            [KeyboardButton("◀️Ortga")],
        ]

    elif type == "🍔 Burger":
        btn = [
            [KeyboardButton("Gamburger"), KeyboardButton("Dablburger")],
            [KeyboardButton("Chizburger"), KeyboardButton("Dablchizburger")],
            [KeyboardButton("◀️Ortga")],
        ]

    elif type == "🌭 Hot Dog":
        btn = [
            [KeyboardButton("Baget Xot Dogi"), KeyboardButton("Baget Dabl Xot Dogi")],
            [KeyboardButton("Xot Dog Kids"), KeyboardButton("An'anaviy Xot Dog")],
            [KeyboardButton("◀️Ortga")],
        ]

    elif type == "🍰 Cake & Bakery":
        btn = [
            [KeyboardButton("Medovik Asalim"), KeyboardButton("Chizkeyk")],
            [KeyboardButton("◀️Ortga")],
        ]

    elif type == "☕ Ichimliklar":
        btn = [
            [KeyboardButton("Pepsi 0.5"), KeyboardButton("Pepsi 1.5")],
            [KeyboardButton("Latte"), KeyboardButton("Kapuchino")],
            [KeyboardButton("Amerikano")],
            [KeyboardButton("◀️Ortga")],
        ]

    elif type == "⚙ Sozlamalar":
        btn = [
            [KeyboardButton('uz🇺🇿')],
            [KeyboardButton("◀️Ortga")],
        ]

    return ReplyKeyboardMarkup(btn, resize_keyboard=True)


def start(update, context):
    user = update.message.from_user
    log['state'] = 0
    update.message.reply_text(
        f"Assalomu aleykum   {user.username}   \n\nRo'yxatdan o'tish uchun, Tilni tanlang👇", reply_markup=button("til"))
    update.message.reply_text(
        "🇺🇿 Foydalanuvchilarimizda uzur so'raymiz hali boshqa tillar yo'lga qo'yilmadi ☺ \n\n🇺🇸 Sorry for our users, other languages are not available yet ☺ \n\n🇷🇺 Извините за наших пользователей, другие языки пока недоступны ☺")


def message_handler(update, context):
    msg = update.message.text

    if msg == "🍴 Menyu":
        log["state"] = 6

    if msg == "⚙ Sozlamalar":
        update.message.reply_text("Kechirasiz bu tizim hali yo'lga qo'yilmadi. ")

    if msg == "✍ Fikr bildirish":
        update.message.reply_text("Kechirasiz bu tizim hali yo'lga qo'yilmadi. ")

    if msg == "🛍 Mening buyurtmalarim":
        update.message.reply_text("Siz hech narsa buyurtma bermagansiz. ")

    if msg == "◀️Ortga":
        update.message.reply_text("Jarayonda 😉 ")

    # Ichimliklar
    if msg == "Pepsi 0.5":
        update.message.reply_text("Аlkogolsiz gazlangan ichimlik\nNarxi:8.000 so'm")

    if msg == "Pepsi 1.5":
        update.message.reply_text("Аlkogolsiz gazlangan ichimlik\nNarxi:14.000 so'm")

    if msg == "Latte":
        update.message.reply_text("Narxi: 10.000 so'm")

    if msg == "Kapuchino":
        update.message.reply_text("Narxi: 10.000 so'm")

    if msg == "Amerikano":
        update.message.reply_text("Narxi: 9.000 so'm")

    # Cake & Bakery
    if msg == "Medovik Asalim":
        update.message.reply_text("Narxi: 10.000 so'm")

    if msg == "Chizkeyk":
        update.message.reply_text("Narxi: 10.000 so'm")

    # Hod-dog
    if msg == "Baget Xot Dogi":
        update.message.reply_text("Kunjutli kulcha, sosiska, tuzlangan bodring, pomidorlar,\nyangi muztogʼ salati va maxsus qayla\nNarxi: 11.000 so'm")

    if msg == "Baget Dabl Xot Dogi":
        update.message.reply_text("Kunjutli kulcha, ikkita sosiska, tuzlangan bodringlar,\npomidorlar, yangi muztogʼ salati va maxsus qayla\nNarxi: 17.000 so'm")

    if msg == "Xot Dog Kids":
        update.message.reply_text("Narxi: 8 000 so'm")

    if msg == "An'anaviy Xot Dog":
        update.message.reply_text("Kulcha, sosiska, ketchup va xantal, qovurilgan piyoz\nNarxi: 8 000 so'm")

    # Burger
    if msg == "Gamburger":
        update.message.reply_text(
            "Yumshoq kulcha, yumshoq mol goʼshtidan kotlet,\ntuzlangan bodringlar, yangi pomidorlar, qizil piyoz va\nikkita maxsus qayla bilan qarsildoq muztogʼ salati\nNarxi: 19.000 so'm 😃")

    if msg == "Dablburger":
        update.message.reply_text(
            "Yumshoq kulcha, yumshoq mol goʼshtidan ikkita kotlet,\ntuzlangan bodringlar, yangi pomidorlar, qizil piyoz va\nikkita maxsus qayla bilan qarsildoq muztogʼ salati\nNarxi: 27.000 so'm 😃")

    if msg == "Dablchizburger":
        update.message.reply_text(
            "Yumshoq kulcha, eritilgan Cheddar pishlogʼi boʼlakchalari\nbilan mol goʼshtidan yumshoq ikkita kotlet,\ntuzlangan bodringlar, yangi pomidorlar, qizil piyoz va\nikkita maxsus qayla bilan qarsildoq muztogʼ salati\nNarxi: 31.000 so'm 😃")

    if msg == "Chizburger":
        update.message.reply_text(
            "Yumshoq kulcha, bir boʼlak eritilgan Cheddar pishlogʼi\nbilan mol goʼshtidan yumshoq kotlet, tuzlangan bodring,\nyangi pomidorlar, qizil piyoz va ikkita maxsus qayla bilan\nqarsildoq muztogʼ salati\nNarxi: 21 000 so'm 😃")

    # Donar
    if msg == "Mol goʼshtidan donar":
        update.message.reply_text(
            "Yumshoq mol goʼshti, qovurilgan kartoshka, guruch va\nsabzavot salatidan iborat toʼyimli toʼplam.\nBizning pomidordan tayyorlangan maxsus qaylamiz bilan birga tortiladi\nNarxi: 38.000 so'm")

    if msg == "Tovuq goʼshtidan donar":
        update.message.reply_text(
            "Yumshoq tovuq goʼshti, qovurilgan kartoshka, guruch va\nsabzavot salatidan iborat toʼyimli toʼplam.\nBizning pomidordan tayyorlangan maxsus qaylamiz bilan birga tortiladi\nNarxi: 36.000 so'm")

    # Shauama
    if msg == "Tovuq goʼshtidan taʼmi oʼtkir shaurma":
        update.message.reply_text("Mini 21.000 so'm\nBig 24.000 so'm 😊")

    if msg == "Mol goʼshtidan taʼmi oʼtkir shaurma":
        update.message.reply_text("Mini 19.000 so'm\nBig 23.000 so'm 😊")

    if msg == "Tovuq goʼshtidan shaurma":
        update.message.reply_text("Mini 18.000 so'm\nBig 21.000 so'm 😊")

    if msg == "Mol goʼshtidan shaurma":
        update.message.reply_text("Mini 19.000 so'm\nBig 23.000 so'm 😊")

    # set
    if msg == "COMBO+":
        update.message.reply_text(
            "Yeng yaxshi taklif! Issiq qarsildoq qovurilgan kartoshka va\nbir stakan Pepsi\nNarxi: 14.000 so'm 😊")

    if msg == "Kids COMBO":
        update.message.reply_text("Mini Xod dog hamda\nqovurilgan kartoshka va Bliss so'ki\nNarxi: 15.000 so'm 😊")

    # Lavash
    if msg == "Tovuq goʼshtli qalampirli lavash":
        update.message.reply_text(
            "Yangi bodring va pomidorlar, qarsildoq chipslar bilan\nlavashga oʼralgan qovurilgan tovuq filesi, bizning taʼmi\noʼtkir maxsus qayla bilan\nNarxi: 21.500 so'm 😊")

    if msg == "Tovuq goʼshtli pishloqli lavash":
        update.message.reply_text("Mini 21.000 so'm\nBig 24.000 so'm 😊")

    if msg == "Mol goʼshtidan lavash":
        update.message.reply_text("Mini 20.000 so'm\nBig 23.000 so'm 😊")

    if msg == "Mol goʼshtidan qalampirli lavash":
        update.message.reply_text(
            "Qarsildoq chipslar, yangi bodring va pomidorlar bilan\nlavashga oʼralgan yumshoq mol goʼshti, bizning taʼmi oʼtkir\nqayla bilan\nNarxi: 23.500 so'm 😊")

    if msg == "FITTER":
        update.message.reply_text(
            "Tovuq goʼshti, qarsildoq muztogʼ salati, yangi bodring\nva pomidorlar, fetaksa va bizning maxsus qaylamiz - barchasi yashil lavashga oʼralgan\nNarxi: 21.000 so'm 😊   ")

    if log['state'] == 0:
        log['til'] = msg
        log['state'] = 1
        update.message.reply_text(f"Yaxshi 😊\nIsmingizni kiriting📝")

    elif log['state'] == 1:
        log['ism'] = msg
        log["state"] = 2
        update.message.reply_text(f"Yaxshi {msg}\nFamiliyangizni kiriting📝")

    elif log['state'] == 2:
        log['familiya'] = msg
        log['state'] = 3
        update.message.reply_text("Raqamingizni kiriting 📞", reply_markup=contact)

    elif log['state'] == 3:
        update.message.reply_text('Iltimos contact tugmasini bosing 👇')

    elif log["state"] == 4:
        log['state'] = 5
        log['lokatsiya'] = msg
        update.message.reply_text("Tabriklayman siz muvaffaqiyatli ro'yxatda o'tdingiz 😊")
        update.message.reply_text("Quyidagilardan birini tanlang", reply_markup=button("menu"))

    elif log['state'] == 6:
        log['state'] = 7
        update.message.reply_text("Bo'limni tanlang. ", reply_markup=button("menu_ctg"))

    elif log['state'] == 7:
        log['state'] = 8
        update.message.reply_text("Quyidagilardan birini tanlang. ", reply_markup=button(msg))


def contact_handler(update, context):
    msg = update.message.contact
    print(msg)

    if log['state'] == 3:
        log['raqam'] = msg.phone_number
        log['state'] = 4
        update.message.reply_text('Joylashuvni tanlang 📍', reply_markup=button(type="location"))
