from django.shortcuts import render


class Custom404Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 404:
            # 如果返回的状态码是 404，则渲染自定义的 404 页面
            return render(request, '404.html')
        return response
