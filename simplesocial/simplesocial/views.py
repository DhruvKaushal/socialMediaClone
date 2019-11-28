from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = 'index.html'

class testPage(TemplateView):
    template_name = 'test.html'

class thanksPage(TemplateView):
    template_name = 'thanks.html'