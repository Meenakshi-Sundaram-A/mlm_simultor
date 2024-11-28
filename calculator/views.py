import json
import math
import requests
from .forms import FormData, UniLevelFormData
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def binarylevel_input_view(request):
    print(request.POST)
    binary_form = FormData(request.POST)
    if request.method == "POST":
        try:
            num_of_users = request.POST.get('num_of_users')
            users_per_product = request.POST.getlist('users_per_product')
            users_per_product = list(map(int, users_per_product))
            users_per_cycle = sum(users_per_product)
            
            product_price = request.POST.getlist('product_price')
            product_price = list(map(int, product_price))
            percentage_str = request.POST.getlist('matching_bonus_percentages')
            percentage_str = list(map(int, percentage_str))
            
            cycle = math.ceil(float(num_of_users) / float(users_per_cycle))
                
            
            data = {
                    "num_of_users": int(request.POST.get('num_of_users')),
                    "product_price": product_price,
                    "users_per_product": users_per_product,
                    "sponsor_bonus_percentage": float(request.POST.get('sponsor_bonus_percentage')),
                    "binary_bonus_percentage": float(request.POST.get('binary_bonus_percentage')),
                    "percentage_string": percentage_str,
                    "ratio_choice": request.POST.get("ratio_choice"),
                    "ratio_amount": float(request.POST.get("ratio_amount")),
                    "capping_scope": request.POST.get('capping_scope'),
                    "capping_amount": float(request.POST.get('capping_amount')),
                    "cycle": cycle,
                    "plan_type": "binary",
                }

            response = requests.post('http://localhost:8080/api/processData', json=data)
            response.raise_for_status()
            results = response.json()

            return render(request, 'display_members.html', {'all_results': results})

        except ValueError as e:
            error_message = f"Input error: {str(e)}"
        except requests.exceptions.RequestException as e:
            error_message = f"Failed to communicate with the Go server: {str(e)}"
        except Exception as e:
            error_message = f"Unexpected error: {str(e)}"

        return render(request, 'form_template.html', {
            'binary_form': binary_form,
            'error_message': error_message,
        })

    # Render empty forms for a GET request
    return render(request, 'form_template.html', {'binary_form': binary_form, 'binary':True})

def unilevel_input_view(request):
    unilevel_form = UniLevelFormData(request.POST)
    if request.method == "POST":
        try:
            num_of_users = request.POST.get('num_of_users')
            users_per_product = request.POST.getlist('users_per_product')
            users_per_product = list(map(int, users_per_product))
            users_per_cycle = sum(users_per_product)
            
            product_price = request.POST.getlist('product_price')
            product_price = list(map(int, product_price))
            percentage_str = request.POST.getlist('matching_bonus_percentages')
            percentage_str = list(map(int, percentage_str))
            
            cycle = math.ceil(float(num_of_users) / float(users_per_cycle))
                
            data = {
                    "num_of_users": int(request.POST.get('num_of_users')),
                    "max_child": int(request.POST.get('max_child')),
                    "product_price": product_price,
                    "users_per_product": users_per_product,
                    "sponsor_bonus_percentage": float(request.POST.get('sponsor_bonus_percentage')),
                    "percentage_string": percentage_str,
                    "capping_scope": request.POST.get('capping_scope'),
                    "capping_amount": float(request.POST.get('capping_amount')),
                    "cycle": cycle,
                    "plan_type": "unilevel",
                }

            # Send data to the Go server and process the response
            response = requests.post('http://localhost:8080/api/processData', json=data)
            response.raise_for_status()
            results = response.json()

            return render(request, 'display_members.html', {'all_results': results})

        except ValueError as e:
            error_message = f"Input error: {str(e)}"
        except requests.exceptions.RequestException as e:
            error_message = f"Failed to communicate with the Go server: {str(e)}"
        except Exception as e:
            error_message = f"Unexpected error: {str(e)}"

        # Render the form with an error message
        return render(request, 'form_template.html', {
            'unilevel_form': unilevel_form,
            'error_message': error_message,
        })

    # Render empty forms for a GET request
    return render(request, 'form_template.html', {'unilevel_form': unilevel_form, 'unilevel':True})

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
            'nodes': nodes,
        }

        try:
            return render(request, 'display_members.html', context)
        except Exception as e:
            return JsonResponse({'error': f'Template rendering error: {str(e)}'}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)
