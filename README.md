# Django Project with Tailwind CSS

This repository contains a Django project set up with Tailwind CSS for styling. Follow the instructions below to clone the repository and set up the project on your local machine.

## Prerequisites

Ensure you have the following installed:

- Python 3.8 or higher
- pip (Python package installer)
- Node.js (for Tailwind CSS)
- npm (Node package manager)

## Step 1: Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/HakashiKatake/Django-Project
cd DjangPractice
```

## Step 2: Set Up a Virtual Environment

1. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

## Step 3: Install Python Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

Make sure `requirements.txt` includes Django and django-tailwind.

## Step 4: Install Node.js Dependencies

1. Navigate to the static directory where your Tailwind CSS files are located (if applicable):

   ```bash
   cd static
   ```

2. Install Tailwind CSS and other Node.js dependencies:

   ```bash
   npm install
   ```

## Step 5: Configure Tailwind CSS

1. Initialize Tailwind CSS (if not already done):

   ```bash
   npx tailwindcss init
   ```

2. Ensure your `tailwind.config.js` file is set up correctly to include your templates and static files.

## Step 6: Run Tailwind CSS

Start the Tailwind CSS build process:

```bash
npx tailwindcss -i ./css/styles.css -o ./css/output.css --watch
```

## Step 7: Run Database Migrations

Run the following command to apply database migrations:

```bash
python manage.py migrate
```

## Step 8: Start the Django Development Server

Run the Django server:

```bash
python manage.py runserver
```

Open your browser and navigate to `http://127.0.0.1:8000/` to see your Django project with Tailwind CSS.

## Conclusion

You have successfully cloned and set up the Django project with Tailwind CSS. You can now start developing your application!