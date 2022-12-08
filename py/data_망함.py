'''
eng = {'a': ('a', 'i', 'u', 'e', 'o'),
       'ka': ('ka', 'ki', 'ku', 'ke', 'ko'),
       'sa': ('sa', 'shi', 'su', 'se', 'so'),
       'ta': ('ta', 'chi', 'tsu', 'te', 'to'),
       'na': ('na', 'ni', 'nu', 'ne', 'no'),
       'ha': ('ha', 'hi', 'hu', 'he', 'ho'),
       'ma': ('ma', 'mi', 'mu', 'me', 'mo'),
       'ya': ('ya', 'yu', 'yo', '', ''),
       'ra': ('ra', 'ri', 'ru', 're', 'ro'),
       'wa': ('wa', 'wo', 'ng', '', ''),
       }
kor = {'a': ('아', '이', '우', '에', '오'),
       'k': ('카', '키', '쿠', '케', '코'),
       's': ('사', '시', '스', '세', '소'),
       't': ('타', '치', '츠', '테', '토'),
       'n': ('나', '니', '누', '네', '노'),
       'h': ('하', '히', '후', '헤', '호'),
       'm': ('마', '미', '무', '메', '모'),
       'y': ('야', '유', '요'),
       'r': ('라', '리', '루', '레', '로'),
       'w': ('와'),
       'g': ('가', '기', '구', '게', '고'),
       'j': ('자', '지', '즈', '제', '조'),
       'd': ('다', '디', '드', '데', '도'),
       'b': ('바', '비', '부', '베', '보'),
       'p': ('파', '피', '푸', '페', '포'),
       '받': ('ㅇ', 'ㄴ', 'ㄱ', 'ㅅ'),
       '조사': ('ㅇㅗ', 'ㅎㅏ', 'ㅇㅘ'),
       }
jap = {'a': ('あ', 'い', 'う', 'え', 'お'),
       'k': ('か', 'き', 'く', 'け', 'こ'),
       's': ('さ', 'し', 'す', 'せ', 'そ'),
       't': ('た', 'ち', 'つ', 'て', 'と'),
       'n': ('な', 'に', 'ぬ', 'ね', 'の'),
       'h': ('は', 'ひ', 'ふ', 'へ', 'ほ'),
       'm': ('ま', 'み', 'む', 'め', 'も'),
       'y': ('や', 'ゆ', 'よ'),
       'r': ('ら', 'り', 'る', 'れ', 'ろ'),
       'w': ('わ'),
       'g': ('が', 'ぎ', 'ぐ', 'げ', 'ご'),
       'j': ('ざ', 'じ', 'ず', 'ぜ', 'ぞ'),
       'd': ('だ', 'ぢ', 'づ', 'で', 'ど'),
       'b': ('ば', 'び', 'ぶ', 'べ', 'ぼ'),
       'p': ('ぱ', 'ぴ', 'ぷ', 'ぺ', 'ぽ'),
       '받': ('ん', 'ん', 'っ', 'っ'),
       '요': ('ゃ', 'ゅ', 'ょ'),
       '조사':('を', 'は', 'は'),
       }
'''
# kor # 우 쿠 누 후 무 루 구 부 푸
kor = [' ','아', '이', '으', '에', '오',
       '카', '키', '크', '케', '코',
       '사', '시', '스', '세', '소',
       '타', '치', '츠', '테', '토', '차', '체', '초',
       '나', '니', '느', '네', '노',
       '하', '히', '흐', '헤', '호',
       '마', '미', '므', '메', '모',
       '야', '유', '요',
       '라', '리', '르', '레', '로',
       '와',
       '가', '기', '그', '게', '고',
       '자', '지', '즈', '제', '조',
       '다', '디', '드', '데', '도',
       '바', '비', '브', '베', '보',
       '파', '피', '프', '페', '포',
       'ㅇ', 'ㄴ', 'ㄱ', 'ㅅ',
       'ㅑ', 'ㅠ', 'ㅛ',
       #'ㅗ', 'ㅏ', 'ㅘ',]
       ]
