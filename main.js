// SR Travels - Enhanced Bus Booking System JavaScript
// Version 2.0 - Complete Rebuild

'use strict';

// Global variables
let currentUser = null;
let bookingData = {};
let selectedSeats = [];
let paymentGateway = 'razorpay';

// Initialize application
document.addEventListener('DOMContentLoaded', function() {
    initializeApp();
});

function initializeApp() {
    // Initialize components
    initializeFormValidation();
    initializeTooltips();
    initializeModals();
    initializeNotifications();
    initializeDatePickers();
    initializeSearchAutocomplete();
    
    // Load user session
    loadUserSession();
    
    // Initialize page-specific functionality
    const currentPage = getCurrentPage();
    switch(currentPage) {
        case 'index':
            initializeHomePage();
            break;
        case 'search-buses':
            initializeSearchPage();
            break;
        case 'seat-selection':
            initializeSeatSelection();
            break;
        case 'payment':
            initializePaymentPage();
            break;
        case 'user-dashboard':
            initializeUserDashboard();
            break;
        case 'admin-dashboard':
            initializeAdminDashboard();
            break;
    }
}

// Utility Functions
function getCurrentPage() {
    const path = window.location.pathname;
    const page = path.split('/').pop().split('.')[0];
    return page || 'index';
}

function showLoading(message = 'Loading...') {
    const overlay = document.getElementById('loadingOverlay');
    if (overlay) {
        overlay.querySelector('p').textContent = message;
        overlay.style.display = 'flex';
    }
}

function hideLoading() {
    const overlay = document.getElementById('loadingOverlay');
    if (overlay) {
        overlay.style.display = 'none';
    }
}

function showNotification(message, type = 'info', duration = 5000) {
    const notification = document.createElement('div');
    notification.className = `alert alert-${type} alert-dismissible fade show notification-toast`;
    notification.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    // Add to notification container or body
    const container = document.querySelector('.notification-container') || document.body;
    container.appendChild(notification);
    
    // Auto remove after duration
    setTimeout(() => {
        if (notification.parentNode) {
            notification.remove();
        }
    }, duration);
}

function formatCurrency(amount) {
    return new Intl.NumberFormat('en-IN', {
        style: 'currency',
        currency: 'INR'
    }).format(amount);
}

function formatDate(date, format = 'dd/mm/yyyy') {
    const d = new Date(date);
    const day = String(d.getDate()).padStart(2, '0');
    const month = String(d.getMonth() + 1).padStart(2, '0');
    const year = d.getFullYear();
    
    switch(format) {
        case 'dd/mm/yyyy':
            return `${day}/${month}/${year}`;
        case 'yyyy-mm-dd':
            return `${year}-${month}-${day}`;
        case 'readable':
            return d.toLocaleDateString('en-IN', { 
                weekday: 'long', 
                year: 'numeric', 
                month: 'long', 
                day: 'numeric' 
            });
        default:
            return d.toLocaleDateString();
    }
}

function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

function validatePhone(phone) {
    const re = /^[6-9]\d{9}$/;
    return re.test(phone.replace(/\D/g, ''));
}

// API Functions
async function apiCall(endpoint, method = 'GET', data = null) {
    const config = {
        method: method,
        headers: {
            'Content-Type': 'application/json',
            'X-Requested-With': 'XMLHttpRequest'
        }
    };
    
    if (data && method !== 'GET') {
        config.body = JSON.stringify(data);
    }
    
    try {
        const response = await fetch(`api/${endpoint}`, config);
        const result = await response.json();
        
        if (!response.ok) {
            throw new Error(result.message || 'API request failed');
        }
        
        return result;
    } catch (error) {
        console.error('API Error:', error);
        throw error;
    }
}

// User Session Management
function loadUserSession() {
    const userData = sessionStorage.getItem('userData');
    if (userData) {
        currentUser = JSON.parse(userData);
        updateUserInterface();
    }
}

function updateUserInterface() {
    if (currentUser) {
        // Update user-specific UI elements
        const userElements = document.querySelectorAll('[data-user-name]');
        userElements.forEach(el => {
            el.textContent = currentUser.full_name;
        });
        
        const loginElements = document.querySelectorAll('.login-required');
        loginElements.forEach(el => el.style.display = 'block');
        
        const guestElements = document.querySelectorAll('.guest-only');
        guestElements.forEach(el => el.style.display = 'none');
    }
}

// Form Validation
function initializeFormValidation() {
    const forms = document.querySelectorAll('.needs-validation');
    forms.forEach(form => {
        form.addEventListener('submit', function(event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        });
    });
}

// Initialize Components
function initializeTooltips() {
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
}

