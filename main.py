"""
AI Subscription Manager - Main Entry Point
"""
import os
import json
from datetime import datetime
from subscription_manager import SubscriptionManager

def main():
    """Main application entry point."""
    print("🤖 AI Subscription Manager")
    print("=" * 40)
    
    # Initialize the manager
    manager = SubscriptionManager()
    
    # Demo: Add sample subscriptions
    sample_subscriptions = [
        {
            'name': 'Netflix',
            'price': 15.99,
            'billing_cycle': 'monthly',
            'category': 'entertainment'
        },
        {
            'name': 'Spotify',
            'price': 9.99,
            'billing_cycle': 'monthly',
            'category': 'entertainment'
        },
        {
            'name': 'GitHub Pro',
            'price': 4.00,
            'billing_cycle': 'monthly',
            'category': 'developer_tools'
        },
        {
            'name': 'iCloud+',
            'price': 2.99,
            'billing_cycle': 'monthly',
            'category': 'storage'
        }
    ]
    
    # Add subscriptions
    for sub in sample_subscriptions:
        manager.add_subscription(sub)
        print(f"✓ Added: {sub['name']} - ${sub['price']}/mo")
    
    print("\n📊 Analyzing your subscriptions...")
    
    # Get AI insights
    insights = manager.get_ai_insights()
    print("\n💡 AI Insights:")
    print("-" * 40)
    for insight in insights:
        print(f"  • {insight}")
    
    # Get optimization suggestions
    print("\n💰 Optimization Suggestions:")
    print("-" * 40)
    suggestions = manager.optimize_subscriptions()
    for suggestion in suggestions:
        print(f"  • {suggestion}")
    
    # Display summary
    summary = manager.get_summary()
    print("\n📈 Monthly Summary:")
    print("-" * 40)
    print(f"  Total Monthly: ${summary['total_monthly']:.2f}")
    print(f"  Total Yearly: ${summary['total_yearly']:.2f}")
    print(f"  Subscription Count: {summary['count']}")
    print(f"  Categories: {', '.join(summary['categories'])}")

if __name__ == "__main__":
    main()
