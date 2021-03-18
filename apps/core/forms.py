from django import forms
from apps.core.models import UserTeam

class CreateTeamForm(forms.ModelForm):
    class Meta:
        model = UserTeam
        fields = (
            'teamname', 'team_slogan'
        )

class EditTeamForm(forms.ModelForm):
    class Meta:
        model = UserTeam
        fields = (
            'teamname', 'team_slogan'
        )