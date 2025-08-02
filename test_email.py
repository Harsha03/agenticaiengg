#!/usr/bin/env python3
"""
Simple script to test SendGrid email functionality
Run this to debug the 403 error
"""

import os
import sendgrid
from sendgrid.helpers.mail import Email, Mail, Content, To
from dotenv import load_dotenv

load_dotenv()

def test_sendgrid():
    # Check if API key exists
    api_key = os.environ.get('SENDGRID_API_KEY')
    if not api_key:
        print("❌ SENDGRID_API_KEY not found in environment variables")
        return False
    
    print(f"✅ API key found: {api_key[:10]}...")
    
    try:
        # Initialize SendGrid
        sg = sendgrid.SendGridAPIClient(api_key=api_key)
        
        # Create a simple test email
        from_email = Email("jaiganeshharsha@gmail.com")  # Must be verified in SendGrid
        to_email = To("atananyareddy@outlook.com")  # Can be any valid email
        subject = "SendGrid Test Email"
        content = Content("text/html", "<h1>Test Email</h1><p>This is a test email from your research app.</p>")
        
        mail = Mail(from_email, to_email, subject, content)
        
        # Send the email
        response = sg.client.mail.send.post(request_body=mail.get())
        
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Body: {response.body}")
        print(f"Response Headers: {response.headers}")
        
        if response.status_code == 202:
            print("✅ Email sent successfully!")
            return True
        else:
            print(f"❌ Email failed with status {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Error sending email: {str(e)}")
        return False

if __name__ == "__main__":
    print("Testing SendGrid email functionality...")
    test_sendgrid()
