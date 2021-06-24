#from django.http import HttpResponse
from django.shortcuts import render
import joblib
from django.template import Context, Template

def model(request):
    test = joblib.load('stroke_model4.pkl')

    lst=[]
    gender = int(request.POST.get("Gender"))
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


    age = float(request.POST.get('Age'))
    lst.append(age)

    hyper = int(request.POST.get("Hypertension"))
    if hyper == 1:
        lst.append(1)
    else:
        lst.append(0)

    heart = int(request.POST.get("HeartDisease"))
    if heart == 1:
        lst.append(1)
    else:
        lst.append(0)

    mar_status = int(request.POST.get("MarageStatus"))
    if mar_status == 1:
        lst.append(1)
    else:
        lst.append(0)

    work = int(request.POST.get("JobStatus"))
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


    res_status = int(request.POST.get("ResidentStatus"))
    if res_status == 1:
        lst.append(1)
        lst.append(0)
    else:
        lst.append(0)
        lst.append(1)

    lst.append(float(request.POST.get("Glucose")))
    sugar = float(request.POST.get("Glucose"))


    lst.append(float(request.POST.get("BMI")))
    bmi = float(request.POST.get("BMI"))

    smoke = int(request.POST.get("smokeStatus"))
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

    # print(lst)
    ans = test.predict([lst])
    #print(ans[0])
    
    if ans[0] == 1:
        return(1)
    else:
        return(0)

#Rendering the form page

def form(request):
    
    return render(request,'form.html')


# Rendering the result page
def result(request):
    model_res = model(request)

    if model_res == 1:
        res = "You may suffer with Stroke. Please consult with your Doctor to Avoid severe situation."
    else:
        res = "Your provided data have not shown any sign of Stroke.  "
    


    age = float(request.POST.get('Age'))
    hyper = int(request.POST.get("Hypertension"))
    if hyper==1:
        hyper = "Yes"
    else:
        hyper = "No"

    heart = int(request.POST.get("HeartDisease"))
    if heart==1:
        heart = "Yes"
    else:
        heart = "No"

    mar_status = int(request.POST.get("MarageStatus"))
    if mar_status == 1:
        mar_status = "Married"
    else:
        mar_status = "Unmarried"

    res_status = int(request.POST.get("ResidentStatus"))
    if res_status == 1:
        res_status = "Urban"
    else:
        res_status = "Rural"

    sugar = float(request.POST.get("Glucose"))
    bmi = float(request.POST.get("BMI"))

    work = int(request.POST.get("JobStatus"))
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

    gender = int(request.POST.get("Gender"))
    if gender == 1:
        gender = "Male"
    elif gender == 2:
        gender = "Female"
    else:
        gender = "Other"
    

    smoke = request.POST.get("smokeStatus")
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

    return render(request,'result.html',context)


#rendering the result page
def index(request):
    
    return render(request,'index.html')


#rendering the resources page
def resources(request):


    


    return render(request,'resources.html')

#rendering the about page
def about(request):
    return render(request,'about.html')
