from django.shortcuts import render,redirect

import joblib
# Create your views here.

def index(request):
    if request.method == 'POST':
        lst = []
        # Adding Gender to list
        gender = int(request.POST['Gender'])
        if gender == 1:
            lst.append(1)
            lst.append(0)
            lst.append(0)
        elif gender == 2:
            lst.append(0)
            lst.append(1)
            lst.append(0)
        else:
            lst.append(0)
            lst.append(0)
            lst.append(1)

        # Adding age to list

        age = int(request.POST['Age'])
        lst.append(age)

        # Adding hypertension to list

        heart = int(request.POST['HeartDisease'])
        if heart == 1:
            lst.append(1)
        else:
            lst.append(0)

        # Adding marrage status

        mar_status = int(request.POST["MarageStatus"])
        if mar_status == 1:
            lst.append(1)
        else:
            lst.append(0)

        # Adding working status

        work = int(request.POST['JobStatus'])
        if work == 1:
            lst.append(1)
            lst.append(0)
            lst.append(0)
            lst.append(0)
            lst.append(0)
        elif work == 2:
            lst.append(0)
            lst.append(1)
            lst.append(0)
            lst.append(0)
            lst.append(0)
        elif work == 3:
            lst.append(0)
            lst.append(0)
            lst.append(1)
            lst.append(0)
            lst.append(0)
        elif work == 4:
            lst.append(0)
            lst.append(0)
            lst.append(0)
            lst.append(1)
            lst.append(0)
        else:
            lst.append(0)
            lst.append(0)
            lst.append(0)
            lst.append(0)
            lst.append(1)

        # Adding Resident status

        res_status = int(request.POST['ResidentStatus'])
        if res_status == 1:
            lst.append(1)
            lst.append(0)
        else:
            lst.append(0)
            lst.append(1)

        # Adding glucose levels
        sugar = request.POST['Glucose']
        lst.append(float(sugar))

        # Adding BMI 
        bmi = request.POST['BMI']
        lst.append(float(bmi))

        # Adding smoke status
        smoke = int(request.POST['smokeStatus'])
        if smoke == 1:
            lst.append(1) 
            lst.append(0) 
            lst.append(0) 
        elif smoke == 2 :
            lst.append(0) 
            lst.append(1) 
            lst.append(0)
        else: 
            lst.append(0) 
            lst.append(0) 
            lst.append(1)

        print(lst)
        return redirect('index.html')

    return render(request, 'index.html')



def about(request):
    return render(request, 'about.html')




def resources(request):
    return render(request, 'resources.html')