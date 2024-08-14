import random
from django.shortcuts import render, redirect
from .models import Screen


def start_game(request):
    if request.method == "POST":
        request.session['has_started'] = True  # ゲームスタートのセッション設定
        return redirect('game', screen_id=1)  # ゲーム画面にリダイレクト
    return render(request, 'game/start.html')


def end_game(request):
    return render(request, 'game/end.html')


def game_view(request, screen_id=1):
    # ゲームスタート画面へのリダイレクトチェック
    if request.session.get('has_started', False) is False:
        # URL直打ちで入ろうとする曲者には制裁！(初期画面からスタートや！)
        return redirect('start_game')
    
    # スクリーンIDの範囲を確認
    if screen_id < 1 or screen_id > 20:
        return redirect('game', screen_id=1)
    
    # クリア画面
    if screen_id == 9:
        return redirect('end_game')

    try:
        current_screen = Screen.objects.get(screen_id=screen_id)
    except Screen.DoesNotExist:
        return redirect('game', screen_id=1)

    if request.method == "POST":
        user_choice = request.POST.get('choice')
        if user_choice == "option1" or user_choice == "option2":
            # next_screen_id に、screen_id+1 または 1 を保持
            next_screen_id = screen_id + 1 if screen_id < 20 else 1
            # next_screen_id に、screen_id+1 または 1 をランダムで選定して格納
            next_screen_id = random.choice([next_screen_id, 1])
            return redirect('game', screen_id=next_screen_id)

    context = {
        'screen': current_screen
    }
    return render(request, 'game/screen.html', context)
