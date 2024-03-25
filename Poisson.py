def poisson_probability(goals_for, goals_against, goals_scored):
  """
  ฟังก์ชั่นนี้ใช้หาโอกาสชนะเป็นเปอร์เซ็นในฟุตบอลโดยใช้สูตร Poisson

  Args:
    goals_for: ค่าเฉลี่ยของประตูที่ทีมยิงได้ต่อเกม
    goals_against: ค่าเฉลี่ยของประตูที่ทีมเสียต่อเกม
    goals_scored: จำนวนประตูที่ทีมคาดว่าจะยิงได้

  Returns:
    โอกาสชนะเป็นเปอร์เซ็น
  """

  import math

  # หาค่า λ (แลมด้า)
  lambda_value = goals_for

  # หาค่า μ (มิว)
  mu_value = goals_against

  # หาค่า e
  e = math.exp(1)

  # หาค่า k (จำนวนประตูที่ทีมคาดว่าจะยิงได้)
  k = goals_scored

  # หาค่า factorial (แฟกทอเรียล)
  factorial_k = math.factorial(k)

  # หาโอกาสชนะ
  probability = (math.pow(e, -lambda_value) * math.pow(lambda_value, k)) / factorial_k

  # แปลงค่าโอกาสชนะเป็นเปอร์เซ็น
  percentage = probability * 100

  return percentage

# ตัวอย่างการใช้งาน
goals_for = float(input("ประตูที่ทีมยิงได้เฉลี่ยต่อเกม: "))
goals_against = float(input("ประตูที่ทีมเสียเฉลี่ยต่อเกม: "))
goals_scored = int(input("จำนวนประตูที่ทีมคา "))


probability = poisson_probability(goals_for, goals_against, goals_scored)

print(f"โอกาสชนะ: {probability:.2f}%")
