import json
import math
import requests
from .forms import FormData, UniLevelFormData, MatrixLevelFormData
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def binarylevel_input_view(request):
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
                
            print(request.POST.get("ratio_choice"), request.POST.get('binary_bonus_percentage'), request.POST.get("ratio_amount"))
            print("sadjkajsfdj")
            print("Pool Bonus Percentage:",float(request.POST.get('pool_bonus_percentage')) if request.POST.get('pool_bonus_percentage') else 0)
            print("Pool Bonus Count:",float(request.POST.get('pool_bonus_count')) if request.POST.get('pool_bonus_count') else 0)
            data = {
                    "num_of_users": int(request.POST.get('num_of_users')),
                    "product_price": product_price,
                    "users_per_product": users_per_product,
                    "sponsor_bonus_percentage": float(request.POST.get('sponsor_bonus_percentage')),
                    "binary_bonus_percentage": float(request.POST.get('binary_bonus_percentage')) if request.POST.get('binary_bonus_percentage') else 0,
                    "pool_bonus_percentage": float(request.POST.get('pool_bonus_percentage')) if request.POST.get('pool_bonus_percentage') else 0,
                    "pool_bonus_count": float(request.POST.get('pool_bonus_count')) if request.POST.get('pool_bonus_count') else 0,
                    "percentage_string": percentage_str,
                    "ratio_choice": request.POST.get("ratio_choice") if request.POST.get("ratio_choice")!=None else "",
                    "ratio_amount": float(request.POST.get("ratio_amount")) if request.POST.get("ratio_amount")!="" else 0,
                    "capping_scope": request.POST.getlist('capping_scope'),
                    "capping_amount": float(request.POST.get('capping_amount')),
                    "cycle": cycle,
                    "plan_type": "binary",
                }
            response = requests.post('http://localhost:8080/api/processData', json=data)
            response.raise_for_status()
            results = response.json()
            print(results)

            return render(request, 'display_members.html', {'all_results': results,'cycle':cycle})

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
            capping_scope = request.POST.getlist('capping_scope')
            print(capping_scope)
            
            cycle = math.ceil(float(num_of_users) / float(users_per_cycle))
                
            data = {
                    "num_of_users": int(request.POST.get('num_of_users')),
                    "max_child": int(request.POST.get('max_child')),
                    "product_price": product_price,
                    "users_per_product": users_per_product,
                    "sponsor_bonus_percentage": float(request.POST.get('sponsor_bonus_percentage')),
                    "pool_bonus_percentage": float(request.POST.get('pool_bonus_percentage')) if request.POST.get('pool_bonus_percentage') else 0,
                    "pool_bonus_count": float(request.POST.get('pool_bonus_count')) if request.POST.get('pool_bonus_count') else 0,
                    "percentage_string": percentage_str,
                    "capping_scope": request.POST.getlist('capping_scope'),
                    "capping_amount": float(request.POST.get('capping_amount')),
                    "cycle": cycle,
                    "plan_type": "unilevel",
                }

            # Send data to the Go server and process the response
            response = requests.post('http://localhost:8080/api/processData', json=data)
            response.raise_for_status()
            results = response.json()

            return render(request, 'unilevel_result.html', {'all_results': results})

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

def matrixlevel_input_view(request):
    matrixlevel_form = MatrixLevelFormData(request.POST)
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
            capping_scope = request.POST.getlist('capping_scope')
            print(capping_scope)
            
            cycle = math.ceil(float(num_of_users) / float(users_per_cycle))
                
            data = {
                    "num_of_users": int(request.POST.get('num_of_users')),
                    "max_child": int(request.POST.get('max_child')),
                    "product_price": product_price,
                    "users_per_product": users_per_product,
                    "sponsor_bonus_percentage": float(request.POST.get('sponsor_bonus_percentage')),
                    "pool_bonus_percentage": float(request.POST.get('pool_bonus_percentage')) if request.POST.get('pool_bonus_percentage') else 0,
                    "pool_bonus_count": float(request.POST.get('pool_bonus_count')) if request.POST.get('pool_bonus_count') else 0,
                    "percentage_string": percentage_str,
                    "capping_scope": request.POST.getlist('capping_scope'),
                    "capping_amount": float(request.POST.get('capping_amount')),
                    "cycle": cycle,
                    "plan_type": "unilevel",
                }

            # Send data to the Go server and process the response
            response = requests.post('http://localhost:8080/api/processData', json=data)
            response.raise_for_status()
            results = response.json()

            return render(request, 'unilevel_result.html', {'all_results': results})

        except ValueError as e:
            error_message = f"Input error: {str(e)}"
        except requests.exceptions.RequestException as e:
            error_message = f"Failed to communicate with the Go server: {str(e)}"
        except Exception as e:
            error_message = f"Unexpected error: {str(e)}"

        # Render the form with an error message
        return render(request, 'form_template.html', {
            'unilevel_form': matrixlevel_form,
            'error_message': error_message,
        })

    # Render empty forms for a GET request
    return render(request, 'form_template.html', {'matrixlevel_form': matrixlevel_form, 'matrixlevel':True})

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
