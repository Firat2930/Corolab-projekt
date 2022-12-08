import csv
import getpass
from Project import Project
from Ressourcer import Ressourcer

def print_menu():
    print("--------------------------------")
    print(1, "Create an account")
    print(2, " Login to the system")
    print("--------------------------------")
print_menu()

def create_account():
    un=input("Enter your username: ")
    psw = getpass.getpass("Enter Your Password: ")
    role = input("The role is: ")
    data=[[un,psw,role]]
    file= open("Credentials.csv", "a", newline="")
    csvwriter = csv.writer(file)  #  create a csvwriter object
    csvwriter.writerows(data)  #  write  the data

def login():
    un = input("Enter your username")
    psw = getpass.getpass("Enter Your Password : ")
    role = input("Enter your role Employee or Manager: ")
    fo = open("Credentials.csv", 'r')
    csvreader = csv.reader(fo)
    for row in csvreader:
        if row == [un, psw,role]:
            print("You are logged in")
            return True
        if (role == "Manager"):
            vis_menu_maneger()
        elif (role == "Employee"):
            vis_menu_employee()
        else:
            break

def create_project():
    name = input("Enter name")
    beskrivelse = input("Enter beskrivelse")
    statdato = input("Enter Startdato")
    slutdato = input("Enter Slutdato")
    status = input("Enter Status")
    projekt = Project(name, beskrivelse, statdato, slutdato, status)
def Allocate_resources():
    type = input("Enter Type")
    intern = input("Enter intern")
    ekstern = input("Enter ekstern")
    timer = input("Enter timer")
    resources= resources(type,intern,ekstern,timer)
def Display_resources():

def Add_tasks_to_project():

def Display_task_in_project():

def vis_menu_maneger():
    print("-----Manager menu-----")
    print(1,"Create project")
    print(2,"Allocate resources")
    print(3,"Display resources")
    print(4,"Add tasks to a project")
    print(5,"Display tasks in a project")
    print("-----otherwise exit-----")
    while True:
        if(option=="1"):
            create_project()
        elif(option=="2"):
            Allocate_resources()
            if status==True:
                vis_menu_employee()
            else:
                vis_menu_maneger()
            break


def vis_menu_employee():
    print("-----Employee menu-----")
    print(1,"Display tasks in a project")
    print(2,"Select a task")
    print("------------")

while True:
    option=input("Please choose options 1 for new user and 2 for registered users>>")
    if(option=="1"):
        create_account()
    elif(option=="2"):
        status=login()
        if status==True:
            vis_menu_employee()
        else:
            vis_menu_maneger()
            break
