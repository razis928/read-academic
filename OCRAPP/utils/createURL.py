from django.urls import reverse

def create_url(idCard_number, matric_total_marks, matric_obtained_marks, matric_percentage, student_name, father_name, date_of_birth, martic_roll_no, martic_board, fsc_total_marks, fsc_obtained_marks, fsc_percentage, fsc_board, fsc_roll_no):
    print(">>>>> URL created")
    return reverse('form') + f'?idCard_number={idCard_number}&total_marks={matric_total_marks}&obtained_marks={matric_obtained_marks}&percentage={matric_percentage}&student_name={student_name}&father_name={father_name}&date_of_birth={date_of_birth}&roll_no={martic_roll_no}&board={martic_board}&fsc_total_marks={fsc_total_marks}&fsc_obtained_marks={fsc_obtained_marks}&fsc_percentage={fsc_percentage}&fsc_board={fsc_board}&fsc_roll_no={fsc_roll_no}'