
# for i in range(3) :
#     print(i)

# fagorite_number = [ 10 ,4 ,24 ] #array
# # for i in fagorite_number:
# #     print(i)

# print (fagorite_number[2])

# fagorite_Food = [ "banana" , " apple" ]
# # for i in fagorite_Food:
# #     print(i)
# print(fagorite_Food[1])

users = [
    {
        "id": 1 ,
        "name": "sau banh" ,
        "age" : 23,
        "specialize" : "Web" ,
        "experience" : 3
    },
    {
        "id": 2 ,
        "name": "tuan anh" ,
        "age" : 22,
        "specialize" : "App",
        "experience" : 2
    },
    {
        "id": 3 ,
        "name": "Tai le" ,
        "age" : 23,
        "specialize" : "App",
        "experience" : 7
    },
    {
        "id": 4 ,
        "name": "Ai nhu" ,
        "age" : 20,
        "specialize" : "Bao",
        "experience" : 4
    },{
        "id": 5 ,
        "name": "Cuong" ,
        "age" : 22,
        "specialize" : "Web",
        "experience" : 2
    },
    {
        "id": 6 ,
        "name": "Cong" ,
        "age" : 22,
        "specialize" : "API",
        "experience" : 2
    }
]
# print(users[4]["name"])
# print(user["name"])
# for user in users:
#     if user ["id"] %2 == 1:
#         print(user)
# for user in users:
#     if user ["age"] >22:
#         print(user)

for user in users:
    if user["experience"] >2 :
        print(user["name"],user["age"])




