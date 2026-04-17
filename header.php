<?php
// Perfect Navigation Header for SR Travels
if (session_status() === PHP_SESSION_NONE) {
    session_start();
}

// Get current page for active navigation
$current_page = basename($_SERVER['PHP_SELF']);
?>

<!-- Perfect Navigation Header -->
<nav class="navbar navbar-expand-lg navbar-dark fixed-top" style="background: linear-gradient(135deg, #d32f2f, #b71c1c); backdrop-filter: blur(10px); box-shadow: 0 10px 30px rgba(0,0,0,0.1); transition: all 0.3s ease; padding: 1rem 0;">
    <div class="container">
        <a class="navbar-brand" href="index-perfect.php" style="font-weight: 800; font-size: 1.8rem; color: white; display: flex; align-items: center; gap: 10px;">
            <i class="fas fa-bus" style="font-size: 2rem; color: #ffc107;"></i>
            <span>SR TRAVELS</span>
        </a>
        
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
            <span class="navbar-toggler-icon"></span>
        </button>
        
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ms-auto">
                <li class="nav-item">
                    <a class="nav-link <?php echo ($current_page == 'index-perfect.php' || $current_page == 'index.php') ? 'active' : ''; ?>" 
                       href="index-perfect.php" 
                       style="color: white; font-weight: 500; margin: 0 10px; padding: 8px 16px; border-radius: 25px; transition: all 0.3s ease;">
                        <i class="fas fa-home"></i> Home
                    </a>
                </li>
                <li class="nav-item">
                    <a class="nav-link <?php echo $current_page == 'bus-search.php' ? 'active' : ''; ?>" 
                       href="bus-search.php"
                       style="color: white; font-weight: 500; margin: 0 10px; padding: 8px 16px; border-radius: 25px; transition: all 0.3s ease;">
                        <i class="fas fa-search"></i> Search Buses
                    </a>
                </li>
                <li class="nav-item">
                    <a class="nav-link <?php echo ($current_page == 'hotels.php' || $current_page == 'hotel-details.php' || $current_page == 'hotel-booking.php') ? 'active' : ''; ?>" 
                       href="hotels.php"
                       style="color: white; font-weight: 500; margin: 0 10px; padding: 8px 16px; border-radius: 25px; transition: all 0.3s ease;">
                        <i class="fas fa-hotel"></i> Hotels
                    </a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#routes" 
                       style="color: white; font-weight: 500; margin: 0 10px; padding: 8px 16px; border-radius: 25px; transition: all 0.3s ease;">
                        <i class="fas fa-route"></i> Routes
                    </a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#operators"
                       style="color: white; font-weight: 500; margin: 0 10px; padding: 8px 16px; border-radius: 25px; transition: all 0.3s ease;">
                        <i class="fas fa-bus-alt"></i> Operators
                    </a>
                </li>
                
                <?php if (isLoggedIn()): ?>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="accountDropdown" role="button" data-bs-toggle="dropdown"
                           style="color: white; font-weight: 500; margin: 0 10px; padding: 8px 16px; border-radius: 25px; transition: all 0.3s ease;">
                            <i class="fas fa-user-circle"></i> My Account
                        </a>
                        <ul class="dropdown-menu">
                            <li><a class="dropdown-item" href="<?php echo isAdmin() ? 'admin-dashboard-ultimate.php' : 'user-dashboard-enhanced.php'; ?>">
                                <i class="fas fa-tachometer-alt"></i> Dashboard
                            </a></li>
                            <li><a class="dropdown-item" href="booking-management.php"><i class="fas fa-ticket-alt"></i> My Bookings</a></li>
                            <li><a class="dropdown-item" href="user-profile.php"><i class="fas fa-user-edit"></i> Profile</a></li>
                            <li><hr class="dropdown-divider"></li>
                            <li><a class="dropdown-item" href="logout.php"><i class="fas fa-sign-out-alt"></i> Logout</a></li>
                        </ul>
                    </li>
                <?php else: ?>
                    <li class="nav-item">
                        <a class="nav-link" href="login.php"
                           style="color: white; font-weight: 500; margin: 0 10px; padding: 8px 16px; border-radius: 25px; transition: all 0.3s ease;">
                            <i class="fas fa-sign-in-alt"></i> Login
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="register.php"
                           style="color: white; font-weight: 500; margin: 0 10px; padding: 8px 16px; border-radius: 25px; transition: all 0.3s ease;">
                            <i class="fas fa-user-plus"></i> Register
                        </a>
                    </li>
                <?php endif; ?>
            </ul>
        </div>
    </div>
</nav>

<!-- Perfect Header Styles -->
<style>
.navbar-nav .nav-link:hover {
    background: rgba(255,255,255,0.2) !important;
    transform: translateY(-2px);
}

.navbar-nav .nav-link.active {
    background: rgba(255,255,255,0.3) !important;
    font-weight: 600;
}

.dropdown-menu {
    border: none;
    box-shadow: 0 10px 30px rgba(0,0,0,0.15);
    border-radius: 10px;
    padding: 0.5rem 0;
}

.dropdown-item {
    padding: 0.75rem 1.5rem;
    transition: all 0.3s ease;
}

.dropdown-item:hover {
    background: linear-gradient(135deg, #d32f2f, #b71c1c);
    color: white;
    transform: translateX(5px);
}

.dropdown-item i {
    width: 20px;
    margin-right: 10px;
}

/* Responsive adjustments */
@media (max-width: 768px) {
    .navbar-brand {
        font-size: 1.4rem !important;
    }
    
    .navbar-nav .nav-link {
        margin: 5px 0 !important;
        text-align: center;
    }
}
</style>

<!-- Perfect Header JavaScript -->
<script>
document.addEventListener('DOMContentLoaded', function() {
    // Enhanced navbar scroll effect
    window.addEventListener('scroll', function() {
        const navbar = document.querySelector('.navbar');
        if (window.scrollY > 100) {
            navbar.style.background = 'linear-gradient(135deg, rgba(211, 47, 47, 0.95), rgba(183, 28, 28, 0.95))';
            navbar.style.backdropFilter = 'blur(15px)';
            navbar.style.boxShadow = '0 15px 40px rgba(0,0,0,0.2)';
        } else {
            navbar.style.background = 'linear-gradient(135deg, #d32f2f, #b71c1c)';
            navbar.style.backdropFilter = 'blur(10px)';
            navbar.style.boxShadow = '0 10px 30px rgba(0,0,0,0.1)';
        }
    });

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Auto-close mobile menu when clicking on links
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
    const navbarCollapse = document.querySelector('.navbar-collapse');
    
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            if (navbarCollapse.classList.contains('show')) {
                const bsCollapse = new bootstrap.Collapse(navbarCollapse);
                bsCollapse.hide();
            }
        });
    });
});
</script>