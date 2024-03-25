def fair_betting_odds(odds_team_a, odds_draw, odds_team_b):
  """
  ฟังก์ชั่นนี้ใช้หาโอกาสชนะเป็นเปอร์เซ็นของแต่ละทีมในการแข่งขันฟุตบอลโดยใช้สูตร Fair Betting Odds

  Args:
    odds_team_a: ราคาต่อรองของทีม A (Decimal Odds)
    odds_draw: ราคาต่อรองของผลเสมอ (Decimal Odds)
    odds_team_b: ราคาต่อรองของทีม B (Decimal Odds)

  Returns:
    โอกาสชนะเป็นเปอร์เซ็นของทีม A, ผลเสมอ, และทีม B (ตามลำดับ)
  """

  # หาโอกาสชนะเป็น Decimal Odds
  probability_win_a = 1 / odds_team_a
  probability_draw = 1 / odds_draw
  probability_win_b = 1 / odds_team_b

  # แปลงโอกาสชนะเป็นเปอร์เซ็น
  percentage_win_a = probability_win_a * 100
  percentage_draw = probability_draw * 100
  percentage_win_b = probability_win_b * 100

  return percentage_win_a, percentage_draw, percentage_win_b

# ตัวอย่างการใช้งาน
odds_team_a = float(input("ราคาต่อรองของทีม A (Decimal Odds): "))
odds_draw = float(input("ราคาต่อรองของผลเสมอ (Decimal Odds): "))
odds_team_b = float(input("ราคาต่อรองของทีม B (Decimal Odds): "))

percentage_win_a, percentage_draw, percentage_win_b = fair_betting_odds(odds_team_a, odds_draw, odds_team_b)

print(f"โอกาสชนะทีม A: {percentage_win_a:.2f}%")
print(f"โอกาสเสมอ: {percentage_draw:.2f}%")
print(f"โอกาสชนะทีม B: {percentage_win_b:.2f}%")
