// Translation system for Doctor Manager
const translations = {
    'fa': {
        // Navigation
        'داشبورد': 'داشبورد',
        'بیماران': 'بیماران',
        'افزودن بیمار': 'افزودن بیمار',
        'قرار ملاقات‌ها': 'قرار ملاقات‌ها',
        'تنظیمات': 'تنظیمات',
        'خروج': 'خروج',
        'اعلان‌ها': 'اعلان‌ها',
        
        // Dashboard
        'سیستم مدیریت بیماران': 'سیستم مدیریت بیماران',
        'نمای کلی از مطب شما': 'نمای کلی از مطب شما',
        'تعداد کل بیماران': 'تعداد کل بیماران',
        'ویزیت‌های امروز': 'ویزیت‌های امروز',
        'قرار ملاقات‌های نزدیک': 'قرار ملاقات‌های نزدیک',
        'بیماران جدید': 'بیماران جدید',
        'مشاهده همه': 'مشاهده همه',
        'افزودن بیمار جدید': 'افزودن بیمار جدید',
        'تعیین قرار ملاقات': 'تعیین قرار ملاقات',
        'مشاهده بیماران': 'مشاهده بیماران',
        'ویزیت‌های اخیر': 'ویزیت‌های اخیر',
        'بیماران اخیر': 'بیماران اخیر',
        
        // Common
        'نام': 'نام',
        'مشاهده': 'مشاهده',
        'ویرایش': 'ویرایش',
        'حذف': 'حذف',
        'ذخیره': 'ذخیره',
        'لغو': 'لغو',
        'جستجو': 'جستجو',
        'بازگشت به خانه': 'بازگشت به خانه',
        
        // Patient
        'اطلاعات شخصی': 'اطلاعات شخصی',
        'تاریخ تولد': 'تاریخ تولد',
        'جنسیت': 'جنسیت',
        'تلفن': 'تلفن',
        'آدرس': 'آدرس',
        'کد ملی': 'کد ملی',
        'مرد': 'مرد',
        'زن': 'زن',
        
        // Visit
        'تاریخ ویزیت بعدی': 'تاریخ ویزیت بعدی',
        'نسخه': 'نسخه',
        'یادداشت‌ها': 'یادداشت‌ها',
        'تشخیص': 'تشخیص',
        
        // Settings
        'زبان سیستم': 'زبان سیستم',
        'تم سیستم': 'تم سیستم',
        'فعال کردن اعلان‌ها': 'فعال کردن اعلان‌ها',
        'فارسی (Farsi)': 'فارسی (Farsi)',
        'English': 'English',
        'روشن': 'روشن',
        'تیره': 'تیره',
        'خودکار': 'خودکار',
        'اعمال': 'اعمال',
        'فعال': 'فعال',
        'غیرفعال': 'غیرفعال',
        
        // Messages
        'اطلاعات بیمار با موفقیت به‌روزرسانی شد!': 'اطلاعات بیمار با موفقیت به‌روزرسانی شد!',
        'ویزیت جدید با موفقیت ثبت شد!': 'ویزیت جدید با موفقیت ثبت شد!',
        'بیمار با موفقیت اضافه شد!': 'بیمار با موفقیت اضافه شد!',
        'زبان سیستم به': 'زبان سیستم به',
        'تغییر یافت.': 'تغییر یافت.',
        'اعلان‌ها': 'اعلان‌ها',
        'شدند.': 'شدند.',
    },
    
    'en': {
        // Navigation
        'داشبورد': 'Dashboard',
        'بیماران': 'Patients',
        'افزودن بیمار': 'Add Patient',
        'قرار ملاقات‌ها': 'Appointments',
        'تنظیمات': 'Settings',
        'خروج': 'Logout',
        'اعلان‌ها': 'Notifications',
        
        // Dashboard
        'سیستم مدیریت بیماران': 'Patient Management System',
        'نمای کلی از مطب شما': 'Overview of your clinic',
        'تعداد کل بیماران': 'Total Patients',
        'ویزیت‌های امروز': 'Today\'s Visits',
        'قرار ملاقات‌های نزدیک': 'Upcoming Appointments',
        'بیماران جدید': 'New Patients',
        'مشاهده همه': 'View All',
        'افزودن بیمار جدید': 'Add New Patient',
        'تعیین قرار ملاقات': 'Set Appointment',
        'مشاهده بیماران': 'View Patients',
        'ویزیت‌های اخیر': 'Recent Visits',
        'بیماران اخیر': 'Recent Patients',
        
        // Common
        'نام': 'Name',
        'مشاهده': 'View',
        'ویرایش': 'Edit',
        'حذف': 'Delete',
        'ذخیره': 'Save',
        'لغو': 'Cancel',
        'جستجو': 'Search',
        'بازگشت به خانه': 'Back to Home',
        
        // Patient
        'اطلاعات شخصی': 'Personal Information',
        'تاریخ تولد': 'Birth Date',
        'جنسیت': 'Gender',
        'تلفن': 'Phone',
        'آدرس': 'Address',
        'کد ملی': 'National ID',
        'مرد': 'Male',
        'زن': 'Female',
        
        // Visit
        'تاریخ ویزیت بعدی': 'Next Visit Date',
        'نسخه': 'Prescription',
        'یادداشت‌ها': 'Notes',
        'تشخیص': 'Diagnosis',
        
        // Settings
        'زبان سیستم': 'System Language',
        'تم سیستم': 'System Theme',
        'فعال کردن اعلان‌ها': 'Enable Notifications',
        'فارسی (Farsi)': 'Persian (Farsi)',
        'English': 'English',
        'روشن': 'Light',
        'تیره': 'Dark',
        'خودکار': 'Auto',
        'اعمال': 'Apply',
        'فعال': 'Active',
        'غیرفعال': 'Inactive',
        
        // Messages
        'اطلاعات بیمار با موفقیت به‌روزرسانی شد!': 'Patient information updated successfully!',
        'ویزیت جدید با موفقیت ثبت شد!': 'New visit registered successfully!',
        'بیمار با موفقیت اضافه شد!': 'Patient added successfully!',
        'زبان سیستم به': 'System language changed to',
        'تغییر یافت.': '.',
        'اعلان‌ها': 'notifications',
        'شدند.': '.',
    }
};

