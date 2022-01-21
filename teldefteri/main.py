from turtle import clear
from baglanti import baglan
from pymongo import MongoClient
import pprint
import os

os.system('cls')

pp = pprint.PrettyPrinter(indent=4)

myclients =MongoClient(baglan)
mydb=myclients["defter"]
mycollection=mydb["kisiler"]

# print(myclients)
# print(mydb)
# print(mycollection)

def ekle():
    global produceList
    produceList=[
        {"ad":"ahmet","mobil":5555555555},
        {"ad":"mehmet","mobil":5555555555},
        {"ad":"veli","mobil":5555555555},
        {"ad":"hasan","mobil":5555555555},
        {"ad":"hüseyin","mobil":5555555555}
    ]
    result=mycollection.insert_many(produceList)

def listele():
    for i in mycollection.find():
        print(i)

def guncelle():
    mycollection.update_many( # update_one tekli günceller.
        {"ad":"hüseyin"},
        {"$set":{
            "mobil":5555555555
        }}
    )

def sil():
    mycollection.delete_one({"ad":"mehmet"})

def bul():
    result=mycollection.find({
        "ad":{
            "$in":["ahmet"]#içinde sanmsung s6 ve s7 bulunduran verileri seçer
        }
    })
    pp.pprint(result[0])

def sorgu():
    name=input("adınızı giriniz:")
    tel=int(input("Telefon(xxxxxxxxxx):"))
    if mycollection.count_documents({"ad":name,"mobil":tel}):
        print("Hoşgeldinz")
    else:
        print("Yanlış giriş")

