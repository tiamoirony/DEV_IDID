from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Photo

from .forms import PhotoForm


# Create your views here.

# HttpResponse(template.render())
#                       render()

# select * from photo;


def home(request):
    # return HttpResponse('hello photo')

    photos = Photo.objects.all()

    return render(request, "photo_list.html", {"photos": photos})


def post(request):
    # if request.method == 'POST':
    #     title = request.POST['title']
    #     author = request.POST['author']
    #     image = request.POST['image']
    #     description = request.POST['description']
    #     price = request.POST['price']
    #     # print(title, author, image, description, price)

    #     # Photo 객체 생성 / save() = insert
    #     photo = Photo(title=title, author=author, image=image, description=description, price=price)
    #     photo.save()

    #     #등록 완료후 리스트로 이동
    #     # redirect 추가

    #     return redirect('/photo/')

    # return render(request, 'photo_post.html')

    # 폼 사용 방식 ========================

    # get 비어있는 폼  / post 내용일 들어있는 폼

    if request.method == "POST":
        form = PhotoForm(request.POST)
        if form.is_valid():
            photo = form.save()
            return redirect("home")
    else:
        form = PhotoForm()

    return render(request, "photo_post.html", {"form": form})


def detail(request, pk):
    # pk에 해당하는 이미지 정보를 찾아서 같이 보내주기
    # select * from photo where id=pk;

    photo = get_object_or_404(Photo, pk=pk)

    # form = PhotoForm(instance=photo)
    # return render(request, 'photo_detail.html',{'form':form})

    return render(request, "photo_detail.html", {"photo": photo})


def remove(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    photo.delete()

    return redirect("/photo/")


def edit(request, pk):
    photo = get_object_or_404(Photo, pk=pk)

    # get 사용자가 요청 하는 이미지 보여주기
    # post 수정

    # 일반 방식

    # if request.method == 'POST':
    #     photo.price = request.POST['price']
    #     photo.save()

    #     return redirect('/photo/{}'.format(photo.pk))

    if request.method == "POST":
        form = PhotoForm(request.POST, instance=photo)
        if form.is_valid():
            photo = form.save()

            return redirect("detail", pk=photo.pk)

    else:
        form = PhotoForm(instance=photo)

    return render(request, "photo_edit.html", {"form": form})
    # return render(request,'photo_edit.html',{'photo':photo})
