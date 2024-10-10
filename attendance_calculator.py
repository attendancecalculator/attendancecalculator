# Function to calculate attendance percentage
def calculate_attendance(attended_classes, total_classes):
    # Avoid division by zero
    if total_classes == 0:
        return 0
    attendance_percentage = (attended_classes / total_classes) * 100
    return attendance_percentage

# Function to check if the student meets the minimum required attendance
def check_attendance_eligibility(attendance_percentage, min_required=75):
    if attendance_percentage >= min_required:
        return True
    else:
        return False

# Input: Number of classes attended and total classes held
attended_classes = int(input("Enter the number of classes attended: "))
total_classes = int(input("Enter the total number of classes held: "))

# Calculate the attendance percentage
attendance_percentage = calculate_attendance(attended_classes, total_classes)

# Check if the student is eligible
is_eligible = check_attendance_eligibility(attendance_percentage)

# Output the results
print(f"Attendance Percentage: {attendance_percentage:.2f}%")
if is_eligible:
    print("You are eligible.")
else:
    print("You are not eligible due to low attendance.")
