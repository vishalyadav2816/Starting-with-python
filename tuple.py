my_tuple=("apple","orange","pineapple")
print(my_tuple[0:2])
list1=list(my_tuple)
list1.append("vy")
my_tuple=tuple(list1)
print(my_tuple)

tuple1 = (1 , 2 , 3)
tuple2 = (4 , 5 , 6)

tuple1 +=tuple2
print(tuple1)