function initializeModals() {
    // Auto-focus first input in modals
    const modals = document.querySelectorAll('.modal');
    modals.forEach(modal => {
        modal.addEventListener('shown.bs.modal', function() {
            const firstInput = modal.querySelector('input, select, textarea');
            if (firstInput) {
                firstInput.focus();
            }
        });
    });
}

function initializeNotifications() {
    // Create notification container if it doesn't exist
    if (!document.querySelector('.notification-container')) {
        const container = document.createElement('div');
        container.className = 'notification-container position-fixed top-0 end-0 p-3';
        container.style.zIndex = '1060';
        document.body.appendChild(container);
    }
}

function initializeDatePickers() {
    const dateInputs = document.querySelectorAll('input[type="date"]');
    dateInputs.forEach(input => {
        // Set minimum date to today
        if (input.hasAttribute('data-min-today')) {
            input.min = new Date().toISOString().split('T')[0];
        }
        
        // Set maximum date
        if (input.hasAttribute('data-max-days')) {
            const maxDays = parseInt(input.getAttribute('data-max-days'));
            const maxDate = new Date();
            maxDate.setDate(maxDate.getDate() + maxDays);
            input.max = maxDate.toISOString().split('T')[0];
        }
    });
}

function initializeSearchAutocomplete() {
    const cityInputs = document.querySelectorAll('.city-autocomplete');
    cityInputs.forEach(input => {
        let timeout;
        input.addEventListener('input', function() {
            clearTimeout(timeout);
            timeout = setTimeout(() => {
                searchCities(this.value, this);
            }, 300);
        });
    });
}

async function searchCities(query, inputElement) {
    if (query.length < 2) return;
    
    try {
        const response = await apiCall(`search-cities.php?q=${encodeURIComponent(query)}`);
        if (response.success) {
            showCityDropdown(response.data, inputElement);
        }
    } catch (error) {
        console.error('City search error:', error);
    }
}

function showCityDropdown(cities, inputElement) {
    // Remove existing dropdown
    const existingDropdown = inputElement.parentNode.querySelector('.city-dropdown');
    if (existingDropdown) {
        existingDropdown.remove();
    }
    
    if (cities.length === 0) return;
    
    // Create dropdown
    const dropdown = document.createElement('div');
    dropdown.className = 'city-dropdown list-group position-absolute w-100';
    dropdown.style.zIndex = '1000';
    dropdown.style.top = '100%';
    
    cities.forEach(city => {
        const item = document.createElement('button');
        item.className = 'list-group-item list-group-item-action';
        item.textContent = city.name;
        item.addEventListener('click', function() {
            inputElement.value = city.name;
            dropdown.remove();
        });
        dropdown.appendChild(item);
    });
    
    inputElement.parentNode.style.position = 'relative';
    inputElement.parentNode.appendChild(dropdown);
    
    // Close dropdown when clicking outside
    document.addEventListener('click', function(e) {
        if (!inputElement.parentNode.contains(e.target)) {
            dropdown.remove();
        }
    }, { once: true });
}

// Page-specific Initializations
function initializeHomePage() {
    // Initialize hero slider if exists
    const heroSlider = document.querySelector('.hero-slider');
    if (heroSlider) {
        // Initialize slider functionality
    }
    
    // Initialize offer countdown timers
    initializeCountdownTimers();
    
    // Initialize testimonials slider
    initializeTestimonialsSlider();
}

function initializeSearchPage() {
    // Load search results if parameters exist
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.has('from') && urlParams.has('to') && urlParams.has('date')) {
        const searchData = {
            from: urlParams.get('from'),
            to: urlParams.get('to'),
            date: urlParams.get('date'),
            return_date: urlParams.get('return_date')
        };
        searchBuses(searchData);
    }
    
    // Initialize filters
    initializeSearchFilters();
}

function initializeSeatSelection() {
    // Load bus layout and seat availability
    loadSeatLayout();
    
    // Initialize seat selection handlers
    initializeSeatHandlers();
}

function initializePaymentPage() {
    // Initialize payment gateway options
    initializePaymentGateways();
    
    // Load booking summary
    loadBookingSummary();
}

function initializeUserDashboard() {
    // Load user bookings
    loadUserBookings();
    
    // Initialize dashboard widgets
    initializeDashboardWidgets();
}

function initializeAdminDashboard() {
    // Load admin statistics
    loadAdminStats();
    
    // Initialize admin charts
    initializeAdminCharts();
}

// Search Functionality
async function searchBuses(searchData) {
    showLoading('Searching buses...');
    
    try {
        const response = await apiCall('search-buses.php', 'POST', searchData);
        if (response.success) {
            displaySearchResults(response.data);
        } else {
            showNotification(response.message, 'warning');
        }
    } catch (error) {
        showNotification('Search failed. Please try again.', 'danger');
    } finally {
        hideLoading();
    }
}

