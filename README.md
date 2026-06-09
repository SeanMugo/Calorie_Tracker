# 🍎 Calorie Tracker – Daily Calorie Management Made Simple

A clean, fully responsive web application for tracking daily calorie intake, built with Django, Tailwind CSS, and JavaScript. Users can add food items, view consumed calories, delete entries, reset daily logs, and monitor progress toward their daily goals.

---

## 📖 Overview

Calorie Tracker is a Django-powered web app that helps users monitor their daily food consumption and calorie intake. The application provides an intuitive interface for logging meals, calculating total calories, and tracking progress against a daily goal of 2000 calories. All data is persisted in a database, allowing users to track their eating habits over time.

---

## 🍽️ Features

| Feature | Description |
|---------|-------------|
| **Add Food Items** | Simple form to add food name and calorie count |
| **View Food Log** | Display all food items consumed today with timestamps |
| **Delete Entries** | Remove individual food items with confirmation |
| **Total Calculation** | Automatically sums calories for the current day |
| **Reset Day** | Clear all food entries for today with one click |
| **Progress Bar** | Visual indicator showing progress toward 2000 calorie goal |
| **Responsive Design** | Works seamlessly on mobile, tablet, and desktop |
| **Toast Notifications** | Smooth success/error messages instead of browser alerts |

---

## 🛠️ Built With

| Technology | Purpose |
|------------|---------|
| **Django 4.2** | Backend web framework |
| **SQLite / PostgreSQL** | Database for storing food items |
| **Tailwind CSS** | Utility-first styling |
| **HTML5** | Page structure |
| **JavaScript** | Interactive elements and form validation |

---

## 🎨 Color Palette

| Color Name | Hex Code | Usage |
|------------|----------|-------|
| Orange Gradient | `#F97316 → #EC4899` | Total calories card, buttons |
| Green Gradient | `#10B981 → #14B89C` | Daily goal card, progress bar |
| White | `#FFFFFF` | Card backgrounds |
| Slate | `#F8FAFC` | Hover states, borders |
| Red | `#EF4444` | Delete buttons, reset actions |

---

## ✨ Core Functionality

### Add Food Items
Users enter a food name and calorie count. Input validation ensures positive calorie values and prevents empty submissions.

### View Daily Log
All food items for the current day are displayed with timestamps, showing individual calorie counts and a running total.

### Delete & Reset
Individual items can be removed with confirmation, or the entire day's log can be reset with a single click.

### Progress Tracking
A visual progress bar shows how close users are to reaching the 2000-calorie daily goal, with percentage displayed.

### Toast Notifications
User actions trigger styled notifications (success, error, info) instead of browser alerts.

---

## 🖥️ Local Setup

### Prerequisites
- Python 3.8+
- pip package manager

### Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/calorie-tracker.git
cd calorie-tracker

# Create virtual environment
python -m venv myenv

# Activate virtual environment
# Windows:
myenv\Scripts\activate
# Mac/Linux:
source myenv/bin/activate

# Install Django
pip install django

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create admin user (optional)
python manage.py createsuperuser

# Run development server
python manage.py runserver

```
---

## 📁 Project Deployment

- **Live URL:** [https://calorie-tracker-dtd8.onrender.com](https://calorie-tracker-dtd8.onrender.com)
- **Repository:** [https://github.com/SeanMugo/Calorie_Tracker](https://github.com/SeanMugo/Calorie_Tracker)

