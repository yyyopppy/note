# from django.shortcuts import render, redirect, get_object_or_404
# from .models import Reaction
# from .forms import ReactionForm
# from note.models import NotePost


# def add_reaction(request, note_id):
#     if request.method == 'POST':
#         form = ReactionForm(request.POST)
#         if form.is_valid():
#             reaction = form.save(commit=False)
#             reaction.user = request.user
#             reaction.note_id = note_id
#             reaction.save()
#         return redirect('note_detail', note_id=note_id)
#     else:
#         form = ReactionForm()

#     return render(request, 'add_reaction.html', {'form': form})



# def r_detail(request, note_id):
#     note = get_object_or_404(NotePost, pk=note_id)
#     reactions = Reaction.objects.filter(note_id=note_id)
#     form = ReactionForm()
#     return render(request, 'r_detail.html', {'note': note, 'reactions': reactions, 'form': form})