function displaySearchResults(buses) {
    const container = document.getElementById('searchResults');
    if (!container) return;
    
    if (buses.length === 0) {
        container.innerHTML = `
            <div class="text-center py-5">
                <i class="fas fa-bus fa-3x text-muted mb-3"></i>
                <h4>No buses found</h4>
                <p class="text-muted">Try adjusting your search criteria</p>
            </div>
        `;
        return;
    }
    
    container.innerHTML = buses.map(bus => `
        <div class="bus-card card mb-3">
            <div class="card-body">
                <div class="row align-items-center">
                    <div class="col-md-3">
                        <h5 class="bus-name">${bus.bus_name}</h5>
                        <p class="bus-type text-muted">${bus.bus_type}</p>
                    </div>
                    <div class="col-md-2">
                        <div class="departure-time">
                            <strong>${bus.departure_time}</strong>
                            <small class="d-block text-muted">${bus.from_city}</small>
                        </div>
                    </div>
                    <div class="col-md-2">
                        <div class="duration text-center">
                            <i class="fas fa-clock text-primary"></i>
                            <span>${bus.duration}</span>
                        </div>
                    </div>
                    <div class="col-md-2">
                        <div class="arrival-time">
                            <strong>${bus.arrival_time}</strong>
                            <small class="d-block text-muted">${bus.to_city}</small>
                        </div>
                    </div>
                    <div class="col-md-2">
                        <div class="price text-end">
                            <h4 class="text-success">${formatCurrency(bus.fare)}</h4>
                            <small class="text-muted">${bus.available_seats} seats left</small>
                        </div>
                    </div>
                    <div class="col-md-1">
                        <button class="btn btn-primary" onclick="selectBus(${bus.id})">
                            Select
                        </button>
                    </div>
                </div>
            </div>
        </div>
    `).join('');
}

// Seat Selection
function loadSeatLayout() {
    const busId = new URLSearchParams(window.location.search).get('bus_id');
    const travelDate = new URLSearchParams(window.location.search).get('date');
    
    if (!busId || !travelDate) {
        showNotification('Invalid booking parameters', 'danger');
        return;
    }
    
    apiCall(`get-seat-layout.php?bus_id=${busId}&date=${travelDate}`)
        .then(response => {
            if (response.success) {
                renderSeatLayout(response.data);
            }
        })
        .catch(error => {
            showNotification('Failed to load seat layout', 'danger');
        });
}

function renderSeatLayout(seatData) {
    const container = document.getElementById('seatLayout');
    if (!container) return;
    
    // Render seat layout based on bus type
    const { seats, bus_type } = seatData;
    
    if (bus_type === 'seater') {
        renderSeaterLayout(seats, container);
    } else {
        renderSleeperLayout(seats, container);
    }
}

function renderSeaterLayout(seats, container) {
    const rows = Math.ceil(seats.length / 4);
    let html = '<div class="seater-layout">';
    
    for (let row = 0; row < rows; row++) {
        html += '<div class="seat-row">';
        for (let col = 0; col < 4; col++) {
            const seatIndex = row * 4 + col;
            if (seatIndex < seats.length) {
                const seat = seats[seatIndex];
                html += `
                    <div class="seat ${seat.is_available ? 'available' : 'occupied'}" 
                         data-seat="${seat.seat_number}" 
                         data-price="${seat.price}">
                        ${seat.seat_number}
                    </div>
                `;
            }
            if (col === 1) html += '<div class="aisle"></div>';
        }
        html += '</div>';
    }
    
    html += '</div>';
    container.innerHTML = html;
}

function renderSleeperLayout(seats, container) {
    // Similar implementation for sleeper layout
    // This would be more complex with upper/lower berths
    container.innerHTML = '<div class="sleeper-layout">Sleeper layout implementation</div>';
}

function initializeSeatHandlers() {
    document.addEventListener('click', function(e) {
        if (e.target.classList.contains('seat') && e.target.classList.contains('available')) {
            toggleSeat(e.target);
        }
    });
}

function toggleSeat(seatElement) {
    const seatNumber = seatElement.dataset.seat;
    const seatPrice = parseFloat(seatElement.dataset.price);
    
    if (seatElement.classList.contains('selected')) {
        // Deselect seat
        seatElement.classList.remove('selected');
        selectedSeats = selectedSeats.filter(seat => seat.number !== seatNumber);
    } else {
        // Select seat (limit to 6 seats)
        if (selectedSeats.length >= 6) {
            showNotification('Maximum 6 seats can be selected', 'warning');
            return;
        }
        
        seatElement.classList.add('selected');
        selectedSeats.push({
            number: seatNumber,
            price: seatPrice
        });
    }
    
    updateBookingSummary();
}

