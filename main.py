from student import Student 
# import test 


def main():
    print("main function of main.py is called ")
    print("name of the script:", __name__)
    #print(" this is the main funcgion where i will implement the logic of the program")

    students=[]
    students.append(Student("jamal", 1001 ))
    students.append(Student("kamal", 1002 ))

    for s in students:
        print(s)
        


if __name__ == "__main__" :
    main()

