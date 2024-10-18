import pandas as pd
import streamlit as st

# Load the dataset
df = pd.read_csv("Car-Price.csv")
df['Brand'] = df['Brand'].str.lower().str.strip()
df['Model'] = df['Model'].str.lower().str.strip()

# Preprocess the dataset
df.dropna(inplace=True)

st.title("Amiverse Motors Car Price Negotiation Chatbot")

# User input for car brand (case-insensitive search)
car_name = st.text_input("Enter car brand:").lower()  # Convert input to lowercase

if car_name:
    # Display available models for the selected car brand (case-insensitive search)
    available_models = df[df['Brand'].str.lower() == car_name]['Model'].unique()

    if available_models.size > 0:
        model_selected = st.selectbox("Choose a model", ['Select a model...'] + list(available_models))
    else:
        st.write("No models found for this brand.")
        model_selected = None
else:
    model_selected = None

# Only proceed if a model has been selected
if model_selected:
    # Display car details for the selected model
    car_info = df[(df['Brand'].str.lower() == car_name) & (df['Model'] == model_selected)]
    
    if not car_info.empty:
        # Extract features
        year = car_info['Year'].values[0]
        fuel = car_info['Fuel'].values[0]
        transmission = car_info['Transmission'].values[0]
        owner = car_info['Owner'].values[0]
        
        # Check if the 'Selling_Price' column exists and is properly fetched
        if 'Selling_Price' in car_info.columns:
            price = car_info['Selling_Price'].values[0]
        else:
            st.write("Error: Price column not found in the dataset.")
            price = None

        # Only display the details if the price is available
        if price is not None:
            st.write(f"**Car Features**")
            st.write(f"**Year**: {year}")
            st.write(f"**Fuel Type**: {fuel}")
            st.write(f"**Transmission**: {transmission}")
            st.write(f"**Owner Type**: {owner}")
            st.write(f"**Initial Price**: ₦{price}")

            # Create a form to capture the user's offer and submit it
            with st.form(key='negotiation_form'):
                user_offer = st.number_input("Your Offer (₦)", min_value=0)
                submit_button = st.form_submit_button(label="Submit Offer")

                # Respond to the user's input after they submit
                if submit_button:
                    # Basic negotiation logic
                    if user_offer >= price * 0.9:  # Accept if within 10% of original price
                        st.write(f"Offer accepted! The final price is ₦{user_offer}.")
                    elif user_offer >= price * 0.75:  # Counter-offer if within 25% of original price
                        counter_offer = (user_offer + price) / 2  # Midpoint offer
                        st.write(f"We cannot accept ₦{user_offer}, but how about ₦{counter_offer}?")
                    else:  # Refuse if too low
                        st.write(f"Sorry, we cannot go below ₦{price * 0.75}. Our final offer is ₦{price * 0.75}.")
