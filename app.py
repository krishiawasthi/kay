from main import FinanceTracker

def main():
    """Interactive CLI for finance tracker"""
    tracker = FinanceTracker()
    
    print("\n" + "="*50)
    print("   PERSONAL FINANCE TRACKER")
    print("="*50)
    
    while True:
        print("\nOptions:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. View Category Breakdown")
        print("5. View All Transactions")
        print("6. Generate Chart")
        print("7. Exit")
        
        choice = input("\nEnter your choice (1-7): ").strip()
        
        if choice == '1':
            category = input("Enter income category (e.g., Salary): ").strip()
            amount = float(input("Enter amount: $"))
            description = input("Enter description (optional): ").strip()
            tracker.add_transaction(category, "Income", amount, description)
        
        elif choice == '2':
            print("\nCommon expense categories:")
            print("- Groceries")
            print("- Transport")
            print("- Utilities")
            print("- Entertainment")
            print("- Healthcare")
            print("- Other")
            
            category = input("\nEnter expense category: ").strip()
            amount = float(input("Enter amount: $"))
            description = input("Enter description (optional): ").strip()
            tracker.add_transaction(category, "Expense", amount, description)
        
        elif choice == '3':
            tracker.get_summary()
        
        elif choice == '4':
            tracker.get_category_breakdown()
        
        elif choice == '5':
            tracker.show_all_transactions()
        
        elif choice == '6':
            tracker.plot_expenses()
        
        elif choice == '7':
            print("\nThank you for using Finance Tracker. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
