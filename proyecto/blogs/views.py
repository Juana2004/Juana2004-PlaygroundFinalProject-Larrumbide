from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from .forms import BlogForm

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blogs/blog_list.html', {'blogs': blogs})

def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_list')  # Redirigir al usuario a la lista de blogs después de crear un nuevo blog
    else:
        form = BlogForm()
    return render(request, 'blogs/create_blog.html', {'form': form})

def detalle_blog(request, blog_id):
    # Obtener el objeto Blog por su ID
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'blogs/detalle_blog.html', {'blog': blog})

