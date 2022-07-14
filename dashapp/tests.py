from django.test import TestCase
from dashapp.models import Product
# Create your tests here.

#=====Model Test=====
class ModelTest(TestCase):

    def testProductModel(self):
        product = Product.objects.create(product_name="Mobile", product_price=800,product_quantity="20",product_discription="Good Product")
        self.assertEquals(str(product), 'Mobile')
        print("IsInstance : ",isinstance(product,Product))
        self.assertTrue(isinstance(product,Product))


from dashapp.models import Order

class OrderTestCase(TestCase):
    def setUp(self):
        Order.objects.create(product_name="mob", price="2000")
        Order.objects.create(product_name="watch", price="3000")

    def test_order(self):
        
        order1 = Order.objects.get(product_name="mob",price="2000")
        order2 = Order.objects.get(product_name="watch",price="3000")
        # self.assertEqual(order1.speak('The mob price is 2000'), )
        # self.assertEqual(order2.speak('The watch price is 3000'), )
        print(order1)
        print(order2)
    #======URL test=======

# class UrlTest(TestCase):

#     def testHomePage(self):
#         response = self.client.get('/')
#         print(response)

#         self.assertEqual(response.status_code, 200)