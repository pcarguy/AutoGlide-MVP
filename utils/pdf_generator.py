from fpdf import FPDF
import io

def generate_pdf(details, name, email, phone, year, make, model, notes):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="AutoGlide Transport Quote", ln=1, align='C')
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Name: {name}", ln=1)
    pdf.cell(200, 10, txt=f"Email: {email}", ln=1)
    pdf.cell(200, 10, txt=f"Phone: {phone}", ln=1)
    pdf.ln(5)
    pdf.cell(200, 10, txt=f"Vehicle: {year} {make} {model}", ln=1)
    pdf.cell(200, 10, txt=f"Pickup ZIP: {details['pickup']}", ln=1)
    pdf.cell(200, 10, txt=f"Delivery ZIP: {details['delivery']}", ln=1)
    pdf.cell(200, 10, txt=f"Transport Type: {details['transport_type']}", ln=1)
    pdf.cell(200, 10, txt=f"Pickup Date: {details['pickup_date']}", ln=1)
    pdf.cell(200, 10, txt=f"Estimated Quote: ${details['quote']}", ln=1)
    if notes:
        pdf.ln(5)
        pdf.multi_cell(200, 10, txt=f"Special Instructions:\n{notes}")

    pdf_output = io.BytesIO()
    pdf.output(pdf_output)
    return pdf_output.getvalue()
