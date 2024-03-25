def elo_rating(rating_a, rating_b, result_a, k_factor=32):
  """
  ฟังก์ชั่นนี้ใช้หา Elo Rating ใหม่ของทีม A และ B 

  Args:
    rating_a: Elo Rating ปัจจุบันของทีม A
    rating_b: Elo Rating ปัจจุบันของทีม B
    result_a: ผลลัพธ์ของทีม A (1 = ชนะ, 0.5 = เสมอ, 0 = แพ้)
    k_factor: ค่า K-factor (ค่าเริ่มต้น = 32)

  Returns:
    Elo Rating ใหม่ของทีม A และ B (ตามลำดับ)
  """

  expected_score_a = 1 / (1 + 10 ** ((rating_b - rating_a) / 400))
  expected_score_b = 1 - expected_score_a

  new_rating_a = rating_a + k_factor * (result_a - expected_score_a)
  new_rating_b = rating_b + k_factor * ((1 - result_a) - expected_score_b)

  return new_rating_a, new_rating_b

# ตัวอย่างการใช้งาน
rating_a = int(input("Elo Rating ปัจจุบันของทีม A: "))
rating_b = int(input("Elo Rating ปัจจุบันของทีม B: "))
result_a = float(input("ผลลัพธ์ของทีม A (1 = ชนะ, 0.5 = เสมอ, 0 = แพ้): "))

new_rating_a, new_rating_b = elo_rating(rating_a, rating_b, result_a)

print(f"Elo Rating ใหม่ของทีม A: {new_rating_a}")
print(f"Elo Rating ใหม่ของทีม B: {new_rating_b}")
