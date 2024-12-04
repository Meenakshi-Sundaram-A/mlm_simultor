from django import forms


class FormData(forms.Form):
    num_of_users = forms.IntegerField(
        label="Number of users",
        required=True,
        widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Number of users'})
        )
    CURRENCY_CHOICE = [
        ('usd', 'USD'),
        ('inr', 'INR'),
        ('eur', 'EUR'),
    ]
    currency = forms.ChoiceField(
        choices=CURRENCY_CHOICE,
        label="Select Currency",
        required=True,
        widget=forms.Select(attrs={'class':'form-select', 'style':'width:250px; font-size: 16px;'})
        )
    product_price = forms.CharField(
        label="Product Price / BV",
        required=True,
        widget=forms.NumberInput(attrs={'class':'form-control','placeholder': 'Price / BV'})
    )
    users_per_product = forms.CharField(
        label="Quantity",
        required=True,
        widget=forms.NumberInput(attrs={'class':'form-control','placeholder': 'Quantity'})
    )
    sponsor_bonus_percentage = forms.IntegerField(
        label="Sponsor Bonus %",
        required=True,
        widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Sponsor Bonus %'})
        )
    binary_bonus_percentage = forms.IntegerField(
        label="Binary Bonus %",
        required=False,
        widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Binary Bonus %'})
        )
    matching_bonus_percentages = forms.CharField(
        label="Matching Bonus %",
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Level Bonus %'})
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
        required=False
        )
    ratio_amount = forms.IntegerField(
        label="Ratio Amount",
        required=False,
        widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Ratio Amount'})
        )
    pool_bonus_percentage= forms.IntegerField(
        label="Pool Bonus %",
        required=False,
        widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Pool Bonus %'})
    )
    pool_bonus_count= forms.IntegerField(
        label="Number of Users",
        required=False,
        widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Number of Users'})
    )
    capping_scope = forms.MultipleChoiceField(
        choices=CAPPING_SCOPE_CHOICE,
        label="Capping Criteria",
        required=True,
        widget=forms.CheckboxSelectMultiple(attrs={'class':'form-check-input', 'style': 'font-size: 16px;'})
        )
    capping_amount = forms.IntegerField(
        label="Capping Amount",
        required=True,
        widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Capping Amount'})
        )
    # CARRY_CHOICE = [
    #     ('yes','Yes'),
    #     ('no','No'),
    # ]
    # carry_yes_no = forms.ChoiceField(choices=CARRY_CHOICE,widget=forms.RadioSelect,label="Carry Forward (Yes or No)",required=True)
    
    
class UniLevelFormData(forms.Form):
    num_of_users = forms.IntegerField(
        label="Number of Users",
        required=True,
        widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Number of users'})
        )
    max_child = forms.IntegerField(
        label="Max children", 
        required=True,
        widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Max Children'})
        )
    CURRENCY_CHOICE = [
        ('usd', 'USD'),
        ('inr', 'INR'),
        ('eur', 'EUR'),
    ]
    currency = forms.ChoiceField(
        choices=CURRENCY_CHOICE,
        label="Select Currency",
        required=True,
        widget=forms.Select(attrs={'class':'form-select', 'style':'width:200px; font-size: 16px;'})
        )
    product_price = forms.CharField(
        label="Product Price / BV",
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Price / BV'})
    )
    users_per_product = forms.CharField(
        label="Quantity",
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Quantity'})
    )
    sponsor_bonus_percentage = forms.IntegerField(
        label="Sponsor Bonus %",
        required=True,
        widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Sponsor Bonus %'})
        )
    matching_bonus_percentages = forms.CharField(
        label="Matching Bonus %",
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Level Bonus %'})
    )
    pool_bonus_percentage= forms.IntegerField(
        label="Pool Bonus %",
        required=False,
        widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Pool Bonus %'})
    )
    pool_bonus_count= forms.IntegerField(
        label="Number of Users",
        required=False,
        widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Number of Users'})
    )
    CAPPING_SCOPE_CHOICE = [
        ('sponsor_bonus', 'Sponsor Bonus'),
        ('matching_bonus', 'Matching Bonus'),
    ]
    capping_scope = forms.MultipleChoiceField(
        choices=CAPPING_SCOPE_CHOICE,
        label="Capping Criteria",
        required=True,
        widget=forms.CheckboxSelectMultiple(attrs={'class':'form-check-input', 'style': 'font-size: 16px;'})
        )
    capping_amount = forms.IntegerField(
        label="Capping Amount",
        required=True,
        widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Capping Amount'})
        )
    
class MatrixLevelFormData(forms.Form):
    num_of_users = forms.IntegerField(
        label="Number of Users",
        required=True,
        widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Number of users'})
        )
    max_child = forms.IntegerField(
        label="Max children", 
        required=True,
        widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Max Children'})
        )
    CURRENCY_CHOICE = [
        ('usd', 'USD'),
        ('inr', 'INR'),
        ('eur', 'EUR'),
    ]
    currency = forms.ChoiceField(
        choices=CURRENCY_CHOICE,
        label="Select Currency",
        required=True,
        widget=forms.Select(attrs={'class':'form-select', 'style':'width:200px; font-size: 16px;'})
        )
    product_price = forms.CharField(
        label="Product Price / BV",
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Price / BV'})
    )
    users_per_product = forms.CharField(
        label="Quantity",
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Quantity'})
    )
    sponsor_bonus_percentage = forms.IntegerField(
        label="Sponsor Bonus %",
        required=True,
        widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Sponsor Bonus %'})
        )
    matching_bonus_percentages = forms.CharField(
        label="Matching Bonus %",
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Level Bonus %'})
    )
    pool_bonus_percentage= forms.IntegerField(
        label="Pool Bonus %",
        required=False,
        widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Pool Bonus %'})
    )
    pool_bonus_count= forms.IntegerField(
        label="Number of Users",
        required=False,
        widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Number of Users'})
    )
    CAPPING_SCOPE_CHOICE = [
        ('sponsor_bonus', 'Sponsor Bonus'),
        ('matching_bonus', 'Matching Bonus'),
    ]
    capping_scope = forms.MultipleChoiceField(
        choices=CAPPING_SCOPE_CHOICE,
        label="Capping Criteria",
        required=True,
        widget=forms.CheckboxSelectMultiple(attrs={'class':'form-check-input', 'style': 'font-size: 16px;'})
        )
    capping_amount = forms.IntegerField(
        label="Capping Amount",
        required=True,
        widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Capping Amount'})
        )
    