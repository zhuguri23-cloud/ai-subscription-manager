"""
Cost Optimizer - Suggests ways to optimize subscription spending
"""

class CostOptimizer:
    """Optimizes subscription costs."""
    
    def suggest(self, subscriptions):
        """Generate optimization suggestions."""
        suggestions = []
        
        if not subscriptions:
            return ["Add subscriptions to get optimization suggestions"]
        
        # Group by category
        category_groups = {}
        for sub in subscriptions:
            cat = sub.get('category', 'other')
            if cat not in category_groups:
                category_groups[cat] = []
            category_groups[cat].append(sub)
        
        # Check for duplicate services
        for cat, subs in category_groups.items():
            names = [s.get('name', '').lower() for s in subs]
            # Simple duplicate detection
            for i, name in enumerate(names):
                for j, other in enumerate(names):
                    if i != j and name in other or other in name:
                        suggestions.append(f"Possible duplicate: {subs[i]['name']} and {subs[j]['name']}")
        
        # Identify expensive subscriptions
        avg_price = sum(s.get('price', 0) for s in subscriptions) / len(subscriptions)
        for sub in subscriptions:
            if sub.get('price', 0) > 20:
                annual_cost = sub.get('price', 0) * 12
                potential_savings = annual_cost * 0.15
                suggestions.append(
                    f"Switch {sub['name']} to annual billing to save ~${potential_savings:.2f}/year"
                )
        
        # Check for unused categories
        if len(subscriptions) > 10:
            suggestions.append("You have many subscriptions - consider auditing for unused services")
        
        # Suggest annual billing
        monthly_total = sum(s.get('price', 0) for s in subscriptions 
                          if s.get('billing_cycle') == 'monthly')
        if monthly_total > 30:
            annual_savings = monthly_total * 12 * 0.10
            suggestions.append(
                f"Switch all monthly plans to annual to save ~${annual_savings:.2f}/year"
            )
        
        # Storage and utility suggestions
        storage_subs = [s for s in subscriptions if s.get('category') == 'storage']
        for sub in storage_subs:
            if sub.get('price', 0) > 5:
                suggestions.append(
                    f"Check {sub['name']} storage usage - you might not need the current plan"
                )
        
        if not suggestions:
            suggestions.append("Your subscription portfolio looks well-optimized! ✓")
        
        return suggestions
