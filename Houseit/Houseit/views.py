from django.shortcuts import render, redirect
from django.http import HttpResponse
from H1.models import seller,buyer,flat

def home(request):
        return render(request, 'home.html')
def search(request):

        allflat=flat.objects.all()
        context={"allflat":allflat}
        print(allflat)

        return render(request, 'search.html',context)
def giveadd(request):
        if request.method == 'POST':

                 data = flat(f_id=request.POST['fid'],division=request.POST['division'],city=request.POST['city'],area=request.POST['area'],price_range=request.POST['price'],f_email=request.POST['smail'])
                 data.save()
                 return render(request, 'home.html')

        context = {}
        print("7")
        return render(request, 'Give add.html', context)




def signin(request):
        return render(request, 'Sign_in.html')
def signup(request):
        return render(request, 'sign_up.html')
def about(request):
        return render(request, 'about_us.html')
def contact(request):
        return render(request, 'Contact_us.html')
def Bsu(request):

        if request.method == 'POST':
                print("1")
                allbuyer=buyer.objects.all()
                print("2")
                for b in allbuyer:
                        print("3")
                        if request.POST['bemail']==b.b_email:
                                print("4")
                                pass

                else:
                        print("5")
                        if request.POST['bpass'] == request.POST['bpass2']:
                                print("6")
                                sellerdata = buyer(b_name=request.POST['bname'], b_contact=request.POST['bcontact'],
                                                   b_id=request.POST['bid'], b_address=request.POST['baddress'],
                                                   b_email=request.POST['bemail'], b_pass=request.POST['bpass'])
                                sellerdata.save()
                                return render(request, 'home.html')


        context = {}
        print("7")
        return render(request, 'BuyersSu.html',context)


def Ssu(request):
        if request.method == 'POST':
                allseller = seller.objects.all()
                print("2")
                for s in allseller:
                        print("3")
                        if request.POST['semail'] == s.s_email:
                                print("4")
                                pass

                else:
                        if request.POST['spass'] == request.POST['spass2']:
                                sellerdata = seller(s_name=request.POST['sname'], s_contact=request.POST['scontact'],
                                                    s_id=request.POST['sid'], s_address=request.POST['saddress'],
                                                    s_email=request.POST['semail'], s_pass=request.POST['spass'])
                                sellerdata.save()
                                return render(request, 'home.html')




        context = {}
        return render(request, 'SellerSu.html',context)



def bsi(request):
        allbuyer = buyer.objects.all()
        if request.method == 'POST':

                for b in allbuyer:
                        if request.POST['mail'] == b.b_email:
                                if request.POST['pass'] == b.b_pass:
                                        return render(request, 'home.html')

        context = {"allbuyer": allbuyer}

        return render(request, 'buyersSi.html', context)


def ssi(request):
        allseller = seller.objects.all()
        if request.method == 'POST':

                for s in allseller:
                        if request.POST['mail'] == s.s_email:
                                if request.POST['pass'] ==s.s_pass:

                                        return render(request, 'home.html')

        context = {"allseller": allseller}

        return render(request, 'sellerSi.html', context)




