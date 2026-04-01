# ============================================
#       HOSPITAL MANAGEMENT SYSTEM
#       Developer: [Justina Mwango]
#       Date: 2026
# ============================================

from datetime import datetime

#Define the patient dictionary to store patient information
patients = {}
appointments= {}
appointment_counter = [1]


def add_patient():
    print("\n--- ADD NEW PATIENT ---")

    # --- Patient ID ---
    while True:
        patient_id = input("Enter Patient ID (e.g. P001): ").strip().upper()
        if patient_id == "":
            print("❌ Patient ID cannot be empty!")
        elif patient_id in patients:
            print("❌ That ID already exists! Please use a unique ID.")
        else:
            break
 
    # --- Full Name ---
    while True:
        name = input("Enter Full Name: ").strip()
        if name == "":
            print("❌ Patient name is required!")
        else:
            break

    # --- Age ---
    while True:
        age = input("Enter Age: ").strip()
        if age.isdigit() and int(age) > 0:
            age = int(age)
            break
        else:
            print("❌ Age should not be a negative digit")

    # --- Gender ---
    while True:
        gender = input("Enter Gender (Male/Female/Other): ").strip().capitalize()
        if gender in ["Male", "Female", "Other"]:
            break
        else:
            print("❌ Please enter Male, Female, or Other.")

    # --- Diagnosis ---
    while True:
        diagnosis = input("Enter Diagnosis (e.g Malaria): ").strip()
        if diagnosis == "":
            print("❌ Diagnosis cannot be empty!")
        else:
            break

    # --- Treatments ---
    treatments = {}
    print("\nEnter at least 2 treatments.")

    while len(treatments) < 2:
        remaining = 2 - len(treatments)
        print(f"  (You need at least {remaining} more treatment(s))")

        t_name = input("  Treatment name: ").strip()
        if t_name == "":
            print("  ❌ Treatment Field cannot be empty!")
            continue

        while True:
            t_cost = input(f"  Cost for {t_name}: ").strip()
            try:
                t_cost = float(t_cost)
                if t_cost <= 0:
                    print("  ❌ Cost must be a positive number!")
                else:
                    treatments[t_name] = t_cost
                    break
            except ValueError:
                print("  ❌ Please enter a valid digit price!")

    # --- Ask if they want to add more treatments ---
    while True:
        more = input("\nAdd another treatment? (yes/no): ").strip().lower()
        if more == "yes":
            t_name = input("  Treatment name: ").strip()
            if t_name == "":
                print("  ❌ Treatment name cannot be empty!")
                continue
            while True:
                t_cost = input(f"  Cost for {t_name}: ").strip()
                try:
                    t_cost = float(t_cost)
                    if t_cost <= 0:
                        print("  ❌ Cost must be a positive number!")
                    else:
                        treatments[t_name] = t_cost
                        break
                except ValueError:
                    print("  ❌  Invalid number!")
        elif more == "no":
            break
        else:
            print("❌ Please type yes or no.")

    # --- Save to dictionary with timestamp ---
    patients[patient_id] = {
        "name": name,
        "age": age,
        "gender": gender,
        "diagnosis": diagnosis,
        "treatments": treatments,
        "date_added": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    print(f"\n✅ Patient {name} added successfully on {patients[patient_id]['date_added']}!")


def view_all_patients():
    print("\n----- ALL PATIENTS -----")
    if len(patients) == 0:
        print("❌ No patients were registered.")
    
    print(f"{'ID':<10} {'Name':<25} {'Diagnosis':<20} {'Date Added':<25}")
    print("-" * 80)

    for patient_id, info in patients.items():
        print(f"{patient_id:<10} {info['name']:<25} {info['diagnosis']:<20} {info['date_added']:<25}")

    print(f"\nTotal Patients: {len(patients)}")


def view_patient_report():
    print("\n--- VIEW PATIENT REPORT ---")

    if len(patients) == 0:
        print("❌ No patients registered yet.")
        return

    patient_id = input("Enter Patient ID: ").strip().upper()

    if patient_id not in patients:
        print("❌ Patient not found!")
        return

    info = patients[patient_id]
    total_bill = sum(info['treatments'].values())

    print("\n" + "=" * 45)
    print(f"  PATIENT REPORT")
    print("=" * 45)
    print(f"  Patient ID  : {patient_id}")
    print(f"  Name        : {info['name']}")
    print(f"  Age         : {info['age']}")
    print(f"  Gender      : {info['gender']}")
    print(f"  Diagnosis   : {info['diagnosis']}")
    print(f"  Date Added  : {info['date_added']}")
    print("-" * 45)
    print(f"  {'TREATMENT':<25} {'COST (K)':<10}")
    print("-" * 45)

    for treatment, cost in info['treatments'].items():
        print(f"  {treatment:<25} K{cost:<10.2f}")

    print("-" * 45)
    print(f"  {'TOTAL BILL':<25} K{total_bill:<10.2f}")
    print("=" * 45)


def update_patient():
    print("\n--- UPDATE PATIENT ---")

    if len(patients) == 0:
        print("❌ No registered patients yet.")
        return

    patient_id = input("Enter Patient ID to update: ").strip().upper()

    if patient_id not in patients:
        print("❌ couldn't find Patient with that ID")
        return

    info = patients[patient_id]
    print(f"\nPatient found: {info['name']} | Diagnosis: {info['diagnosis']}")

    print("\nWhat would you like to update?")
    print("1. Update Diagnosis")
    print("2. Add New Treatment")
    print("3. Update Treatment Cost")
    print("4. Remove Treatment")

    sub_choice = input("Enter choice (1-4): ").strip()

    # --- Update Diagnosis ---
    if sub_choice == "1":
        print(f"Current Diagnosis: {info['diagnosis']}")
        while True:
            new_diagnosis = input("Enter new diagnosis: ").strip()
            if new_diagnosis == "":
                print("❌ Patient must be diagnosed with something")
            else:
                info['diagnosis'] = new_diagnosis
                print(f"✅ Diagnosis updated to '{new_diagnosis}' successfully!")
                break

    # --- Add New Treatment ---
    elif sub_choice == "2":
        while True:
            t_name = input("Enter new treatment name: ").strip()
            if t_name == "":
                print("❌ Treatment name cannot be empty!")
                continue
            if t_name in info['treatments']:
                print("❌ That treatment already exists! Use option 3 to update its cost.")
                break
            while True:
                t_cost = input(f"Enter cost for {t_name}: ").strip()
                try:
                    t_cost = float(t_cost)
                    if t_cost <= 0:
                        print("❌ Cost must be a positive number!")
                    else:
                        info['treatments'][t_name] = t_cost
                        print(f"✅ Treatment '{t_name}' added successfully!")
                        break
                except ValueError:
                    print("❌ Please enter a valid number!")
            break

    # --- Update Treatment Cost ---
    elif sub_choice == "3":
        if len(info['treatments']) == 0:
            print("❌ This patient has no treatments yet.")
            return

        print("\nCurrent Treatments:")
        for t_name, t_cost in info['treatments'].items():
            print(f"  - {t_name}: K{t_cost:.2f}")

        t_name = input("\nEnter treatment name to update: ").strip()
        if t_name not in info['treatments']:
            print("❌ Treatment not found!")
            return

        while True:
            t_cost = input(f"Enter new cost for {t_name}: ").strip()
            try:
                t_cost = float(t_cost)
                if t_cost <= 0:
                    print("❌ Cost must be a positive number!")
                else:
                    info['treatments'][t_name] = t_cost
                    print(f"✅ Cost for '{t_name}' updated to K{t_cost:.2f} successfully!")
                    break
            except ValueError:
                print("❌ Invalid number! Try Again")

    # --- Remove Treatment ---
    elif sub_choice == "4":
        if len(info['treatments']) <= 2:
            print("❌ Cannot remove treatment! A patient must have at least 2 treatments.")
            return

        print("\nCurrent Treatments:")
        for t_name, t_cost in info['treatments'].items():
            print(f"  - {t_name}: K{t_cost:.2f}")

        t_name = input("\nEnter treatment name to remove: ").strip()
        if t_name not in info['treatments']:
            print("❌ Treatment not found!")
            return

        del info['treatments'][t_name]
        print(f"✅ Treatment '{t_name}' removed successfully!")

    else:
        print("❌ Invalid choice!")



def delete_patient():
    print("\n--- DELETE PATIENT ---")

    if len(patients) == 0:
        print("❌ No patients registered yet.")
        return
    
    patient_id = input("Enter patient ID to delete: ").strip().upper()

    if patient_id not in patients:
        print("❌ Patient not found!")
        return
    
    name = patients[patient_id]['name']

    #--- Confirmation before deletion ---
    confirm = input(f"⚠️ Are you sure you want to delete {name}? (yes/no): ")

    if confirm == "yes":
        del patients[patient_id]
        print(f"☑️ patient {name} deteled successfully!")
    elif confirm == "no":
        print("❌ Deletion Cancelled.")
    else:
        print("❌ Invalid input, Deletion cancelled.")



def search_patient():
    print("\n--- SEARCH PATIENT ---")

    if len(patients) == 0:
        print("❌ No patients registered yet.")
        return
    
    keyword = input("Enter patient ID or name to search: ").strip().upper()
    
    results =[]

    for patient_id, info in patients.items():
        if keyword == patient_id or keyword in info['name'].upper():
            results.append((patient_id, info))

        if len(results) == 0:
            print("❌ No matching patients found!")
            return
        
        print(f"\n{len(results)} results(s) found:")
        print(f"{'ID':<10} {'Name':<20} {'Diagnosis':<20} {'Date Added':<25}")
        print("-" * 80)

        for patient_id, info in results:
            print(f"{patient_id:<10} {info['name']:25} {info['diagnosis']:<20} {info['date_added']:<25}")



def hospital_statistics():
    print("\n--- HOSPITAL STATISTICS ---")

    if len(patients) == 0:
        print("❌ No patients have been registered yet.")
        return

    total_patients = len(patients)
    total_revenue = 0
    highest_bill_patient = None
    lowest_bill_patient = None
    highest_bill = 0
    lowest_bill = float('inf')

    for patient_id, info in patients.items():
        bill = sum(info['treatments'].values())
        total_revenue += bill

        if bill > highest_bill:
            highest_bill = bill
            highest_bill_patient = (patient_id, info['name'])

        if bill < lowest_bill:
            lowest_bill = bill
            lowest_bill_patient = (patient_id, info['name'])

    print("\n" + "=" * 45)
    print("        HOSPITAL STATISTICS REPORT")
    print("=" * 45)
    print(f"  Total Patients        : {total_patients}")
    print(f"  Total Revenue         : K{total_revenue:.2f}")
    print("-" * 45)
    print(f"  Highest Bill Patient  : {highest_bill_patient[1]} ({highest_bill_patient[0]})")
    print(f"  Highest Bill Amount   : K{highest_bill:.2f}")
    print("-" * 45)
    print(f"  Lowest Bill Patient   : {lowest_bill_patient[1]} ({lowest_bill_patient[0]})")
    print(f"  Lowest Bill Amount    : K{lowest_bill:.2f}")
    print("=" * 45)

# I added an appointment feature to ensure patients can book appointments before being examined. 
# This would ensure that each patient has a set time for visiting medical personnels.

# --- SCHEDULE APPOINTMENT ---
def schedule_appointment():
    print("\n--- SCHEDULE APPOINTMENT ---")

    if len(patients) == 0:
        print("❌ No patients registered yet. Please add a patient first.")
        return

    # --- Select Patient ---
    patient_id = input("Enter Patient ID: ").strip().upper()
    if patient_id not in patients:
        print("❌ Patient not found!")
        return

    patient_name = patients[patient_id]['name']
    print(f"✅ Patient found: {patient_name}")

    # --- Doctor Name ---
    while True:
        doctor = input("Enter Doctor's Name: ").strip()
        if doctor == "":
            print("❌ Doctor name is required!")
        else:
            break

    # --- Appointment Date ---
    while True:
        date = input("Enter Appointment Date (e.g. 2026-04-15): ").strip()
        if date == "":
            print("❌ Date cannot be empty!")
        else:
            break

    # --- Appointment Time ---
    while True:
        time = input("Enter Appointment Time (e.g. 10:30 AM): ").strip()
        if time == "":
            print("❌ No that's not the right time format.")
        else:
            break

    # --- Reason ---
    while True:
        reason = input("Enter Reason for Visit: ").strip()
        if reason == "":
            print("❌ Incorrect reason cannot be empty!")
        else:
            break

    # --- Auto generate Appointment ID ---
    appointment_id = f"A{appointment_counter[0]:03d}"
    appointment_counter[0] += 1

    # --- Save Appointment ---
    appointments[appointment_id] = {
        "patient_id": patient_id,
        "patient_name": patient_name,
        "doctor": doctor,
        "date": date,
        "time": time,
        "reason": reason,
        "status": "Scheduled",
        "booked_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    print(f"\n✅ Appointment {appointment_id} scheduled for {patient_name} with Dr. {doctor} on {date} at {time}!")




def view_appointments():
    print("\n--- ALL APPOINTMENTS ---")

    if len(appointments) == 0:
        print("❌ No appointments scheduled yet.")
        return

    print(f"\n{'Appt ID':<10} {'Patient':<20} {'Doctor':<20} {'Date':<15} {'Time':<12} {'Status':<12}")
    print("-" * 90)

    for appt_id, appt in appointments.items():
        print(f"{appt_id:<10} {appt['patient_name']:<20} {appt['doctor']:<20} {appt['date']:<15} {appt['time']:<12} {appt['status']:<12}")

    print(f"\nTotal Appointments: {len(appointments)}")

    # --- Cancel Appointment ---
    print()
    cancel = input("Would you like to cancel an appointment? (yes/no): ").strip().lower()

    if cancel == "yes":
        appt_id = input("Enter Appointment ID to cancel (e.g. A001): ").strip().upper()

        if appt_id not in appointments:
            print("❌ Appointment ID not found!")
            return

        if appointments[appt_id]['status'] == "Cancelled":
            print("❌ That appointment is already cancelled!")
            return

        patient_name = appointments[appt_id]['patient_name']
        confirm = input(f"⚠️  Are you sure you want to cancel {patient_name}'s appointment? (yes/no): ").strip().lower()

        if confirm == "yes":
            appointments[appt_id]['status'] = "Cancelled"
            appointments[appt_id]['cancelled_on'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"✅ Appointment {appt_id} for {patient_name} has been cancelled!")
        elif confirm == "no":
            print("❌ Cancellation abandoned.")
        else:
            print("❌ Invalid input. Cancellation abandoned.")

    elif cancel == "no":
        return
    else:
        print("❌ Invalid input.")



def print_separator():
    print("-" * 45)

#Main menu function
def show_menu():
    print("\n=======MAIN MENU=======")
    print("1. Add Patient")
    print("2. View All Patients")
    print("3. View Patient Report")
    print("4. Update Patient")
    print("5. Delete Patient")
    print("6. Search Patient")
    print("7. Hospital Statistics")
    print("8. Schedule Appointment")
    print("9. View Appointments")
    print("10. Exit")
    print("===========================")





# --- MAIN PROGRAM LOOP ---
while True:
    show_menu()
    choice = input("Enter your choice (1-10): ").strip()

    if choice == "1":
        add_patient()
    elif choice == "2":
       view_all_patients()
    elif choice == "3":
        view_patient_report()
    elif choice == "4":
        update_patient()
    elif choice == "5":
        delete_patient()
    elif choice == "6":
        search_patient()
    elif choice == "7":
       hospital_statistics()
    elif choice == "8":
        schedule_appointment()
    elif choice == "9":
        view_appointments()
    elif choice == "10":
        print("\n" + "=" * 45)
        print("   Thank you for using Justina's Hospital System.")
        print(f"   Session ended: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("\nClosing system...")
        print("=" * 45)
        break
    else:
        print("❌ Invalid choice! Please enter a number between 1 and 10.")