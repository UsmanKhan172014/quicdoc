from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from apps.teams.decorators import login_and_team_required


def home(request):
    if request.user.is_authenticated:
        team = request.team
        if team:
            return HttpResponseRedirect(reverse('web_team:home', args=[team.slug]))
        else:
            messages.info(request, _(
                'Teams are enabled but you have no teams. '
                'Create a team below to access the rest of the dashboard.'
            ))
            return HttpResponseRedirect(reverse('teams:manage_teams'))
    else:
        # return render(request, 'web/landing_page.html')
        return render(request, 'frontend/index.html')


@login_and_team_required
def team_home(request, team_slug):
    assert request.team.slug == team_slug
    # return render(request, 'dashboard/index.html', context={
    #     'team': request.team,
    #     'active_tab': 'dashboard',
    #     'page_title': _('%(team)s Dashboard') % {'team': request.team},
    # })
    return HttpResponseRedirect(reverse('get_all'))


def simulate_error(request):
    raise Exception('This is a simulated error.')
