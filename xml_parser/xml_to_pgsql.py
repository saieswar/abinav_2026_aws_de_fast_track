import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="healthcare_db",
    user="postgres",
    password="Eswar@123",
    port=5432
)

# Create cursor
cur = conn.cursor()

print("Connected to PostgreSQL!")


from lxml import etree
import glob

# Namespace
ns = {
    "hc": "urn:hl7-org:v3"
}

# Get all XML files from folder
xml_files = glob.glob("*.xml")

# Loop through each XML file
for file in xml_files:

    print("\nProcessing file:", file)

    # Parse XML
    tree = etree.parse(file)
    root = tree.getroot()

    # Extract Member ID
    member_id = root.xpath(
        "//hc:recordTarget/hc:patientRole/hc:id/@extension",
        namespaces=ns
    )

    # Extract First Name
    first_name = root.xpath(
        "//hc:patient/hc:name/hc:given/text()",
        namespaces=ns
    )

    # Extract Last Name
    last_name = root.xpath(
        "//hc:patient/hc:name/hc:family/text()",
        namespaces=ns
    )

    # Extract DOB
    dob = root.xpath(
        "//hc:patient/hc:birthTime/@value",
        namespaces=ns
    )

    # Extract Gender
    gender = root.xpath(
        "//hc:patient/hc:administrativeGenderCode/@code",
        namespaces=ns
    )

    # Convert XPath lists into individual values
    member_id = member_id[0] if member_id else None
    first_name = first_name[0] if first_name else None
    last_name = last_name[0] if last_name else None
    dob = dob[0] if dob else None
    gender = gender[0] if gender else None

    # Print extracted information
    print("Member ID:", member_id)
    print("First Name:", first_name)
    print("Last Name:", last_name)
    print("DOB:", dob)
    print("Gender:", gender)

    # INSERT INSIDE THE LOOP
    if member_id:

        cur.execute("""
            INSERT INTO patients (
                member_id,
                first_name,
                last_name,
                dob,
                gender
            )
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (member_id)
            DO UPDATE SET
                first_name = EXCLUDED.first_name,
                last_name = EXCLUDED.last_name,
                dob = EXCLUDED.dob,
                gender = EXCLUDED.gender;
        """, (
            member_id,
            first_name,
            last_name,
            dob,
            gender
        ))

        print("Patient inserted/updated!")

    else:
        print("Member ID missing. Skipping insert.")

# Commit AFTER the loop
conn.commit()

print("\nAll records saved to PostgreSQL!")