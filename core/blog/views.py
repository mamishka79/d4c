from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView

from .forms import CommentForm, PostForm
from .models import Comment, Post


class PostListView(ListView):
    """List all posts with optional author filtering and pagination."""
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        author = self.request.GET.get('author')
        if author:
            queryset = queryset.filter(author__username=author)
        return queryset


class PostDetailView(DetailView):
    """Display a single post with its comments and a comment form."""
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = (
            self.object.comments
                .select_related('user')
                .order_by('-created_at')
        )
        context['form'] = CommentForm()
        return context


@login_required
def add_comment(request, pk):
    """Handle submission of a new comment."""
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.user = request.user
        comment.save()
    return redirect('post_detail', pk=pk)


@login_required
def post_create(request):
    """Create a new post."""
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {
        'form': form,
        'mode': 'create',
    })


@login_required
def post_update(request, pk):
    """Update an existing post (author only)."""
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        return HttpResponseForbidden("Not your post.")
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {
        'form': form,
        'mode': 'update',
    })


@login_required
def post_delete(request, pk):
    """Delete a post (author only)."""
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        return HttpResponseForbidden("Not your post.")
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'blog/post_confirm_delete.html', {
        'post': post,
    })
