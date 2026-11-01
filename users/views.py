from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from users.forms import JoinForm, LoginForm

# Create your views here.


# from midterm/suduku project, subject to change
def join(request):
    if (request.method == "POST"):
        # POST - get the data from JoinForm
        # create a new join_form object from the request the users browser sent (submit)
        join_form = JoinForm(request.POST)
        # check if the form is valid using the rules of each field
        if (join_form.is_valid()):
            # Save form data to DB
            # User model is created and filled out with join_form
            user = join_form.save()

            # Encrypt the password
            # password is hashed, you cannot get it back after this
            user.set_password(user.password)
            # Save encrypted password to DB
            user.save()
            # Success! Redirect to home page.
            return redirect("/")
        else:
            # Form invalid, print errors to console
            # join_form now holds errors, along with previous typed fields that can be converted to html in our form
            page_data = { "join_form": join_form }
            return render(request, 'users/signup.html', page_data)
    else:
        # GET - show them the empty form
        page_data = { "join_form": JoinForm }
        return render(request, 'users/signup.html', page_data)

# from midterm project/sudoku, subject to change
def user_login(request):
    if (request.method == 'POST'):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # First get the username and password supplied
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            # Django's built-in authentication function:
            user = authenticate(username=username, password=password)
            # If we have a user
            if user:
                #Check it the account is active
                if user.is_active:
                    # Log the user in.
                    login(request,user)
                    # Send the user back to homepage
                    return redirect("/")
                else:
                    # If account is not active:
                    return HttpResponse("Your account is not active.")
            else:
                print("Someone tried to login and failed.")
                print("They used username: {} and password: {}".format(username,password))
                return render(request, 'users/login.html', {"login_form": LoginForm})
    else:
        #Nothing has been provided for username or password.
        return render(request, 'users/login.html', {"login_form": LoginForm})


# from midterm project subject to change
@login_required(login_url='/login/')    
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return redirect("/")
