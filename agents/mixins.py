from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect


class OrganisorAndLoginRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        """Verify that the current user is authenticated."""
        if not request.user.is_authenticated:
            print('not loggedin')
            return self.handle_no_permission()
        """Verify that the current user is organisor."""
        if not request.user.is_organisor:
            print('not organisor')
            return redirect('lead:lead-list')

        return super().dispatch(request, *args, **kwargs)