from django import forms
from .models import Product,Employee,Order


#order

 
#DataFlair
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'




        #orderform

class OrderForm(forms.ModelForm):
    product_name = forms.CharField(label="Product Name", widget=forms.TextInput(attrs={'class': 'form-control order'}))
    price = forms.IntegerField(label="$ Price", widget=forms.TextInput(attrs={'class': 'form-control order'}))
    product_quantity=forms.CharField(label="Product Quantity", widget=forms.TextInput(attrs={'class': 'form-control order'}))
    # created_time = forms.DateTimeField(label="Created Time", widget=forms.TextInput(
    #     attrs={'class': 'form-control order', 'placeholder': 'YYYY-mm-dd'}))

    class Meta:
        model = Order
        fields = ['product_name', 'price','product_quantity',]