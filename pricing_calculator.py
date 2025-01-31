import streamlit as st

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

st.title("Stamps Home Furniture Pricing Calculator")

vendor_price = st.number_input("Enter Vendor Price ($)", min_value=0.0, step=0.01)
shipping_cost = st.number_input("Enter Shipping Cost ($)", min_value=0.0, step=0.01)
markup_percentage = st.slider("Select Markup Percentage (%)", 20, 60, 50)

if st.button("Calculate Price"):
    cogs, shopify_fees, final_price = calculate_final_price(vendor_price, shipping_cost, markup_percentage)
    
    # Display detailed breakdown
    st.subheader("📊 Pricing Breakdown")
    st.write(f"**Vendor Price:** ${vendor_price:.2f}")
    st.write(f"**Shipping Cost:** ${shipping_cost:.2f}")
    st.write(f"**Total Cost (COGS):** ${cogs:.2f}")
    st.write(f"**Markup Applied:** {markup_percentage}%")
    st.write(f"**Shopify Fees (2.9% + $0.30):** ${shopify_fees:.2f}")
    
    # Display Final Price
    st.success(f"**Recommended Selling Price: ${final_price:.2f}**")
