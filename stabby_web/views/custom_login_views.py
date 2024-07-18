from django.contrib.auth.views import LoginView
from stabby_web.services import DashboardService, TimeZoneService


class custom_login_view(LoginView):
    def get_context_data(self, **kwargs):
        now = TimeZoneService.get_now()
        context = super().get_context_data(**kwargs)
        context["number_of_days"] = DashboardService.get_number_of_days_since_purchase(
            now
        )
        return context