# jap
jap = ['-', 'あ', 'い', 'う', 'え', 'お',
       'か', 'き', 'く', 'け', 'こ',
       'さ', 'し', 'す', 'せ', 'そ', ############################
       'た', 'ち', 'つ', 'て', 'と', 'た', 'て', 'と',
       'な', 'に', 'ぬ', 'ね', 'の',
       'は', 'ひ', 'ふ', 'へ', 'ほ', ##########################
       'ま', 'み', 'む', 'め', 'も',
       'や', 'ゆ', 'よ',
       'ら', 'り', 'る', 'れ', 'ろ',
       'わ',
       'が', 'ぎ', 'ぐ', 'げ', 'ご',
       'ざ', 'じ', 'ず', 'ぜ', 'ぞ', ############################
       'だ', 'ぢ', 'づ', 'で', 'ど',
       'ば', 'び', 'ぶ', 'べ', 'ぼ',
       'ぱ', 'ぴ', 'ぷ', 'ぺ', 'ぽ',
       'ん', 'ん', 'っ', 'っ',
       'ゃ', 'ゅ', 'ょ',
       'を', 'は', 'は',
       'ぁ','ぃ','ぅ','ぇ','ぉ']
# gatakana
jak = ['ア', 'イ', 'ウ', 'エ', 'オ',
        'カ', 'キ', 'ク', 'ケ', 'コ',
        'サ', 'シ', 'ス', 'セ', 'ソ',
        'タ', 'チ', 'ツ', 'テ', 'ト',
        'ナ', 'ニ', 'ヌ', 'ネ', 'ノ',
        'ハ', 'ヒ', 'フ', 'ヘ', 'ホ',
        'マ', 'ミ', 'ム', 'メ', 'モ',
        'ヤ', 'ユ', 'ヨ',
        'ラ', 'リ', 'ル', 'レ', 'ロ',
        'ワ',
        'ガ', 'ギ', 'グ', 'ゲ', 'ゴ',
        'ザ', 'ジ', 'ズ', 'ゼ', 'ゾ',
        'ダ', 'ヂ', 'ヅ', 'デ', 'ド',
        'バ', 'ビ', 'ブ', 'ベ', 'ボ',
        'パ', 'ピ', 'プ', 'ペ', 'ポ',
        'ン', 'ン', 'ッ', 'ッ',
        'ヲ', 'ハ', 'ハ',
        'ャ', 'ュ', 'ョ',]

a_h = ['아', '이', '우', '에', '오', '야', '유', '요']
batchim_h = ['ん', 'っ', 'む', 'る']
batchim_g = ['ン', 'ッ', 'ム', 'ル']
no_ja = ['あ', 'い', 'う', 'え', 'お','わ','や', 'ゆ', 'よ']
s_line = ['さ', 'し', 'す', 'せ', 'そ']
b_line = ['ば', 'び', 'ぶ', 'べ', 'ぼ',]
# ja # yo
jaeum = ['ㅋ', 'ㅅ', 'ㅌ', 'ㅊ', 'ㄴ', 'ㅎ',
         'ㅁ', 'ㄹ', 'ㄱ', 'ㅈ', 'ㅂ', 'ㅍ', 'ㄷ']
jap_yo = ['き', 'し', 'ち', 'ち', 'に', 'ひ',
       'み', 'り', 'ぎ', 'じ', 'び', 'ぴ', 'ぢ']
jap_yk = ['キ', 'シ', 'チ', 'チ', 'ニ', 'ヒ',
     'ミ', 'リ', 'ギ', 'ヂ', 'ビ', 'ピ', 'ヂ']

# ja_ex 모든 한글 자음 (겹받침 제외)
jaeum_ex = ['ㄱ', 'ㄴ', 'ㄷ', 'ㄹ', 'ㅁ',
         'ㅂ', 'ㅅ', 'ㅇ', 'ㅈ', 'ㅊ',
         'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ',
         'ㅃ', 'ㅉ', 'ㄸ', 'ㄲ', 'ㅆ']
# mo 모든 한글 모음
moeum = ['ㅏ', 'ㅑ', 'ㅓ', 'ㅕ', 'ㅗ', 'ㅛ',
      'ㅜ', 'ㅠ', 'ㅡ', 'ㅣ', 'ㅐ', 'ㅔ',
      'ㅑ', 'ㅒ', 'ㅕ', 'ㅖ', 'ㅘ', 'ㅙ',
      'ㅛ', 'ㅝ', 'ㅞ', 'ㅠ', 'ㅢ']

baats = ['ㄱ', 'ㄷ', 'ㅅ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅎ',] #  'ㅂ' 어색할때가 많아서 부로 바꿀래
baatn = ['ㅇ', 'ㄴ']

