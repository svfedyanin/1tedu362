import csv
import datetime

from faker import Faker
import dateutil
from faker import Faker
from faker import Faker
import random
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DateType
from pyspark.sql import functions as F

products = ["Твикс","Марс","Сникерс","Баунти","Плитки шоколадные","Конфеты шоколадные","Карамели"
,"Карамельные леденцы","Мармелад","Вафли","Пряники","Пряники к чаю","Печенье 'Эсмеральда'"
,"Печенье ювелирное","Печенье овсяное","Печенье утреннее","Печенье 'Юбилейное'","Кексы"
,"Мини рулеты","Рулеты","Коржи бисквитные","Сухари 'Киевские'","Сушки","Пюре карт. мягк. уп. (120 гр.)"
,"Орбит","Дирол","Холлс","Масло сливочное","Сыр голландский","Сыр 'Гауда'","Сыр колбасный"
,"Сыр плавленый","Сыр 'косички'","Сыр балкарский","Сыр копченый","Колбаса сыро-копченая"
,"Колбаса варено-копченая","Творог","Сметана","Молоко 'Кубанская буренка'","Молоко сухое"
,"Сливки сухие","Айран","Кефир","'Активия'","Йогурт","Творожок","Яйца","Перец черный","Соль 'Экстра' (200 гр.)"
,"Соль йодированая","Сахар (весов)","Сахар-рафинад","Лавровый лист","Кетчуп 'Чили'","Кетчуп 'Гурман'"
,"Кетчуп в мягк. упак.","Майонез 'Байсад' в ведр./150гр.","Майонез 'Кальве'","Майонез 'Байсад' в мяг. уп."
,"Паста томатн. 'Байсад' в банке (5 шт.)","Масло растительтное","Дрожжи","Ванилин","Лимон","Сухари панировочные"
,"Мясо","Рыба свежая","Филе","Печень трески","Куриные бедра","Мясо 300 руб. – 1 кг.","Чай 'Ахмад' разовый (чёрный, зелёный)"
,"Чай 'Гринфилд' разовый (чёрный, зелёный)","Чай 'Липтон' (чёрный)","Чай 'Акбар' (чёрный)","Чай растворимый фруктовый"
,"Каркаде","'Гринфилд' листовой (чёрный, зелёный)","Кофе растворимый (баночн.)","Кофе нерастворимый для турки"
,"Какао 'Золотой ярлык'","Какао 'З в 1'","Кофе разовый","Мак кофе","Кисель растворимый","Кисель в брикетах"
,"Горячий шоколад","Молоко сгущённое","Какао сгущённое","Сгущёнка вареная","Мороженое","Джем в ведёрках"
,"Варенье в мягкой упаковке","Рис","Гречка","Манка","Пшенка","Геркулес","Овсяные хлопья 'Солнышко'","Мюсли"
,"Каша 'Быстров'","Каша 'Минутка'","Сливочный вкус","Горох","Перловка","Макароны 'Макфа'","Макароны 'Байсад'"
,"Спагетти","Лапша яичная","Суп дня (разн.)","Борщи","Доширак","Биг-Ланч","Биг-Бон","Роллтон вермишель (бич. пакеты)"
,"Магги 'Горячая кружка'","Чернослив (фасов.)","Курага (фасов.)","Изюм (фасов.)","Финики (фасов.)","Райские яблочки (фасов.)"
,"Сушеные бананы (фасов.)","Смесь сухофруктов","Орехов. смесь","Козинаки (семечки, арахис)","Халва (фасов.)"
,"Семечки","Оливки","Маслины","Грибы маринов.","Кукуруза маринов.","Фасоль маринов.","Помидоры","Огурцы (1 л, 3 л)"
,"Икра кабачков./баклажан.","Ананасы консерв.","Абрикосы консерв.","Клубника консерв.","Зеленый горошек"
,"'Горбуша' натур.","'Горбуша' в томат. соусе","Сайра натур.","Сайра в томат. соусе","Скумбрия натур."
,"Скумбрия в томат. соусе","Тушенка 'Калининградская'","Минтай натур.","Минтай в томат. соусе"
,"Килька в томат. соусе","Карась в т/с","Сардина т/с (натур.)","Сардинелла т/с (натур.)","Ставрида"
,"Сельдь в масле","Шпроты","Паштет","Икра (красная, чёрная)","Чипсы","Кальмары","'Янтарная рыбка'"
,"“Желтый полосатик'","Анчоусы","Вобла","Кукурузные палочки","Фисташки (солен.)","Арахис (слад./солен.)"
,"Уксус","Груша 1,5 литр","Груша стекло","Соки натуральные","Кола","Спрайт","Фанта","Чай холодный"
,"Минеральная вода","Водка","Пиво 0.5 л, 1.5 л, 2.5 л","Пиво 'Терек' стекл.","Коньяк Прасковейский"
,"Вино красное","Вино белое","Шампанское","Сигареты разные","Огурцы","Помидоры","Апельсины","Яблоки"
,"Мандарины","Бананы","Бытовые предметы","Бумага туалетная","Свечки","Перчатки рабочие","Карты игральные"
,"Спички","Батарейки	Салфетки влажные","Платочки бумажные","Ватные палочки","Ватные диски","Мыло хоз. Шампунь"
,"Порошок","Зажигалки"]


