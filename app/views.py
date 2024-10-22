from profile import Profile
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm, ProfileUpdateForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from .models import Post , Profile
from django.contrib import messages



class RegisterView(FormView):
    template_name = 'app/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # Save the user
        user = form.save()

        # Create a related profile
        Profile.objects.get_or_create(
            user=user,
            age=form.cleaned_data['age'],
            gender=form.cleaned_data['gender'],
            phone_number=form.cleaned_data['phone_number'],
            middle_name=form.cleaned_data['middle_name']
        )

        # Log the user in
        login(self.request, user)

        # Add success message
        messages.success(self.request, "Registration successful! You are now logged in.")

        # Redirect to the success URL
        return super().form_valid(form)

    def form_invalid(self, form):
        # Add error message when form is invalid
        messages.error(self.request, "There was an error in your registration. Please correct the errors below.")
        return super().form_invalid(form)

# Login View
class LoginView(FormView):
    template_name = 'app/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None, "Invalid username or password")
            return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context


@method_decorator(login_required, name='dispatch')
class ProfileView(DetailView):
    model = Profile
    template_name = 'app/profile.html'

    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.request.user)


@method_decorator(login_required, name='dispatch')
class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'app/edit_profile.html'

    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.request.user)


    def get_initial(self):
        initial = super().get_initial()
        user = self.request.user
        initial['username'] = user.username
        initial['first_name'] = user.first_name
        initial['last_name'] = user.last_name
        initial['email'] = user.email
        return initial

    def get_success_url(self):
        return reverse_lazy('profile')

    def form_valid(self, form):
        user = self.request.user


        user.username = form.cleaned_data['username']
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.email = form.cleaned_data['email']
        user.save()


        profile = form.save(commit=False)
        profile.user = user
        profile.save()

        return super().form_valid(form)


# Logout View
def logout_view(request):
    logout(request)
    return redirect('login')

def home(request):
    return render(request, 'app/home.html')



class HomePageView(ListView):
    model = Profile
    context_object_name = 'profiles'
    template_name = 'app/home.html'

    def get_queryset(self):

        return Profile.objects.all()

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

class ContactPageView(TemplateView):
    template_name = 'app/contact.html'

class BlogListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name ='app/blog_list.html'

class BlogDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'app/blog_detail.html'

class BlogCreateView(CreateView):
    model = Post
    fields = ['title', 'author', 'body','post_image','post_categories']
    template_name = 'app/blog_create.html'

class BlogUpdateView(UpdateView):
    model = Post
    fields = ['title', 'author', 'body','post_image','post_categories']
    template_name = 'app/blog_update.html'

    def get_success_url(self):
        return reverse_lazy('blog_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the author if required
        return super().form_valid(form)

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'app/blog_delete.html'
    success_url = reverse_lazy('blog')