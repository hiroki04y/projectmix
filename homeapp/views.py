from django.views import generic
from .forms import InquiryForm
import logging
from django.urls import reverse_lazy
from django.contrib import messages

# ロガーの取得
logger = logging.getLogger(__name__)

# Create your views here.

# reverse_lazyはTemplateViewで使い、renderはfunctionで実装する場合に使用する

# クラスベースビュー
# ホーム画面
class homefunc(generic.TemplateView):
    template_name = "home.html"

# お問い合わせ画面
class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('homeapp:inquiry')

    # フォームバリデーションに問題が無かったら実行される
    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'メッセージを送信しました。')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)
