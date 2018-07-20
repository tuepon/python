from django.shortcuts import render, redirect
from .forms import AccountCreateForm
from .models import Account

def index(request):
    context = {
        'account_list':Account.objects.all(),
    }
    return render(request, 'deposit/account_list.html')

def add(request):
    # 送信内容を基にフォームを作る。POSTじゃなければ、空のフォーム
    form = AccountCreateForm(request.POST or None)
    
# method=POST、つまり送信ボタン押下時、入力内容が問題なければ
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('deposit:index')
    #通常時のページアクセスや、入力内容に誤りがあればまたページを表示
    context = {
       'form':form
    }
    return render(request, 'deposit/account_form.html', context)