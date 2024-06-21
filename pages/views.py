# pages/views.py
from django.views.generic import TemplateView, ListView,  DetailView

from pages.models import Company, Department


class HomePageView(ListView):
    model = Company
    template_name = 'home.html'

class CompanyDetailView(DetailView): # new
    model = Company
    template_name = 'company/detail.html'

    # slug_field = 'companyId'
    # slug_url_kwarg = 'companyId'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['departments'] = Department.objects.filter(company=self.object)
    #     return context

class DepartmentDetailView(DetailView): # new
    model = Department
    template_name = 'department/detail.html'

    def get_context_data(self, **kwargs):
        context = super(DepartmentDetailView, self).get_context_data(**kwargs)
        page_alt = CompanyDetailView.objects.get(id=self.kwargs.get('pk1', ''))
        context['page_alt'] = page_alt
        return context