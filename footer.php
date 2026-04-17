<?php
// Include config for site constants
if (!defined('SITE_NAME')) {
    require_once dirname(__DIR__) . '/config.php';
}
?>

<footer class="main-footer bg-dark text-white">
    <!-- Main Footer Content -->
    <div class="footer-content py-5">
        <div class="container">
            <div class="row">
                <!-- Company Info -->
                <div class="col-lg-4 col-md-6 mb-4">
                    <div class="footer-section">
                        <div class="footer-logo mb-3">
                            <img src="assets/images/logo-white.png" alt="<?php echo SITE_NAME; ?>" height="40" class="mb-2">
                            <h4><?php echo SITE_NAME; ?></h4>
                            <p class="text-muted">Premium Bus Travel Experience</p>
                        </div>
                        <p>Your trusted partner for comfortable and safe bus travel across India. Experience luxury, reliability, and exceptional service with every journey.</p>
                        <div class="social-links mt-3">
                            <a href="#" class="social-link"><i class="fab fa-facebook-f"></i></a>
                            <a href="#" class="social-link"><i class="fab fa-twitter"></i></a>
                            <a href="#" class="social-link"><i class="fab fa-instagram"></i></a>
                            <a href="#" class="social-link"><i class="fab fa-linkedin-in"></i></a>
                            <a href="#" class="social-link"><i class="fab fa-youtube"></i></a>
                        </div>
                    </div>
                </div>

                <!-- Quick Links -->
                <div class="col-lg-2 col-md-6 mb-4">
                    <div class="footer-section">
                        <h5 class="footer-title">Quick Links</h5>
                        <ul class="footer-links">
                            <li><a href="index.php">Home</a></li>
                            <li><a href="search-buses.php">Search Buses</a></li>
                            <li><a href="about.php">About Us</a></li>
                            <li><a href="contact.php">Contact</a></li>
                            <li><a href="careers.php">Careers</a></li>
                            <li><a href="blog.php">Blog</a></li>
                        </ul>
                    </div>
                </div>

                <!-- Services -->
                <div class="col-lg-2 col-md-6 mb-4">
                    <div class="footer-section">
                        <h5 class="footer-title">Services</h5>
                        <ul class="footer-links">
                            <li><a href="bus-tracking.php">Live Tracking</a></li>
                            <li><a href="holiday-packages.php">Holiday Packages</a></li>
                            <li><a href="group-booking.php">Group Booking</a></li>
                            <li><a href="corporate-booking.php">Corporate Travel</a></li>
                            <li><a href="charter-services.php">Charter Services</a></li>
                            <li><a href="loyalty-program.php">Loyalty Program</a></li>
                        </ul>
                    </div>
                </div>

                <!-- Support -->
                <div class="col-lg-2 col-md-6 mb-4">
                    <div class="footer-section">
                        <h5 class="footer-title">Support</h5>
                        <ul class="footer-links">
                            <li><a href="help-center.php">Help Center</a></li>
                            <li><a href="faq.php">FAQ</a></li>
                            <li><a href="cancellation-policy.php">Cancellation Policy</a></li>
                            <li><a href="refund-policy.php">Refund Policy</a></li>
                            <li><a href="terms.php">Terms & Conditions</a></li>
                            <li><a href="privacy.php">Privacy Policy</a></li>
                        </ul>
                    </div>
                </div>

                <!-- Contact Info -->
                <div class="col-lg-2 col-md-6 mb-4">
                    <div class="footer-section">
                        <h5 class="footer-title">Contact Info</h5>
                        <div class="contact-info">
                            <div class="contact-item mb-3">
                                <i class="fas fa-map-marker-alt"></i>
                                <div>
                                    <strong>Address:</strong><br>
                                    123 Travel Street,<br>
                                    Mumbai, Maharashtra 400001
                                </div>
                            </div>
                            <div class="contact-item mb-3">
                                <i class="fas fa-phone"></i>
                                <div>
                                    <strong>Phone:</strong><br>
                                    <?php echo SITE_PHONE; ?>
                                </div>
                            </div>
                            <div class="contact-item mb-3">
                                <i class="fas fa-envelope"></i>
                                <div>
                                    <strong>Email:</strong><br>
                                    <?php echo SITE_EMAIL; ?>
                                </div>
                            </div>
                            <div class="contact-item">
                                <i class="fas fa-clock"></i>
                                <div>
                                    <strong>Support Hours:</strong><br>
                                    24/7 Available
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Newsletter Section -->
    <div class="newsletter-section bg-primary py-4">
        <div class="container">
            <div class="row align-items-center">
                <div class="col-lg-6 mb-3 mb-lg-0">
                    <div class="newsletter-content">
                        <h5 class="mb-1">📧 Stay Updated with Latest Offers!</h5>
                        <p class="mb-0">Subscribe to our newsletter and never miss exclusive deals and travel updates.</p>
                    </div>
                </div>
                <div class="col-lg-6">
                    <form class="newsletter-form" id="newsletterForm">
                        <div class="input-group">
                            <input type="email" class="form-control" placeholder="Enter your email address" required>
                            <button class="btn btn-light" type="submit">
                                <i class="fas fa-paper-plane"></i> Subscribe
                            </button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>

    <!-- Payment Methods -->
    <div class="payment-section py-3 bg-light text-dark">
        <div class="container">
            <div class="row align-items-center">
                <div class="col-md-6 mb-2 mb-md-0">
                    <h6 class="mb-2">💳 We Accept:</h6>
                    <div class="payment-methods">
                        <img src="assets/images/payments/visa.png" alt="Visa" height="30">
                        <img src="assets/images/payments/mastercard.png" alt="Mastercard" height="30">
                        <img src="assets/images/payments/rupay.png" alt="RuPay" height="30">
                        <img src="assets/images/payments/paytm.png" alt="Paytm" height="30">
                        <img src="assets/images/payments/phonepe.png" alt="PhonePe" height="30">
                        <img src="assets/images/payments/googlepay.png" alt="Google Pay" height="30">
                        <img src="assets/images/payments/upi.png" alt="UPI" height="30">
                        <img src="assets/images/payments/netbanking.png" alt="Net Banking" height="30">
                    </div>
                </div>
                <div class="col-md-6 text-md-end">
                    <h6 class="mb-2">🔒 Secured By:</h6>
                    <div class="security-badges">
                        <img src="assets/images/security/ssl.png" alt="SSL Secured" height="30">
                        <img src="assets/images/security/pci.png" alt="PCI Compliant" height="30">
                        <img src="assets/images/security/verified.png" alt="Verified" height="30">
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Bottom Footer -->
    <div class="footer-bottom py-3 border-top border-secondary">
        <div class="container">
            <div class="row align-items-center">
                <div class="col-md-6 mb-2 mb-md-0">
                    <p class="mb-0">&copy; <?php echo date('Y'); ?> <?php echo SITE_NAME; ?>. All rights reserved.</p>
                </div>
                <div class="col-md-6 text-md-end">
                    <div class="footer-bottom-links">
                        <a href="sitemap.php">Sitemap</a>
                        <span class="separator">|</span>
                        <a href="terms.php">Terms</a>
                        <span class="separator">|</span>
                        <a href="privacy.php">Privacy</a>
                        <span class="separator">|</span>
                        <a href="cookies.php">Cookies</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</footer>

