from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse,reverse_lazy
import joblib
# Create your views here.

def model(request):
    
        test = joblib.load('stroke_model4.pkl')
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
        hyper = int(request.POST["Hypertension"])
        if hyper == 1:
            lst.append(1)
        else:
            lst.append(0)

        # Adding heart disease

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

        ans = test.predict([lst])

        if ans == 1:
            res = "You may suffer with Stroke. Please consult with your Doctor to Avoid severe situation."
        else:
            res = "Your provided data have not shown any sign of Stroke.  "

        return res





# def PredictionView(request):
#     if request.method == 'POST':
#         res = model(request)
#     print(res)


#     return redirect('index')


def index(request):
    if request.method == 'POST':
        gender = int(request.POST['Gender'])
        age = int(request.POST['Age'])
        hyper = int(request.POST["Hypertension"])
        heart = int(request.POST['HeartDisease'])
        mar_status = int(request.POST["MarageStatus"])
        work = int(request.POST['JobStatus'])
        res_status = int(request.POST['ResidentStatus'])
        sugar = request.POST['Glucose']
        bmi = request.POST['BMI']
        smoke = int(request.POST['smokeStatus'])
        res = model(request)

        if hyper==1:
            hyper = "Yes"
        else:
            hyper = "No"



        if heart==1:
            heart = "Yes"
        else:
            heart = "No"

        if mar_status == 1:
            mar_status = "Married"
        else:
            mar_status = "Unmarried"

        
        if res_status == 1:
            res_status = "Urban"
        else:
            res_status = "Rural"


        if work == 1:
            work = "Government Job"
        elif work == 2:
            work = "Never worked"
        elif work == 3:
            work = "Private Job"
        elif work == 4:
            work = "Self Employed"
        else:
            work = "Child (Not at work)"


        if gender == 1:
            gender = "Male"
        elif gender == 2:
            gender = "Female"
        else:
            gender = "Other"


        if smoke == '1' :
            smoke = "Formerly Smoke"
        elif smoke == '2' :
            smoke = "Never Smoked"
        elif smoke == '3' :
            smoke = "Smoke"
        else:
            smoke = "None"

        context = {"result": res,
            "age":age,
            "hypertension":hyper,
            "heart":heart,
            "marrage":mar_status,
            "residence":res_status,
            "sugar":sugar,
            "bmi":bmi,
            "work":work,
            "gender":gender,
            "smoke":smoke

        }
        return render(request, 'index.html',context)


    return render(request, 'index.html')



def about(request):
    return render(request, 'about.html')




def resources(request):
    return render(request, 'resources.html')