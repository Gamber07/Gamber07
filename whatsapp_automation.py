"""
WhatsApp Automation Script - Free Version
Automatically send WhatsApp messages without costs using pywhatkit library.

This script uses WhatsApp Web through automation, completely free of charge.
No API keys or paid services required.

Author: @Gamber07
"""

import pywhatkit as kit
import time
import json
import os
from datetime import datetime, timedelta
from typing import List, Dict, Optional


class WhatsAppAutomation:
    """
    Free WhatsApp automation class using pywhatkit library.
    Sends messages through WhatsApp Web without any costs.
    """
    
    def __init__(self, config_file: str = "whatsapp_config.json"):
        """
        Initialize WhatsApp automation.
        
        Args:
            config_file: Path to configuration file
        """
        self.config_file = config_file
        self.config = self.load_config()
    
    def load_config(self) -> Dict:
        """Load configuration from JSON file."""
        default_config = {
            "contacts": {},
            "default_wait_time": 20,
            "tab_close": True,
            "messages": []
        }
        
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                    # Merge with defaults
                    for key, value in default_config.items():
                        if key not in config:
                            config[key] = value
                    return config
            except Exception as e:
                print(f"Error loading config: {e}")
                return default_config
        else:
            self.save_config(default_config)
            return default_config
    
    def save_config(self, config: Dict = None):
        """Save configuration to JSON file."""
        if config is None:
            config = self.config
        
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Error saving config: {e}")
    
    def add_contact(self, name: str, phone_number: str):
        """
        Add a contact to the configuration.
        
        Args:
            name: Contact name
            phone_number: Phone number with country code (e.g., +393xxxxxxxxx)
        """
        # Ensure phone number starts with +
        if not phone_number.startswith('+'):
            print("Warning: Phone number should include country code with + prefix")
            print("Example: +393xxxxxxxxx for Italy")
        
        self.config["contacts"][name] = phone_number
        self.save_config()
        print(f"Contact '{name}' added successfully: {phone_number}")
    
    def remove_contact(self, name: str):
        """Remove a contact from configuration."""
        if name in self.config["contacts"]:
            del self.config["contacts"][name]
            self.save_config()
            print(f"Contact '{name}' removed successfully")
        else:
            print(f"Contact '{name}' not found")
    
    def list_contacts(self):
        """List all saved contacts."""
        if not self.config["contacts"]:
            print("No contacts saved")
            return
        
        print("Saved contacts:")
        for name, phone in self.config["contacts"].items():
            print(f"  {name}: {phone}")
    
    def send_message_now(self, phone_number: str, message: str, wait_time: int = None):
        """
        Send a WhatsApp message immediately.
        
        Args:
            phone_number: Phone number with country code
            message: Message to send
            wait_time: Wait time before sending (seconds)
        """
        if wait_time is None:
            wait_time = self.config.get("default_wait_time", 20)
        
        try:
            print(f"Sending message to {phone_number}...")
            print(f"Message: {message}")
            print(f"Wait time: {wait_time} seconds")
            
            kit.sendwhatmsg_instantly(
                phone_no=phone_number,
                message=message,
                wait_time=wait_time,
                tab_close=self.config.get("tab_close", True)
            )
            
            print("Message sent successfully!")
            return True
            
        except Exception as e:
            print(f"Error sending message: {e}")
            return False
    
    def send_message_scheduled(self, phone_number: str, message: str, 
                             hour: int, minute: int, wait_time: int = None):
        """
        Schedule a WhatsApp message.
        
        Args:
            phone_number: Phone number with country code
            message: Message to send
            hour: Hour to send (24-hour format)
            minute: Minute to send
            wait_time: Wait time before sending
        """
        if wait_time is None:
            wait_time = self.config.get("default_wait_time", 20)
        
        try:
            print(f"Scheduling message to {phone_number} at {hour:02d}:{minute:02d}")
            print(f"Message: {message}")
            
            kit.sendwhatmsg(
                phone_no=phone_number,
                message=message,
                time_hour=hour,
                time_min=minute,
                wait_time=wait_time,
                tab_close=self.config.get("tab_close", True)
            )
            
            print("Message scheduled successfully!")
            return True
            
        except Exception as e:
            print(f"Error scheduling message: {e}")
            return False
    
    def send_to_contact(self, contact_name: str, message: str, 
                       scheduled_time: Optional[tuple] = None, wait_time: int = None):
        """
        Send message to a saved contact.
        
        Args:
            contact_name: Name of the contact
            message: Message to send
            scheduled_time: Tuple of (hour, minute) for scheduling, None for immediate
            wait_time: Wait time before sending
        """
        if contact_name not in self.config["contacts"]:
            print(f"Contact '{contact_name}' not found. Use list_contacts() to see available contacts.")
            return False
        
        phone_number = self.config["contacts"][contact_name]
        
        if scheduled_time:
            hour, minute = scheduled_time
            return self.send_message_scheduled(phone_number, message, hour, minute, wait_time)
        else:
            return self.send_message_now(phone_number, message, wait_time)
    
    def bulk_send_messages(self, contacts: List[str], message: str, 
                          delay_between_messages: int = 30):
        """
        Send the same message to multiple contacts.
        
        Args:
            contacts: List of contact names
            message: Message to send
            delay_between_messages: Delay between each message (seconds)
        """
        successful_sends = 0
        failed_sends = 0
        
        for i, contact_name in enumerate(contacts):
            if contact_name not in self.config["contacts"]:
                print(f"Contact '{contact_name}' not found. Skipping...")
                failed_sends += 1
                continue
            
            print(f"\nSending message {i+1}/{len(contacts)} to {contact_name}...")
            
            if self.send_to_contact(contact_name, message):
                successful_sends += 1
                print(f"Message sent to {contact_name}")
            else:
                failed_sends += 1
                print(f"Failed to send message to {contact_name}")
            
            # Wait between messages to avoid being blocked
            if i < len(contacts) - 1:  # Don't wait after the last message
                print(f"Waiting {delay_between_messages} seconds before next message...")
                time.sleep(delay_between_messages)
        
        print(f"\nBulk send completed!")
        print(f"Successful: {successful_sends}")
        print(f"Failed: {failed_sends}")
        
        return successful_sends, failed_sends


