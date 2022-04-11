from django.db import models

# Create your models here.
class Image(models.Model):
    image=models.ImageField(upload_to="img/%y")

# class superuser(models.Model):
#     username=models.CharField(max_length=20)
#     password=models.CharField(max_length=20)

#     def __str__(self):
#         return self.username

class services(models.Model):
    
    caption=models.CharField(max_length=20)
    details=models.TextField(max_length=300, default='some_value')
    picture=models.ImageField(upload_to="img/%y", default='default.jpg')
    
    
    
    def __str__(self):
        return self.caption 
        
class faq(models.Model):
    question=models.CharField(max_length=300)
    answer=models.TextField(max_length=2000)
    
class clien(models.Model):
    client_id = models.IntegerField(default=0)
    client_name = models.CharField(max_length=50,null=False,blank=False)
    client_address = models.CharField(max_length=50,null=False,blank=False)
    # GChoises= (
    #     ('M', 'Male'),
    #     ('F', 'Female'),
    #     ('O', 'Other')
    # )
    # client_gender= models.CharField(max_length=1,null=True, choices=GChoises) 
    client_phone=models.IntegerField(null=False,default=0000)
    
    def __str__(self):
        return self.client_name

class order(models.Model):
    order_no=models.CharField(max_length=20, null=False,blank=False)
    date=models.DateField(auto_now_add=False,auto_now=False, blank=False)
    deadline=models.DateField(auto_now_add=False,auto_now=False, blank=False)
    client_id=models.ForeignKey(clien,default=0,on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.order_no
    

class distribution(models.Model):
    address = models.CharField( max_length=50, null=False, blank=False)
    transportation = models.CharField( max_length=50, null=False, blank=False)
    distribution_id = models.CharField( max_length=20,null=False, default=0)
    client_id=models.CharField(max_length=50,null=False,blank=False)
    


    def __str__(self):
        return self.distribution_id

class paper(models.Model):
    size =  models.CharField( max_length=20, null=False, blank=False)
    thickness =  models.CharField( max_length=50, null=False, blank=False)
    purchase_date = models.DateField(auto_now_add=False,auto_now=False, blank=False)
    quantity = models.CharField( max_length=20, null=False, blank=False)

    def __str__(self):
        return self.size
class ink(models.Model):
    colour= models.CharField( max_length=20, null=False, blank=False)
    brand_name=models.CharField( max_length=20, null=False, blank=False)
    purchase_date=models.DateField(auto_now_add=False,auto_now=False, blank=False)
    quantity=models.CharField( max_length=20, null=False, blank=False)
