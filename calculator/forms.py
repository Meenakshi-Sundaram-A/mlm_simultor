from django import forms

class FormData(forms.Form):
    num_of_users = forms.IntegerField(label="Enter the numberof users",required=True)
    package_price = forms.FloatField(label="Enter the price of the package",required=True)
    sponsor_bonus_percentage = forms.IntegerField(label="Enter Sponsor Bonus Percentage",required=True)
    binary_bonus_percentage = forms.IntegerField(label="Enter Binary Bonus Percentage",required=True)
    matching_bonus_percentages = forms.CharField(
        label="Enter Matching Bonus Percentages (eg: 50,25,10)",
        required=True,
    )
    CAPPING_SCOPE_CHOICE = [
        ('binary_bonus', 'Binary Bonus'),
        ('sponsor_bonus', 'Sponsor Bonus'),
        ('matching_bonus', 'Matching Bonus'),
    ]
    capping_scope = forms.ChoiceField(choices=CAPPING_SCOPE_CHOICE,label="Select Capping Criteria",required=True)
    capping_amount = forms.IntegerField(label="Enter the Capping Amount")
    CARRY_CHOICE = [
        ('yes','Yes'),
        ('no','No'),
    ]
    carry_yes_no = forms.ChoiceField(choices=CARRY_CHOICE,widget=forms.RadioSelect,label="Carry Forward (Yes or No)",required=True)
    
    
class UniLevelFormData(forms.Form):
    num_of_users = forms.IntegerField(label="Enter the number of Users",required=True)
    package_price = forms.FloatField(label="Enter the price of the package",required=True)
    sponsor_bonus_percentage = forms.IntegerField(label="Enter Sponsor Bonus Percentage")
    matching_bonus_percentages = forms.CharField(
        label="Enter Matching Bonus Percentages (eg: 50,25,10)",
        required=True,
    )
    max_child = forms.IntegerField(label="Enter max children per person", required=True)
    capping_amount = forms.IntegerField(label="Enter the Capping Amount")
    