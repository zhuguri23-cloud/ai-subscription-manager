"""
Subscription Tracker - Data management for subscriptions
"""
import json
import os
from datetime import datetime
from pathlib import Path

class SubscriptionTracker:
    """Tracks and manages subscriptions."""
    
    def __init__(self, data_path=None):
        if data_path is None:
            # Default to data/subscriptions.json in project directory
            project_dir = Path(__file__).parent.parent
            data_path = project_dir / "data" / "subscriptions.json"
        
        self.data_path = Path(data_path)
        self._ensure_data_dir()
        self.subscriptions = self._load()
    
    def _ensure_data_dir(self):
        """Create data directory if it doesn't exist."""
        self.data_path.parent.mkdir(parents=True, exist_ok=True)
    
    def _load(self):
        """Load subscriptions from file."""
        if self.data_path.exists():
            with open(self.data_path, 'r') as f:
                return json.load(f)
        return []
    
    def _save(self):
        """Save subscriptions to file."""
        with open(self.data_path, 'w') as f:
            json.dump(self.subscriptions, f, indent=2)
    
    def generate_id(self):
        """Generate unique ID for subscription."""
        return f"sub_{datetime.now().strftime('%Y%m%d%H%M%S')}"
    
    def add(self, subscription):
        """Add a new subscription."""
        self.subscriptions.append(subscription)
        self._save()
        return subscription['id']
    
    def remove(self, sub_id):
        """Remove subscription by ID."""
        self.subscriptions = [s for s in self.subscriptions if s.get('id') != sub_id]
        self._save()
        return True
    
    def update(self, sub_id, updates):
        """Update subscription details."""
        for sub in self.subscriptions:
            if sub.get('id') == sub_id:
                sub.update(updates)
                self._save()
                return True
        return False
    
    def list_all(self):
        """List all subscriptions."""
        return self.subscriptions
    
    def get_by_category(self, category):
        """Get subscriptions by category."""
        return [s for s in self.subscriptions if s.get('category') == category]
    
    def get_upcoming_renewals(self, days=7):
        """Get subscriptions renewing in the next N days."""
        # This would need billing dates implementation
        return []
