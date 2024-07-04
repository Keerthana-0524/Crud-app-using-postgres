# views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile
from .forms import ProfileForm

def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, 'profiles/profile_list.html', {'profiles': profiles})

def profile_create(request):
    form = ProfileForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            profile = form.save()
            # Redirect to profile_detail for the newly created profile
            return redirect('profile_detail', pk=profile.pk)
    return render(request, 'profiles/profile_form.html', {'form': form})

def profile_update(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    form = ProfileForm(request.POST or None, instance=profile)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('profile_detail', pk=profile.pk)
    return render(request, 'profiles/profile_form.html', {'form': form})
    
def profile_delete(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        profile.delete()
        return redirect('profile_list')  # Redirect to profile_list after deletion
    # Handle GET request if needed
    return render(request, 'profiles/profile_delete.html', {'profile': profile})

def profile_detail(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    return render(request, 'profiles/profile_detail.html', {'profile': profile})
