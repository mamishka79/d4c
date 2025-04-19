## ✅ **Project: Mini Social Platform**

A simple Django web application where users can:
- Register and log in
- Create a profile with avatar and bio
- Write posts
- Comment on others’ posts
- Reset password via email

---

## 👥 **Team**
- **Amir** – Backend, models, logic, GitHub manager  
- **Alisher** – Frontend, templates, visual design  
- **Shazia** – Authentication, email reset, deployment  

---

## 📆 Project Plan with Task Distribution

---

### 🔹 PHASE 1 – Project Setup

#### ✅ Amir
- Create Django project: `django-admin startproject core`
- Create 2 apps:  
  - `users` – for profile and registration  
  - `blog` – for posts and comments

#### 💡 How:
```bash
django-admin startproject core
cd core
python manage.py startapp users
python manage.py startapp blog
```

- Add apps to `settings.py` in `INSTALLED_APPS`

- Push project to GitHub and invite team

---

### 🔹 PHASE 2 – Database Models

#### ✅ Amir
Create 3 models:

1. **Profile** (`users/models.py`)
```python
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
```

2. **Post** (`blog/models.py`)
```python
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
```

3. **Comment** (`blog/models.py`)
```python
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
```

#### 💡 How:
```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 🔹 PHASE 3 – Templates and Views

#### ✅ Alisher

1. Create templates folder:
```
core/
├── templates/
    ├── base.html
    ├── post_list.html
    ├── post_detail.html
    ├── post_form.html
    ├── comment_form.html
    ├── profile.html
```

2. Add `base.html` with Bootstrap connected  
3. Use `{% extends "base.html" %}` in all other templates  
4. Add navigation bar with links: home, login, logout, create post  

#### 💡 How:
- Create `templates` folder inside `core`
- Use Django template syntax:
```html
{% for post in posts %}
  <h2>{{ post.title }}</h2>
  <p>{{ post.content }}</p>
{% endfor %}
```

---

### 🔹 PHASE 4 – Authentication

#### ✅ Shazia

1. Set up Django built-in **login**, **register**, and **logout**
2. Create views and templates:
```
users/
├── templates/registration/
    ├── login.html
    ├── register.html
```

3. Add URLs for login/register/logout
4. Add password reset with email (SMTP or console backend)

#### 💡 How:
In `settings.py`:
```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

In `urls.py`:
```python
from django.contrib.auth import views as auth_views

urlpatterns += [
  path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
  path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]
```

---

### 🔹 PHASE 5 – CRUD Logic

#### ✅ Amir

- Create views for:
  - Listing posts (`PostListView`)
  - Detail of post
  - Creating new post
  - Editing/deleting post (only for the author)
  - Adding comment
- Use class-based or function-based views

#### 💡 How:
```python
from django.contrib.auth.decorators import login_required

@login_required
def post_create(request):
    ...
```

Use `get_object_or_404(Post, id=id)` for safe access.

---

### 🔹 PHASE 6 – Deployment

#### ✅ Alisher

- Create PythonAnywhere account
- Deploy the project:
  - Upload files or connect GitHub repo
  - Set static/media paths
  - Run migrations
  - Test live link

---

### 🔹 PHASE 7 – GitHub & Reporting

#### ✅ Shazia

- Add teacher to GitHub repo
- Create Excel file:
  - Team member names
  - GitHub repo link
  - Project link (PythonAnywhere)

---

## ✅ Summary – Who does what

| Team Member | Tasks |
|-------------|-------|
| **Amir** | Django setup, models, CRUD views, GitHub management |
| **Alisher** | HTML templates, Bootstrap design, page layout |
| **Shazia** | Auth, password reset, deployment, documentation |

---
