from os import sep
from mongoengine import Document, StringField

class Todos(Document):
    title = StringField(required=True, max_length=70)
    author = StringField(required=True, max_length=20)

def baglan():
    from mongoengine import connect
    global client
    client = connect(db="test", host="localhost", port=27017)
    print(client)
    print("*"*20)

def ekle():
    t1 = Todos(
        title="Beautiful Soup: Build a Web Scraper With Python",
        author="Martin"
        )

    t1.save() 
    print("Kayıt Eklendi.")
    print("*"*20)

def listele():
    for doc in Todos.objects:
        print("Title : ",doc.title,end="   *X*   ")
        print("Author : ",doc.author,end="\n")

baglan()
# ekle()
listele()


