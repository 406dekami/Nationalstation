from django.contrib import admin

from .models import AfghanistanPopulation, Submission, User

admin.site.site_header = '国情小站管理系统'
admin.site.site_title = '阿富汗国情小站管理系统'
admin.site.index_title = '欢迎使用阿富汗国情小站管理系统'


@admin.register(AfghanistanPopulation)
class AfghanistanPopulationAdmin(admin.ModelAdmin):
    list_display = (
        'year', 'population', 'yearly_change', 'yearly_change_0', 'migrants_net_field', 'median_age', 'fertility_rate',
        'density_p_km2_field', 'urban_pop_field', 'urban_population', 'country_s_share_of_world_pop',
        'world_population',
        'afghanistanglobal_rank')
    list_editable = (
        'population', 'yearly_change_0', 'migrants_net_field', 'median_age', 'fertility_rate', 'density_p_km2_field',
        'urban_pop_field', 'urban_population', 'country_s_share_of_world_pop', 'world_population')
    list_display_links = None  # 禁用list_display_links，因为这些字段并非链接到change页面
    ordering = ('year',)  # 设定默认排序字段

    def get_list_display(self, request):
        # 重写get_list_display方法以确保某些字段可以直接编辑
        base_list_display = super().get_list_display(request)
        if self.list_editable:
            return base_list_display + self.list_editable
        return base_list_display


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # User模型的管理界面设置
    list_display = ('email', 'ip_address', 'submit_time')
    list_filter = ('submit_time',)
    search_fields = ('email', 'ip_address')


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    # Submission模型的管理界面设置
    list_display = ('name', 'email', 'message', 'submit_time')
    list_filter = ('submit_time',)
    search_fields = ('name', 'email')