"""
AI Analyzer - AI-powered subscription analysis
"""

class AIAnalyzer:
    """Analyzes subscriptions using AI-like logic."""
    
    def analyze(self, subscriptions):
        """Analyze subscriptions and provide insights."""
        insights = []
        
        if not subscriptions:
            insights.append("No subscriptions tracked yet. Add some to get started!")
            return insights
        
        # Calculate total spending
        total = sum(s.get('price', 0) for s in subscriptions)
        insights.append(f"You spend ${total:.2f} monthly on subscriptions")
        
        # Category analysis
        categories = {}
        for sub in subscriptions:
            cat = sub.get('category', 'other')
            categories[cat] = categories.get(cat, 0) + sub.get('price', 0)
        
        if categories:
            top_cat = max(categories.items(), key=lambda x: x[1])
            insights.append(f"Most spending is on '{top_cat[0]}' (${top_cat[1]:.2f}/month)")
        
        # Billing cycle analysis
        monthly_subs = [s for s in subscriptions if s.get('billing_cycle') == 'monthly']
        yearly_subs = [s for s in subscriptions if s.get('billing_cycle') == 'yearly']
        
        if len(monthly_subs) > len(yearly_subs):
            insights.append("Consider switching to annual billing to save money")
        
        # Price analysis
        avg_price = total / len(subscriptions) if subscriptions else 0
        expensive_subs = [s for s in subscriptions if s.get('price', 0) > avg_price * 1.5]
        
        if expensive_subs:
            names = ", ".join([s['name'] for s in expensive_subs[:3]])
            insights.append(f"Consider reviewing: {names} - they cost above average")
        
        # Entertainment vs utility
        entertainment = sum(s.get('price', 0) for s in subscriptions 
                         if s.get('category') == 'entertainment')
        if entertainment > total * 0.3:
            insights.append("Over 30% of spending is on entertainment subscriptions")
        
        # Value\n        insights.append("Tip: Review annual plans for potential 20% savings")
        
        return insights
