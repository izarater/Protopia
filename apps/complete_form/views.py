from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from apps.complete_form.forms import *
from django.shortcuts import get_object_or_404

# Create your views here.
@login_required
def mainPage(request):
    context ={}
    # create object of form
    if request.method == 'POST':
        if request.POST['ContactoSeleccionado']:
            selectedContact = request.POST['ContactoSeleccionado']
        else:
            selectedContact = None
        # check if form data is valid
        request.session['selectedContact'] = selectedContact
        return redirect(secondPage)
    else:
        form = ContactoSelect(user_id=request.user.id)
        context['form']= form
        return render(request, 'mainPage.html',context)
def secondPage(request):
    context ={}
    if request.session['selectedContact']:
        selectedContact =  Contacto.objects.get(IdContacto = request.session['selectedContact'])
        form = ContactoForm(request.POST or None, instance = selectedContact)
    else:
        selectedContact = Contacto()
        request.session['selectedContact'] = selectedContact.IdContacto
        selectedContact.IdCreador = request.user
        form = ContactoForm(request.POST or None, instance=selectedContact)
    # check if form data is valid
    if form.is_valid():
        form.save()
        #request.session['selectedContact'] = selectedContact.IdContacto
        #request.session['selectedContact'] = selectedContact.Oficios.set(Oficio.NombreOficio)
        return redirect(mainPage)
    
    #form.Meta.widgets['Oficios'].set(Oficio.NombreOficio)
    context['form']= form
    return render(request, 'secondPage.html',context)

@login_required
def contact_delete(request):
    contactoAEliminar =  get_object_or_404(Contacto,IdContacto=request.session['selectedContact'])
    if request.method == 'POST':
        # delete the band from the database
        contactoAEliminar.delete()
        # redirect to the bands list
        return redirect(mainPage)
    return render(request,
                'contactDelete.html',
                {'contacto':contactoAEliminar})
            