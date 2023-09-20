from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView


def news_home(request):
    news = Articles.objects.order_by('-date') # здесь мы импортируем и сортируем статьи по дате
    #news = Articles.objects.all() # здесь мы из класса articles импортируем все объекты (статьи)
    return render(request, 'news/news_home.html', {'news': news})

# создаем класс NewsDetailView для открытия динамических страниц со статьями
class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'
    form_class = ArticlesForm

class NewsDeleteView(DeleteView):
    model = Articles
    template_name = 'news/news-delete.html'

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма не заполнена'
    form = ArticlesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)