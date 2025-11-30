# print("Hellow World!") if 5<3 else print("Hello Earth")


# user_decision = 1
# while user_decision == 1:
#     Name = input("Enter your name : ")
#     age = int(input("Enter your age : "))
#     if age>=18:
#         print("You can drive Mr.",Name)
#     else:
#         print("You have to wait",18-age,"years to drive Mr.",Name)
#     user_decision = int(input("Enter 1 for continue another and 0 for quit"))

fruits = ['banana','Mango','Watermelon','Grapes','Pineapple','Apple']
choice = input("Enter your favorite fruit name : ")
if choice in fruits:
    print("your fruit is available in our list")
    for choices in fruits:
        if choices == choice:
            print("your favorite fruit position is index : ", fruits.index(choices))
else:
    fruits.append(choice)
    print("it wasn't available in our list. we just add it")
    print("your favorite fruit position is index : ", fruits.index(choice))
