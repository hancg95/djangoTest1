from django.shortcuts import render
from .models import Product
from .models import Customer

# Create your views here.

def index(request): #메인 페이지
	products = Product.objects #DB에 있는 상품목록 불러오기
	return render(request,'index.html',{'products' : products})

def item(request,word): #상품 정보 페이지 , word를 통해 사용자가 무슨 상품을 선택했나 확인
	products = Product.objects #DB에 있는 상품목록 불러오기
	pick = Product.objects.get(title=word) #사용자가 선택한 상품 정보 불러오기
	return render(request,'item.html',{'products' : products,'pick' : pick})

def buy(request,word): #구매 페이지, word를 통해 사용자가 무슨 상품을 선택했나 확인
	among = request.GET['among'] #구매자가 선택한 수량 확인
	pick = Product.objects.get(title=word) #사용자가 선택한 상품 정보 불러오기
	result = int(pick.price) * int(among) #상품 금액과 수량을 곱한 합계 저장
	return render(request,'buy.html',{'among' : among,'pick' : pick, 'result' : result})

def success(request):
	product = request.GET['product'] #구매 상품 이름
	among = int(request.GET['among'].rstrip('/')) # 수량
	f_name = request.GET['f_name'] #구매자 First Name
	l_name = request.GET['l_name'] #구매자 Last Name
	email = request.GET['email'] #구매자 Email
	phone = request.GET['phone'] #구매자 Phone
	address = request.GET['address'] #구매자 주소 
	comment = request.GET['comment'] #구매자의 기타 의견사항
	#DB에 주문 추가하는 내용--
	Customer(product=product, among=among, f_name=f_name, l_name=l_name, email=email, phone=phone, address=address, comment=comment).save()
	#-----------------------
	return render(request,'buy_success.html',{'f_name' : f_name,'l_name' : l_name})