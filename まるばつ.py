
from random import randint
#コンピュータを動作させるためにインポートした

class GM:
#ゲーム進行を担当する、メイン関数のようなもの
    def __init__(self):
        table = Table()
        while True:
            table.chose_num()
            table.put_koma()
            table.check_win_lose()
            if table.win_lose:
                break
        GM()
    
class White:
#player1　が使うこま
    def __repr__(self):
    #テーブルに表示される
        return "⚪️"
    
    def __str__(self):
    #プレイヤーの勝利判定に使用する
        return "⚪️"
    
class Black:
#player2　が使うこま
    def __repr__(self):
    #テーブルに表示される
        return "●"
    
    def __repr__(self):
    #プレイヤーの勝利判定に使用する
        return "●"
    
class Table:
#まるばつゲームに関する、変数とメソッドをまとめたクラス、GMクラスに管理される
    def __init__(self):
    
        self.table_condition=[
            None,
            [None,1,2,3],
            [None,4,5,6],
            [None,7,8,9],
            ]
        #テーブルの状況を保存する変数
        
        self.round = 1
        #ゲームのラウンド数を記録する
        self.win_lose = False
        #プレイヤーのいづれかが勝利した際にTRUEにする
        self.pl_num = None
        #プレイヤーがテーブルコンディションを変化させるときに使う
        self.pl_num_list = None
        #プレイヤーが選択した数を、実際に、テーブルに表示させるときに使う
    
    def chose_num(self):
    #テーブルコンディションを変化させる場所をプレイヤーに選択させる
    
            #print(f'¥\nラウンド{self.round}\n')
            # self.show_table()
            for _ in range(1):
                print("")
            
            print("〜まるばつゲーム〜")
            print("⚪️：あなた　●：コンピュータ")
            print("⚪️を三つ並べればあなたのかち")
            print("")
            
            
            if self.round % 2 ==1:
                self.show_table()
                print("")
                print("あなたの番、白駒をおこう")
                while True:
                    
                    try:
                        print("\n１から９で選んでください。下に入力してください")
                        for _ in range(1):
                            print("")
                        
                        self.pl_num = input('1~9:')
                        self.pl_num = int(self.pl_num)
                        
                    except:
                        for _ in range(4):
                            print("")
                        print('文字はエラーです。表示されている数のいづれかを打ち込んでください\n')
                        print("")
                        self.show_table()
                        continue
                    
                    
                    if not 1 <= self.pl_num <= 9:
                        for _ in range(4):
                            print("")
                        print('正しい数を打ち込んでください\n')
                        print("")
                        self.show_table()
                        continue
                                        
                    self.change_num()
                    x,y = self.pl_num_list
                    
                    if type(self.table_condition[x][y]) == type(White()) or type(self.table_condition[x][y]) == type(Black()):
                        for _ in range(4):
                            print("")
                        print("すでに埋められています,もう一度選んでください\n")
                        print("")
                        self.show_table()
                        continue
                    
                    else:
                        break                                      
                
            elif self.round % 2 ==0:
                print("\nコンピュータの番")
                while True:
                    self.pl_num = randint(1,9)
                    self.change_num()
                    x,y = self.pl_num_list
                    if type(self.table_condition[x][y]) == type(White()) or type(self.table_condition[x][y]) == type(Black()):
                        #print("すでに埋められています,もう一度選んでください")
                        continue
                                 
                    else:
                        break 
                
                print(f'コンピュータは{self.pl_num}を選んだ')
                
    def change_num(self):
    #f_chose_num から受け取ったpl_numをpl_num_listに変換する
        
            self.pl_num_list = []
            
            #リストのうちの一つ目のかず
            if 1 <= self.pl_num <= 3:
                self.pl_num_list.append(1)
            
            if 4 <= self.pl_num <= 6:
                self.pl_num_list.append(2)
            
            if 7 <= self.pl_num <= 9:
                self.pl_num_list.append(3)
            
            #リストのうちの２つ目の数
            mode_num = self.pl_num % 3
            if mode_num == 0:
                mode_num += 3

            self.pl_num_list.append(mode_num)

    def put_koma(self):
    #table_conditionを書き換える、選択されたプレイヤーと、場所に応じて     
            x,y = self.pl_num_list
            
            if self.round % 2 ==1:
                self.table_condition[x][y] = White()
                
            
            if self.round % 2 ==0:
                self.table_condition[x][y] = Black()
                
    def check_win_lose(self):
    #table_conditionからデータを取得し、プレイヤーの勝敗を判定する
    
        player1_win = ['⚪️', '⚪️','⚪️']
        player2_win = ['●',"●", '●'] 
        
        #行の勝敗を判定する
        for m in range(1,4):
            win_lose_list = []
            for n in range(1,4):
                win_lose_list.append(str(self.table_condition[m][n]))
            if win_lose_list == player1_win or win_lose_list == player2_win:
                self.win_lose = True
                break
            
        #列の勝敗を判定する
        for m in range(1,4):
            win_lose_list = []
            for n in range(1,4):
                win_lose_list.append(str(self.table_condition[n][m]))
            if win_lose_list == player1_win or win_lose_list == player2_win:
                self.win_lose = True
                break
        
        #右下がり斜めの勝敗を判定する
        win_lose_list = []
        for m in range(1,4):
            win_lose_list.append(str(self.table_condition[m][m]))
        if win_lose_list == player1_win or win_lose_list == player2_win:
                self.win_lose = True
        
        #右あがり斜めの勝敗を判定する
        num_list = [1,2,3]
        win_lose_list = []
        for m in range(1,4):
            x = num_list.pop()
            win_lose_list.append(str(self.table_condition[x][m]))
        if win_lose_list == player1_win or win_lose_list == player2_win:
                self.win_lose = True
        
        #どちらかのプレイヤーが以上の条件のいづれかを満たしたとき、勝者に応じで、勝利を宣言する
        if self.win_lose:

                if self.round % 2 ==1:
                    print('Player1の勝利')
                    
                if self.round % 2 ==0:
                    print('Player2の勝利')
                    
        else:
            self.round += 1
            
            
    def show_table(self):
    #テーブルコンディションに基づいた、テーブルを表示する
        
        #一度、テーブルコンディション（二次元リスト）を一次元リストであるgame_condition_tableに変換して、それを、
        #tableに当てはめることで、tableを表示させる。
        
        self.game_conditon_for_tabel=[None]
        
        for i in range(1,4):
            for i, line in enumerate(self.table_condition[i]):
                if i == 0:
                    continue
                else:
                    self.game_conditon_for_tabel.append(line)
        
        self.table = [
        [f" {self.game_conditon_for_tabel[1]}  | {self.game_conditon_for_tabel[2]}  | {self.game_conditon_for_tabel[3]}  "],
        [f"--------------"],
        [f" {self.game_conditon_for_tabel[4]}  | {self.game_conditon_for_tabel[5]}  | {self.game_conditon_for_tabel[6]}  "],
        [f"--------------"],
        [f" {self.game_conditon_for_tabel[7]}  | {self.game_conditon_for_tabel[8]}  | {self.game_conditon_for_tabel[9]}  "]
        ]
        
        for _ in self.table:
            print(_[0])
      
if __name__ == '__main__':
    GM()
    

