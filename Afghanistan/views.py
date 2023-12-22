from django.http import Http404, HttpResponse, JsonResponse, request
from django.shortcuts import render
from django.utils import timezone
from Afghanistan.forms import FormSubmissionForm
from Afghanistan.models import AfghanistanPopulation, User, Submission


# Create your views here.

def check_path_and_return_page(requested_path):
    allowed_paths = [
        '',
        'Afghanistan/',
        'Afghanistan/history/',
        'Afghanistan/diplomacy/',
        'Afghanistan/culture/',
        'Afghanistan/message/',
        'Afghanistan/contact/',
        'Afghanistan/map/',
        'Afghanistan/review/'
    ]

    if requested_path in allowed_paths:
        # 如果请求的路径在允许的路径列表中，则返回相应的页面
        return render(request, requested_path + '.html')
    else:
        # 如果请求的路径不在允许的路径列表中，则返回404.html页面
        return render(request, '404.html')


def afghanistan_overview(request):
    # 在这里编写你获取阿富汗概况信息的逻辑
    country_name = "阿富汗"
    population = "38,928,346"
    capital = "喀布尔"
    language = "普什图语、达里语"
    currency = "阿富汗尼"
    # ... 其他信息或数据

    context = {
        'country_name': country_name,
        'population': population,
        'capital': capital,
        'language': language,
        'currency': currency,
        # ... 其他信息或数据
    }

    return render(request, 'afghanistan_overview.html', context)


def history(request):
    return render(request, 'history.html')


def diplomacy(request):
    return render(request, 'diplomacy.html')


def culture(request):
    return render(request, 'culture.html')


def output_all_entries(request):
    all_entries = AfghanistanPopulation.objects.all()
    return render(request, 'message.html', {'entries': all_entries})


def contact(request):
    return render(request, 'contact.html')


def map(request):
    return render(request, 'map.html')


def error(request):
    raise Http404(request, '404.html')


def get_client_ip(request):
    # 获取客户端IP地址的标准方法
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def process_form(request):
    if request.method == 'POST':
        # 获取表单数据
        email = request.POST.get('email')

        # 获取用户IP地址
        ip_address = get_client_ip(request)

        # 获取当前时间
        submit_time = timezone.now()

        # 创建一个新的User对象
        user = User(email=email, ip_address=ip_address, submit_time=submit_time)

        # 保存到数据库
        user.save()

        # 返回响应给客户端
        return HttpResponse('表单已成功提交，您的IP地址是：' + ip_address)


def form_submission(request):
    if request.method == 'POST':
        form = FormSubmissionForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            submit_time = timezone.now()
            submission = Submission(name=name, email=email, message=message, submit_time=submit_time)
            submission.save()
            return JsonResponse({'status': 'success'})
        return JsonResponse({'status': 'fail'})

