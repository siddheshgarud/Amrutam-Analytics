from django.db import models


# Create your models here.
'''class product(models.model):
  product_id= models.AutoField
  
  product_name = models.CharField(max_length=50)
  product_desc = models.CharField(max_length = 300)
  product_date = models.DataField()'''

""" Order- id, , number , order_key , created_via , currency , date_created , status , discount_total , discount_tax , shipping_tax , shipping_total , total , total_tax , customer_id , payment_method , payment_method_title , transaction_id , date_paid_gmt , line_items , 
line_items - order_id , customer_id , id , name , product_id , variation_id , quantity , tax_class , subtotal , subtotal_tax, total , total_tax, price , sku.
coupon_lines - order_id , customer_id , coupon_id1 , coupon_id2 , coupon_id3
refund - order_id , customer_id , id , refund , total.
products , product_variation , product_categories , product_reviews , product_attribut """

class Customers(models.Model):
  id  = models.AutoField(primary_key=True)
  username = models.CharField(max_length =100 , blank=True)
  first_Name = models.CharField(max_length = 50 ,blank=True)
  last_Name = models.CharField(max_length = 50 , blank=True)
  role = models.CharField(max_length = 50 , blank=True)
  email= models.CharField(max_length=100 , blank=True)
  phone = models.IntegerField(blank=True)
  address1 = models.CharField(max_length=200 , blank=True)
  address2 = models.CharField(max_length=200 , blank=True)
  pincode = models.IntegerField(blank=True)
  city = models.CharField(max_length=50 ,blank=True)
  state = models.CharField(max_length=50, blank=True)
  country = models.CharField(max_length=50, blank=True)
  is_paying_customer = models.BooleanField()
  avatar_url = models.URLField(max_length=300,blank=True )
  date_created_gmt = models.DateField()
  date_modified_gmt = models.DateField()
  def __str__(self):
      return self.Customers



class Line_items(models.Model):
  id = models.AutoField(primary_key=True)
  customer = models.ForeignKey(Customers , on_delete=models.DO_NOTHING  , blank = True  , null = True)
  order = models.ForeignKey('Orders' , on_delete=models.DO_NOTHING , blank = True  , null = True )
  product = models.ForeignKey('Products' , on_delete=models.DO_NOTHING )
  sku = models.CharField(max_length=50 , blank=True)
  name = models.CharField(max_length=100 , blank=True)
  variation_id = models.IntegerField(blank=True)
  quantity = models.IntegerField(blank=True)
  tax_class = models.CharField(max_length=50 , blank=True)
  subtotal = models.FloatField(blank=True)
  subtotal_tax = models.FloatField(blank=True)
  total = models.FloatField(blank=True)
  total_tax = models.FloatField(blank=True)
  price = models.FloatField(blank=True)






class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100 , blank=True)
    phone = models.IntegerField(blank=True)
    customer = models.IntegerField(blank=True)
    line_items_id = models.IntegerField(blank=True)
    number = models.IntegerField(blank=True)
    status = models.CharField(max_length = 30 ,blank=True)
    order_key = models.CharField(max_length=200 , blank=True)
    created_via  = models.CharField(max_length=50 , blank=True)
    currency = models.CharField(max_length=50 , blank=True)
    payment_method =  models.CharField(max_length = 50 ,blank=True)
    payment_method_title =  models.CharField(max_length = 70 ,blank=True)
    transaction_id =  models.CharField(max_length = 50 ,blank=True)
    date_paid_gmt = models.DateField(blank=True)
    discount_total = models.FloatField(blank=True)
    discount_tax = models.FloatField(blank=True)
    shipping_tax = models.FloatField(blank=True)
    shipping_total = models.FloatField(blank=True)
    total_tax = models.FloatField(blank=True)
    total = models.FloatField(blank=True)

    date_created = models.DateField(blank=True)
    date_modified_gmt = models.DateField(blank=True)
    
    def __str__(self):
      return self.Order

class Categories(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=100 , blank=True)
  slug = models.CharField(max_length=200 , blank=True)
  def __str__(self):
      return self.Categories

class Attributes(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=100 , blank=True)
  slug = models.CharField(max_length=200 , blank=True)
  def __str__(self):
      return self.Attributes


class Reviews(models.Model):
  id = models.AutoField(primary_key=True)
  customer_id   =  models.IntegerField(blank=True)
  product_id =  models.IntegerField(blank=True)
  date_created_gmt = models.DateField(blank=True)
  status = models.CharField(max_length=100 , blank=True)
  reviewer= models.CharField(max_length=100 , blank=True)
  reviewer_email= models.CharField(max_length=100 , blank=True)
  review = models.CharField(max_length=200 , blank=True)
  rating = models.CharField(max_length=100 , blank=True)
  verified = models.BooleanField()

  def __str__(self):
      return self.Product_reviews


class Images(models.Model):
  id = models.AutoField(primary_key=True)
  date_created_gmt = models.DateField(blank=True)
  src = models.CharField(max_length=200 , blank=True)
  date_modified_gmt  = models.DateField(blank=True)
  def __str__(self):
      return self.Images


