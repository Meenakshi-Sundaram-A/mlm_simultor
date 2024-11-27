import json
import math
import requests
from .forms import FormData, UniLevelFormData
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Utility function for processing form input fields
def process_form_data(form,user_count):
    percentages_str = form.cleaned_data['matching_bonus_percentages']
    matching_bonus_percentages = [int(x.strip()) for x in percentages_str.split(",")]

    # product_price_str = form.cleaned_data['product_price']
    # product_price = [int(x.strip()) for x in product_price_str.split(",")]

    # users_per_product_str = form.cleaned_data['users_per_product']
    # users_per_product = [int(x.strip()) for x in users_per_product_str.split(",")]

    cycle = math.ceil(form.cleaned_data['num_of_users'] / user_count)

    return matching_bonus_percentages, cycle


# def user_input_view(request):
#     binary_form = FormData(request.POST or None)
#     #print("This is binary Form:",binary_form)
#     unilevel_form = UniLevelFormData(request.POST or None)
#     #print("This is Uni Form:",unilevel_form)
#     plan_type = request.POST.get("plan_type", "")
#     print("plan is:",plan_type)
#     data_type = request.POST.get('data_field')
#     print("Type:",data_type)

#     if request.method == "POST":
#         try:
#             if plan_type == "binary" and binary_form.is_valid():
#                 print(plan_type)
#                 product_price = request.POST.getlist('product_price[]')
#                 users_per_product = request.POST.getlist('users_per_product[]')
#                 print("Product Price:",product_price)
#                 print("User per Product:",users_per_product)
#                 users_per_cycle = sum(users_per_product)
#                 matching_bonus_percentages, cycle = process_form_data(binary_form,users_per_cycle)
                
#                 data = {
#                     "num_of_users": binary_form.cleaned_data['num_of_users'],
#                     "product_price": product_price,
#                     "users_per_product": users_per_product,
#                     "sponsor_bonus_percentage": binary_form.cleaned_data['sponsor_bonus_percentage'],
#                     "binary_bonus_percentage": binary_form.cleaned_data['binary_bonus_percentage'],
#                     "percentage_string": matching_bonus_percentages,
#                     "ratio_choice": binary_form.cleaned_data["ratio_choice"],
#                     "ratio_amount": binary_form.cleaned_data["ratio_amount"],
#                     "capping_scope": binary_form.cleaned_data['capping_scope'],
#                     "capping_amount": binary_form.cleaned_data['capping_amount'],
#                     "cycle": cycle,
#                     "plan_type": "binary",
#                 }

#             elif plan_type == "unilevel" and unilevel_form.is_valid():
#                 #product_price, users_per_product, matching_bonus_percentages, cycle = process_form_data(unilevel_form)
#                 data = {
#                     "num_of_users": unilevel_form.cleaned_data['num_of_users'],
#                     "product_price": product_price,
#                     "users_per_product": users_per_product,
#                     "sponsor_bonus_percentage": unilevel_form.cleaned_data['sponsor_bonus_percentage'],
#                     "percentage_string": matching_bonus_percentages,
#                     "max_child": unilevel_form.cleaned_data['max_child'],
#                     "capping_scope": unilevel_form.cleaned_data['capping_scope'],
#                     "capping_amount": unilevel_form.cleaned_data['capping_amount'],
#                     "cycle": cycle,
#                     "plan_type": "unilevel",
#                 }
#             else:
#                 raise ValueError("Invalid input for the selected plan type.")

#             # Send data to the Go server and process the response
#             response = requests.post('http://localhost:8080/api/processData', json=data)
#             response.raise_for_status()
#             results = response.json()

#             return render(request, 'display_members.html', {'all_results': results})

#         except ValueError as e:
#             error_message = f"Input error: {str(e)}"
#         except requests.exceptions.RequestException as e:
#             error_message = f"Failed to communicate with the Go server: {str(e)}"
#         except Exception as e:
#             error_message = f"Unexpected error: {str(e)}"

#         # Render the form with an error message
#         return render(request, 'form_template.html', {
#             'binary_form': binary_form,
#             'unilevel_form': unilevel_form,
#             'error_message': error_message,
#         })

#     # Render empty forms for a GET request
#     return render(request, 'form_template.html', {'binary_form': binary_form, 'unilevel_form': unilevel_form})


def binarylevel_input_view(request):
    print(request.POST)
    binary_form = FormData(request.POST)
    print(binary_form)
    if request.method == "POST":
        try:
            product_price = binary_form.cleaned_data['product_price']
            users_per_product = binary_form.cleaned_data['user_per_product']
            print("Product Price:",product_price)
            print("User per Product:",users_per_product)
            users_per_cycle = sum(users_per_product)
            matching_bonus_percentages, cycle = process_form_data(binary_form,users_per_cycle)
                
            data = {
                    "num_of_users": binary_form.cleaned_data['num_of_users'],
                    "product_price": product_price,
                    "users_per_product": users_per_product,
                    "sponsor_bonus_percentage": binary_form.cleaned_data['sponsor_bonus_percentage'],
                    "binary_bonus_percentage": binary_form.cleaned_data['binary_bonus_percentage'],
                    "percentage_string": matching_bonus_percentages,
                    "ratio_choice": binary_form.cleaned_data["ratio_choice"],
                    "ratio_amount": binary_form.cleaned_data["ratio_amount"],
                    "capping_scope": binary_form.cleaned_data['capping_scope'],
                    "capping_amount": binary_form.cleaned_data['capping_amount'],
                    "cycle": cycle,
                    "plan_type": "binary",
                }
            print("Idhu data:",data)

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
            'binary_form': binary_form,
            'error_message': error_message,
        })

    # Render empty forms for a GET request
    return render(request, 'form_template.html', {'binary_form': binary_form, 'binary':True})

def unilevel_input_view(request):
    unilevel_form = UniLevelFormData(request.POST)
    if request.method == "POST":
        try:
            product_price = request.POST.getlist('product_price[]')
            users_per_product = request.POST.getlist('users_per_product[]')
            print("Product Price:",product_price)
            print("User per Product:",users_per_product)
            users_per_cycle = sum(users_per_product)
            matching_bonus_percentages, cycle = process_form_data(unilevel_form,users_per_cycle)
                
            data = {
                    "num_of_users": unilevel_form.cleaned_data['num_of_users'],
                    "product_price": product_price,
                    "users_per_product": users_per_product,
                    "sponsor_bonus_percentage": unilevel_form.cleaned_data['sponsor_bonus_percentage'],
                    "binary_bonus_percentage": unilevel_form.cleaned_data['binary_bonus_percentage'],
                    "percentage_string": matching_bonus_percentages,
                    "ratio_choice": unilevel_form.cleaned_data["ratio_choice"],
                    "ratio_amount": unilevel_form.cleaned_data["ratio_amount"],
                    "capping_scope": unilevel_form.cleaned_data['capping_scope'],
                    "capping_amount": unilevel_form.cleaned_data['capping_amount'],
                    "cycle": cycle,
                    "plan_type": "binary",
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
            'binary_form': unilevel_form,
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
