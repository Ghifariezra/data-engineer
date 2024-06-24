import pymongo
from datetime import date, datetime
import math
import random
from bson.objectid import ObjectId

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["dskola"]
mycol = mydb["books"]

for i in range(0, 100) :

    my_dict = {
        "title": "Book Title " + str(i),
        "author": "Author " + str((i % 10 + 1)), # 10 different authors
        "genre": random.choice(["Fiction", "Dystopian", "Adventure", "Science Fiction", "Fantasy"]), # 5 different genres
        "published_year": 1950 + (i % 70), # Published between 1950 and 2019
        "copies_available": math.floor(random.randint(1, 9) * 10) + 1, # 1 to 10 copies available
        "borrowed_by": [
            {
                "user_id": ObjectId(),
                "borrowed_date": datetime(2024, random.randint(1, 12), random.randint(1, 30)), # Borrowed dates spread over the year 2024
                "return_date": None
            }
        ]
    }
    mycol.insert_one(my_dict)
