from django.urls import path
from . import views
from .views import AnnouncementListView, NotePostLikeView


app_name = 'note'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post/', views.CreateNoteView.as_view(), name='post'),
    path('post_done', views.PostSuccessView.as_view(), name='post_done'),
    path('notes/<int:category>',
        views.CategoryView.as_view(),name = 'notes_cat'),
    path('user-list/<int:user>', views.UserView.as_view(), name = 'user_list'),
    #path('note-detail/<int:pk>', views.NoteDetailView.as_view(), name = 'note_detail'),
    path('note/<int:pk>/', views.NoteDetailView.as_view(), name = 'detail'),
    path('mypage', views.MypageView.as_view(), name = 'mypage'),
    path('note/<int:pk>/delete/', views.NoteDeleteView.as_view(), name = 'note_delete'),
    path('note/edit/<int:pk>/' ,views.NoteUpdateView.as_view(), name= 'edit'),
    path('note/search', views.NoteSearchView.as_view(), name= 'note_search'),
    #path('note/<int:pk>/react/', views.ReactionCreateView.as_view(), name='reaction_form'),
    #path('reaction/<int:pk>/good/', GoodView.as_view(), name='good'),
    path('note/<int:pk>/comment/', views.CommentCreateView.as_view(), name='add_comment'),
    path('announcements/', AnnouncementListView.as_view(), name='announcement_list'),
    path('note/like/<int:pk>/', NotePostLikeView.as_view(), name='notepost_like'),

]   
