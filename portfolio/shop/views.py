from django.shortcuts import render, redirect
# from portfolio.shop.forms import NewProductForm, ProductForm
# from django.views import View
# from django.contrib import messages
# from django.shortcuts import get_object_or_404
# from portfolio.shop.models import ProductImage, Product, Comment, Category
# from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse

# # Create your views here.

# # HOME PAGE
# def for_all_pages(request):
#     categories = Category.objects.all()
#     return {"categories":categories}

# class IndexView(View):
#     def get(self, request):
#         products = Product.objects.all()
#         q=request.GET.get('q', '')
#         if q:
#             products = products.filter(title__icontains=q)
#         return render(request, "shop/index.html", {'products':products})
    
# class CategoryView(View):
#     def get(self, request, category_name):
#         category = get_object_or_404(Category, name=category_name)
#         products = Product.objects.filter(category=category)
#         q=request.GET.get('q', '')
#         if q:
#             products = products.filter(title__icontains=q)
#         return render(request, "shop/category.html", {'products':products, "category":category})  



    





# PRODUCT VIEWS
@login_required(login_url='login')
def new_product(request):
    if request.method == "GET":
        form = NewProductForm()
        return render(request, 'shop/product_new.html', {'form':form})
    elif request.method == "POST":
        form = NewProductForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            product = form.save(request)
            productimages = []
            for image in request.FILES.getlist("images"):
                productimages.append(ProductImage(image=image, product=product))
            ProductImage.objects.bulk_create(
                productimages
            )
            
            messages.success(request, "Successfully Created!")    
            return redirect('index')
        return render(request, 'shop/product_new.html', {'form':form})
    
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if "recently_viewed" in request.session:
        r_viewed = request.session["recently_viewed"]
        if not product.id in r_viewed:
            r_viewed.append(product.id)
            request.session.modified = True
    else:
        request.session["recently_viewed"] = [product.id,]
    return render(request, 'shop/product_detail.html', {'product':product})

@login_required(login_url='login')
def product_update(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.user==product.author:
        if request.method=='GET':
            form = ProductForm(instance=product)
            return render(request, 'shop/product_update.html', {'form':form, 'pr':product})
        elif request.method == 'POST':
            form = ProductForm(instance = product, data=request.POST, files=request.FILES)
            if form.is_valid():
                form.save()
                if request.FILES.getlist('images'):
                    ProductImage.objects.filter(product=product).delete()
                    productimages = []
                    for image in request.FILES.getlist("images"):
                        productimages.append(ProductImage(image=image, product=product))
                    ProductImage.objects.bulk_create(
                        productimages
                    )
                messages.success(request, 'Successfully Updated!')        
                return redirect('detail', product.id)
            return render(request, 'shop/product_update.html', {'form':form, 'pr':product})
    else:
        messages.error(request, 'Access danied!')
        return redirect('index')   
     
@login_required(login_url='login')    
def product_delete(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.user==product.author:  
        if request.method=='POST':
            product.delete()
            messages.info(request, 'Successfully Deleted!')
            return redirect('index') 
        return render(request, "shop/product_delete.html", {'product':product})
    else:
        messages.error(request, 'Access danied!')
        return redirect('index')  
    
@login_required(login_url='login')
def new_comment(request, product_id):
    product = get_object_or_404(Product, id=product_id)   
    if request.method == 'POST':
        Comment.objects.create(
            author = request.user,
            product= product,
            body = request.POST['body']
        )
        messages.info(request, 'Successfully Sended!')
        return redirect('detail', product_id)
    return HttpResponse("add comment")

@login_required(login_url='login')
def delete_comment(request, product_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user == comment.author:
        comment.delete()
        messages.info(request, 'Successfully Deleted!')
        return redirect('detail', product_id)
    return redirect('detail', product_id)

                        


