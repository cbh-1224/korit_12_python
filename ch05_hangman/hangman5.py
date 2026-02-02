import random

word_list = [
    # A (20)
    "able","about","above","accept","across","act","action","active","add","afraid",
    "after","again","age","agree","air","alive","allow","alone","already","also",

    # B (20)
    "baby","back","bad","balance","ball","band","base","basic","beach","bear",
    "beautiful","because","become","begin","behind","believe","below","best","better","between",

    # C (20)
    "call","calm","care","carry","catch","center","chance","change","child","choose",
    "circle","city","class","clean","clear","close","cloud","color","come","common",

    # D (20)
    "dance","dark","data","day","decide","deep","develop","different","difficult","direction",
    "discover","distance","doctor","dog","door","dream","drive","drop","during","duty",

    # E (20)
    "each","early","earth","easy","eat","education","effect","egg","eight","either",
    "electric","else","end","enemy","energy","enjoy","enough","enter","equal","even",

    # F (20)
    "face","fact","fall","family","famous","fast","father","fear","feel","field",
    "fight","final","find","finish","fire","first","fish","follow","food","forest",

    # G (20)
    "game","garden","general","get","girl","give","glass","go","goal","gold",
    "good","government","great","green","ground","group","grow","guess","guide","gun",

    # H (20)
    "habit","half","hand","happen","happy","hard","health","hear","heart","heavy",
    "help","here","high","history","hold","home","hope","horse","hospital","human",

    # I (20)
    "idea","important","interest","inside","instead","iron","island","issue","item","imagine",
    "increase","industry","information","invite","include","instant","introduce","ill","improve","independent",

    # J (20)
    "job","join","judge","jump","just","journey","joy","joke","jungle","junior",
    "justice","jeans","jacket","jelly","January","July","June","journal","jealous","jog",

    # K (20)
    "keep","key","kick","kid","kill","kind","king","kitchen","knee","knife",
    "know","knowledge","koala","korea","keyboard","kite","knock","kettle","kitten","kilo",

    # L (20)
    "language","large","last","late","laugh","learn","leave","left","lesson","letter",
    "level","life","light","like","line","listen","little","live","long","love",

    # M (20)
    "machine","main","make","man","many","market","matter","mean","measure","meet",
    "member","memory","middle","milk","mind","minute","money","month","moon","mountain",

    # N (20)
    "name","nation","nature","near","necessary","need","never","new","night","noise",
    "normal","north","note","nothing","notice","number","nurse","nut","network","now",

    # O (20)
    "object","ocean","offer","office","often","oil","old","once","only","open",
    "operate","opinion","order","other","outside","over","own","owner","oxygen","orange",

    # P (20)
    "page","pain","pair","paper","parent","part","party","pass","peace","people",
    "perfect","period","person","phone","picture","place","plan","plant","play","point",

    # Q (20)
    "quality","question","quick","quiet","quite","queen","quarter","quiz","quote","queue",
    "quantity","quickly","quit","quake","quarrel","quilt","quizmaster","quotation","quest","queueing",

    # R (20)
    "race","rain","raise","reach","read","ready","real","reason","receive","record",
    "remember","repeat","reply","rest","result","rich","right","river","road","rock",

    # S (20)
    "safe","same","save","school","science","sea","second","see","seem","sense",
    "sentence","serious","serve","set","share","ship","short","show","simple","since",

    # T (20)
    "table","take","talk","teach","team","tell","test","than","thank","that",
    "their","there","thing","think","time","today","together","town","travel","true"
]

chosen_word = random.choice(word_list)
print(chosen_word)
display = []

for _ in range(len(chosen_word)):
    display.append('_')

logo = '''
                                                                                      
                                                                                      
  ,---,                                                 ____                          
,--.' |                                               ,'  , `.                        
|  |  :                      ,---,                 ,-+-,.' _ |                 ,---,  
:  :  :                  ,-+-. /  |  ,----._,.  ,-+-. ;   , ||             ,-+-. /  | 
:  |  |,--.  ,--.--.    ,--.'|'   | /   /  ' / ,--.'|'   |  || ,--.--.    ,--.'|'   | 
|  :  '   | /       \  |   |  ,"' ||   :     ||   |  ,', |  |,/       \  |   |  ,"' | 
|  |   /' :.--.  .-. | |   | /  | ||   | .\  .|   | /  | |--'.--.  .-. | |   | /  | | 
'  :  | | | \__\/: . . |   | |  | |.   ; ';  ||   : |  | ,    \__\/: . . |   | |  | | 
|  |  ' | : ," .--.; | |   | |  |/ '   .   . ||   : |  |/     ," .--.; | |   | |  |/  
|  :  :_:,'/  /  ,.  | |   | |--'   `---`-'| ||   | |`-'     /  /  ,.  | |   | |--'   
|  | ,'   ;  :   .'   \|   |/       .'__/\_: ||   ;/        ;  :   .'   \|   |/       
`--''     |  ,     .-./'---'        |   :    :'---'         |  ,     .-./'---'        
           `--`---'                  \   \  /                `--`---'                 
                                      `--`-'                                          
'''
print(logo)

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

lives = 6
end_of_game = False

while not end_of_game:
    print(stages[lives])
    print(' '.join(display))
    print(f'기회가 {lives} 번 남았습니다.')
    print()
    guess = input('알파벳을 추측해서 입력하세요 >>> ').lower()

    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess
    print(f'기회가 {lives} 번 남았습니다.')

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            print(stages[lives])
            print(f'모든 기회를 잃었습니다.')
            end_of_game = True
            print(f'정답은 {chosen_word}입니다.')

    if '_' not in display:
        print()
        print(' '.join(display))
        print('정답입니다 !!')
        end_of_game = True