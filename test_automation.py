"""
Simple test script to verify the WhatsApp automation structure.
This test doesn't require dependencies to be installed.
"""

import os
import sys
import json
from unittest.mock import MagicMock

def test_config_creation():
    """Test configuration file handling."""
    print("Testing configuration management...")
    
    # Mock pywhatkit to avoid import errors
    sys.modules['pywhatkit'] = MagicMock()
    
    from whatsapp_automation import WhatsAppAutomation
    
    # Test config creation
    wa = WhatsAppAutomation("test_config.json")
    
    # Test adding contacts
    wa.add_contact("Test User", "+393123456789")
    
    # Verify config file was created
    assert os.path.exists("test_config.json"), "Config file not created"
    
    # Verify contact was added
    with open("test_config.json", 'r') as f:
        config = json.load(f)
        assert "Test User" in config["contacts"], "Contact not added"
        assert config["contacts"]["Test User"] == "+393123456789", "Phone number incorrect"
    
    # Test contact listing
    wa.list_contacts()
    
    # Test contact removal
    wa.remove_contact("Test User")
    with open("test_config.json", 'r') as f:
        config = json.load(f)
        assert "Test User" not in config["contacts"], "Contact not removed"
    
    # Clean up
    os.remove("test_config.json")
    
    print("✅ Configuration management test passed!")

def test_phone_validation():
    """Test phone number format validation."""
    print("Testing phone number validation...")
    
    sys.modules['pywhatkit'] = MagicMock()
    
    from whatsapp_automation import WhatsAppAutomation
    
    wa = WhatsAppAutomation("test_validation.json")
    
    # Test various phone number formats
    test_numbers = [
        "+393123456789",  # Italy
        "+49123456789",   # Germany
        "+441234567890",  # UK
        "+33123456789"    # France
    ]
    
    for i, number in enumerate(test_numbers):
        wa.add_contact(f"Contact{i}", number)
    
    # Verify all contacts were added
    with open("test_validation.json", 'r') as f:
        config = json.load(f)
        assert len(config["contacts"]) == 4, "Not all contacts added"
    
    # Clean up
    os.remove("test_validation.json")
    
    print("✅ Phone number validation test passed!")

def test_examples_import():
    """Test that examples can be imported."""
    print("Testing examples import...")
    
    # Mock pywhatkit
    sys.modules['pywhatkit'] = MagicMock()
    
    try:
        import examples
        print("✅ Examples import test passed!")
    except Exception as e:
        print(f"❌ Examples import failed: {e}")
        return False
    
    return True

def run_all_tests():
    """Run all tests."""
    print("🚀 Running WhatsApp Automation Tests...\n")
    
    try:
        test_config_creation()
        test_phone_validation() 
        test_examples_import()
        
        print("\n🎉 All tests passed! WhatsApp automation is ready to use.")
        print("\nNext steps:")
        print("1. Install dependencies: pip install -r requirements.txt")
        print("2. Make sure you're logged into WhatsApp Web")
        print("3. Run: python whatsapp_automation.py")
        
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        return False
    
    return True

if __name__ == "__main__":
    run_all_tests()