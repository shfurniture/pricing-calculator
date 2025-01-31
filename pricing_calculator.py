import streamlit as st

def calculate_final_price(vendor_price, shipping_cost, markup_percentage, shopify_fee_percentage=2.9, transaction_fee=0.30):
    cogs = vendor_price + shipping_cost
    selling_price_before_fees = cogs + (cogs * (markup_percentage / 100))
    final_price = selling_price_before_fees / (1 - (shopify_fee_percentage / 100))
    final_price += transaction_fee
    final_price = round(final_price - 1) + 0.99  # Adjust to end with .99
    return final_price

st.title("Stamps Home Furniture Pricing Calculator")

vendor_price = st.number_input("Enter Vendor Price ($)", min_value=0.0, step=0.01)
shipping_cost = st.number_input("Enter Shipping Cost ($)", min_value=0.0, step=0.01)
markup_percentage = st.slider("Select Markup Percentage (%)", 20, 60, 50)

if st.button("Calculate Price"):
    final_price = calculate_final_price(vendor_price, shipping_cost, markup_percentage)
    st.success(f"Recommended Selling Price: ${final_price}")
