from django.shortcuts import render, HttpResponse,redirect
from django.contrib import messages
from .models import Registration, Trips


def home(request):
    if 'id' in request.session:

        context = {
            "all_trips": Trips.objects.all(),
            "logged_user": Registration.objects.get(id = request.session['id']),
        }
        return render(request,"home.html", context)
    
    else:
        return redirect("/")

def addTrip(request):
    return render(request,"addTrip.html")

def createTrip(request):
    
    errors = Trips.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request, value)
        return redirect("/content/addTrip")
    else:
        destination_from_form = request.POST['destination']
        plan_from_form = request.POST['plan']
        start_date_from_form = request.POST['start_date']
        end_date_from_form = request.POST['end_date']
        user_id = int(request.POST['user_id'])

        logged_user = Registration.objects.get(id = user_id)

        Trips.objects.create(destination = destination_from_form, plan = plan_from_form, user = logged_user, start_date = start_date_from_form, end_date = end_date_from_form)

        return redirect('/content/home')

def editTrip(request,id):

    context= {
        "trip_id": int(id),
        "trip_details": Trips.objects.get(id = int(id)),
    }
    
    return render(request,"editTrip.html", context)



def updateTrip(request,id):
    errors = Trips.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request, value)
        return redirect(f"/content/{id}/edit")
    else:
        trip_id = int(id)
        new_destination_from_form = request.POST['destination']
        new_start_date_from_form = request.POST['start_date']
        new_end_date_from_form = request.POST['end_date']
        new_plan_from_form = request.POST['plan']
        
        trip_to_edit = Trips.objects.get(id=trip_id)

        trip_to_edit.destination = f"{new_destination_from_form}"
        trip_to_edit.start_date = f"{new_start_date_from_form}" 
        trip_to_edit.end_date = f"{new_end_date_from_form}" 
        trip_to_edit.plan = f"{new_plan_from_form}"

        trip_to_edit.save()

        return redirect("/content/home")

# def grant(request, id):

#     wish_id = int(id)
#     wish_to_grant = Wishes.objects.get(id = wish_id)
#     wish_to_grant.granted = "True"
#     wish_to_grant.save()


#     return redirect('/content/home')

    
# #     user_id = int(request.POST['user_id'])
# #     logged_user = Registration.objects.get(id = user_id)
# #     all_wishes = Wishes.objects.all()


# #     return render(request,"grantedWishes.html")

# def stats(request,id):
    
#     user_id = int(id)
#     logged_user = Registration.objects.get(id = user_id)

#     user_wishes_granted = 0
#     for wishes in Wishes.objects.filter(user = logged_user, granted= 'True'):
#         user_wishes_granted += 1
    
#     user_wishes_ungranted = 0
#     for wishes in Wishes.objects.filter(user = logged_user, granted= 'False'):
#         user_wishes_ungranted += 1
    
#     user_total_wishes = user_wishes_granted + user_wishes_ungranted


#     total_wishes = 0
#     for wishes in Wishes.objects.filter(granted = 'True'):
#         total_wishes += 1

    

#     context = {
#         "user_wishes_granted": user_wishes_granted,
#         "user_wishes_ungranted": user_wishes_ungranted,
#         "user_total_wishes": user_total_wishes,
#         "total_wishes": total_wishes
#     }

#     return render(request,"stats.html", context)
def removeJoin(request,id,userid):
    trip_id = int(id)
    trip_to_unjoin = Trips.objects.get(id = trip_id)
    user_id = int(userid)
    logged_user = Registration.objects.get(id = user_id)

    trip_to_unjoin.join.remove(logged_user)
    
    return redirect('/content/home')

def joinTrip(request,id,userid):
    trip_id = int(id)
    trip_to_join = Trips.objects.get(id = trip_id)
    user_id = int(userid)
    logged_user = Registration.objects.get(id = user_id)

    trip_to_join.join.add(logged_user)
    
    return redirect('/content/home')

def tripDetails(request,id):

    context = {
        "trip_details": Trips.objects.get(id=int(id))
    }

    return render(request,"tripDetails.html",context)


def destroyTrip(request,id):
    trip_to_delete = Trips.objects.get(id =int(id))
    trip_to_delete.delete()
    return redirect("/content/home")