######
sajs = ['ㅆ', 'ㅃ', 'ㅉ', 'ㄲ'] # 검출하기 위한 리스트 모든항목 넣어서 if in 돌리면 될 듯
saj_1 = 'ㅆ' # ㅅ 받침에 ㅆ은 ㅅ+ㅅ으로 바꿔야겟다
saj_2 = 'ㅃ' # ㅍ
saj_3 = 'ㅉ' # ㅊ
saj_4 = 'ㄲ' # ㅋ
###### 변수로 쓸 필욘 없을거같은데 일단 해두자

##########
sams = ['ㅓ', 'ㅕ', 'ㅐ','ㅒ','ㅖ', 'ㅜ', 'ㅡ']
sam_1 = ['ㅓ']# ㅗ
sam_2 = ['ㅕ'] # ㅛ
sam_3 = ['ㅐ','ㅒ','ㅖ'] # ㅔㅣ
sam_5 = ['ㅜ'] # ㅜ ㅡ 통일해야되겠네 하 참나
##########
utoeu = ['우','쿠','수','투','누','후','무','루','구','주','두','부','푸'] #ㅜㅡ통일용
##########
excs = ['투', '트', '티', '틔', '튀']
exc_1 = ['투', '트', '틔'] # to 츠 or 추 ㅜㅡ 통일하고나서 할것
exc_2 = ['티', '튀'] # to 치
##########
##########
# 겹모음
is_fu = ['ㅙ', 'ㅚ', 'ㅞ', 'ㅘ', 'ㅝ', 'ㅟ', 'ㅢ']
fu_1 = ['ㅙ', 'ㅚ',] # [자음+ㅗ] [에] 로 나누기
fu_2 = ['ㅞ'] # ㅜ ㅔ
fu_3 = ['ㅝ'] # =ㅘ [자음+ㅗ] 아 로 나누기인데 ㅘ는 이미 바꾸는게 전처리에 한번 있어가지고 생각좀 해봐라
fu_4 = ['ㅟ', 'ㅢ'] # ㅡ ㅣ
fu_hina = ['ぁ','ぃ','ぅ','ぇ','ぉ']
fu_gana = ['ァ','ィ','ュ','ェ','ォ']
#ぁ #ァ행 ヴァ/va/ ツァ/tsa/ ファ/fa/
#ぃ #ィ행 ヴィ/vi/ ツィ/tsi/ フィ/fi/ ウィ/wi/ ティ/ti/ ディ/di/
#ぅ #ュ행 ヴ/vu/ ツ/tsu/ フ/fu/ トゥ/tu/ ドゥ/du/
#ぇ #ェ행 ヴェ/ve/ ツェ/tse/ フェ/fe/ イェ/ye/ シェ/she/ ジェ/je/ チェ/che/ ウェ/we/
#ぉ #ォ행 ヴォ/vo/ ツォ/tso/ フォ/fo/ ウォ/wo/
#화나네 진짜
##########

##########
# 겹받침 이거 언제 다 나누고 앉았냐
is_im_sads = ['ㄵ', 'ㄶ', 'ㄳ', 'ㅄ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ',]
im_sad1 = ['ㄵ','ㄶ']
im_sad2 = ['ㄳ', 'ㅄ']
im_sad3 = ['ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ']
im_sad = ['ㄵ', 'ㄶ', # n +자음
          'ㄳ', 'ㅄ', # 츠 + 자음
        ## 얘네 해야됨
          'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ',] #
##########

##########
# 단일 자음 변환 ㅋㅋㅋ 같은거
wow1 = ['ㅇ', 'ㅋ', 'ㅅ', 'ㅊ', 'ㅁ', 'ㅎ', 'ㄴ', 'ㄹ', 'ㄱ', 'ㅈ', 'ㄷ', 'ㅂ', 'ㅍ']
wow2 = ['う', 'w', 'す', 'つ', 'ぬ', 'ふ', 'む', 'る', 'ぐ', 'ず', 'づ', 'ぶ', 'ぷ']
##########
new_ = ['じ', 'ず', 'ジ', 'ズ']
old_ = ['ぢ', 'づ', 'ヂ', 'ヅ']

### 차 체 초
## 챠 치ㅔ 쵸로 바꿔야되겠다
# 바꾸면 kor jap에 차체초 지워야됨
ch = ['차', '체', '초']