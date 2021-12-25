from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import Http404
from user.models import User
from tag.models import Tag
from .models import Board
from .forms import BoardForm

from .serializers import BoardSerializer
from rest_framework import generics
from rest_framework import mixins


def board_detail(request, pk):
    try:
        board = Board.objects.get(pk=pk) 
    except Board.DoesNotExist:
        raise Http404('게시글을 찾을 수 없습니다')

    return render(request, 'board_detail.html', {'board': board})


def board_write(request):
    if not request.session.get('user'):
        return redirect('/user/login/')

    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            fcuser = User.objects.get(pk=user_id)

            tags = form.cleaned_data['tags'].split(',')

            board = Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = fcuser
            board.save()

            for tag in tags:
                if not tag:
                    continue

                _tag, _ = Tag.objects.get_or_create(name=tag)
                board.tags.add(_tag)

            return redirect('/board/list/')
    else:
        form = BoardForm()

    return render(request, 'board_write.html', {'form': form})


def board_list(request):
    all_boards = Board.objects.all().order_by('-id')
    page = int(request.GET.get('p', 1))
    paginator = Paginator(all_boards, 3)

    boards = paginator.get_page(page)
    return render(request, 'board_list.html', {'boards': boards})



class BoardListAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = BoardSerializer

    def get_queryset(self):
        print("AAAA")
        return Board.objects.all().order_by('id')

    def get(self, request, *args, **kwargs):
        print("BBBB")
        return self.list(request, *args, **kwargs)


class BoardDetailAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = BoardSerializer
    pass