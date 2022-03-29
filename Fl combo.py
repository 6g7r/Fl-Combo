from colorama import Fore
import os,random
clear = lambda: os.system('cls')
clear()

print(f"{Fore.GREEN}<<+>> {Fore.RESET}By insta : @6g7r")
print(f"""{Fore.LIGHTMAGENTA_EX}

       ／⌒ヽ.    [<?>] What is this tool?
　　　/° ω°.           [<=>] This tool will help you choose a 
　＿ノ ヽ　ノ ＼＿.    [<=>] specific number from the big combo
`/　`/ ⌒Ｙ⌒ Ｙ　ヽ 
( 　(三ヽ人　 /　　  |
|　ﾉ⌒＼ ￣￣ヽ　 ノ
ヽ＿＿＿＞､＿＿_／
　　 ｜( 王 ﾉ〈
　　 /ﾐ`ー―彡ヽ
　　/　ヽ_／　 |.

""")
class Ready:
  def __init__(self):
    self.name_file=input('<<+>> Name File : ')
    self.How_many=int(input("<<+>> How many do you want :"))
    self.combo=open(f"{self.name_file}.txt").read().splitlines()
    self.Done=0
  def start(self):
    for i in range(self.How_many):
      empa= str(random.choice(self.combo))
      with open(f"combo{self.How_many}.txt", "a") as mix:
        mix.write(f"{empa}\n")
        mix.close()
if __name__ == '__main__':
  m=Ready()
  m.start()

  
  
