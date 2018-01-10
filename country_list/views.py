from django.shortcuts import render, redirect
import vk, collections

app_id = 6327767

def logon_func(request):
    return render(request, 'logon_page.html')

def country_list_func(request):
    form_name = request.POST.get('vk_name','default')
    form_pw = request.POST.get('vk_pw','default')

    request.session['vk_name'] = form_name
    request.session['vk_pw'] = form_pw

    session = vk.AuthSession(app_id, user_login = form_name, user_password = form_pw)
    vk_api = vk.API(session)
    country_dict = vk_api.database.getCountries()


    tmp_value = request.session.get('vk_name', 'it doesn t work :(')
    return render(request, 'home.html', {'countries' : country_dict})

def cities_list_func(request, country_id_value):
    form_name =  request.session['vk_name']
    form_pw = request.session['vk_pw']

    session = vk.AuthSession(app_id, user_login = form_name, user_password = form_pw)
    vk_api = vk.API(session)

    cities_dict = vk_api.database.getCities(country_id = country_id_value)
    
    need_sort = request.GET.get('sorted',0)
    
    cities_list = []

    for city in cities_dict:
        cities_list.append(city['title'])
    if need_sort:
        cities_list = sorted(cities_list)
    return render(request, 'cities.html', {'cities' : cities_list})