// Translation function
function translateText(text, language = 'fa') {
    if (translations[language] && translations[language][text]) {
        return translations[language][text];
    }
    return text; // Return original text if translation not found
}

// Apply translations to page
function applyTranslations(language = 'fa') {
    // Get all elements with data-translate attribute
    const elements = document.querySelectorAll('[data-translate]');
    
    elements.forEach(element => {
        const originalText = element.getAttribute('data-translate');
        const translatedText = translateText(originalText, language);
        element.textContent = translatedText;
    });
    
    // Update page direction
    if (language === 'fa') {
        document.documentElement.setAttribute('dir', 'rtl');
        document.documentElement.setAttribute('lang', 'fa');
    } else {
        document.documentElement.setAttribute('dir', 'ltr');
        document.documentElement.setAttribute('lang', 'en');
    }
}

// Change language function
function changeLanguage(language) {
    // Store language preference in session via AJAX
    fetch('/settings/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]')?.value || ''
        },
        body: `action=change_language&language=${language}`
    }).then(() => {
        // Apply translations immediately
        applyTranslations(language);
        
        // Show success message
        showMessage(`زبان سیستم به ${language === 'fa' ? 'فارسی' : 'انگلیسی'} تغییر یافت.`, 'success');
    }).catch(error => {
        console.error('Error changing language:', error);
        showMessage('خطا در تغییر زبان سیستم.', 'error');
    });
}

// Show message function
function showMessage(message, type = 'info') {
    // Create message element
    const messageDiv = document.createElement('div');
    messageDiv.className = `fixed top-4 right-4 p-4 rounded-lg shadow-lg z-50 ${
        type === 'success' ? 'bg-green-100 text-green-800 border border-green-200' :
        type === 'error' ? 'bg-red-100 text-red-800 border border-red-200' :
        'bg-blue-100 text-blue-800 border border-blue-200'
    }`;
    messageDiv.textContent = message;
    
    // Add to page
    document.body.appendChild(messageDiv);
    
    // Remove after 3 seconds
    setTimeout(() => {
        messageDiv.remove();
    }, 3000);
}

// Initialize translations on page load
document.addEventListener('DOMContentLoaded', function() {
    // Get language from session or default to 'fa'
    const currentLanguage = document.body.getAttribute('data-language') || 'fa';
    applyTranslations(currentLanguage);
    
    // Add event listeners to language change buttons
    document.querySelectorAll('[data-change-language]').forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const language = this.getAttribute('data-change-language');
            changeLanguage(language);
        });
    });
});
