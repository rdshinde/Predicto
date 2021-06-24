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

    print(lst)
    ans = test.predict([lst])
    #print(ans[0])
    
    if ans[0] == 1:
        return(1)
    else:
        return(0)
