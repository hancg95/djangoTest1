from django.shortcuts import render
from .models import Product
from datetime import datetime

# Create your views here.
# class Index(View):

#     def get(self, request, *args, **kwargs):
#         # request.session['step1_complete'] = False
#         # request.session['step2_complete'] = False
#         return render(request, 'index.html',{'products':product})

#     def post(self, request, *args, **kwargs):
#         # request.session['step1_complete'] = True
#         return redirect(reverse('index.html'),{'products':product})
#         # return redirect(reverse('step2'),{'products':product})

def index(request):
	products = Product.objects
	return render(request,'index.html',{'products' : products})

def item(request,word):
	products = Product.objects
	pick = Product.objects.get(title=word)
	return render(request,'item.html',{'products' : products,'pick' : pick})

def buy(request,word):
	among = request.GET['among']
	pick = Product.objects.get(title=word)
	result = int(pick.price) * int(among)
	return render(request,'buy.html',{'among' : among,'pick' : pick, 'result' : result})

def success(request):
	product = request.GET['product']
	among = request.GET['among']
	f_name = request.GET['f_name']
	l_name = request.GET['l_name']
	email = request.GET['email']
	phone = request.GET['phone']
	address = request.GET['address']
	comment = request.GET['comment']
	now = datetime.now() # 현재시각 가져옴
	date = '%s-%s-%s' % ( now.year, now.month, now.day )
	#DB에 주문 추가하는 내용--
	#--------------nothing--
	return render(request,'buy_success.html',{'f_name' : f_name,'l_name' : l_name})