# 🧸 Plush Pals

**Plush Pals** is a product showcase web application built using Django. It features a handpicked collection of adorable, handcrafted plushies. While it does not include e-commerce functionality, users can explore various plush toy entries and submit feedback in the form of reviews and star ratings.

## 🌐 Live Demo

> _Coming Soon_ — Deployed on [Heroku/Vercel/Render] (add link when deployed)

## 🛠 Tech Stack

- **Frontend**: HTML5, CSS3
- **Backend**: Django (Python)
- **Database**: SQLite3 (development)
- **Other Tools**: Django Template Language (DTL), Django Forms

## II. Core Features

1. **🧸 Product Display:**

   - Showcases 8+ plush toys with images, names, prices, and descriptions.
   - Each product links to a detail page with extended information.

2. **⭐ User Feedback:**

   - Users can submit reviews and assign star ratings (1–5).
   - All feedback is displayed under the corresponding product in a blog-style layout.

3. **🛠 Admin Panel:**
   - Admin interface allows adding, editing, or deleting products.
   - All user-submitted reviews are listed in a feedback report section.

## 📁 Features Overview

### 🏠 Home Page

- Introduction to the seasonal collection (_Sakura Friends_)
- Navigation links: `Home`, `Shop`, `About`, `Contact`
- Clean, pastel-themed layout with the Plush Pals logo

### 🧸 Shop Page

- Features both “Featured Plushies” and “All Plushies”
- Product cards include image, name, price, and short description

### 📄 Product Detail Page

- Larger image with full description
- Displays average rating with star icons
- Includes customer reviews with name and text
- Interactive review form (Name, Rating, Review)

### 💌 Contact Page

- Contact info section: support email, phone number, and address
- “Send Us a Message” form to collect user input

### 🧵 About Page

- Tells the Plush Pals story
- Highlights values: Craftsmanship, Sustainability, Community

# Django Project Setup with Specific Dependencies

This guide outlines the steps to set up a Django project with the following dependencies:

- **Django 5.1.5**
- **Pillow 10.2.0**

---

## 🔧 Prerequisites

Make sure you have Python 3.10+ and `pip` installed. You can check with:

```bash
python --version
pip --version
```


### 1. Create a Virutal Environment (Recommended)
```bash
cd plushpals
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Requirements
```bash
pip3 install -r requirements.txt
```

### 3. Run the Server
```bash
./runserver.sh
# or
python3 manage.py migrate
python3 manage.py runserver
```

## 🔑 Admin Login
```bash
username: admin
email: admin@plushpals.com
password: Sunny42Moon!
```

## 📌 Credits

This project was developed as part of the **IS218 Final Project (Spring 2025)** at NJIT.

**Created by:**

- Justin Cordova
- Taryn Faccenda
- Jonathan Ocampo
- Katelyn Reyes
- Jasmin Rutter
