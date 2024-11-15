import json
import requests
from .forms import FormData, UniLevelFormData
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
# def user_input_view(request):
#     if request.method == "POST":
#         form = FormData(request.POST)
        
#         if form.is_valid():
#             num_of_users = form.cleaned_data['num_of_users']
#             package_price = form.cleaned_data['package_price']
#             plan_type = form.cleaned_data['plan_type']
#             sponsor_bonus_percentage = form.cleaned_data['sponsor_bonus_percentage']
#             binary_bonus_percentage = form.cleaned_data['binary_bonus_percentage']
#             lev1_percentage = form.cleaned_data['lev1_percentage']
#             lev2_percentage = form.cleaned_data['lev2_percentage']
#             capping_scope = form.cleaned_data['capping_scope']
#             capping_amount = form.cleaned_data['capping_amount']
#             carry_yes_no = form.cleaned_data['carry_yes_no']
            
#             data = {
#                 "num_of_users":num_of_users,
#                 "package_price":package_price,
#                 "plan_type":plan_type,
#                 "sponsor_bonus_percentage":sponsor_bonus_percentage,
#                 "binary_bonus_percentage":binary_bonus_percentage,
#                 "lev1_percentage":lev1_percentage,
#                 "lev2_percentage":lev2_percentage,
#                 "capping_scope":capping_scope,
#                 "capping_amount":capping_amount,
#                 "carry_yes_no":carry_yes_no
#             }
            
#             try:
#                 response = requests.post('http://localhost:8080/api/processData', json=data)
#                 response.raise_for_status()
#                 results = response.json()
#                 return render(request, 'display_members.html', {
#                     'results': results,
#                 })
#             except requests.exceptions.RequestException as e:
#                 return JsonResponse({'error': f'Failed to communicate with Go server: {str(e)}'}, status=500)
#         else:
#             return render(request, 'form_template.html', {'form': form})
            
#     else:
#         form = FormData()
#         return render(request, 'form_template.html', {'form': form})
    
def user_input_view(request):
    
    binary_form = FormData(request.POST or None)
    unilevel_form = UniLevelFormData(request.POST or None)
    plan_type = request.POST.get("plan_type","")
    print(plan_type)
    
    if request.method == "POST":
        if plan_type == "binary" and binary_form.is_valid():
            data = {
                    "num_of_users": binary_form.cleaned_data['num_of_users'],
                    "package_price":binary_form.cleaned_data['package_price'],
                    "sponsor_bonus_percentage":binary_form.cleaned_data['sponsor_bonus_percentage'],
                    "binary_bonus_percentage":binary_form.cleaned_data['binary_bonus_percentage'],
                    "lev1_percentage":binary_form.cleaned_data['lev1_percentage'],
                    "lev2_percentage":binary_form.cleaned_data['lev2_percentage'],
                    "capping_scope":binary_form.cleaned_data['capping_scope'],
                    "capping_amount":binary_form.cleaned_data['capping_amount'],
                    "carry_yes_no":binary_form.cleaned_data['carry_yes_no'],
                    "plan_type":"binary",
                }
        elif plan_type == "unilevel" and unilevel_form.is_valid():
            data = {
                    "num_of_users": unilevel_form.cleaned_data['num_of_users'],
                    "package_price":unilevel_form.cleaned_data['package_price'],
                    "sponsor_bonus_percentage":unilevel_form.cleaned_data['sponsor_bonus_percentage'],
                    "max_child":unilevel_form.cleaned_data['max_child'],
                    "plan_type":"unilevel",
                }
            
        if plan_type in ["binary", "unilevel"]:
            try:
                response = requests.post('http://localhost:8080/api/processData', json=data)
                response.raise_for_status()
                results = response.json()
                return render(request, 'display_members.html', {'results': results})
            except requests.exceptions.RequestException as e:
                return JsonResponse({'error': f'Failed to communicate with Go server: {str(e)}'}, status=500)
            
        return render(request, 'form_template.html', {
            'binary_form': binary_form,
            'unilevel_form': unilevel_form
        })
    else:
        return render(request, 'form_template.html', {'binary_form': binary_form,'unilevel_form': unilevel_form})

    
@csrf_exempt
def process_results(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

        sponsor_bonus = data.get('total_sponsor_bonus', 0.0)
        binary_bonus = data.get('total_binary_bonus', 0.0)
        nodes = data.get('tree_structure', [])

        context = {
            'sponsor_bonus': sponsor_bonus,
            'binary_bonus': binary_bonus,
            'nodes': nodes
        }

        try:
            render_context = render(request, 'display_members.html', context)
            return render_context
        except Exception as e:
            return JsonResponse({'error': 'Template rendering error'}, status=500)

    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
