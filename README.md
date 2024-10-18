# price-negotiation-bot
# Amiverse Motors Car Price Negotiation Chatbot

This is a Streamlit-based web app that allows users to negotiate car prices for different car models from Amiverse Motors. The app provides basic negotiation logic, displaying available models, and allows users to input their offers for a given car.

## Features
- Display car features such as year, fuel type, transmission, and owner type.
- Allows users to make offers and receive counter-offers based on initial pricing.
- Provides a final price based on negotiation.

## How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/amakaogbu/price-negotiation-bot.git
2. Navigate to the project directory:
    cd your-repo
3. Install dependencies:
    pip install -r requirements.txt
4. Run the Streamlit app:
    streamlit run app.py
Open the app in your browser at http://localhost:8501.

## Dataset
The app uses a dataset Car-Price.csv, which contains the details of various car brands and models along with their prices.

## Libraries Used
Streamlit: For creating interactive web apps.
Pandas: For data manipulation and analysis.
Transformers: For integrating the GPT model for system prompts.
## License
This project is licensed under the MIT License - see the LICENSE file for details.
