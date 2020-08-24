from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 설치 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 사용합니다. 'dbsparta' db가 없다면 새로 만듭니다.

all_items = list(db.project.find({}))
print(all_items[0])

#ID 값 0부터 부여하는 코드
for index, item in enumerate(all_items):
    print(index, item)
    db.project.update_one({'ID': item['ID']}, {'$set': {'ID': str(index)}})