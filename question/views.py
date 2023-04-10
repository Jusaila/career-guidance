from django.shortcuts import render
from career_guidence import settings
from pandas import read_excel
from sklearn.tree import DecisionTreeClassifier
# Create your views here.
def post(request):
    if request.method=='POST':
        a1 = request.POST.get('q1')
        a2 = request.POST.get('q2')
        a3 = request.POST.get('q3')
        a4 = request.POST.get('q4')
        a5 = request.POST.get('q5')
        a6 = request.POST.get('q6')
        a7 = request.POST.get('q7')
        a8 = request.POST.get('q8')
        a9 = request.POST.get('q9')
        a10 = request.POST.get('q10')
        a11 = request.POST.get('q11')
        a12 = request.POST.get('q12')
        a13 = request.POST.get('q13')
        a14 = request.POST.get('q14')
        a15 = request.POST.get('q15')
        a16 = request.POST.get('q16')
        a17 = request.POST.get('q17')
        a18 = request.POST.get('q18')
        a19 = request.POST.get('q19')
        a20 = request.POST.get('q20')
        a21 = request.POST.get('q21')
        a22 = request.POST.get('q22')
        a23 = request.POST.get('q23')
        a24 = request.POST.get('q24')
        a25 = request.POST.get('q25')
        a26 = request.POST.get('q26')
        a27 = request.POST.get('q27')
        a28 = request.POST.get('q28')
        a29 = request.POST.get('q29')
        a30 = request.POST.get('q30')
        a31 = request.POST.get('q31')
        a32 = request.POST.get('q32')
        a33 = request.POST.get('q33')
        a34 = request.POST.get('q34')
        a35 = request.POST.get('q35')
        a36 = request.POST.get('q36')
        a37 = request.POST.get('q37')
        a38 = request.POST.get('q38')
        a39 = request.POST.get('q39')
        a40 = request.POST.get('q40')
        a41 = request.POST.get('q41')

        imgpath = str(settings.BASE_DIR) + str(settings.STATIC_URL) + "train.xlsx"
        data = read_excel(imgpath, "Sheet1")
        X = data.iloc[:, 0:41].values
        y = data.iloc[:, 41].values
        dtc = DecisionTreeClassifier()
        dtc.fit(X, y)
        test = [int(a1),int(a2),int(a3),int(a4),int(a5),int(a6),int(a7),int(a8),int(a9),
                int(a10), int(a11), int(a12), int(a13), int(a14), int(a15),
                int(a16), int(a17), int(a18), int(a19), int(a20), int(a21),
                int(a22), int(a23), int(a24), int(a25), int(a26), int(a27),
                int(a28), int(a29), int(a30), int(a31), int(a32), int(a33),
                int(a34), int(a35), int(a36), int(a37), int(a38), int(a39),
                int(a40),int(a41),]
        y_pred = dtc.predict([test])

        print("hello")
        print(y_pred)
        # ress=""
        # try:
        #     if y_pred[0]==1:
        #         ress="detected"
        #     else:
        #         ress="not predicted "
        # except:
        #     ress="not"

        context={
            "res":y_pred[0],
        }
        return render(request,'question/result.html',context)

    return render(request,'question/Test_mcq.html')



def prediction(request):
    return render(request,'question/result.html')
