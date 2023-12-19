from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.views import View
from django.views.generic.list import ListView
from django.views.generic import TemplateView, ListView
from django.views.generic import CreateView, DetailView, DeleteView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.db.models import Q 
from .forms import NotePostForm, SearchForm, CommentForm #ReactionForm 
from .models import NotePost, Comment, Announcement  #reaction
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# from reactions.models import Reaction


#from django.db.models.query import QuerySet


class IndexView(ListView):
    template_name ="index.html"
    queryset = NotePost.objects.order_by('-posted_at')
    #extra_context={"form":ReactionForm()}
    paginate_by = 100


class AnnouncementListView(ListView):
    model = Announcement
    template_name = 'announcement_list.html'
    context_object_name = 'announcements'

    def get_queryset(self):
        # 最新の5件のお知らせを取得
        return Announcement.objects.all().order_by('-published_date')[:5]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # お知らせの日付をフォーマットして追加
        for announcement in context['announcements']:
            announcement.formatted_date = announcement.published_date.strftime('%Y年%m月%d日')
        return context


class TopPageView(TemplateView):
    template_name = 'top_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # トップページに表示する「いいね」の数を取得
        top_posts = NotePost.objects.all()[:10]  # トップ10の投稿を取得する例

        context['top_posts'] = top_posts  # トップページに表示する投稿
        return context

@method_decorator(login_required, name= 'dispatch')
class CreateNoteView(CreateView):
    form_class = NotePostForm
    template_name = "post_note.html"
    success_url = reverse_lazy('note:post_done')
    
    def form_valid(self, form):
        postdata = form.save(commit=False)
        postdata.user = self.request.user
        postdata.save()
        return super().form_valid(form)
    
    
class PostSuccessView(TemplateView):
    template_name = 'post_success.html'


class CategoryView(ListView):
    template_name = 'index.html'
    paginate_by = 15

    def get_queryset(self): 
        category_id = self.kwargs['category']
        categories = NotePost.objects.filter(
        category=category_id).order_by('-posted_at') 
        return categories
    

class UserView(ListView):
    template_name ='index.html'
    paginate_by= 15

    def get_queryset(self):
        print(self.kwargs)
        user_id=self.kwargs["user"]
        user_list=NotePost.objects.filter(
        user=user_id).order_by("-posted_at")
        return user_list
    

class NoteDetailView(DetailView):
    model = NotePost
    template_name ='detail.html'
    context_object_name = 'object'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=self.object)
        
        liked = False
        if self.object.likes.filter(id=self.request.user.id).exists():
            liked = True
        context['number_of_likes'] = self.object.number_of_likes()
        context['post_is_liked'] = liked
        context['liked_users'] = self.object.likes.all()

        return context
    

class NotePostLikeView(LoginRequiredMixin, View):
    
    def post(self, request, pk):
        post = get_object_or_404(NotePost, id=pk)
        
        # ユーザーが既に「いいね」している場合は、それを取り消す
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            # それ以外の場合は「いいね」を追加
            post.likes.add(request.user)
        return redirect('note:detail', pk=pk)


#commentで追加した12/18
class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'

    def form_valid(self, form):
        post = get_object_or_404(NotePost, pk=self.kwargs['pk'])
        form.instance.user = self.request.user
        form.instance.post = post
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('note:detail', kwargs={'pk': self.object.post.pk})
    



class MypageView(ListView):
    template_name ='mypage.html'
    paginate_by = 15
    
    def get_queryset(self):
        queryset = NotePost.objects.filter(
            user=self.request.user).order_by('-posted_at')
        return queryset



class NoteDeleteView(DeleteView):
    model = NotePost
    template_name ='note_delete.html'
    success_url = reverse_lazy('note:mypage')

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    


@method_decorator(login_required, name='dispatch')
class NoteUpdateView(UpdateView):
    model=NotePost
    form_class = NotePostForm
    template_name = "edit.html"
    success_url = reverse_lazy('note:post_done')

    def form_valid(self, form):
        postdata = form.save(commit=False)
        postdata.user = self.request.user
        postdata.save()
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class NoteSearchView(ListView):
    model = NotePost
    template_name = 'note_search.html'  
    context_object_name = 'note_list'
    paginate_by = 10

    def get_queryset(self):
        form = SearchForm(self.request.GET)
        if form.is_valid():
            query = form.cleaned_data.get('query')
            if query:
                return NotePost.objects.filter(
                    Q(title__icontains=query) | Q(comment__icontains=query)
                )
        return NotePost.objects.none()
    




# #@method_decorator(login_required, name='dispatch')
#     def detail(request, note_id):
#         note = get_object_or_404(NotePost, pk=note_id)
#         reactions = Reaction.objects.filter(note=note)
#         return render(request, 'detail.html', {'note': note, 'reactions': reactions})


    

# @method_decorator(login_required, name= 'dispatch')
# class ReactionCreateView(CreateView):
#     template_name = "reaction_form.html"
#     model = Reaction
#     form_class = ReactionForm 

#     def form_valid(self, form):
#         postdata = form.save(commit=False)
#         postdata.user = self.request.user
#         postdata.save()
#         reaction_type = self.request.POST.get('reaction_type') 
#         reaction = Reaction.objects.create(user=self.request.user, post=postdata, reaction_type=reaction_type)

#         reaction.save()
#         return super().form_valid(form)

# class GoodView(CreateView):
#     def post(self, request, pk):
#         post = get_object_or_404(ReactionForm, pk=pk)
#         post.good += 1
#         post.save()
#         return redirect('list')