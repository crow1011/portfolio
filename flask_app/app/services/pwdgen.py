import random

class Password:
    """ Генерирует пароль по параметрам """
    def __init__(self):
       pass

    def _gen_syllabels_block(self, conf: dict):
        vowels = ''
        consonants = ''
        if conf['use_lowcase_consonants']:
            consonants += conf['upcase_consonants']
        if conf['use_lowcase_consonants']:
            consonants += conf['lowcase_consonants']
        if conf['use_lowcase_vowels']:
            vowels += conf['upcase_vowels']
        if conf['use_lowcase_vowels']:
            vowels += conf['lowcase_vowels']
        rand_vowel = random.randint(0, len(vowels) - 1)
        rand_consonant = random.randint(0, len(consonants) - 1)
        return consonants[rand_consonant] + vowels[rand_vowel]

    def _gen_single_block(self, conf: dict):
        charters = ''
        if conf['use_single_nums']:
            charters += conf['single_nums']
        if conf['use_single_letters']:
            charters += conf['single_letters']
        if conf['use_single_symbols']:
            charters += conf['single_symbols']
        rand_charter = random.randint(0, len(charters) - 1)
        return charters[rand_charter]

    def gen_pwd(self, conf: dict) -> str:
        """
        Генерирует пароль
        логика генерации направлена на максимальное заданное соотношение слогов
        чтобы пароль легко было запонить
        """
        syllables_count = int((conf['pwd_length'] // 2) * conf['syllables_ratio'])
        single_count = conf['pwd_length'] -  (syllables_count * 2)
        blocks = []
        for i in range(syllables_count):
            blocks.append(self._gen_syllabels_block(conf))
        for i in range(single_count):
            blocks.append(self._gen_single_block(conf))
        if conf['pwd_length'] % 2 != 0:
            blocks.append(self._gen_single_block(conf))

        print(syllables_count)
        return blocks





import get_config
conf = get_config.get_conf('pwdgen.yml')
pwd = Password()
tst = pwd.gen_pwd(conf)
print(tst)

