from django.views.generic import ListView, DetailView, CreateView

from .models import Post, Comment, Recipe
from .forms import CommentForm, RecipeForm


class HomeView(ListView):
    model = Post
    paginate_by = 9
    template_name = "blog/home.html"


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs.get("slug")).select_related('category')


class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"
    slug_url_kwarg = 'post_slug'

    def __init__(self, **kwargs):
        super(PostDetailView).__init__()
        self.object = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context


class CreateComment(CreateView):
    model = Comment
    form_class = CommentForm

    def __init__(self, **kwargs):
        super(CreateComment).__init__()
        self.object = None

    def form_valid(self, form):
        form.instance.post_id = self.kwargs.get('pk')
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.post.get_absolute_url()


class RecipeDetailView(DetailView):
    model = Recipe
    context_object_name = "recipe"
    slug_url_kwarg = 'recipe_slug'

    def __init__(self, **kwargs):
        super(RecipeDetailView).__init__()
        self.object = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context


class CreateRecipe(CreateView):
    model = Recipe
    form_class = RecipeForm

    def __init__(self, **kwargs):
        super(CreateRecipe).__init__()
        self.object = None

    def form_valid(self, form):
        form.instance.post_id = self.kwargs.get('pk')
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.recipe.get_absolute_url()
