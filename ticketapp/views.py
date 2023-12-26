from django.shortcuts import render,redirect,get_object_or_404
from . models import PickupRequest
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'ticketapp/index.html')

def ticket_reports(request):
    tickets_list=PickupRequest.objects.all()
    context={
        'tickets_list':tickets_list,
    }
    return render(request,'ticketapp/data_table.html',context)

def ticket_list(request):
    ticket_list=PickupRequest.objects.all()
    context={
        'ticket_list':ticket_list,
    }
    return render(request,'ticketapp/ticket_list.html',context)

def accept_ticket(request, ticket_id):
    ticket = PickupRequest.objects.get(id=ticket_id)
    ticket.status = 'accept'
    ticket.save()
    messages.success(request, f'Ticket {ticket.ticket_id} accepted successfully.')
    return redirect('ticket_list')

def decline_ticket(request, ticket_id):
    ticket = PickupRequest.objects.get(id=ticket_id)
    ticket.status = 'decline'
    ticket.save()
    messages.error(request, f'Ticket {ticket.ticket_id} declined successfully.')
    return redirect('ticket_list')

def ticket_page(request):
    return render(request,'ticketapp/basic_card.html')

def ticket_details(request, tkt_id):
    ticket = get_object_or_404(PickupRequest, ticket_id=tkt_id)

    # Print the front_image URL to the console for debugging
    print("Front Image URL:", ticket.front_image.url)

    return render(request, 'ticketapp/Product_Details.html', {'ticket': ticket})
