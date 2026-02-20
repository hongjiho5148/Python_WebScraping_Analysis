def greet(name, msg="안녕하세요", end="님!"):
    print(f"{msg}, {name}{end}")

name1 = input()
greet(name1) 

name2 = input()
greet(name2, msg="Hello", end="!") 

name3 = input()
greet(name3, end="님! 좋은 하루 되세요!") 