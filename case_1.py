class type_fruit:
    def __init__(self, fruitId, fruitName, fruitType, stock):
        self.fruitId = fruitId
        self.fruitName = fruitName
        self.fruitType = fruitType
        self.stock = stock

fruits = [
    type_fruit(1,'apel','IMPORT',10),
    type_fruit(2,'kurma','IMPORT',20),
    type_fruit(3,'Apel','IMPORT',50),
    type_fruit(4,'manggis','LOCAL',100),
    type_fruit(5,'jeruk bali','LOCAL',20),
    type_fruit(5,'kurma','IMPORT',20),
    type_fruit(5,'salak','LOCAL',150),
    type_fruit(5,'melon','CAMPURAN',150),
    type_fruit(5,'mangga','CAMPURAN',150),
    type_fruit(5,'stroberi','LUAR NEGRI',150),


    
]

def soal_1(input):
    tempchar = []
    for i in input:
        buah = i.fruitName
        if i.fruitName.lower() in tempchar:
            pass
        else:
            tempchar.append(i.fruitName.lower())
    return tempchar

def print_catagori(input):
    tempchar = []
    for i in input:
        tempchar.append(i.fruitType)
    tempchar = set(tempchar)
    return tempchar

def soal_2(input):
    cat = print_catagori(input)
    dic = {category: set([]) for category in cat}
    for i in input:
        dic[i.fruitType].add(i.fruitName.lower())
    return len(cat),dic

    

def soal_3(input):
    cat = print_catagori(input)
    dic = {category: 0 for category in cat}
    for i in input:
        if i.fruitType in cat:
            dic[i.fruitType]+=i.stock
    return dic



print("Soal no.1 = "+str(soal_1(fruits)))
soal2 = soal_2(fruits)
print("Soal no.2 = jumlah ember adalah",str((soal2[0])), "Buahnya adalah "+str(soal2[1]))
print("Soal no.3 = "+str(soal_3(fruits)))