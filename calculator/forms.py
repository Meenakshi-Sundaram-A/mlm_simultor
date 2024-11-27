from django import forms


class FormData(forms.Form):
    num_of_users = forms.IntegerField(
        label="Number of users",
        required=True,
        widget=forms.NumberInput(attrs={'class':'form-control'})
        )
    product_price = forms.CharField(
        label="Product Price",
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    users_per_product = forms.CharField(
        label="No of Users per Product",
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    sponsor_bonus_percentage = forms.IntegerField(
        label="Sponsor Bonus %",
        required=True,
        widget=forms.NumberInput(attrs={'class':'form-control'})
        )
    binary_bonus_percentage = forms.IntegerField(
        label="Binary Bonus %",
        required=True,
        widget=forms.NumberInput(attrs={'class':'form-control'})
        )
    matching_bonus_percentages = forms.CharField(
        label="Matching Bonus %",
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    CAPPING_SCOPE_CHOICE = [
        ('binary_bonus', 'Binary Bonus'),
        ('sponsor_bonus', 'Sponsor Bonus'),
        ('matching_bonus', 'Matching Bonus'),
    ]
    RATIO_CHOICE = [
        ('one_one','1:1'),
        ('one_two','1:2'),
        ('two_one','2:1'),
    ]
    ratio_choice = forms.ChoiceField(
        choices=RATIO_CHOICE,
        widget=forms.RadioSelect(attrs={'class':'form-check-input'}),
        label="Ratio Choice",
        required=True
        )
    ratio_amount = forms.IntegerField(
        label="Ratio Amount",
        required=True,
        widget=forms.NumberInput(attrs={'class':'form-control'})
        )
    capping_scope = forms.ChoiceField(
        choices=CAPPING_SCOPE_CHOICE,
        label="Capping Criteria",
        required=True,
        widget=forms.Select(attrs={'class':'form-select', 'style':'width:300px; font-size: 16px;'})
        )
    capping_amount = forms.IntegerField(
        label="Capping Amount",
        required=True,
        widget=forms.NumberInput(attrs={'class':'form-control'})
        )
    # CARRY_CHOICE = [
    #     ('yes','Yes'),
    #     ('no','No'),
    # ]
    # carry_yes_no = forms.ChoiceField(choices=CARRY_CHOICE,widget=forms.RadioSelect,label="Carry Forward (Yes or No)",required=True)
    
    
class UniLevelFormData(forms.Form):
    num_of_users = forms.IntegerField(
        label="Enter the number of Users",
        required=True,
        widget=forms.NumberInput(attrs={'class':'form-control'})
        )
    max_child = forms.IntegerField(
        label="Enter max children per person", 
        required=True,
        widget=forms.NumberInput(attrs={'class':'form-control'})
        )
    product_price = forms.CharField(
        label="Enter Product Price (eg: 50,25,10)",
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    users_per_product = forms.CharField(
        label="Enter No of User per Product (eg: 50,25,10)",
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    sponsor_bonus_percentage = forms.IntegerField(
        label="Enter Sponsor Bonus Percentage",
        required=True,
        widget=forms.NumberInput(attrs={'class':'form-control'})
        )
    matching_bonus_percentages = forms.CharField(
        label="Enter Matching Bonus Percentages (eg: 50,25,10)",
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    CAPPING_SCOPE_CHOICE = [
        ('binary_bonus', 'Binary Bonus'),
        ('sponsor_bonus', 'Sponsor Bonus'),
        ('matching_bonus', 'Matching Bonus'),
    ]
    capping_scope = forms.ChoiceField(
        choices=CAPPING_SCOPE_CHOICE,
        label="Select Capping Criteria",
        required=True,
        widget=forms.Select(attrs={'class':'form-select', 'style':'width:300px; font-size: 16px;'})
        )
    capping_amount = forms.IntegerField(
        label="Enter the Capping Amount",
        required=True,
        widget=forms.NumberInput(attrs={'class':'form-control'})
        )
    