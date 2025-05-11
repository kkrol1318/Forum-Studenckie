# 🧰 Bootstrap Guide – Poradnik dla zespołu

## 🎯 Cel:
Tworzysz nową podstronę? Skorzystaj z tego przewodnika, żeby:
- zbudować układ strony,
- dodać nagłówki, teksty, kolumny,
- używać gotowych komponentów jak karty, przyciski, alerty.

---

## 🧱 1. Struktura strony

Zawsze owijaj zawartość w `<div class="container">`, np.:

```html
{% extends "layout.html" %}

{% block title %}About Us{% endblock %}

{% block content %}
<div class="container">
    <h1>About Our Team</h1>
    <p>We are a group of Django enthusiasts...</p>
</div>
{% endblock %}
```

---

## 🪟 2. Podział na kolumny (grid system)

```html
<div class="row">
  <div class="col-md-6">
    <p>This is the left column</p>
  </div>
  <div class="col-md-6">
    <p>This is the right column</p>
  </div>
</div>
```

---

## 🧩 3. Karty (`card`)

```html
<div class="card" style="width: 18rem;">
  <div class="card-body">
    <h5 class="card-title">Team Member</h5>
    <p class="card-text">Short description here.</p>
  </div>
</div>
```

---

## 🧱 4. Alerty (np. do komunikatów)

```html
<div class="alert alert-success" role="alert">
  This is a success message!
</div>
```

---

## 🕹️ 5. Przyciski

```html
<button class="btn btn-primary">Click me</button>
<a href="#" class="btn btn-outline-secondary">Link Button</a>
```

---

## 📑 6. Lista (np. lista członków)

```html
<ul class="list-group">
  <li class="list-group-item">Member 1</li>
  <li class="list-group-item">Member 2</li>
</ul>
```

---

## 🎯 7. Ikony Bootstrap (opcjonalne, ale ładne)

Działa po dodaniu tej linijki do `layout.html`:

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons/font/bootstrap-icons.css">
```

Przykład użycia:

```html
<i class="bi bi-check-circle-fill text-success"></i> Success
```

---

## 📌 8. Praktyczne wskazówki

- **Nie używaj `style=""`** – wygląd ogarniemy później.
- **Nie wklejaj `<html>`, `<head>`, `<body>`** – masz `layout.html`.
- **Nie zmieniaj klas Bootstrap** – używaj ich „tak, jak są”.
- **Kopiuj z tego poradnika lub z [getbootstrap.com](https://getbootstrap.com/docs/5.3/getting-started/introduction/)**.