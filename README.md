1. có mấy loại biến :
có 5 loại :
- String
- Number
- Boolean:True/False
- Array:[String]/[Number]/[String,Number]
- Object:{"key": valua("String",number)}


```python
# hiện kiểu dữ liệu trong mảng
user = { 
    "name": "sau banh",
    "age": 22 
}#object
print ("age")
print(type("age"))

```

```python
books = [
    {
        "id": 1,
        "name": "Tiengviet",
        "author": "Taile",
    },
    {
        "id": 2,
        "name": "English",
        "author": "saubanh",
    },
    {
        "id": 3,
        "name": "History",
        "author": "Cong",
    },
    {
        "id": 4,
        "name": "Math",
        "author": "Cuong",
    },
]

print(books[2])

```

2. Vòng lập For
```python
books = [
    {
        "id": 1,
        "name": "Tiengviet",
        "author": "Taile",
    },
    {
        "id": 2,
        "name": "English",
        "author": "saubanh",
    },
    {
        "id": 3,
        "name": "History",
        "author": "Cong",
    },
    {
        "id": 4,
        "name": "Math",
        "author": "Cuong",
    },
]
# hiện tên của tất cả cuốn sách có trong books
for book in books:
    print(book["name"])

# hiện thông tin của tất cả sách có id là số chẵn
for book in books:
    if book["id"] % 2 == 0:
        print(book)

# hiện name của tất cả sách có id là số chẵn
for book in books:
    if book["id"] % 2 == 0:
        print(book["name"])



```