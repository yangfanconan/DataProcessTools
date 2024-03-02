import unittest
from Is_english_name import is_english_names

class TestIsEnglishNames(unittest.TestCase):

    def test_is_english_names(self):
        self.assertEqual(is_english_names(r"George Washington"), True)  # 乔治·华盛顿  
        self.assertEqual(is_english_names(r"William Shakespeare"), True)  # 威廉·莎士比亚  
        self.assertEqual(is_english_names(r"Albert Einstein"), True)  # 阿尔伯特·爱因斯坦  
        self.assertEqual(is_english_names(r"Leonardo da Vinci"), True)  # 莱昂纳多·达·芬奇  
        self.assertEqual(is_english_names(r"Marilyn Monroe"), True)  # 玛丽莲·梦露  
        self.assertEqual(is_english_names(r"Elvis Presley"), True)  # 埃尔维斯·普雷斯利  
        self.assertEqual(is_english_names(r"John Lennon"), True)  # 约翰·列侬  
        self.assertEqual(is_english_names(r"Michael Jackson"), True)  # 迈克尔·杰克逊  
        self.assertEqual(is_english_names(r"Bruce Lee"), True)  # 李小龙  
        self.assertEqual(is_english_names(r"Audrey Hepburn"), True)  # 奥黛丽·赫本  
        self.assertEqual(is_english_names(r"Pablo Picasso"), True)  # 巴勃罗·毕加索  
        self.assertEqual(is_english_names(r"Charles Chaplin"), True)  # 查理·卓别林  
        self.assertEqual(is_english_names(r"Jane Austen"), True)  # 简·奥斯汀  
        self.assertEqual(is_english_names(r"Isaac Newton"), True)  # 艾萨克·牛顿  
        self.assertEqual(is_english_names(r"Galileo Galilei"), True)  # 伽利略·伽利莱  
        self.assertEqual(is_english_names(r"Martin Luther King Jr"), True)  # 马丁·路德·金  
        self.assertEqual(is_english_names(r"Winston Churchill"), True)  # 温斯顿·丘吉尔  
        self.assertEqual(is_english_names(r"Malala Yousafzai"), True)  # 马拉拉·优素福扎伊  
        self.assertEqual(is_english_names(r"Barack Obama"), True)  # 巴拉克·奥巴马  
        self.assertEqual(is_english_names(r"Angela Merkel"), True)  # 安格拉·默克尔  
        self.assertEqual(is_english_names(r"David Beckham"), True)  # 大卫·贝克汉姆  
        self.assertEqual(is_english_names(r"Emma Watson"), True)  # 艾玛·沃特森  
        self.assertEqual(is_english_names(r"Tom Hanks"), True)  # 汤姆·汉克斯  
        self.assertEqual(is_english_names(r"Meryl Streep"), True)  # 梅丽尔·斯特里普  
        self.assertEqual(is_english_names(r"Arnold Schwarzenegger"), True)  # 阿诺德·施瓦辛格  
        self.assertEqual(is_english_names(r"Oprah Winfrey"), True)  # 奥普拉·温弗瑞  
        self.assertEqual(is_english_names(r"Prince William"), True)  # 威廉王子  
        self.assertEqual(is_english_names(r"Lady Gaga"), True)  # 嘎嘎小姐  
        self.assertEqual(is_english_names(r"Rihanna"), True)  # 蕾哈娜  
        self.assertEqual(is_english_names(r"Taylor Swift"), True)  # 泰勒·斯威夫特  
        self.assertEqual(is_english_names(r"Taylor/Swift"), True)  # 泰勒·斯威夫特 
        self.assertEqual(is_english_names(r"TAYLOR/SWIFT"), True)  # 泰勒·斯威夫特
        
        self.assertEqual(is_english_names(r"Beijing"), False)
        self.assertEqual(is_english_names(r"Georgia"), False)
        self.assertEqual(is_english_names(r"Martin Luther King Jr."), False)  # 马丁·路德·金  带了特殊字符
        self.assertEqual(is_english_names(r""), False)
        self.assertEqual(is_english_names(r" "), False)
if __name__ == '__main__':
    unittest.main()