fake = Faker("ru_Ru")
# print("-------")
# print(datetime.date(datetime.date.today().year,1,1))
# print("-------")
# print(datetime.date.today())
# print("-------")
#
# for _ in range(5):
#     print(fake.date_between_dates(datetime.date
#     (datetime.date.today().year,1,1), datetime.
#     date.today()))

#функция для генерации списка формата [название продукта, цена]
#она необходима для того, чтобы цена на все одинаковые товары была одинаковая.
#если это не сделать, то мы при генерации можем получить ситуацию, когда
#для одноименных товаров с одинаковым количеством цена будет разной (а это не верно)

def productsPrice (products, minPrice, maxPrice):
    productsPriceList=[]
    for product in products:
        productsPriceList.append([product,random.randint(minPrice,maxPrice)])
    return productsPriceList

def getDatas(countLine, minCountProducts, maxCountProducts, products):
    tempData = []
    spark = SparkSession.builder.appName("shop").getOrCreate()
    shemaShop = StructType([
        StructField("orderDate", DateType(), True),
        StructField("userId", IntegerType(), True),
        StructField("product", StringType(), True),
        StructField("count", IntegerType(), True),
        StructField("price", StringType(), True)
    ])
    for _ in range (countLine+1):
        productsId = random.randint(0, len(products)-1)
        countProducts = random.randint(minCountProducts, maxCountProducts)
        tempData.append([fake.date_between_dates(datetime.date(datetime.date.today().year,1,1), datetime.date.today()),  #генерация даты в пределах - началогода - текущая дата
                         random.randint(0, countLine), #генерация UserID
                         products[productsId][0], #получение название товара по ранее сгенерированному ID
                         countProducts,
                         countProducts*products[productsId][1]
                         ])


    df = spark.createDataFrame(tempData,shemaShop)
    # df.write.format("csv").option("header", "true").save("datas.csv")
    with open("datas.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(["orderDate", "userId", "product", "count", "price"])
        writer.writerows(tempData)
    # df.show()
    spark.stop()



if __name__ == "__main__":
    while True:
        count = int(input("Введите количество записей(более 1000): "))
        if count < 1000:
            count = int(input("Введите количество записей(более 1000): "))
        break
    minPrice = int(input("Введите минимальную цену: "))
    maxPrice = int(input("Введите максимальную цену: "))
    minCountProducts = int(input("Введите минимальное количество товаров: "))
    maxCountProducts = int(input("Введите максимальное количество товаров: "))

    getDatas(count, minCountProducts, maxCountProducts, productsPrice(products, minPrice, maxPrice))