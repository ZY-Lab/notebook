##is_staff权限验证

    @user_passes_test(lambda u: u.is_staff)  
或者

    from django.contrib.admin.views.decorators import staff_member_required
    @staff_member_required

####基于类的视图：
    from django.contrib.auth.mixins import PermissionRequiredMixin
    from django.http import HttpResponse
    
    class MyView(PermissionRequiredMixin, View):

    permission_required = 'is_staff'
    
    def get(self, request):
        return HttpResponse('result')
或者

    from django.contrib.auth.decorators import permission_required

    url(r'^your-url$', permission_required('is_staff')(YourView.as_view()), name='my-view'),