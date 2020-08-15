from django.shortcuts import render ,redirect ,get_object_or_404
from .models import Contact ,Male ,Female
from .forms import commentForm , femaleForm , maleForm 
from django.contrib import messages
from .filters import *

# Create your views here.
def index(request):
    template_name = 'index.html'
    return render(request,template_name)


def info(request):
    template_name = 'info.html'
    contacts = Contact.objects.all()
    filter_info = InfoFilter(request.GET , queryset=contacts)
    contacts = filter_info.qs
    context = {
          'contacts' : contacts,
         'filter_info' : filter_info,
        
          }
    return render(request,template_name,context)


def features(request):
    template_name = 'features.html'
    return render(request,template_name)

def add(request):
    template_name = 'add.html'
    c_form = commentForm()
    m_form = maleForm()   
    f_form = femaleForm()                     
    contact = Contact.objects.all()  
    if request.method =='POST':
        c_form = commentForm(request.POST)
        m_form = maleForm(request.POST)
        f_form = femaleForm(request.POST)
        if c_form.is_valid() and (m_form.is_valid() or f_form.is_valid()):
           
                username= c_form.cleaned_data.get('name')
                contact = c_form.save()     
                
                if 'female' in contact.gender:
                       
                        female = f_form.save(commit=False)
                        female.contact2 = contact
                        female.save()
                        messages.success(request, f"Form Submitted: {username}")
                        return redirect("success")
                else:
                        male = m_form.save(commit=False)
                        male.contact1 = contact
                        male.save()
                       
                        messages.success(request, f"Form Submitted: {username}")
                        return redirect("success")     
        else:     
                    c_form = commentForm()
                    m_form = maleForm()   
                    f_form = femaleForm()
                    
       
              
    context = {
      
        'c_form' : c_form,
        'm_form' : m_form,
        'f_form' : f_form,
        'contact' : contact,

    }

    return render(request , template_name , context)
    

def success(request):
    template_name = "add.html"
    form = commentForm()
    context = {"form" : form}
    return render(request , template_name  ,context)





def whatUpdate(request,pk):
    template_name = 'update-noti.html'
    contact = Contact.objects.get(id=pk)
    
    context = {
        'contact' : contact
    }

    return render(request,template_name,context)


# def contactUpdate(request,pk):
#     template_name = 'update.html'
#     contact = Contact.objects.get(pk=pk)
#     contact_form = commentForm(instance=contact)
#     if request.method == 'POST':
#         contact_form = commentForm(request.POST,instance=contact)
#         if contact_form.is_valid():
#             contact_form.save()
#             messages.success(request, "Contact Updated")
#             return redirect("info")         
#     else:     
#            contact_form = commentForm()      


#     context = {
#         'contact_form' : contact_form,
#         'contact' : contact

#     }

#     return render(request,template_name,context)



# def femaleUpdate(request,pk):
#     contact = Contact.objects.get(pk=pk)
  

#     female = Female.objects.get(pk=pk)
#     f_form = femaleForm(instance=female)
      

#     if request.method == 'POST':

#         f_form = femaleForm(request.POST,instance=female)

#         if f_form.is_valid():
#             females = f_form.save()
#             females.contact2 = female
#             females.save()
       
#             messages.success(request, "Measurement Updated for female")
#             return redirect('info')      
#         else:
#             f_form = femaleForm()
#             messages.success(request, "Error")

#     context = {

#         'contact' : contact,
#         'f_form' : f_form,
        
#     }
#     template_name = 'female-update.html' 
#     return render(request , template_name , context)



    

# def maleUpdate(request,pk):

#     contact = Contact.objects.get(pk=pk)
 
#     male = Male.objects.get(pk=pk)
#     m_form = maleForm(instance=male)  

#     if request.method == 'POST':
#         m_form = maleForm(request.POST,instance=male)
#         if m_form.is_valid(): 
#             males = m_form.save(commit=False)
#             males.contact1 = male
#             males.save()
#             messages.success(request, "Measurement Updated for male")
#             return redirect('info')      
#         else:
#              m_form = maleForm()
#              messages.success(request, "Error")
#     context = {

#         'm_form' : m_form,
#         'contact' : contact,
      
#     }
#     template_name = 'male-update.html' 
#     return render(request , template_name , context)





def contactUpdate(request,pk):
    template_name = 'female-update.html'
    contact = Contact.objects.get(pk=pk)

    female = Female.objects.all()
    c_form = commentForm(instance=contact)
   
    f_form = femaleForm(instance=contact.female)             
    
    if request.method =='POST':
        c_form = commentForm(request.POST,instance=contact)
   
        f_form = femaleForm(request.POST,instance=contact.female)
        if c_form.is_valid() and (f_form.is_valid()):
           
                contact = c_form.save()   
                username= c_form.cleaned_data.get('name')  
                
             
                       
                female = f_form.save(commit=False)
                female.contact2 = contact
                female.save()
                messages.success(request, f"Form Submitted: {username}")
     
                    
                      
                return redirect("info")     
        else:     
                    c_form = commentForm()
                  
                    f_form = femaleForm()
                    
       
              
    context = {
      
        'c_form' : c_form,
      
        'f_form' : f_form,
        'contact' : contact,

    }

    return render(request , template_name , context)
    




def contactUpdate1(request,pk):
    template_name = 'male-update.html'
    contact = Contact.objects.get(pk=pk)
    male = Male.objects.all()

    c_form = commentForm(instance=contact)
    m_form = maleForm(instance=contact.male)   
          
    
    if request.method =='POST':
        c_form = commentForm(request.POST,instance=contact)
        m_form = maleForm(request.POST,instance=contact.male)
     
        if c_form.is_valid() and (m_form.is_valid()):
                
                username= c_form.cleaned_data.get('name')
                contact = c_form.save()     
                
                if 'male' in contact.gender:
                       
        
                        male = m_form.save(commit=False)
                        male.contact1 = contact
                        male.save()
                       
                        messages.success(request, f"Form Submitted: {username}")
                        return redirect("info")    
                else:

                    return redirect('info') 





        else:     
                    c_form = commentForm()
                    m_form = maleForm()   
               
                    
       
              
    context = {
      
        'c_form' : c_form,
        'm_form' : m_form,

        'contact' : contact,

    }

    return render(request , template_name , context)
    





def delete(request,pk_test):
    template_name = 'delete.html'
    item = Contact.objects.get(id=pk_test)
    if request.method == 'POST':
     
        item.delete()
        return redirect('info')
   
    context = {

        'item' : item
    }

    return render(request,template_name,context)




def productDetail(request):
    template_name = 'product_detail.html'
    context = {}
    return render(request,template_name,context)


def listCart(request):
    template_name = 'cart.html'
    context = {}
    return render(request,template_name,context)