class Products(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=400 , blank=True)
  slug = models.CharField(max_length=400 , blank=True)
  permalink = models.CharField(max_length=400 , blank=True)
  date_created_gmt = models.DateField(blank=True)
  date_modified_gmt = models.DateField(blank=True)
  type = models.CharField(max_length=40 , blank=True)
  status = models.CharField(max_length=40 , blank=True)
  featured   = models.BooleanField()
  catalog_visibility = models.CharField(max_length=40 , blank=True)
  short_description = models.CharField(max_length=400 , blank=True)
  sku  = models.CharField(max_length=40 , blank=True)
  price  = models.CharField(max_length=40 , blank=True)
  regular_price = models.CharField(max_length=40 , blank=True)
  sale_price = models.CharField(max_length=40 , blank=True)
  date_on_sale_from_gmt = models.DateField(blank=True)
  date_on_sale_to_gmt  = models.DateField(blank=True)
  on_sale = models.BooleanField()
  price_html = models.CharField(max_length=40 , blank=True)
  purchasable = models.BooleanField(blank=True)
  total_sales = models.IntegerField(blank=True)
  downloadable = models.BooleanField(blank=True)
  tax_status = models.CharField(max_length=40 , blank=True)
  stock_quantity = models.IntegerField(blank=True)
  backorders = models.CharField(max_length=40 , blank=True)
  backorders_allowed = models.BooleanField(blank=True)
  backordered = models.BooleanField(blank=True)
  manage_stock= models.BooleanField(blank=True)
  stock_status = models.CharField(max_length=40 , blank=True)
  sold_individually = models.BooleanField(blank=True)
  weight = models.CharField(max_length=40 , blank=True)
  average_rating   = models.CharField(max_length=40 , blank=True)
  reviews_allowed  = models.BooleanField(blank=True)
  rating_count  = models.IntegerField(blank=True)
  categories = models.IntegerField(blank=True)
  images  = models.IntegerField(blank=True)
  attributes  = models.IntegerField(blank=True)
  

  def __str__(self):
      return self.Products

class Product_Categories(models.Model):
  id  = models.AutoField(primary_key=True)
  product_id  = models.ForeignKey(Products, on_delete=models.DO_NOTHING)
  category_id =  models.ForeignKey(Categories, on_delete=models.DO_NOTHING)
  def __str__(self):
      return self.Product_Categories


class Product_Attributes(models.Model):
  id  = models.AutoField(primary_key=True)
  product_id  = models.ForeignKey(Products, on_delete=models.DO_NOTHING)
  attributes_id =  models.ForeignKey(Attributes, on_delete=models.DO_NOTHING)
  def __str__(self):
      return self.Product_Categories

class Product_Images(models.Model):
  id  = models.AutoField(primary_key=True)
  product_id  = models.ForeignKey(Products, on_delete=models.DO_NOTHING)
  images_id =  models.ForeignKey(Images, on_delete=models.DO_NOTHING)
  def __str__(self):
      return self.Product_Images



class Product_reviews(models.Model):
  id  = models.AutoField(primary_key=True)
  product_id  = models.ForeignKey(Products, on_delete=models.DO_NOTHING)
  reviews_id =  models.ForeignKey(Reviews, on_delete=models.DO_NOTHING)
  def __str__(self):
      return self.Product_reviews

""" 
class Categories(models.Model):
  id = models.AutoField(primary_key=True) """



"""
Tables: 
Order - order ID, Product IDs, User IDs, Order Total - Order API data 
User - user ID, first name, last name, phone, email, address, - user API data 
Product table - product name, price, taxes, total price, discounts, etc. - Product API data 
Coupon Codes - Coupon name, discount total, percent off or money off, etc. - Coupon API data 




Order- id, , number , order_key , created_via , currency , date_created , status , discount_total , discount_tax , shipping_tax , shipping_total , total , total_tax , customer_id , payment_method , payment_method_title , transaction_id , date_paid_gmt , line_items , 
line_items - order_id , customer_id , id , name , product_id , variation_id , quantity , tax_class , subtotal , subtotal_tax, total , total_tax, price , sku.
coupon_lines - order_id , customer_id , coupon_id1 , coupon_id2 , coupon_id3
refund - order_id , customer_id , id , refund , total.
products , product_variation , product_categories , product_reviews , product_attributes

User - id , date_created_gmt , date_modified_gmt , email , first_name ,  last_name , username , "role , address_1 , address_2 , city , state , country , phone , is_paying_customer , avatar_url





Product table - id , name , slug , permalink , date_created_gmt , date_modified_gmt , type , status , featured , catalog_visibility , short_description , sku , price , regular_price , sale_price , date_on_sale_from_gmt , date_on_sale_to_gmt , price_html , on_sale , purchasable , total_sales , downloadable , tax_status , stock_quantity , manage_stock , stock_status , backorders , backorders_allowed ,backordered , sold_individually , weight , reviews_allowed , average_rating , rating_count , categories , images , attributes , grouped_products 
grouped_products - product_id , id 
images - product_id , id , date_created_gmt , src , date_modified_gmt , 
attributes -  id , name , variation , 
product_attributes - id , attributes_id , product_id

options - attributes_id , option_name
categories -  , id , name , slug 
product_categories -  , id , , product_id , catehory_id ,
product_reviews - product_id , id , customer_id , date_created_gmt , status , reviewer , reviewer_email , review , rating , verified , ": {
         

coupon - order_id , id , code , amount , date_created_gmt , date_modified_gmt , discount_type , date_expires_gmt , usage_count , individual_use , product_ids ,excluded_product_ids , usage_limit , usage_limit_per_user , limit_usage_to_x_items , free_shipping , minimum_amount , maximum_amount , used_by
used_by - coupon_id , customer_id , id , order_id
product_ids - coupon_id , product_id , id
excluded_product_ids - coupon_id , product_id , id




"""


