// Modern Dashboard JavaScript Utilities - Enhanced & Responsive

// Utility object for common functions
const Utils = {
    // Toast notification system
    showToast: function(message, type = 'info', duration = 4000) {
        // Remove existing toasts
        const existingToasts = document.querySelectorAll('.toast');
        existingToasts.forEach(toast => toast.remove());
        
        // Create toast container if it doesn't exist
        let container = document.querySelector('.toast-container');
        if (!container) {
            container = document.createElement('div');
            container.className = 'toast-container position-fixed top-0 end-0 p-3';
            container.style.zIndex = '1055';
            document.body.appendChild(container);
        }
        
        // Create toast element
        const toast = document.createElement('div');
        toast.className = `toast align-items-center text-white bg-${type} border-0`;
        toast.setAttribute('role', 'alert');
        toast.innerHTML = `
            <div class="d-flex">
                <div class="toast-body">
                    <i class="fas fa-${this.getToastIcon(type)} me-2"></i>
                    ${message}
                </div>
                <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast"></button>
            </div>
        `;
        
        container.appendChild(toast);
        
        // Initialize and show toast
        const bsToast = new bootstrap.Toast(toast, { delay: duration });
        bsToast.show();
        
        // Remove toast after it's hidden
        toast.addEventListener('hidden.bs.toast', () => {
            toast.remove();
        });
    },
    
    getToastIcon: function(type) {
        const icons = {
            'success': 'check-circle',
            'danger': 'exclamation-triangle',
            'warning': 'exclamation-circle',
            'info': 'info-circle',
            'primary': 'bell'
        };
        return icons[type] || 'info-circle';
    },
    
    // Confirmation dialog
    confirm: function(message, callback) {
        if (confirm(message)) {
            callback(true);
        } else {
            callback(false);
        }
    },
    
    // Loading state for buttons
    setButtonLoading: function(button, loading = true) {
        if (loading) {
            button.classList.add('btn-loading');
            button.disabled = true;
            button.dataset.originalText = button.innerHTML;
            button.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>Chargement...';
        } else {
            button.classList.remove('btn-loading');
            button.disabled = false;
            button.innerHTML = button.dataset.originalText || button.innerHTML;
        }
    },
    
    // Format numbers with animation
    animateNumber: function(element, target, duration = 2000) {
        const start = parseInt(element.textContent) || 0;
        const increment = (target - start) / (duration / 16);
        let current = start;
        
        const timer = setInterval(() => {
            current += increment;
            if ((increment > 0 && current >= target) || (increment < 0 && current <= target)) {
                current = target;
                clearInterval(timer);
            }
            element.textContent = Math.floor(current);
        }, 16);
    },
    
    // Debounce function for search
    debounce: function(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    },
    
    // Format phone numbers
    formatPhone: function(phone) {
        const cleaned = phone.replace(/\D/g, '');
        if (cleaned.startsWith('212')) {
            return `+212 ${cleaned.slice(3, 4)} ${cleaned.slice(4, 6)} ${cleaned.slice(6, 8)} ${cleaned.slice(8, 10)} ${cleaned.slice(10, 12)}`;
        }
        return phone;
    },
    
    // Validate Moroccan CIN
    validateCIN: function(cin) {
        const cinRegex = /^[A-Z]{1,2}\d{1,6}$/;
        return cinRegex.test(cin.toUpperCase());
    },
    
    // Get Moroccan cities
    getMoroccanCities: function() {
        return [
            'Casablanca', 'Rabat', 'Fès', 'Marrakech', 'Agadir', 'Tanger',
            'Meknès', 'Oujda', 'Kenitra', 'Tétouan', 'Safi', 'Mohammedia',
            'Khouribga', 'El Jadida', 'Béni Mellal', 'Nador'
        ];
    }
};

