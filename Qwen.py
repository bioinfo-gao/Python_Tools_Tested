import random

def show_ascii_art(choice):
    """显示对应选择的 ASCII 图像"""
    arts = {
        "石头": """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
        "剪刀": """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""",
        "布": """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
    }
    print(arts.get(choice, ""))

def main():
    choices = ["石头", "剪刀", "布"]  # 注意：这里用“剪刀”更符合常用词
    win_count = 0
    lose_count = 0
    tie_count = 0

    print("🎮 欢迎来到【石头剪刀布】游戏！")
    print("=" * 50)

    while True:
        # 显示选项图像
        print("\n请选择你的出拳（输入对应数字）：")
        print("1 → 石头")
        show_ascii_art("石头")
        print("2 → 剪刀")
        show_ascii_art("剪刀")
        print("3 → 布")
        show_ascii_art("布")
        print("0 → 退出游戏\n")

        user_input = input("请输入你的选择 (0/1/2/3)：").strip()

        if user_input == "0":
            print(f"\n🎉 游戏结束！总战绩 → 胜: {win_count} | 负: {lose_count} | 平: {tie_count}")
            print("👋 谢谢游玩！再见！")
            break

        if user_input not in ["1", "2", "3"]:
            print("❌ 无效输入！请重新输入 0、1、2 或 3。")
            continue

        # 映射数字到选择
        user_choice = choices[int(user_input) - 1]
        computer_choice = random.choice(choices)

        print("\n" + "="*30)
        print("🎮 你出的是：")
        show_ascii_art(user_choice)
        print(f"→ {user_choice}")

        print("\n🤖 计算机出的是：")
        show_ascii_art(computer_choice)
        print(f"→ {computer_choice}")
        print("="*30)

        # 判断胜负
        if user_choice == computer_choice:
            print("🤝 平局！")
            tie_count += 1
        elif (user_choice == "石头" and computer_choice == "剪刀") or \
             (user_choice == "剪刀" and computer_choice == "布") or \
             (user_choice == "布" and computer_choice == "石头"):
            print("🏆 你赢了！")
            win_count += 1
        else:
            print("😭 你输了！")
            lose_count += 1

        print(f"📊 当前战绩 → 胜: {win_count} | 负: {lose_count} | 平: {tie_count}")

if __name__ == "__main__":
    main()