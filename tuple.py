# Tuples

example_Tuples = (2,3,4,5,6,0,6)

print(example_Tuples)

# accessing tuple using positive indexing

print(example_Tuples[3])

# accessing tuple using positive indexing

print(example_Tuples[-4])

# accessing tuple using ranges

tuple_string = ("latifa","nancy","dorcas","esther","fanny")

print(tuple_string[2:4])

print(tuple_string[1:])

print(tuple_string[:3])

print(tuple_string[-4:-2])

# checking if the variable exists in a tuple using in Keyword

if "nancy" in tuple_string:
    print("nancy is in class")

# workarounds on tuples to change
    
    list_tuple = ("orange","mango","book",2,3,5,True)

    type( list_tuple)

    new_list = list( list_tuple)

    type(new_list)

    new_list.append("latifa")

    new_list.extend(["nancy","kiwi","pen"])

    print(new_list)

# removing an element in a tuple we use the workaround way 

    new_list.remove("pen")

    print(type(new_list))

    print(new_list)

    list_tuple = tuple(new_list)

    print(type( list_tuple))

    print( list_tuple)

    # how to delete the tuple

    tuple_remove = ("latifa",False,2,1.0)

    del tuple_remove

# when we try to acces tuple_remove, it will throw an error because it no longer exist

    # print(tuple_remove) 

# adding tuple to another tuple
    
    new_tuple = (3,)

    list_tuple += new_tuple

    print( list_tuple) 

# printing one element in a tuple by unpacking a tuple
    
   
(a,b,c,d,e) = tuple_string

print(a)
print(b)
print(c)
print(d)
print(e)


