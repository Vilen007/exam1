from django.shortcuts import render,  HttpResponse,redirect
from .models import User_Role,User_Table,Users_Rights,User_assign_role
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    role_name = ""
    role_detail = ""
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        uname = request.POST['uname']
        phone = request.POST['phone']
        date = request.POST['date']
        address = request.POST['address']
        password = request.POST['password']
        guest = request.POST.get('guest','off')
        userr = request.POST.get('user','off')
        adminn = request.POST.get('admin','off')
        if guest == "on":
            right_name = "No Rights"
            right_detail = "A guest user can only login into the system"
            role_name = "guest"
            role_detail = "A guest user can only login into the system"
        elif userr == "on":
            role_name = "user"
            role_detail = "A user is a kind of user who can be assigned different rights by admin"
        elif adminn == "on":
            role_name = "admin"
            role_detail = "Admin user have all rights"
        user_table = User_Table(uname=uname, fname=fname, lname=lname, phone=phone, address=address,created=date, password=password)
        user_table.save()
        user_role = User_Role(rname=role_name,rdetail=role_detail)
        user_role.save()
        user_assign = User_assign_role(ftname=fname, ltname=lname,uname=uname, role_name=role_name)
        user_assign.save()

        if role_name == "user":
            myuser = User.objects.create_user(uname, password)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            return redirect("/")
        elif role_name == "admin":
            myuser = User.objects.create_superuser(uname, password)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            return redirect("/")
        elif role_name == "guest":
            myuser = User.objects.create_user(uname, password)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            return redirect("/")

    return render(request, "users/home.html")

def home1(request):
    right_name = ""
    right_detail = ""
    if request.method == "POST":
        rid = request.POST['rid']
        uname = request.POST['uname']
        r1 = request.POST.get('r1', 'off')
        r2 = request.POST.get('r2', 'off')
        r3 = request.POST.get('r3', 'off')
        r4 = request.POST.get('r4', 'off')
        r5 = request.POST.get('r5', 'off')
        r6 = request.POST.get('r6', 'off')
        r7 = request.POST.get('r7', 'off')
        if r1 == "on":
            right_name += "Install/Uninstall, "
            right_detail += "User can install any application ,"
        if r2 == "on":
            right_name += "Insert/update, "
            right_detail += "User can uninstall any application, "
        if r3 == "on":
            right_name += "Delete, "
            right_detail += "User can delete any file or folder, "
        if r4 == "on":
            right_name += "Disable Internet, "
            right_detail += "User cannot use internet, "
        if r5 == "on":
            right_name += "Disable USB, "
            right_detail += "User cannot use USB stick, "
        if r6 == "on":
            right_name += "User Internet, "
            right_detail += "User can use internet, "
        if r7 == "on":
            right_name += "View, "
            right_detail += "User can use some specific file or folder, "
        if rid == "1":
            right_name = "No Rights"
            right_detail = "A guest user can only login into the system"
        if rid == "3":
            right_name = "All rights"
            right_detail = "Admin have all rights, admin can do anything"
        user_right = Users_Rights(role_id=rid,uname=uname, right_name=right_name, right_detail=right_detail)
        user_right.save()

        return redirect("/")

def users(request):
    us = User_Table.objects.all()
    return render(request,"users/users.html", {'us' : us})

def details(request):
    if request.method == 'POST':
        user = request.POST['user']
        data = User_assign_role.objects.filter(uname=user)
        rdata = Users_Rights.objects.filter(uname=user)


    return render(request, "users/details.html", {'data':data, 'rdata':rdata})