import tabula  # simple wrapper for tabula-java, read tables from PDF into csv
import os

print("[-+-] Initializing PDF converter")
print("[-+-] Import the PDF")
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
print("[-+-] importing required packages for pdf_csv.py...")
# from modules.defaults import df # local module
print("[-+-] pdf_csv.py packages imported! \n")
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

def pdf_csv():  # convert pdf to csv
    print("default filenames:")
    # Insert the desired PDF nder filename
    filename = "arabic"
    pdf = filename + ".pdf"
    csv = filename + ".csv"
    print(pdf)
    print(csv + "\n")

    defaultdir = os.getcwd()
    print(defaultdir + "\n")

    pdf_path = os.path.join(defaultdir, pdf)
    csv_path = os.path.join(defaultdir, csv)
    print(pdf_path)
    print(csv_path + "\n")

    if os.path.exists(pdf_path) == True:  # check if the default pdf exists
        print("pdf found: " + pdf + "\n")
        pdf_flag = True
    else:
        print("Looking for another PDF...")
        add_pdf = [
            defaultdir for defaultdir in os.listdir()
            if defaultdir.endswith(".pdf")
        ]
        if len(add_pdf) == 1:
            print("PDF found: " + add_pdf[0] + "\n")
            pdf_path = os.path.join(defaultdir, add_pdf[0])
            pdf_flag = True
        elif len(add_pdf) > 1:
            print("It seems there are more than 1 PDFs present, exiting script!")
            pdf_flag = False
        else:
            print("pdf cannot be found, exiting script!")
            pdf_flag = False

    if pdf_flag == True:
        try:
            print("Looking for defaulkt csv")
            open(csv_path, "r")
            print("csv found: "  + csv + "\n")
        except IOError:
            print("")
            print("")
            open(csv_path, "w")
        
        print("")

        try:
            tabula.convert_into(pdf_path,
                                csv_path,
                                output_format = "csv",
                                pages = "all")
            print("")
        except IOError:
            print("PDF conversion failed!")
            print("Please insert a correct PDF into the directory")
        print("Converted csv file was found!!!")
        print("")

pdf_csv() # Run the program

