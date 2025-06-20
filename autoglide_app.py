import streamlit as st
from utils.quote_engine import calculate_quote
from utils.pdf_generator import generate_pdf

st.set_page_config(page_title="AutoGlide", layout="centered")

st.markdown(
    "<h1 style='color:#1DB954;'>AutoGlide</h1><h4 style='color:#B3B3B3;'>Nationwide vehicle shipping, simplified.</h4>",
    unsafe_allow_html=True,
)
st.markdown("---")

with st.form("quote_form"):
    st.subheader("Get Your Quote")
    pickup = st.text_input("Pickup ZIP Code")
    delivery = st.text_input("Delivery ZIP Code")
    vehicle_type = st.selectbox("Vehicle Type", ["Sedan", "SUV", "Truck", "Van"])
    transport_type = st.selectbox("Transport Type", ["Open", "Enclosed", "Inoperable", "Expedited"])
    pickup_date = st.date_input("Pickup Date")

    submitted = st.form_submit_button("Calculate Quote")

if submitted:
    if pickup and delivery:
        quote = calculate_quote(pickup, delivery, vehicle_type, transport_type)
        st.success(f"Estimated Quote: ${quote:,}")
        st.session_state['quote_details'] = {
            "pickup": pickup,
            "delivery": delivery,
            "vehicle_type": vehicle_type,
            "transport_type": transport_type,
            "pickup_date": pickup_date,
            "quote": quote
        }
        st.button("Continue to Booking", on_click=lambda: st.session_state.update({"show_booking": True}))
    else:
        st.warning("Please enter both ZIP codes.")

if st.session_state.get("show_booking"):
    st.markdown("---")
    st.subheader("Book Your Transport")

    with st.form("booking_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        phone = st.text_input("Phone Number")
        year = st.text_input("Vehicle Year")
        make = st.text_input("Vehicle Make")
        model = st.text_input("Vehicle Model")
        notes = st.text_area("Special Instructions (optional)")
        confirm = st.form_submit_button("Confirm Booking")

    if confirm:
        details = st.session_state['quote_details']
        pdf = generate_pdf(details, name, email, phone, year, make, model, notes)
        st.success("Booking confirmed! Your PDF is ready.")
        st.download_button("Download PDF", data=pdf, file_name="AutoGlide_Quote.pdf")
