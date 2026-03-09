from fpdf import FPDF
from fpdf.enums import Align


def main():
    student_name = get_name()
    shirtificate_pdf = create_shirtificate_pdf()
    customise_shirtificate(shirtificate_pdf, student_name)


def get_name():
    return input("What is your name?: ").strip()


def create_shirtificate_pdf():
    shirtificate = FPDF()
    return shirtificate


def customise_shirtificate(pdf: FPDF, student_name: str):
    pdf.add_page()
    pdf.set_font("helvetica", style="B", size=50)
    pdf.set_y(y=25)
    pdf.cell(w=190, h=10, text="CS50 Shirtificate", align="C")
    pdf.image(name="shirtificate.png", x=Align.C, y=60, keep_aspect_ratio=True)
    pdf.set_y(y=125)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("helvetica", style="B", size=28)
    pdf.cell(w=190, h=10, text=student_name + " took CS50", align="C")
    return pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
