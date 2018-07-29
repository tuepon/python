from django.shortcuts import render, redirect, get_object_or_404
from .forms import DepositCreateForm
from .models import Deposit


def index(request):
    context = {
        'deposit_list': Deposit.objects.all(),
    }
    return render(request, 'deposit/deposit_list.html', context)


def add(request):
    # 送信内容を基にフォームを作る。POSTじゃなければ空のフォーム
    form = DepositCreateForm(request.POST or None)

    # method=POST、つまり送信ボタン押下時、入力内容が問題なければ
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('deposit:index')

    # 通常時のページアクセスや、入力内容に誤りがあればまたページを表示
    context = {
        'form':DepositCreateForm()
    }
    return render(request, 'deposit/deposit_form.html', context)

def update(request, pk):
  # urlのpkを基に、Depositを取得
  Deposit = get_object_or_404(Deposit, pk=pk)

  # フォームに、取得したDepositを紐づける
  form = DepositCreateForm(request.POST or None, instance=Deposit)

  # method=POST、つまり送信ボタン押下時、入力内容が問題なければ
  if request.method == 'POST' and form.is_valid():
    form.save()
    return redirect('deposit:index')

  # 通常時のページアクセスや、入力内容に誤りがあればまたページを表示
  context = {
    'form':form
  }
  return render(request, 'deposit/deposit_form.html', context)