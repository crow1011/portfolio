import random
import secrets


class Password:
    """ Генерирует пароль по параметрам """
    def __init__(self):
       pass

    def _gen_syllabels_block(self, conf: dict) -> str:
        '''Генерирует случайный слог по заданным параметрам '''
        vowels = ''
        consonants = ''
        if conf['use_syllable_lowcase_consonants']:
            consonants += conf['syllable_upcase_consonants']
        if conf['use_syllable_lowcase_consonants']:
            consonants += conf['syllable_lowcase_consonants']
        if conf['use_syllable_lowcase_vowels']:
            vowels += conf['syllable_upcase_vowels']
        if conf['use_syllable_lowcase_vowels']:
            vowels += conf['syllable_lowcase_vowels']
        return secrets.choice(vowels) + secrets.choice(consonants)

    def _gen_single_block(self, conf: dict) -> str:
        ''' Генерирует случайный символ '''
        characters = ''
        if conf['use_single_nums']:
            characters += conf['single_nums']
        if conf['use_single_letters']:
            characters += conf['single_letters']
        if conf['use_single_symbols']:
            characters += conf['single_symbols']
        return secrets.choice(characters)

    def gen_pwd(self, conf: dict) -> str:
        """
        Генерирует пароль
        логика генерации направлена на заданное соотношение слогов
        чтобы пароль легко было запонить
        """
        syllables_count = int((conf['pwd_length']  * conf['syllables_ratio']) // 2)
        print('syllables_coun', syllables_count)
        single_count = conf['pwd_length'] -  (syllables_count * 2)
        print('single_count', single_count)
        blocks = []
        for i in range(syllables_count):
            blocks.append(self._gen_syllabels_block(conf))
        for i in range(single_count):
            blocks.append(self._gen_single_block(conf))

        random.shuffle(blocks)
        pwd = ''.join(blocks)
        print(len(pwd))
        return pwd


