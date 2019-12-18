from django.db import models

# Create your models here.
class Product(models.Model): #상품들
	num = models.AutoField(primary_key=True) #기본키
	title = models.CharField(max_length=255) #상품 이름
	body = models.TextField() #설명
	price = models.IntegerField() #가격
	image1 = models.ImageField(upload_to = 'images/') #미리보기 이미지
	image2 = models.ImageField(upload_to = 'images/') #상세 이미지
	

	def __str__(self): #어드민 사이트의 오브젝트 목록을 타이틀 명으로 변경해줌
		return self.title

class Customer(models.Model): #주문 목록
	num = models.AutoField(primary_key=True) #기본키
	product = models.CharField(max_length=255) #상품 이름
	among = models.IntegerField() # 수량
	f_name = models.CharField(max_length=255) #구매자 First Name
	l_name = models.CharField(max_length=255) #구매자 Last Name
	email = models.CharField(max_length=255) #구매자 Email
	phone = models.CharField(max_length=255) #구매자 Phone
	address = models.TextField() #구매자 주소 
	comment = models.TextField() #구매자의 기타 의견사항
	date = models.DateField(auto_now_add=True) # 현재 시각 가져옴

	def __str__(self): #어드민 사이트의 오브젝트 목록을 First Name으로 변경해줌
		return self.f_name