function updateBookingSummary() {
    const summaryContainer = document.getElementById('bookingSummary');
    if (!summaryContainer) return;
    
    const totalAmount = selectedSeats.reduce((sum, seat) => sum + seat.price, 0);
    const seatNumbers = selectedSeats.map(seat => seat.number).join(', ');
    
    summaryContainer.innerHTML = `
        <div class="booking-summary-card">
            <h5>Booking Summary</h5>
            <div class="summary-item">
                <span>Selected Seats:</span>
                <span>${seatNumbers || 'None'}</span>
            </div>
            <div class="summary-item">
                <span>Number of Seats:</span>
                <span>${selectedSeats.length}</span>
            </div>
            <div class="summary-item total">
                <span>Total Amount:</span>
                <span>${formatCurrency(totalAmount)}</span>
            </div>
            <button class="btn btn-primary w-100 mt-3" 
                    ${selectedSeats.length === 0 ? 'disabled' : ''} 
                    onclick="proceedToPayment()">
                Proceed to Payment
            </button>
        </div>
    `;
}

// Payment Processing
function initializePaymentGateways() {
    const gatewayOptions = document.querySelectorAll('input[name="payment_gateway"]');
    gatewayOptions.forEach(option => {
        option.addEventListener('change', function() {
            paymentGateway = this.value;
            updatePaymentForm();
        });
    });
}

function updatePaymentForm() {
    const paymentForm = document.getElementById('paymentForm');
    if (!paymentForm) return;
    
    // Update form based on selected gateway
    switch(paymentGateway) {
        case 'razorpay':
            showRazorpayForm();
            break;
        case 'paytm':
            showPaytmForm();
            break;
        case 'phonepe':
            showPhonePeForm();
            break;
        default:
            showDefaultForm();
    }
}

function processPayment() {
    if (!validatePaymentForm()) {
        return;
    }
    
    showLoading('Processing payment...');
    
    const paymentData = {
        gateway: paymentGateway,
        amount: bookingData.totalAmount,
        booking_data: bookingData
    };
    
    apiCall('process-payment.php', 'POST', paymentData)
        .then(response => {
            if (response.success) {
                initiatePaymentGateway(response.data);
            } else {
                showNotification(response.message, 'danger');
            }
        })
        .catch(error => {
            showNotification('Payment processing failed', 'danger');
        })
        .finally(() => {
            hideLoading();
        });
}

// Utility Functions for Specific Features
function initializeCountdownTimers() {
    const timers = document.querySelectorAll('.countdown-timer');
    timers.forEach(timer => {
        const endDate = new Date(timer.dataset.endDate);
        updateCountdown(timer, endDate);
        
        setInterval(() => {
            updateCountdown(timer, endDate);
        }, 1000);
    });
}

function updateCountdown(element, endDate) {
    const now = new Date().getTime();
    const distance = endDate.getTime() - now;
    
    if (distance < 0) {
        element.innerHTML = 'EXPIRED';
        return;
    }
    
    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);
    
    element.innerHTML = `${days}d ${hours}h ${minutes}m ${seconds}s`;
}

function initializeTestimonialsSlider() {
    // Initialize testimonials slider if library is available
    const slider = document.querySelector('.testimonials-slider');
    if (slider && typeof Swiper !== 'undefined') {
        new Swiper(slider, {
            slidesPerView: 1,
            spaceBetween: 30,
            autoplay: {
                delay: 5000,
            },
            pagination: {
                el: '.swiper-pagination',
                clickable: true,
            },
            breakpoints: {
                768: {
                    slidesPerView: 2,
                },
                1024: {
                    slidesPerView: 3,
                }
            }
        });
    }
}

// Export functions for global access
window.SR = {
    showLoading,
    hideLoading,
    showNotification,
    formatCurrency,
    formatDate,
    apiCall,
    searchBuses,
    selectBus: function(busId) {
        window.location.href = `seat-selection.php?bus_id=${busId}&date=${new URLSearchParams(window.location.search).get('date')}`;
    },
    proceedToPayment: function() {
        if (selectedSeats.length === 0) {
            showNotification('Please select at least one seat', 'warning');
            return;
        }
        
        bookingData = {
            seats: selectedSeats,
            totalAmount: selectedSeats.reduce((sum, seat) => sum + seat.price, 0)
        };
        
        window.location.href = 'payment.php';
    },
    processPayment
};

// Make functions globally available
Object.assign(window, window.SR);