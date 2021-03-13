from django import forms
from apps.core.models import UserTeams

class CreateTeamForm(forms.ModelForm):
    class Meta:
        model = UserTeams
        fields = (
            'username', 'teamname', 'team_slogan'
        )

class EditTeamForm(forms.ModelForm):
    class Meta:
        model = UserTeams
        fields = (
            'teamname', 'team_slogan'
        )