"""
AI Subscription Manager - Core Package
"""

from .tracker import SubscriptionTracker
from .analyzer import AIAnalyzer
from .optimizer import CostOptimizer
from datetime import datetime

class SubscriptionManager:
    """Main subscription manager class."""
    
    def __init__(self, data_path=None):
        self.tracker = SubscriptionTracker(data_path)
        self.analyzer = AIAnalyzer()
        self.optimizer = CostOptimizer()
    
    def add_subscription(self, subscription):
        """Add a new subscription."""
        subscription['created_at'] = datetime.now().isoformat()
        subscription['id'] = self.tracker.generate_id()
        return self.tracker.add(subscription)
    
    def remove_subscription(self, sub_id):
        """Remove a subscription by ID."""
        return self.tracker.remove(sub_id)
    
    def get_subscriptions(self):
        """Get all subscriptions."""
        return self.tracker.list_all()
    
    def get_ai_insights(self):
        """Get AI-powered insights about subscriptions."""
        subscriptions = self.get_subscriptions()
        return self.analyzer.analyze(subscriptions)
    
    def optimize_subscriptions(self):
        """Get optimization suggestions."""
        subscriptions = self.get_subscriptions()
        return self.optimizer.suggest(subscriptions)
    
    def get_summary(self):
        """Get subscription summary."""
        subscriptions = self.get_subscriptions()
        
        total_monthly = sum(s.get('price', 0) for s in subscriptions)
        total_yearly = total_monthly * 12
        
        categories = list(set(s.get('category', 'other') for s in subscriptions))
        
        return {
            'total_monthly': total_monthly,
            'total_yearly': total_yearly,
            'count': len(subscriptions),
            'categories': categories
        }
