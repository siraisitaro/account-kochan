import random
import time

class ChurchGame:
    def __init__(self):
        # --- 初期ステータス（盛岡の開拓教会レベル） ---
        self.church_name = "盛岡開拓伝道所"
        self.money = 100000  # 初期資金：10万円
        self.believers = 5   # 初期信徒：5人
        self.week = 1        # 経過週数
        
        # --- 設備パラメータ ---
        self.capacity = 10   # 収容人数（最初は狭い）
        self.charm = 10      # 教会の魅力（高いほど新規が来る）
        self.pastor_skill = 10 # 牧師の説教力（高いほど献金が増える）

    def show_status(self):
        """現在の教会ステータスを表示"""
        print(f"\n=== {self.church_name} (第{self.week}週) ===")
        print(f"💰 資金: ¥{self.money:,}")
        print(f"👥 信徒: {self.believers}人 / 収容: {self.capacity}人")
        print(f"✨ 魅力: {self.charm} | 🎤 説教力: {self.pastor_skill}")
        print("===============================")

    def hold_service(self):
        """【コマンド1】主日礼拝を行う（メインループ）"""
        print(f"\n✝️ 第{self.week}週の主日礼拝を行います...")
        time.sleep(1) # 演出ウェイト

        # 1. 来会者数の計算（信徒数とキャパシティの小さい方）
        attendees = min(self.believers, self.capacity)
        
        # キャパオーバーの機会損失
        if self.believers > self.capacity:
            loss = self.believers - self.capacity
            print(f"⚠️ 会堂が狭すぎて、{loss}人が帰ってしまいました！")

        # 2. 献金計算（基本単価1000円 + 説教力ボーナス + ランダム幅）
        base_offering = 1000
        offering_per_person = base_offering + (self.pastor_skill * 10) + random.randint(-100, 100)
        total_income = attendees * offering_per_person
        
        self.money += total_income
        print(f"  -> {attendees}人が礼拝に出席しました。")
        print(f"  -> 本日の献金総額: ¥{total_income:,} GET!")

        # 3. 新規来会者判定（魅力依存）
        # 魅力値%の確率で新規が増える（上限あり）
        new_comers = 0
        if random.randint(1, 100) <= self.charm:
            new_comers = random.randint(1, 3) # 1〜3人増える
            self.believers += new_comers
            print(f"  -> ✨ 素晴らしい礼拝でした！ 新しい信徒が{new_comers}人増えました！")
        else:
            print("  -> 新しい来会者はいませんでした...")

        self.week += 1

    def invest_facility(self):
        """【コマンド2】設備投資メニュー"""
        while True:
            print("\n--- 🔨 設備投資メニュー ---")
            print("1. パイプ椅子追加 (¥50,000) -> 収容+5")
            print("2. 音響機材購入 (¥100,000) -> 魅力+5")
            print("3. 神学書購入 (¥30,000) -> 説教力+2")
            print("0. 戻る")
            
            choice = input("投資を選択してください: ")
            
            if choice == "1":
                if self.money >= 50000:
                    self.money -= 50000
                    self.capacity += 5
                    print("🔨 パイプ椅子を並べました！より多くの人を呼べます！")
                else:
                    print("❌ 資金が足りません！")
            
            elif choice == "2":
                if self.money >= 100000:
                    self.money -= 100000
                    self.charm += 5
                    print("🔨 スピーカーを新調しました！若者が興味を持ちそうです！")
                else:
                    print("❌ 資金が足りません！")

            elif choice == "3":
                if self.money >= 30000:
                    self.money -= 30000
                    self.pastor_skill += 2
                    print("🔨 牧師が勉強しました！説教に深みが出ました！")
                else:
                    print("❌ 資金が足りません！")
            
            elif choice == "0":
                break
            else:
                print("無効な選択です。")

    def run(self):
        """ゲーム実行"""
        print("✝️ 教会経営シミュレーション『Pro Church』へようこそ！")
        while True:
            self.show_status()
            print("1: 主日礼拝を行う（週を進める）")
            print("2: 設備投資を行う")
            print("3: ゲーム終了")
            
            cmd = input("コマンドを選択 > ")
            
            if cmd == "1":
                self.hold_service()
            elif cmd == "2":
                self.invest_facility()
            elif cmd == "3":
                print("ゲームを終了します。お疲れ様でした！")
                break
            else:
                print("無効なコマンドです。")

# --- 実行 ---
if __name__ == "__main__":
    game = ChurchGame()
    game.run()
