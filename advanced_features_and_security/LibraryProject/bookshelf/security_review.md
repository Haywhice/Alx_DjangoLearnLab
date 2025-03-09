Security Review: HTTPS and Secure Redirects
Implemented Security Measures
    1. Enforced HTTPS
        Enabled SECURE_SSL_REDIRECT = True to force HTTPS.
        Configured SECURE_HSTS_SECONDS = 31536000 to enforce HTTPS at the browser level.
    
    2. Secured Cookies
        Enabled SESSION_COOKIE_SECURE = True and CSRF_COOKIE_SECURE = True to prevent data transmission over HTTP.
    3. Secured HTTP Headers
        Set X_FRAME_OPTIONS = "DENY" to prevent clickjacking.
        Enabled SECURE_BROWSER_XSS_FILTER = True to mitigate XSS risks.
    4. Deployment Configuration
        Updated Nginx configuration to redirect HTTP traffic to HTTPS.
        Set up SSL certificates using Let’s Encrypt.
    5. Next Steps
        Perform security testing using curl -I https://yourdomain.com.
        Regularly update SSL certificates to avoid expiration.

        