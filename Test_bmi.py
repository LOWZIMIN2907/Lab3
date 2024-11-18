from Lab2.bmi import calculate_bmi #calculate_bmi is a function under the file 'bmi.py'

def test_bmi_under_weight():
    # Test for BMI value that should be classified as "Under Weight"
    assert calculate_bmi(1.8, 50) == -1

def test_bmi_normal_weight():
    # Test for BMI value that should be classified as "Normal Weight"
    assert calculate_bmi(1.75, 70) == 0

def test_bmi_over_weight():
    # Test for BMI value that should be classified as "Over Weight"
    assert calculate_bmi(1.6, 80) == 1