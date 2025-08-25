#!/usr/bin/env python3
"""
Quick Start Script for WhatsApp Automation
Installs dependencies and provides guidance for first use.
"""

import subprocess
import sys
import os

def install_dependencies():
    """Install required dependencies."""
    print("📦 Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False

def check_browser():
    """Check if Chrome/Chromium is available."""
    print("🔍 Checking for Chrome/Chromium browser...")
    
    browsers = ['google-chrome', 'chromium-browser', 'chromium', 'chrome']
    browser_found = False
    
    for browser in browsers:
        try:
            subprocess.run([browser, '--version'], capture_output=True, check=True)
            print(f"✅ Found browser: {browser}")
            browser_found = True
            break
        except (subprocess.CalledProcessError, FileNotFoundError):
            continue
    
    if not browser_found:
        print("⚠️  Chrome/Chromium not found!")
        print("Please install Chrome or Chromium:")
        print("  Ubuntu/Debian: sudo apt-get install chromium-browser")
        print("  macOS: brew install chromium")
        print("  Windows: Download from https://www.google.com/chrome/")
    
    return browser_found

def show_usage_guide():
    """Show quick usage guide."""
    print("\n" + "="*60)
    print("🚀 WhatsApp Automation - Quick Start Guide")
    print("="*60)
    
    print("\n📋 IMPORTANT REQUIREMENTS:")
    print("1. You must be logged into WhatsApp Web (web.whatsapp.com)")
    print("2. Chrome/Chromium browser must be installed")
    print("3. Phone numbers must include country code (+39 for Italy)")
    
    print("\n⚡ QUICK START:")
    print("1. Run the main program:")
    print("   python whatsapp_automation.py")
    print("\n2. Or try the examples:")
    print("   python examples.py")
    
    print("\n📱 PHONE NUMBER FORMAT:")
    print("  Italy: +393xxxxxxxxx")
    print("  Germany: +49xxxxxxxxxx") 
    print("  France: +33xxxxxxxxx")
    print("  UK: +44xxxxxxxxxx")
    
    print("\n🔒 SAFETY TIPS:")
    print("- Only send messages to people who expect them")
    print("- Don't spam or send unsolicited messages")
    print("- Test with your own number first")
    print("- Keep WhatsApp Web open during sending")
    
    print("\n📞 Support: @giacomo.gamberi on Instagram")
    print("="*60)

def main():
    """Main setup function."""
    print("🤖 WhatsApp Automation Setup")
    print("Setting up automatic WhatsApp messaging without costs...\n")
    
    # Check if we're in the right directory
    if not os.path.exists("whatsapp_automation.py"):
        print("❌ Please run this script from the project directory")
        print("Make sure whatsapp_automation.py is in the current folder")
        return
    
    # Install dependencies
    if not install_dependencies():
        return
    
    # Check browser
    check_browser()
    
    # Show usage guide
    show_usage_guide()
    
    # Ask if user wants to start
    print("\nReady to start? (y/n): ", end="")
    try:
        if input().lower().strip() == 'y':
            print("\n🚀 Starting WhatsApp Automation...")
            os.system("python whatsapp_automation.py")
    except KeyboardInterrupt:
        print("\n\nSetup completed! Run 'python whatsapp_automation.py' when ready.")

if __name__ == "__main__":
    main()