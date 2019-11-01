from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from . models import Contact


def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id'] 
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # Check if user has made inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'Yo have already made an inquiry for this accommodation')
                return redirect('/listings/'+listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)
        contact.save()

        # Send email
        send_mail(
            'Accommodation Inquiry',
            'There has been an inquiry for ' + listing + '. The student details are as follows. Name: '+ name +' Email: '+ email +' Phone: '+ phone +' . Kindly contact the student as early as possible.',
            'siddhesh.esskay.92@gmail.com',
            [realtor_email],
            fail_silently=False
        )

        messages.success(request, 'Your request has been submitted, we will get back to you soon')
        return redirect('/listings/'+listing_id)