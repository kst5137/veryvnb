from time import timezone

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from cart.forms import AddProductForm
from .forms import *
from django.db import transaction
from django.http import HttpResponseNotAllowed
#
from allauth.account.signals import user_signed_up
from django.dispatch import receiver


def func2(abcde) :
    return render(abcde, 'templates/users01/login.html')

def product_in_category(request, category_slug=None):
    current_category = None
    categories = Category.objects.all()
    products = Product.objects.filter(display=True)

    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=current_category)

    return render(request, 'shop/list.html', {'current_category': current_category,
                                              'categories': categories,
                                              'products': products,
                                              })


def product_detail(request, id, product_slug=None):
    product = get_object_or_404(Product, id=id, slug=product_slug)
    add_to_cart = AddProductForm(initial={'quantity': 1})
    return render(request, 'shop/detail.html', {'product': product, 'add_to_cart': add_to_cart})

#
# @receiver(user_signed_up)
# def user_signed_up_(**kwargs):
#     user = kwargs['user']
#     extra_data = user.socialaccount_set.filter(provider='naver')[0].extra_data
#     user.last_name = extra_data['name'][0:4]
#     user.first_name = extra_data['name'][4:]
#     user.save()
# from django.shortcuts import render

# Create your views here.

@login_required
def create_product(request) :
    if request.method == 'POST':

        product_form = ProductForm(request.POST)
        type_form = TypeForm(request.POST)
        size_form = SizeForm(request.POST)
        attribute_form = AttributeForm(request.POST)
        facility_form = FacilityForm(request.POST)
        rule_form = RuleForm(request.POST)
        safety_form = SafetyForm(request.POST)
        image_formset = ImageFormSet(request.POST, request.FILES)
        if product_form.is_valid() and image_formset.is_valid():
            product = product_form.save(commit=False)
            type = type_form.save(commit=False)
            size = size_form.save(commit=False)
            attribute = attribute_form.save(commit=False)
            facility = facility_form.save(commit=False)
            rule = rule_form.save(commit=False)
            safety = safety_form.save(commit=False)
            product.user = request.user

            with transaction.atomic():
                product.save()
                type.save()
                size.save()
                attribute.save()
                facility.save()
                rule.save()
                safety.save()
                image_formset.instance = product
                image_formset.save()
                return redirect('shop:product_all')
    else:
        product_form = ProductForm()
        image_formset = ImageFormSet()
        type_form = TypeForm()
        size_form = SizeForm()
        attribute_form = AttributeForm()
        facility_form = FacilityForm()
        rule_form = RuleForm()
        safety_form = SafetyForm()

    context = {'product_form' : product_form, 'image_formset' : image_formset,
               'type_form':type_form, 'size_form':size_form, 'attribute_form':attribute_form,
               'facility_form':facility_form, 'rule_form':rule_form, 'safety_form':safety_form}
    return render(request, 'shop/create_product.html', context)

@login_required
def delete_product(request, product_id) :
    product = get_object_or_404(Product, pk=product_id)
    if request.user != product.user :
        return redirect('shop:product_detail')
    product.delete()
    return redirect('shop:product_all')



def inquiry_create(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        form = InquiryForm(request.POST)
        print(form)
        if form.is_valid():
            inquiry = form.save(commit=False)
            print(inquiry)
            inquiry.user = request.user
            inquiry.product = product
            inquiry.save()
            print('save', inquiry)
            return redirect('shop:product_detail', product_id = product_id)
    else:
        print('else')
        return HttpResponseNotAllowed('Only POST is possible.')
    context = {'product': product, 'form': form}
    return render(request, 'shop/detail.html', context)

#             comment = commentForm.save(commit=False)
#             comment.writer = request.user
#             comment.post = post
#             comment.save()
#             return redirect('/read/' + str(bid))


def inquiry_delete(request, product_id, inquiry_id) :
    inquiry = get_object_or_404(Product, pk=inquiry_id)
    if request.method == "POST" :
        if request.user == inquiry.user :
            inquiry.delete()
    return redirect('shop:product_detail', product_id)

@login_required(login_url='product:login')
def register_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.user != product.user:
        return redirect('shop:product_detail', product_id=product.id)
    if request.method == "GET":
        productForm = ProductForm(instance=product)
        return render(request, 'shop/register_product.html', {'productForm' : productForm})
    else:
        productForm = ProductForm(request.POST)
        if productForm.is_valid():
            product.category = productForm.cleaned_data['category']
            product.type = productForm.cleaned_data['type']
            product.name = productForm.cleaned_data['name']
            product.slug = productForm.cleaned_data['slug']
            product.addr = productForm.cleaned_data['addr']
            product.content = productForm.cleaned_data['content']
            product.price = productForm.cleaned_data['price']
            product.stock = productForm.cleaned_data['stock']
            product.size = productForm.cleaned_data['size']
            product.attribute = productForm.cleaned_data['attribute']
            product.facility = productForm.cleaned_data['facility']
            product.rule = productForm.cleaned_data['rule']
            product.safety = productForm.cleaned_data['safety']
            product.display = productForm.cleaned_data['display']
            product.order = productForm.cleaned_data['order']
            product.save()
            return redirect('shop:product_detail')
    return render(request, 'shop/list.html', )