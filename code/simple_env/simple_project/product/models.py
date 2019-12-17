from django.db import models

# Create your models here.
class Product(models.Model): #상품들
	num = models.AutoField(primary_key=True)
	title = models.CharField(max_length=255) #제목
	body = models.TextField() #설명
	price = models.IntegerField() #가격
	image1 = models.ImageField(upload_to = 'images/') #이미지
	image2 = models.ImageField(upload_to = 'images/')
	

	def __str__(self): #어드민 사이트의 오브젝트 목록을 타이틀 명으로 변경해줌
		return self.title

	def gett(self, arg):
		val = Product.objects.filter(title__contains=arg)
		return val
