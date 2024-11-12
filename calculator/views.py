from django.shortcuts import render
from .forms import FormData

# Create your views here.
def user_input_view(request):
    if request.method == "POST":
        form = FormData(request.POST)
        
        if form.is_valid():
            num_of_users = form.cleaned_data['num_of_users']
            package_price = form.cleaned_data['package_price']
            sponsor_bonus_percentage = form.cleaned_data['sponsor_bonus_percentage']
            binary_bonus_percentage = form.cleaned_data['binary_bonus_percentage']
            lev1_percentage = form.cleaned_data['lev1_percentage']
            lev2_percentage = form.cleaned_data['lev2_percentage']
            capping_scope = form.cleaned_data['capping_scope']
            capping_amount = form.cleaned_data['capping_amount']
            carry_yes_no = form.cleaned_data['carry_yes_no']
            
            data = {
                "num_of_users":num_of_users,
                "package_price":package_price,
                "sponsor_bonus_percentage":sponsor_bonus_percentage,
                "binary_bonus_percentage":binary_bonus_percentage,
                "lev1_percentage":lev1_percentage,
                "lev2_percentage":lev2_percentage,
                "capping_scope":capping_scope,
                "capping_amount":capping_amount,
                "carry_yes_no":carry_yes_no
            }
            
            return render(request, 'success.html', {'data': form.cleaned_data})
        else:
            # If the form is not valid, return the form with errors
            return render(request, 'form_template.html', {'form': form})