# Simple Product Showcase & Feedback Prototype

## I. Project Goal

The goal of this project is to create a Django-powered website where users can browse products, provide feedback, and allow administrators to manage products and view feedback reports. The platform will help management make product decisions based on user feedback.

## II. Core Features

1. **Product Display:**
   - List of 8+ products with details (name, description, image, price).
   - Individual product pages with deeper details and feedback options.

2. **User Feedback:**
   - Feedback mechanism with star ratings and comment boxes.
   - User reviews and comments displayed in a blog-style layout.

3. **Admin Panel:**
   - Admin login for managing products (add, edit, delete).
   - Feedback report listing all user comments.

## III. Project Requirements

1. **Models:**
   - `Product`: name, description, price, image.
   - `Feedback`: product (foreign key), rating, comment.

2. **Views:**
   - Display product list and individual details.
   - Handle feedback submissions.
   - Admin-protected view to display all feedback.

3. **Templates:**
   - Product list, product details, and feedback report templates.
   - Base template for layout consistency.

4. **Forms:**
   - Feedback form for users.

5. **Blog Features:**
   - Blog-like comments for each product page.

6. **Admin Panel:**
   - Register `Product` and `Feedback` models.

7. **Feedback Report:**
   - Admin-only report page showing all feedback.