import csv
import getpass
from Project import Project
from Ressourcer import Ressourcer
from Aktiviteter import Aktiviteter
from Catalogue import Catalogue

catalogue=Catalogue()
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
            vis_menu_manager()
        elif (role == "Employee"):
            vis_menu_employee()
        else:
            break

def create_project():
    name = input("Enter name")
    id= input("Enter Id")
    beskrivelse = input("Enter beskrivelse")
    statdato = input("Enter Startdato")
    slutdato = input("Enter Slutdato")
    status = input("Enter Status")
    projekt = Project(name, id, beskrivelse, statdato, slutdato, status,)
    Catalogue.projectlist.append(projekt)

def Allocate_resources():
    id = input("Enter the id of the ressources")
    foundressources= search_ressources_by_id(id)
    pid=input("Please enter the project id")
    foundproject = Search_project_by_id(pid)
    foundproject.ressourcerslist.append(foundressources)
def search_ressources_by_id(id):
    for r in Catalogue.ressourlist:
        if r.id == id:
            return r
def create_reosources():
    type = input("Enter Type")
    intern = input("Enter intern")
    ekstern = input("Enter ekstern")
    id = input("Enter resscources ID")
    ressourcer= Ressourcer(type,intern,ekstern, id)
    Catalogue.ressourlist.append(ressourcer)
def Display_resources():
    for r in Catalogue.ressourlist:
        print(r.type, r.ekstern, r.intern, r.id)

def Search_project_by_id(id):
    for pro in Catalogue.projectlist:
        if pro.pid== id:
            return pro
def Add_tasks_to_project():
    a_estimate = input("Enter the estimate")
    a_assign = input("Enter your name")
    a_status = "to do"
    a_id = input("Enter task id")
    aktiviteter1 = Aktiviteter(a_estimate, a_assign,a_status, a_id)
    projectid=input("please enter the project ID")
    foundproject=Search_project_by_id(projectid)
    foundproject.tasklist.append(aktiviteter1)
def Display_task_in_project():
    id = input("project id")
    found_project = Search_project_by_id(id)
    for t in found_project.tasklist:
        print(t.a_status, t.a_assing, t.a_estimate, t.a_id)
def Change_status_of_task():
    id = input("project id")
    found_project = Search_project_by_id(id)
    for t in found_project.tasklist:
        print(t.a_status, t.a_assing, t.a_estimate, t.a_id)
        taskid = input("Enter the task id")
        if taskid==t.a_id:
            if t.a_status=="to do":
                t.a_status="Doing"
            elif t.a_status=="Doing":
                t.a_status="Done"
            else:
                print("Error")
def Display_all_projects():
    print(Catalogue.projectlist)
    for p in Catalogue.projectlist:
        print(p.pid, p.pbeskrivelse, p.pstartdato, p.pslutdato, p.pstatus)

def vis_menu_manager():
    print("-----Manager menu-----")
    print(0,"Create Ressource")
    print(1,"Create project")
    print(2,"Allocate resources")
    print(3,"Display resources")
    print(4,"Add tasks to a project")
    print(5,"Display tasks in a project")
    print(6,"Display all projects")
    print(7,"Display Employee menu")
    print("-----otherwise exit-----")
    while True:
        option=input("Select an option 0,1,2,3,4, 5, 6 or 7 ")
        if(option=="0"):
            create_reosources()
        elif(option=="1"):
            create_project()
        elif(option=="2"):
            Allocate_resources()
        elif(option=="3"):
            Display_resources()
        elif(option=="4"):
            Add_tasks_to_project()
        elif(option=="5"):
            Display_task_in_project()
        elif(option=="6"):
            Display_all_projects()
        elif(option=="7"):
            print_menu()
        else:
            exit()


def vis_menu_employee():
    print("-----Employee menu-----")
    print(0,"Display all projects")
    print(1,"Display tasks in a project")
    print(2,"Select a task and change status of task")
    print("------------")
    while True:
        option=input("Please choose option 0, 1 or 2")
        if (option=="0"):
            Display_all_projects()
        if (option=="1"):
            Display_task_in_project()
        elif(option=="2"):
            Change_status_of_task()
        else:
            exit()

def print_menu():
    print("--------------------------------")
    print(1, "Create an account")
    print(2, " Login to the system")
    print("--------------------------------")
    while True:
        option=input("Please choose options 1 for new user and 2 for registered users>>")
        if(option=="1"):
            create_account()
        elif(option=="2"):
            status=login()
            if status==True:
                vis_menu_employee()
            else:
                vis_menu_manager()
        else:
            exit()

print_menu()