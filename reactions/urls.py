from django.urls import path
from .views import NotePostLikeView
# from .views import add_reaction, detail  # インポート修正

app_name = 'reactions'

urlpatterns = [

    path('notepost-like/<int:pk>/', NotePostLikeView.as_view(), name="notepost_like"),
#   path('add_reaction/<int:note_id>/', add_reaction, name='add_reaction'),
#   path('detail/<int:note_id>/', detail, name='detail'),  # インポート修正

]
