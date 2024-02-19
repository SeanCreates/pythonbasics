my_list = ["Toyota", "Mercedes", "BMW", "G-wagon"]
my_list.append("Mazda")
print(my_list)
print(my_list[0])
print(my_list[-1])
print(my_list[1])
print(my_list[2])
print(my_list[3])
print(f"{my_list[1]} is manufactured in Germany.")
print(my_list[1],"is manufactured in Germany." )
my_list[1] = "Bentley" #mutable
print(f"{my_list[1]} was very expensive in The Tokyo drift.")
print(type(my_list))

thislist = ["Paris", "Santorini", "Milan", "Bali"]
thislist.insert(0, "Together")
print(thislist)

# tuple datastructure
my_tuple = ("Nana", "Kindness", "Kisha", "Melissa", "Ijeleha", "Pearl", "Neema")
print(my_tuple)
print(my_tuple[2:4])
print(my_tuple[2:])

if "Neema" in my_tuple:
    print("Yes! 'Neema' is in my_tuple")

# my_tuple(1) = "Melissa" immutable

# babe you cannot reassign a value in a tuple

# set  datasructures #noindexes;unordered
my_set = {"Tomiwa", "Nicole", "Breanna", "Liane"}
print(my_set)

# dictionary datastructures #mutable
my_dict = {"name": "Neema", "Age":18, "Gender": "Female"}
print(my_dict)
print(my_dict["Age"])