// Dashboard specific functions
const Dashboard = {
    // Initialize dashboard
    init: function() {
        this.initSidebar();
        this.initStatCards();
        this.initCharts();
        this.initSearch();
        this.initResponsive();
    },
    
    // Initialize sidebar
    initSidebar: function() {
        const sidebarLinks = document.querySelectorAll('.sidebar .nav-link');
        const currentPath = window.location.pathname;
        
        sidebarLinks.forEach(link => {
            if (link.getAttribute('href') === currentPath) {
                link.classList.add('active');
            }
            
            link.addEventListener('click', function(e) {
                // Remove active class from all links
                sidebarLinks.forEach(l => l.classList.remove('active'));
                // Add active class to clicked link
                this.classList.add('active');
            });
        });
    },
    
    // Initialize stat cards with animation
    initStatCards: function() {
        const statNumbers = document.querySelectorAll('.stat-number[data-target]');
        
        // Intersection Observer for animation trigger
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const target = parseInt(entry.target.dataset.target);
                    Utils.animateNumber(entry.target, target);
                    observer.unobserve(entry.target);
                }
            });
        });
        
        statNumbers.forEach(element => {
            observer.observe(element);
        });
    },
    
    // Initialize charts
    initCharts: function() {
        // Only initialize if Chart.js is available and canvas exists
        if (typeof Chart !== 'undefined') {
            const chartCanvas = document.getElementById('inscriptionsChart');
            if (chartCanvas) {
                this.createInscriptionsChart(chartCanvas);
            }
        }
    },
    
    // Create inscriptions chart
    createInscriptionsChart: function(canvas) {
        const ctx = canvas.getContext('2d');
        new Chart(ctx, {
            type: 'line',
            data: {
                labels: ['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Jun', 'Jul', 'Aoû', 'Sep', 'Oct', 'Nov', 'Déc'],
                datasets: [{
                    label: 'Inscriptions',
                    data: [12, 19, 15, 25, 22, 30, 28, 35, 32, 40, 38, 45],
                    borderColor: '#2E8B57',
                    backgroundColor: 'rgba(46, 139, 87, 0.1)',
                    borderWidth: 3,
                    fill: true,
                    tension: 0.4,
                    pointBackgroundColor: '#2E8B57',
                    pointBorderColor: '#fff',
                    pointBorderWidth: 2,
                    pointRadius: 5
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        display: false
                    },
                    tooltip: {
                        backgroundColor: 'rgba(46, 139, 87, 0.9)',
                        titleColor: '#fff',
                        bodyColor: '#fff',
                        borderColor: '#2E8B57',
                        borderWidth: 1
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        grid: {
                            color: 'rgba(0, 0, 0, 0.1)'
                        },
                        ticks: {
                            color: '#666'
                        }
                    },
                    x: {
                        grid: {
                            display: false
                        },
                        ticks: {
                            color: '#666'
                        }
                    }
                },
                interaction: {
                    intersect: false,
                    mode: 'index'
                }
            }
        });
    },
    
    // Initialize search functionality
    initSearch: function() {
        const searchInput = document.getElementById('searchInput');
        if (searchInput) {
            const debouncedSearch = Utils.debounce(this.performSearch, 300);
            searchInput.addEventListener('input', debouncedSearch);
        }
    },
    
    // Perform search
    performSearch: function(event) {
        const searchTerm = event.target.value.toLowerCase();
        const items = document.querySelectorAll('.student-item, .formation-item, .trainer-item');
        
        items.forEach(item => {
            const text = item.textContent.toLowerCase();
            if (text.includes(searchTerm)) {
                item.style.display = 'block';
                item.style.animation = 'fadeInUp 0.3s ease-out';
            } else {
                item.style.display = 'none';
            }
        });
        
        // Show no results message if needed
        const visibleItems = Array.from(items).filter(item => item.style.display !== 'none');
        if (visibleItems.length === 0 && searchTerm.length > 0) {
            Utils.showToast('Aucun résultat trouvé', 'warning');
        }
    },
    
    // Initialize responsive features
    initResponsive: function() {
        // Mobile sidebar toggle
        const sidebarToggle = document.querySelector('[data-bs-toggle="sidebar"]');
        const sidebar = document.querySelector('.sidebar');
        
        if (sidebarToggle && sidebar) {
            sidebarToggle.addEventListener('click', () => {
                sidebar.classList.toggle('show');
            });
        }
        
        // Close sidebar on mobile when clicking outside
        document.addEventListener('click', (e) => {
            if (window.innerWidth <= 991.98) {
                if (!sidebar.contains(e.target) && !sidebarToggle.contains(e.target)) {
                    sidebar.classList.remove('show');
                }
            }
        });
        
        // Handle window resize
        window.addEventListener('resize', () => {
            if (window.innerWidth > 991.98) {
                sidebar.classList.remove('show');
            }
        });
    }
};

// Form validation utilities
const FormValidator = {
    // Validate student form
    validateStudentForm: function(form) {
        const errors = [];
        
        // Required fields
        const requiredFields = form.querySelectorAll('[required]');
        requiredFields.forEach(field => {
            if (!field.value.trim()) {
                errors.push(`Le champ ${field.previousElementSibling.textContent} est requis`);
                field.classList.add('is-invalid');
            } else {
                field.classList.remove('is-invalid');
            }
        });
        
        // CIN validation
        const cinField = form.querySelector('input[name="cin"]');
        if (cinField && cinField.value && !Utils.validateCIN(cinField.value)) {
            errors.push('Format CIN invalide (ex: A123456)');
            cinField.classList.add('is-invalid');
        }
        
        // Email validation
        const emailField = form.querySelector('input[type="email"]');
        if (emailField && emailField.value) {
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(emailField.value)) {
                errors.push('Format email invalide');
                emailField.classList.add('is-invalid');
            }
        }
        
        // Phone validation
        const phoneField = form.querySelector('input[type="tel"]');
        if (phoneField && phoneField.value) {
            const phoneRegex = /^(\+212|0)[5-7]\d{8}$/;
            if (!phoneRegex.test(phoneField.value.replace(/\s/g, ''))) {
                errors.push('Format téléphone invalide (+212 6 12 34 56 78)');
                phoneField.classList.add('is-invalid');
            }
        }
        
        return errors;
    },
    
    // Show validation errors
    showErrors: function(errors) {
        if (errors.length > 0) {
            const errorMessage = errors.join('\n');
            Utils.showToast(errorMessage, 'danger', 6000);
            return false;
        }
        return true;
    }
};

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    Dashboard.init();
    
    // Initialize AOS if available
    if (typeof AOS !== 'undefined') {
        AOS.init({
            duration: 600,
            easing: 'ease-out',
            once: true,
            offset: 50
        });
    }
    
    // Initialize tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
    
    // Initialize popovers
    const popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });
    
    // Show welcome message
    setTimeout(() => {
        Utils.showToast('Bienvenue dans votre centre de formation!', 'success');
    }, 1000);
});

// Export utilities for global use
window.Utils = Utils;
window.Dashboard = Dashboard;
window.FormValidator = FormValidator;