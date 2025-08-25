"""
Example usage script for WhatsApp automation.
This demonstrates how to use the WhatsApp automation class.
"""

from whatsapp_automation import WhatsAppAutomation
from datetime import datetime, timedelta

def example_basic_usage():
    """Basic usage example."""
    print("=== Basic Usage Example ===")
    
    # Initialize automation
    wa = WhatsAppAutomation()
    
    # Add some contacts (example - replace with real numbers)
    wa.add_contact("Test Contact", "+393xxxxxxxxx")  # Replace with real number
    
    # Send immediate message
    # wa.send_to_contact("Test Contact", "Hello! This is an automated message.")
    
    print("Basic setup completed. Uncomment the send_to_contact line to test.")

def example_scheduled_messages():
    """Example of scheduling messages."""
    print("=== Scheduled Messages Example ===")
    
    wa = WhatsAppAutomation()
    
    # Schedule a message for later today
    now = datetime.now()
    future_time = now + timedelta(minutes=5)  # 5 minutes from now
    
    # wa.send_to_contact(
    #     "Test Contact", 
    #     "This is a scheduled message!",
    #     scheduled_time=(future_time.hour, future_time.minute)
    # )
    
    print(f"Message scheduled for {future_time.hour:02d}:{future_time.minute:02d}")
    print("Uncomment the send_to_contact line to test scheduling.")

def example_bulk_messages():
    """Example of sending bulk messages."""
    print("=== Bulk Messages Example ===")
    
    wa = WhatsAppAutomation()
    
    # Add multiple contacts
    contacts = {
        "Friend1": "+393xxxxxxxxx",  # Replace with real numbers
        "Friend2": "+393yyyyyyyyy",
        "Family": "+393zzzzzzzzz"
    }
    
    for name, phone in contacts.items():
        wa.add_contact(name, phone)
    
    # Send bulk message
    message = "Hello everyone! This is an automated message sent to multiple contacts."
    contact_names = list(contacts.keys())
    
    # wa.bulk_send_messages(contact_names, message, delay_between_messages=30)
    
    print("Bulk message setup completed. Uncomment the bulk_send_messages line to test.")

def example_interactive_mode():
    """Run the interactive mode."""
    print("=== Interactive Mode ===")
    from whatsapp_automation import main
    main()

if __name__ == "__main__":
    print("WhatsApp Automation Examples")
    print("Choose an example to run:")
    print("1. Basic usage")
    print("2. Scheduled messages")
    print("3. Bulk messages")
    print("4. Interactive mode")
    
    choice = input("Enter choice (1-4): ").strip()
    
    if choice == "1":
        example_basic_usage()
    elif choice == "2":
        example_scheduled_messages()
    elif choice == "3":
        example_bulk_messages()
    elif choice == "4":
        example_interactive_mode()
    else:
        print("Invalid choice")