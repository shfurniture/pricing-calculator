import streamlit as st
import pandas as pd
import plotly.express as px

def calculate_final_price(vendor_price, shipping_cost, markup_percentage, shopify_fee_percentage=2.9, transaction_fee=0.30):
    # Calculate COGS (Cost of Goods Sold)
    cogs = vendor_price + shipping_cost
    
    # Calculate the price before Shopify fees
    selling_price_before_fees = cogs + (cogs * (markup_percentage / 100))
    
    # Adjust for Shopify fees
    shopify_fees = selling_price_before_fees * (shopify_fee_percentage / 100) + transaction_fee
    final_price = selling_price_before_fees + shopify_fees
    
    # Round to nearest .99 for psychological pricing
    final_price = round(final_price - 1) + 0.99  
    return cogs, shopify_fees, final_price

# Streamlit UI enhancements
st.set_page_config(page_title="Stamps Home Furniture Pricing Calculator", layout="centered")
st.title("🛋️ Stamps Home Furniture Pricing Calculator")
st.markdown("**Easily determine your best selling price with automated calculations!**")

# Sidebar for inputs
st.sidebar.header("🛠️ Input Pricing Details")
vendor_price = st.sidebar.number_input("Enter Vendor Price ($)", min_value=0.0, step=0.01)
shipping_cost = st.sidebar.number_input("Enter Shipping Cost ($)", min_value=0.0, step=0.01)
markup_percentage = st.sidebar.slider("Select Markup Percentage (%)", 20, 60, 50)

if st.sidebar.button("💰 Calculate Price"):
    cogs, shopify_fees, final_price = calculate_final_price(vendor_price, shipping_cost, markup_percentage)
    
    # Display detailed breakdown with styled markdown
    st.markdown("### 📊 Pricing Breakdown")
    breakdown_data = {
        "Metric": ["Vendor Price", "Shipping Cost", "Total Cost (COGS)", "Markup Applied", "Shopify Fees (2.9% + $0.30)", "Final Selling Price"],
        "Value": [f"${vendor_price:.2f}", f"${shipping_cost:.2f}", f"${cogs:.2f}", f"{markup_percentage}%", f"${shopify_fees:.2f}", f"${final_price:.2f}"]
    }
    df = pd.DataFrame(breakdown_data)
    st.table(df)
    
    # Interactive chart for visualization
    fig = px.bar(df, x="Metric", y="Value", text="Value", title="Cost Breakdown", template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)
    
    # Final price callout
    st.success(f"### 🎯 Recommended Selling Price: **${final_price:.2f}**")