<!-- Back to Top Button -->
<button class="back-to-top" id="backToTop" onclick="scrollToTop()">
    <i class="fas fa-chevron-up"></i>
</button>

<!-- WhatsApp Float Button -->
<div class="whatsapp-float">
    <a href="https://wa.me/<?php echo str_replace(['+', '-', ' '], '', SITE_PHONE); ?>?text=Hi, I need help with bus booking" target="_blank" class="whatsapp-btn">
        <i class="fab fa-whatsapp"></i>
        <span class="whatsapp-text">Need Help?</span>
    </a>
</div>

<!-- Cookie Consent Banner -->
<div class="cookie-banner" id="cookieBanner">
    <div class="container">
        <div class="row align-items-center">
            <div class="col-md-8 mb-2 mb-md-0">
                <p class="mb-0">
                    <i class="fas fa-cookie-bite me-2"></i>
                    We use cookies to enhance your browsing experience and provide personalized content. 
                    <a href="privacy.php" class="text-primary">Learn more</a>
                </p>
            </div>
            <div class="col-md-4 text-md-end">
                <button class="btn btn-primary btn-sm me-2" onclick="acceptCookies()">Accept All</button>
                <button class="btn btn-outline-light btn-sm" onclick="declineCookies()">Decline</button>
            </div>
        </div>
    </div>
</div>

<script>
// Footer functionality
document.addEventListener('DOMContentLoaded', function() {
    // Newsletter form
    document.getElementById('newsletterForm').addEventListener('submit', function(e) {
        e.preventDefault();
        const email = this.querySelector('input[type="email"]').value;
        
        fetch('api/subscribe-newsletter.php', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ email: email })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Thank you for subscribing! You will receive our latest offers and updates.');
                this.reset();
            } else {
                alert(data.message || 'Subscription failed. Please try again.');
            }
        })
        .catch(error => {
            alert('Network error. Please try again later.');
        });
    });

    // Back to top button
    window.addEventListener('scroll', function() {
        const backToTop = document.getElementById('backToTop');
        if (window.scrollY > 300) {
            backToTop.style.display = 'block';
        } else {
            backToTop.style.display = 'none';
        }
    });

    // Show cookie banner if not accepted
    if (!localStorage.getItem('cookiesAccepted')) {
        setTimeout(() => {
            document.getElementById('cookieBanner').style.display = 'block';
        }, 2000);
    }
});

function scrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}

function acceptCookies() {
    localStorage.setItem('cookiesAccepted', 'true');
    document.getElementById('cookieBanner').style.display = 'none';
}

function declineCookies() {
    localStorage.setItem('cookiesAccepted', 'false');
    document.getElementById('cookieBanner').style.display = 'none';
}
</script>