def main():
    """Example usage of WhatsApp automation."""
    # Initialize WhatsApp automation
    wa = WhatsAppAutomation()
    
    print("=== WhatsApp Automation - Free Version ===")
    print("This tool uses WhatsApp Web to send messages automatically.")
    print("No costs, no API keys required!\n")
    
    while True:
        print("\nOptions:")
        print("1. Add contact")
        print("2. List contacts")
        print("3. Send immediate message")
        print("4. Schedule message")
        print("5. Send to saved contact")
        print("6. Bulk send messages")
        print("7. Remove contact")
        print("8. Exit")
        
        choice = input("\nEnter your choice (1-8): ").strip()
        
        if choice == "1":
            name = input("Enter contact name: ").strip()
            phone = input("Enter phone number (with country code, e.g., +393xxxxxxxxx): ").strip()
            wa.add_contact(name, phone)
        
        elif choice == "2":
            wa.list_contacts()
        
        elif choice == "3":
            phone = input("Enter phone number (with country code): ").strip()
            message = input("Enter message: ").strip()
            wa.send_message_now(phone, message)
        
        elif choice == "4":
            phone = input("Enter phone number (with country code): ").strip()
            message = input("Enter message: ").strip()
            hour = int(input("Enter hour (24-hour format): "))
            minute = int(input("Enter minute: "))
            wa.send_message_scheduled(phone, message, hour, minute)
        
        elif choice == "5":
            wa.list_contacts()
            if wa.config["contacts"]:
                contact = input("Enter contact name: ").strip()
                message = input("Enter message: ").strip()
                schedule = input("Schedule message? (y/n): ").strip().lower()
                
                if schedule == 'y':
                    hour = int(input("Enter hour (24-hour format): "))
                    minute = int(input("Enter minute: "))
                    wa.send_to_contact(contact, message, (hour, minute))
                else:
                    wa.send_to_contact(contact, message)
        
        elif choice == "6":
            wa.list_contacts()
            if wa.config["contacts"]:
                contacts_input = input("Enter contact names (comma-separated): ").strip()
                contacts = [c.strip() for c in contacts_input.split(",")]
                message = input("Enter message: ").strip()
                delay = input("Delay between messages in seconds (default 30): ").strip()
                delay = int(delay) if delay else 30
                wa.bulk_send_messages(contacts, message, delay)
        
        elif choice == "7":
            wa.list_contacts()
            if wa.config["contacts"]:
                name = input("Enter contact name to remove: ").strip()
                wa.remove_contact(name)
        
        elif choice == "8":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()