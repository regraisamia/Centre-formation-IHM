// Utilitaires globaux pour l'application
class Utils {
    // Afficher des notifications toast
    static showToast(message, type = 'info', duration = 3000) {
        // Créer le conteneur de toasts s'il n'existe pas
        let toastContainer = document.getElementById('toast-container');
        if (!toastContainer) {
            toastContainer = document.createElement('div');
            toastContainer.id = 'toast-container';
            toastContainer.style.cssText = `
                position: fixed;
                top: 20px;
                right: 20px;
                z-index: 9999;
                max-width: 350px;
            `;
            document.body.appendChild(toastContainer);
        }

        // Créer le toast
        const toast = document.createElement('div');
        const bgColor = {
            'success': '#28a745',
            'error': '#dc3545',
            'warning': '#ffc107',
            'info': '#17a2b8'
        }[type] || '#17a2b8';

        toast.style.cssText = `
            background: ${bgColor};
            color: white;
            padding: 12px 20px;
            margin-bottom: 10px;
            border-radius: 6px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            transform: translateX(100%);
            transition: transform 0.3s ease;
            display: flex;
            align-items: center;
            justify-content: space-between;
        `;

        const icon = {
            'success': 'fas fa-check-circle',
            'error': 'fas fa-exclamation-circle',
            'warning': 'fas fa-exclamation-triangle',
            'info': 'fas fa-info-circle'
        }[type] || 'fas fa-info-circle';

        toast.innerHTML = `
            <div>
                <i class="${icon} me-2"></i>
                ${message}
            </div>
            <button onclick="this.parentElement.remove()" style="background:none;border:none;color:white;font-size:18px;cursor:pointer;margin-left:10px;">&times;</button>
        `;

        toastContainer.appendChild(toast);

        // Animation d'entrée
        setTimeout(() => {
            toast.style.transform = 'translateX(0)';
        }, 100);

        // Suppression automatique
        setTimeout(() => {
            toast.style.transform = 'translateX(100%)';
            setTimeout(() => {
                if (toast.parentElement) {
                    toast.remove();
                }
            }, 300);
        }, duration);
    }

    // Confirmer une action
    static confirm(message, callback) {
        if (confirm(message)) {
            callback();
        }
    }

    // Formater les nombres
    static formatNumber(number) {
        return new Intl.NumberFormat('fr-FR').format(number);
    }

    // Formater les dates
    static formatDate(date) {
        return new Intl.DateTimeFormat('fr-FR').format(new Date(date));
    }

    // Valider un email
    static isValidEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    }

    // Valider un téléphone marocain
    static isValidPhone(phone) {
        const re = /^(\+212|0)[5-7][0-9]{8}$/;
        return re.test(phone.replace(/\s/g, ''));
    }

    // Loader
    static showLoader(element) {
        const loader = document.createElement('div');
        loader.className = 'spinner-border spinner-border-sm me-2';
        loader.setAttribute('role', 'status');
        element.prepend(loader);
        element.disabled = true;
    }

    static hideLoader(element) {
        const loader = element.querySelector('.spinner-border');
        if (loader) loader.remove();
        element.disabled = false;
    }
}

// Fonctions globales pour les actions communes
function handleAjaxError(xhr) {
    let message = 'Une erreur est survenue';
    if (xhr.responseJSON && xhr.responseJSON.message) {
        message = xhr.responseJSON.message;
    } else if (xhr.status === 404) {
        message = 'Ressource non trouvée';
    } else if (xhr.status === 500) {
        message = 'Erreur serveur';
    }
    Utils.showToast(message, 'error');
}

// Initialisation au chargement de la page
document.addEventListener('DOMContentLoaded', function() {
    // Ajouter des animations aux cartes
    const cards = document.querySelectorAll('.card, .stat-card');
    cards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'all 0.3s ease';
        
        setTimeout(() => {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, index * 100);
    });

    // Améliorer les tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Auto-focus sur les premiers champs des modals
    const modals = document.querySelectorAll('.modal');
    modals.forEach(modal => {
        modal.addEventListener('shown.bs.modal', function() {
            const firstInput = modal.querySelector('input, select, textarea');
            if (firstInput) firstInput.focus();
        });
    });

    // Validation en temps réel des formulaires
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        const inputs = form.querySelectorAll('input[required], select[required], textarea[required]');
        inputs.forEach(input => {
            input.addEventListener('blur', function() {
                validateField(this);
            });
        });
    });

    // Recherche en temps réel
    const searchInputs = document.querySelectorAll('input[placeholder*="Rechercher"]');
    searchInputs.forEach(input => {
        let timeout;
        input.addEventListener('input', function() {
            clearTimeout(timeout);
            timeout = setTimeout(() => {
                // Ici vous pouvez ajouter la logique de recherche AJAX
                console.log('Recherche:', this.value);
            }, 500);
        });
    });
});

// Validation des champs
function validateField(field) {
    const value = field.value.trim();
    let isValid = true;
    let message = '';

    // Validation selon le type
    if (field.type === 'email' && value && !Utils.isValidEmail(value)) {
        isValid = false;
        message = 'Email invalide';
    } else if (field.type === 'tel' && value && !Utils.isValidPhone(value)) {
        isValid = false;
        message = 'Numéro de téléphone invalide';
    } else if (field.hasAttribute('required') && !value) {
        isValid = false;
        message = 'Ce champ est requis';
    }

    // Appliquer les styles
    if (isValid) {
        field.classList.remove('is-invalid');
        field.classList.add('is-valid');
    } else {
        field.classList.remove('is-valid');
        field.classList.add('is-invalid');
        
        // Afficher le message d'erreur
        let feedback = field.parentElement.querySelector('.invalid-feedback');
        if (!feedback) {
            feedback = document.createElement('div');
            feedback.className = 'invalid-feedback';
            field.parentElement.appendChild(feedback);
        }
        feedback.textContent = message;
    }

    return isValid;
}

// Fonction pour imprimer
function printPage() {
    window.print();
}

// Fonction pour exporter en PDF (nécessite une bibliothèque comme jsPDF)
function exportToPDF() {
    Utils.showToast('Fonctionnalité d\'export PDF en développement', 'info');
}

// Gestion des erreurs globales
window.addEventListener('error', function(e) {
    console.error('Erreur JavaScript:', e.error);
    Utils.showToast('Une erreur inattendue s\'est produite', 'error');
});

// Gestion des erreurs AJAX globales
document.addEventListener('ajaxError', function(e) {
    handleAjaxError(e.detail);
});