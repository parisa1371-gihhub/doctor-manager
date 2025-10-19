# Doctor Manager - Patient Management System

A clean, modern, responsive dashboard website for a doctor's private patient management system built with Django and Tailwind CSS.

## Features

### 🏥 Dashboard
- Overview statistics (total patients, today's visits, weekly/monthly visits)
- Quick action buttons
- Recent visits and patients display
- Clean, medical-themed design

### 👥 Patient Management
- **Patient List**: Searchable table with patient information
- **Add Patient**: Complete form with personal and contact information
- **Patient Details**: Comprehensive patient profile with medical history
- **Add Visit**: Record new medical visits with diagnosis, prescription, and notes

### 🎨 Design Features
- **Responsive Layout**: Works on desktop and tablet
- **Sidebar Navigation**: Easy access to all features
- **Top Navbar**: Doctor information and logout
- **Tailwind CSS**: Modern, clean styling with medical theme
- **Lucide Icons**: Professional iconography
- **Form Validation**: Client and server-side validation

## Technology Stack

- **Backend**: Django 5.1.7
- **Frontend**: Tailwind CSS (via CDN)
- **Icons**: Lucide Icons
- **Database**: SQLite (development)
- **Template Engine**: Django Templates with inheritance

## Project Structure

```
doctormanager/
├── doctormanager/          # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── patients/               # Main app
│   ├── models.py          # Patient and Visit models
│   ├── views.py           # All views
│   ├── forms.py           # Django forms
│   ├── admin.py           # Admin interface
│   └── urls.py            # URL patterns
├── templates/             # HTML templates
│   ├── base.html          # Base template with layout
│   ├── dashboard.html     # Dashboard page
│   ├── patients.html      # Patient list
│   ├── add_patient.html   # Add patient form
│   ├── patient_detail.html # Patient details
│   └── add_visit.html     # Add visit form
├── static/                # Static files
│   └── css/
│       └── style.css      # Custom Tailwind styles
└── manage.py
```

## Installation & Setup

1. **Clone or download the project**
2. **Install dependencies** (if using virtual environment):
   ```bash
   pip install django
   ```

3. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

4. **Create superuser** (already created):
   - Username: `doctor`
   - Password: `doctor123`

5. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the application**:
   - Main dashboard: http://127.0.0.1:8000/
   - Admin interface: http://127.0.0.1:8000/admin/

## Usage

### Dashboard
- View statistics and recent activity
- Quick access to common actions
- Overview of recent patients and visits

### Patient Management
1. **Add Patient**: Click "Add Patient" to register new patients
2. **View Patients**: Browse all patients with search functionality
3. **Patient Details**: Click "View" to see complete patient information
4. **Add Visit**: Record medical visits with diagnosis and prescriptions

### Admin Interface
- Access at `/admin/` with doctor credentials
- Manage patients and visits
- View detailed records

## Models

### Patient Model
- Personal information (name, national ID, birth date, gender)
- Contact information (phone, address)
- Automatic age calculation
- Timestamps for creation and updates

### Visit Model
- Linked to patient
- Visit date (auto-generated)
- Medical information (diagnosis, prescription, notes)
- Next visit scheduling
- Timestamps for creation and updates

## Features Implemented

✅ **Responsive Design**: Works on desktop and tablet  
✅ **Sidebar Navigation**: Dashboard, Patients, Add Patient, Appointments, Settings  
✅ **Top Navbar**: Doctor name and logout functionality  
✅ **Dashboard Page**: Statistics, quick actions, recent activity  
✅ **Patients List**: Searchable table with patient information  
✅ **Add Patient Form**: Complete patient registration  
✅ **Patient Details**: Comprehensive patient profile  
✅ **Add Visit Form**: Medical visit recording  
✅ **Template Inheritance**: Clean, maintainable code structure  
✅ **Tailwind Styling**: Modern, medical-themed design  
✅ **Form Validation**: Both client and server-side  
✅ **Admin Interface**: Full CRUD operations  
✅ **Search Functionality**: Find patients quickly  
✅ **Responsive Tables**: Mobile-friendly data display  

## Customization

### Styling
- Modify `static/css/style.css` for custom Tailwind components
- Update color scheme in base template
- Customize icons by replacing Lucide icons

### Functionality
- Add new fields to models in `patients/models.py`
- Create new views in `patients/views.py`
- Add new templates following the existing pattern

## Security Notes

- Change default superuser password in production
- Set `DEBUG = False` in production
- Configure proper database settings
- Add CSRF protection (already included)
- Implement proper authentication if needed

## Browser Support

- Modern browsers (Chrome, Firefox, Safari, Edge)
- Responsive design for desktop and tablet
- Mobile-friendly interface

## License

This project is created for educational and demonstration purposes.

