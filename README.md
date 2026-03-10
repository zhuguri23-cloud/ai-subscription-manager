# AI Subscription Manager 🤖📱

AI-powered subscription management tool that helps track, analyze, and optimize recurring payments.

## Features

- 📊 **Smart Tracking** - Automatically track all your subscriptions in one place
- 💡 **AI Analysis** - Get insights on spending patterns and optimization suggestions
- 🔔 **Renewal Reminders** - Never miss a payment with smart notifications
- 💰 **Cost Optimization** - Identify unused subscriptions and save money
- 📈 **Budget Planning** - Forecast future spending and set budget goals

## Installation

```bash
# Clone the repository
git clone https://github.com/zhuguri23-cloud/ai-subscription-manager.git
cd ai-subscription-manager

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

## Usage

```python
from subscription_manager import SubscriptionManager

# Initialize the manager
manager = SubscriptionManager()

# Add a subscription
manager.add_subscription({
    'name': 'Netflix',
    'price': 15.99,
    'billing_cycle': 'monthly',
    'category': 'entertainment'
})

# Get AI-powered insights
insights = manager.get_ai_insights()
print(insights)

# Check for optimization opportunities
suggestions = manager.optimize_subscriptions()
for suggestion in suggestions:
    print(suggestion)
```

## Project Structure

```
ai-subscription-manager/
├── main.py                 # Main application entry point
├── subscription_manager/   # Core package
│   ├── __init__.py
│   ├── tracker.py         # Subscription tracking
│   ├── analyzer.py        # AI analysis engine
│   ├── notifier.py        # Notification system
│   └── optimizer.py       # Cost optimization
├── data/                  # Data storage
├── tests/                 # Test suite
├── requirements.txt       # Dependencies
└── README.md            # This file
```

## Tech Stack

- **Python 3.9+** - Core language
- **OpenAI GPT** - AI analysis and insights
- **SQLite** - Local data storage
- **Pandas** - Data analysis

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - feel free to use this project for any purpose.

---

⭐ Star this repo if you find it useful!
