name = input("请输入姓名:")

# score1为数值,需要参与数学计算,使用eval()函数
score1 = eval(input("请输入科目1成绩:"))
score2 = eval(input("请输入科目2成绩:"))
print("\n您的总成绩是:", (score1 + score2))
