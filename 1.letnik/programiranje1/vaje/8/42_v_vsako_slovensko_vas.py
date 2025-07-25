# =============================================================================
# 42 v vsako slovensko vas
#
# Kot veste, je 
# [število 42](https://www.wikiwand.com/en/Phrases_from_The_Hitchhiker's_Guide_to_the_Galaxy#/Answer_to_the_Ultimate_Question_of_Life.2C_the_Universe.2C_and_Everything_.2842.29)
# izjemno pomemembno.
# =====================================================================@028222=
# 1. podnaloga
# Napiši funkcijo `imam42(tab)`, ki ugotovi ali tabela števil
# `tab_stevil` vsebuje število 42.
# 
# **_Primer:_**
# 
#         >>> tab = [42, 5, 4, -7, 2, 12, -3, -4, 11, 42, 2]
#         >>> print(imam42(tab))
#         True
# 
# Seveda mora funkcija delati za poljubno tabelo in ne samo za tabelo iz primera.
# =============================================================================
def imam42(tab):
    """ugotovi ali tab vsebuje stevilo 42"""
    for stevilo in tab:
        if stevilo == 42:
            return True
    return False
# =====================================================================@028223=
# 2. podnaloga
# [Zaphod](https://www.wikiwand.com/en/Zaphod_Beeblebrox) je ves vesel naše
# funkcije. A zanima ga tudi kje (na katerem indeksu) v tabeli se prvič pojavi 
# število 42.
# Funkcijo `imam42(tab)` predelaj v funkcijo `kje_je_42(tab)`,
# ki ugotovi, kje se v tabeli števil `tab` prvič pojavi število 42.
# Če pa števila 42 v tabeli ni, naj funkcija vrne -1.
# 
# **_Primeri:_**
# 
#         >>> tab1 = [2, 42, 5, 4, -7, 2, 12, -3, -4, 11, 42, 2]
#         >>> print(kje_je_42(tab1))
#         1
#         >>> tab2 = [1, 2, 3]
#         >>> print(kje_je_42(tab2))
#         -1
#         >>> tab3 = [1, 2, 42, 2, 42, 5]
#         >>> print(kje_je_42(tab3))
#         2
# =============================================================================
def kje_je_42(tab):
    """kje se prvič v tabeli pojavi stevilo 42, ce pa se ne pa vrne -1"""
    for indeks, stevilo in enumerate(tab):
        if stevilo == 42:
            return indeks
    return -1
# =====================================================================@028224=
# 3. podnaloga
# [Arthur Dent](https://www.wikiwand.com/en/Arthur_Dent) se glasno pritožuje, 
# da si s prvo pojavitvijo 42 nima kaj pomagati, saj ga zanima zadnji odgovor 
# na ... (saj veste kaj). Zato mu sestavite funkcijo `kje_zadnjic_42(tab)`, 
# ki pove, kje (na katerem indeksu) v tabeli se zadnjič pojavi 42.
# Če 42 v tabeli ni, tudi tokrat vrni -1.
# 
# **_Primeri:_**
# 
#         >>> tab1 = [2, 42, 5, 4, -7, 2, 12, -3, -4, 11, 42, 2]
#         >>> print(kje_zadnjic_42(tab1))
#         1
#         >>> tab2 = [1, 2, 3]
#         >>> print(kje_zadnjic_42(tab2))
#         -1
#         >>> tab3 = [1, 2, 42, 2, 42, 5]
#         >>> print(kje_zadnjic_42(tab3))
#         2
# =============================================================================
def kje_zadnjic_42(tab):
    """vrne kje se zadnjic pojavi stevilo 42, ce se ne vrne -1"""
    obrnjena_tab = tab[::-1]
    for indeks, stevilo in enumerate(obrnjena_tab):
        if stevilo == 42:
            return indeks
    return -1
# =====================================================================@028225=
# 4. podnaloga
# [Deep Thought](https://www.wikiwand.com/en/List_of_minor_The_Hitchhiker's_Guide_to_the_Galaxy_characters#/Deep_Thought) 
# ("ta pravi" in ne [slučajno tale](https://www.wikiwand.com/en/Deep_Thought_(chess_computer)))
# se glasno pritožuje, da ima že dovolj Arthurjevih in Zaphodovih prepirov
# glede tega, katera funkcija je bolj koristna.
# Zato kar sam sestavi funkcijo `indeksi42(tab)`, ki za tabelo `tab` vrne
# (urejeno) tabelo indeksov, kjer se pojavi število 42.
# 
# **_Primeri:_**
# 
#         >>> tab1 = [42, 5, 4, -7, 2, 12, -3, -4, 11, 42, 2]
#         >>> print(indeksi(tab1))
#         [0, 9]
#         >>> tab2 = [1, 2, 3]
#         >>> print(indeksi(tab2))
#         []
#         >>> tab3 = [1, 2, 42, 2, 42, 5]
#         >>> print(indeksi(tab3))
#         [3]
# 
# A kaj, ko se mu bitki premešajo in sedaj ves nesrečen strmi v kodo
# 
#      def indeksi42(tab):
#         '''Vrne urejeno tabelo indeksov, kjer se v tabeli pojavi število 42'''
#         ind = 1
#         while ind <= len(tab):
#            if tab[ind] >= 42: # hura, našli smo
#               indeksi = indeksi + [[ind]]
#         return indeksi
# 
# Pomagaj mu in jo ustrezno popravi!
# =============================================================================
def indeksi42(tab):
    '''Vrne urejeno tabelo indeksov, kjer se v tabeli pojavi število 42'''
    ind = 0
    indeksi = []
    while ind < len(tab):
        if tab[ind] == 42: # hura, našli smo
            indeksi.append(ind)
        ind += 1
    return indeksi
# =====================================================================@028226=
# 5. podnaloga
# [Vogonci](https://www.wikiwand.com/en/Vogon) že razvijajo naprednejšo
# funkcijo `indeksi_veckratnikov_42(tab)`, ki bi lahko še bolj zbirokratizirala
# delovanje Galaksije. Rešitev je le v tem, da jih prehitimo. 
# Zato hitro sestavi funkcijo `indeksi_veckratnikov_42(tab)`, ki za tabelo 
# `tab` vrne (urejeno) tabelo indeksov, kjer nastopajo večkratniki števila 42.
# 
# **_Primeri:_**
# 
#         >>> tab1 = [42, 1, 84, 42, 1, 1, 1, 420, 4200000]
#         >>> print(indeksi_veckratnikov_42(tab1))
#         [0, 2, 3, 7, 8]
#         >>> tab2 = [1, 2, 3]
#         >>> print(indeksi_veckratnikov_42(tab2))
#         []
# =============================================================================
def indeksi_veckratnikov_42(tab):
    tabela_vec = []
    for indeks, stevilo in enumerate(tab):
        if stevilo % 42 == 0:
            tabela_vec.append(indeks)
    return tabela_vec




































































































# ============================================================================@

'Če vam Python sporoča, da je v tej vrstici sintaktična napaka,'
'se napaka v resnici skriva v zadnjih vrsticah vaše kode.'

'Kode od tu naprej NE SPREMINJAJTE!'


















































import json, os, re, sys, shutil, traceback, urllib.error, urllib.request


import io, sys
from contextlib import contextmanager

class VisibleStringIO(io.StringIO):
    def read(self, size=None):
        x = io.StringIO.read(self, size)
        print(x, end='')
        return x

    def readline(self, size=None):
        line = io.StringIO.readline(self, size)
        print(line, end='')
        return line


class Check:
    parts = None
    current_part = None
    part_counter = None

    @staticmethod
    def has_solution(part):
        return part['solution'].strip() != ''

    @staticmethod
    def initialize(parts):
        Check.parts = parts
        for part in Check.parts:
            part['valid'] = True
            part['feedback'] = []
            part['secret'] = []

    @staticmethod
    def part():
        if Check.part_counter is None:
            Check.part_counter = 0
        else:
            Check.part_counter += 1
        Check.current_part = Check.parts[Check.part_counter]
        return Check.has_solution(Check.current_part)

    @staticmethod
    def feedback(message, *args, **kwargs):
        Check.current_part['feedback'].append(message.format(*args, **kwargs))

    @staticmethod
    def error(message, *args, **kwargs):
        Check.current_part['valid'] = False
        Check.feedback(message, *args, **kwargs)

    @staticmethod
    def clean(x, digits=6, typed=False):
        t = type(x)
        if t is float:
            x = round(x, digits)
            # Since -0.0 differs from 0.0 even after rounding,
            # we change it to 0.0 abusing the fact it behaves as False.
            v = x if x else 0.0
        elif t is complex:
            v = complex(Check.clean(x.real, digits, typed), Check.clean(x.imag, digits, typed))
        elif t is list:
            v = list([Check.clean(y, digits, typed) for y in x])
        elif t is tuple:
            v = tuple([Check.clean(y, digits, typed) for y in x])
        elif t is dict:
            v = sorted([(Check.clean(k, digits, typed), Check.clean(v, digits, typed)) for (k, v) in x.items()])
        elif t is set:
            v = sorted([Check.clean(y, digits, typed) for y in x])
        else:
            v = x
        return (t, v) if typed else v

    @staticmethod
    def secret(x, hint=None, clean=None):
        clean = Check.get('clean', clean)
        Check.current_part['secret'].append((str(clean(x)), hint))

    @staticmethod
    def equal(expression, expected_result, clean=None, env=None, update_env=None):
        global_env = Check.init_environment(env=env, update_env=update_env)
        clean = Check.get('clean', clean)
        actual_result = eval(expression, global_env)
        if clean(actual_result) != clean(expected_result):
            Check.error('Izraz {0} vrne {1!r} namesto {2!r}.',
                        expression, actual_result, expected_result)
            return False
        else:
            return True

    @staticmethod
    def approx(expression, expected_result, tol=1e-6, env=None, update_env=None):
        try:
            import numpy as np
        except ImportError:
            Check.error('Namestiti morate numpy.')
            return False
        if not isinstance(expected_result, np.ndarray):
            Check.error('Ta funkcija je namenjena testiranju za tip np.ndarray.')

        if env is None:
            env = dict()
        env.update({'np': np})
        global_env = Check.init_environment(env=env, update_env=update_env)
        actual_result = eval(expression, global_env)
        if type(actual_result) is not type(expected_result):
            Check.error("Rezultat ima napačen tip. Pričakovan tip: {}, dobljen tip: {}.",
                        type(expected_result).__name__, type(actual_result).__name__)
            return False
        exp_shape = expected_result.shape
        act_shape = actual_result.shape
        if exp_shape != act_shape:
            Check.error("Obliki se ne ujemata. Pričakovana oblika: {}, dobljena oblika: {}.", exp_shape, act_shape)
            return False
        try:
            np.testing.assert_allclose(expected_result, actual_result, atol=tol, rtol=tol)
            return True
        except AssertionError as e:
            Check.error("Rezultat ni pravilen." + str(e))
            return False

    @staticmethod
    def run(statements, expected_state, clean=None, env=None, update_env=None):
        code = "\n".join(statements)
        statements = "  >>> " + "\n  >>> ".join(statements)
        global_env = Check.init_environment(env=env, update_env=update_env)
        clean = Check.get('clean', clean)
        exec(code, global_env)
        errors = []
        for (x, v) in expected_state.items():
            if x not in global_env:
                errors.append('morajo nastaviti spremenljivko {0}, vendar je ne'.format(x))
            elif clean(global_env[x]) != clean(v):
                errors.append('nastavijo {0} na {1!r} namesto na {2!r}'.format(x, global_env[x], v))
        if errors:
            Check.error('Ukazi\n{0}\n{1}.', statements,  ";\n".join(errors))
            return False
        else:
            return True

    @staticmethod
    @contextmanager
    def in_file(filename, content, encoding=None):
        encoding = Check.get('encoding', encoding)
        with open(filename, 'w', encoding=encoding) as f:
            for line in content:
                print(line, file=f)
        old_feedback = Check.current_part['feedback'][:]
        yield
        new_feedback = Check.current_part['feedback'][len(old_feedback):]
        Check.current_part['feedback'] = old_feedback
        if new_feedback:
            new_feedback = ['\n    '.join(error.split('\n')) for error in new_feedback]
            Check.error('Pri vhodni datoteki {0} z vsebino\n  {1}\nso se pojavile naslednje napake:\n- {2}', filename, '\n  '.join(content), '\n- '.join(new_feedback))

    @staticmethod
    @contextmanager
    def input(content, visible=None):
        old_stdin = sys.stdin
        old_feedback = Check.current_part['feedback'][:]
        try:
            with Check.set_stringio(visible):
                sys.stdin = Check.get('stringio')('\n'.join(content) + '\n')
                yield
        finally:
            sys.stdin = old_stdin
        new_feedback = Check.current_part['feedback'][len(old_feedback):]
        Check.current_part['feedback'] = old_feedback
        if new_feedback:
            new_feedback = ['\n  '.join(error.split('\n')) for error in new_feedback]
            Check.error('Pri vhodu\n  {0}\nso se pojavile naslednje napake:\n- {1}', '\n  '.join(content), '\n- '.join(new_feedback))

    @staticmethod
    def out_file(filename, content, encoding=None):
        encoding = Check.get('encoding', encoding)
        with open(filename, encoding=encoding) as f:
            out_lines = f.readlines()
        equal, diff, line_width = Check.difflines(out_lines, content)
        if equal:
            return True
        else:
            Check.error('Izhodna datoteka {0}\n  je enaka{1}  namesto:\n  {2}', filename, (line_width - 7) * ' ', '\n  '.join(diff))
            return False

    @staticmethod
    def output(expression, content, env=None, update_env=None):
        global_env = Check.init_environment(env=env, update_env=update_env)
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        try:
            exec(expression, global_env)
        finally:
            output = sys.stdout.getvalue().rstrip().splitlines()
            sys.stdout = old_stdout
        equal, diff, line_width = Check.difflines(output, content)
        if equal:
            return True
        else:
            Check.error('Program izpiše{0}  namesto:\n  {1}', (line_width - 13) * ' ', '\n  '.join(diff))
            return False

    @staticmethod
    def difflines(actual_lines, expected_lines):
        actual_len, expected_len = len(actual_lines), len(expected_lines)
        if actual_len < expected_len:
            actual_lines += (expected_len - actual_len) * ['\n']
        else:
            expected_lines += (actual_len - expected_len) * ['\n']
        equal = True
        line_width = max(len(actual_line.rstrip()) for actual_line in actual_lines + ['Program izpiše'])
        diff = []
        for out, given in zip(actual_lines, expected_lines):
            out, given = out.rstrip(), given.rstrip()
            if out != given:
                equal = False
            diff.append('{0} {1} {2}'.format(out.ljust(line_width), '|' if out == given else '*', given))
        return equal, diff, line_width

    @staticmethod
    def init_environment(env=None, update_env=None):
        global_env = globals()
        if not Check.get('update_env', update_env):
            global_env = dict(global_env)
        global_env.update(Check.get('env', env))
        return global_env

    @staticmethod
    def generator(expression, expected_values, should_stop=None, further_iter=None, clean=None, env=None, update_env=None):
        from types import GeneratorType
        global_env = Check.init_environment(env=env, update_env=update_env)
        clean = Check.get('clean', clean)
        gen = eval(expression, global_env)
        if not isinstance(gen, GeneratorType):
            Check.error("Izraz {0} ni generator.", expression)
            return False

        try:
            for iteration, expected_value in enumerate(expected_values):
                actual_value = next(gen)
                if clean(actual_value) != clean(expected_value):
                    Check.error("Vrednost #{0}, ki jo vrne generator {1} je {2!r} namesto {3!r}.",
                                iteration, expression, actual_value, expected_value)
                    return False
            for _ in range(Check.get('further_iter', further_iter)):
                next(gen)  # we will not validate it
        except StopIteration:
            Check.error("Generator {0} se prehitro izteče.", expression)
            return False

        if Check.get('should_stop', should_stop):
            try:
                next(gen)
                Check.error("Generator {0} se ne izteče (dovolj zgodaj).", expression)
            except StopIteration:
                pass  # this is fine
        return True

    @staticmethod
    def summarize():
        for i, part in enumerate(Check.parts):
            if not Check.has_solution(part):
                print('{0}. podnaloga je brez rešitve.'.format(i + 1))
            elif not part['valid']:
                print('{0}. podnaloga nima veljavne rešitve.'.format(i + 1))
            else:
                print('{0}. podnaloga ima veljavno rešitev.'.format(i + 1))
            for message in part['feedback']:
                print('  - {0}'.format('\n    '.join(message.splitlines())))

    settings_stack = [{
        'clean': clean.__func__,
        'encoding': None,
        'env': {},
        'further_iter': 0,
        'should_stop': False,
        'stringio': VisibleStringIO,
        'update_env': False,
    }]

    @staticmethod
    def get(key, value=None):
        if value is None:
            return Check.settings_stack[-1][key]
        return value

    @staticmethod
    @contextmanager
    def set(**kwargs):
        settings = dict(Check.settings_stack[-1])
        settings.update(kwargs)
        Check.settings_stack.append(settings)
        try:
            yield
        finally:
            Check.settings_stack.pop()

    @staticmethod
    @contextmanager
    def set_clean(clean=None, **kwargs):
        clean = clean or Check.clean
        with Check.set(clean=(lambda x: clean(x, **kwargs))
                             if kwargs else clean):
            yield

    @staticmethod
    @contextmanager
    def set_environment(**kwargs):
        env = dict(Check.get('env'))
        env.update(kwargs)
        with Check.set(env=env):
            yield

    @staticmethod
    @contextmanager
    def set_stringio(stringio):
        if stringio is True:
            stringio = VisibleStringIO
        elif stringio is False:
            stringio = io.StringIO
        if stringio is None or stringio is Check.get('stringio'):
            yield
        else:
            with Check.set(stringio=stringio):
                yield


def _validate_current_file():
    def extract_parts(filename):
        with open(filename, encoding='utf-8') as f:
            source = f.read()
        part_regex = re.compile(
            r'# =+@(?P<part>\d+)=\s*\n' # beginning of header
            r'(\s*#( [^\n]*)?\n)+?'     # description
            r'\s*# =+\s*?\n'            # end of header
            r'(?P<solution>.*?)'        # solution
            r'(?=\n\s*# =+@)',          # beginning of next part
            flags=re.DOTALL | re.MULTILINE
        )
        parts = [{
            'part': int(match.group('part')),
            'solution': match.group('solution')
        } for match in part_regex.finditer(source)]
        # The last solution extends all the way to the validation code,
        # so we strip any trailing whitespace from it.
        parts[-1]['solution'] = parts[-1]['solution'].rstrip()
        return parts

    def backup(filename):
        backup_filename = None
        suffix = 1
        while not backup_filename or os.path.exists(backup_filename):
            backup_filename = '{0}.{1}'.format(filename, suffix)
            suffix += 1
        shutil.copy(filename, backup_filename)
        return backup_filename

    def submit_parts(parts, url, token):
        submitted_parts = []
        for part in parts:
            if Check.has_solution(part):
                submitted_part = {
                    'part': part['part'],
                    'solution': part['solution'],
                    'valid': part['valid'],
                    'secret': [x for (x, _) in part['secret']],
                    'feedback': json.dumps(part['feedback']),
                }
                if 'token' in part:
                    submitted_part['token'] = part['token']
                submitted_parts.append(submitted_part)
        data = json.dumps(submitted_parts).encode('utf-8')
        headers = {
            'Authorization': token,
            'content-type': 'application/json'
        }
        import ssl
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        request = urllib.request.Request(url, data=data, headers=headers)
        response = urllib.request.urlopen(request, context=ctx)
        return json.loads(response.read().decode('utf-8'))

    def update_attempts(old_parts, response):
        updates = {}
        for part in response['attempts']:
            part['feedback'] = json.loads(part['feedback'])
            updates[part['part']] = part
        for part in old_parts:
            valid_before = part['valid']
            part.update(updates.get(part['part'], {}))
            valid_after = part['valid']
            if valid_before and not valid_after:
                wrong_index = response['wrong_indices'].get(str(part['part']))
                if wrong_index is not None:
                    hint = part['secret'][wrong_index][1]
                    if hint:
                        part['feedback'].append('Namig: {}'.format(hint))


    filename = os.path.abspath(sys.argv[0])
    file_parts = extract_parts(filename)
    Check.initialize(file_parts)

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjo2NDgzLCJwYXJ0IjoyODIyMn0:1mxbwr:haBzMI1XE9cTwybVYKoXq07YRuM'
        try:
            Check.equal('imam42([3, 7, 42])', True) and \
                Check.equal('imam42([3, 7])', False) and \
                Check.equal('imam42([42])', True) and \
                Check.equal('imam42([])', False) and \
                Check.equal('imam42([43, 17, 11, 11, 1, 1, 2, 3, 4, 42])', True) and \
                Check.equal('imam42([4, 2, 422, 421])', False) and \
                Check.equal('imam42([42, 5, 6])', True) and \
                Check.equal('imam42([7])', False) and \
                Check.equal('imam42([-42, 42])', True) and \
                Check.equal('imam42([-42])', False)
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjo2NDgzLCJwYXJ0IjoyODIyM30:1mxbwr:lF5GbaZU2nhVozboSg9aU4ndTsk'
        try:
            Check.equal('kje_je_42([3, 7, 42])', 2) and \
                Check.equal('kje_je_42([3, 7])', -1) and \
                Check.equal('kje_je_42([3, 42, 7, 42, 7])', 1) and \
                Check.equal('kje_je_42([42])', 0) and \
                Check.equal('kje_je_42([])', -1) and \
                Check.equal('kje_je_42([43, 17, 11, 11, 1, 1, 2, 3, 4, 42])', 9) and \
                Check.equal('kje_je_42([4, 2, 422, 421])', -1) and \
                Check.equal('kje_je_42([42, 5, 6])', 0) and \
                Check.equal('kje_je_42([7])', -1) and \
                Check.equal('kje_je_42([-42, 42])', 1) and \
                Check.equal('kje_je_42([-42])', -1)
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjo2NDgzLCJwYXJ0IjoyODIyNH0:1mxbwr:ZRalIXMBhTBIp45FB4oRMlsle8c'
        try:
            Check.equal('kje_zadnjic_42([3, 42, 7, 42])', 3) and \
                Check.equal('kje_zadnjic_42([3, 7])', -1) and \
                Check.equal('kje_zadnjic_42([42])', 0) and \
                Check.equal('kje_zadnjic_42([])', -1) and \
                Check.equal('kje_zadnjic_42([43, 17, 11, 11, 1, 1, 2, 3, 4, 42])', 9) and \
                Check.equal('kje_zadnjic_42([4, 2, 422, 421])', -1) and \
                Check.equal('kje_zadnjic_42([42, 5, 4, -7, 2, 12, -3, -4, 11, 42, 2])', 9) and \
                Check.equal('kje_zadnjic_42([42, 42, 42, 42, 42, 42])', 5) and \
                Check.equal('kje_zadnjic_42([42, 42, 42, 5, 6])', 2) and \
                Check.equal('kje_zadnjic_42([7])', -1) and \
                Check.equal('kje_zadnjic_42([-42, 42, 41])', 1) and \
                Check.equal('kje_zadnjic_42([-42])', -1)
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjo2NDgzLCJwYXJ0IjoyODIyNX0:1mxbwr:G6b12hLAlYnSIkys_8Z9VmyM57E'
        try:
            Check.equal('indeksi42([3, 42, 7, 42])', [1, 3]) and \
                Check.equal('indeksi42([3, 7])', []) and \
                Check.equal('indeksi42([42])', [0]) and \
                Check.equal('indeksi42([])', []) and \
                Check.equal('indeksi42([43, 17, 11, 11, 1, 1, 2, 3, 4, 42])', [9]) and \
                Check.equal('indeksi42([4, 2, 422, 421])', []) and \
                Check.equal('indeksi42([42, 5, 4, -7, 2, 12, -3, -4, 11, 42, 2])', [0, 9]) and \
                Check.equal('indeksi42([42, 42, 42, 42, 42, 42])', [0, 1, 2, 3, 4, 5]) and \
                Check.equal('indeksi42([42, 42, 42, 5, 6])', [0, 1, 2]) and \
                Check.equal('indeksi42([7])', []) and \
                Check.equal('indeksi42([-42, 42, 41])', [1]) and \
                Check.equal('indeksi42([-42])', [])
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjo2NDgzLCJwYXJ0IjoyODIyNn0:1mxbwr:A9KMFjsmgJxa_uE8l_3m4q8TlH0'
        try:
            Check.equal('indeksi_veckratnikov_42([3, 42, 7, 42])', [1, 3]) and \
                Check.equal('indeksi_veckratnikov_42([42, 1, 84, 42, 1, 1, 1, 420, 4200000])', [0, 2, 3, 7, 8]) and \
                Check.equal('indeksi_veckratnikov_42([42])', [0]) and \
                Check.equal('indeksi_veckratnikov_42([])', []) and \
                Check.equal('indeksi_veckratnikov_42([43, 17, 11, 11, 1, 1, 2, 3, 4, 420])', [9]) and \
                Check.equal('indeksi_veckratnikov_42([4, 2, 422, 421])', []) and \
                Check.equal('indeksi_veckratnikov_42([84, 5, 4, -7, 2, 12, -3, -4, 11, 42, 2])', [0, 9]) and \
                Check.equal('indeksi_veckratnikov_42([42000000, 420, 42, 42000, 84, 42])', [0, 1, 2, 3, 4, 5]) and \
                Check.equal('indeksi_veckratnikov_42([42, -42, -420000, 5, 6])', [0, 1, 2]) and \
                Check.equal('indeksi_veckratnikov_42([7])', []) and \
                Check.equal('indeksi_veckratnikov_42([-42, 42, 41])', [0, 1]) and \
                Check.equal('indeksi_veckratnikov_42([-42])', [0])
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    print('Shranjujem rešitve na strežnik... ', end="")
    try:
        url = 'https://www.projekt-tomo.si/api/attempts/submit/'
        token = 'Token 8386a0252615c3bd9fa483e87dba321eee45b936'
        response = submit_parts(Check.parts, url, token)
    except urllib.error.URLError:
        message = ('\n'
                   '-------------------------------------------------------------------\n'
                   'PRI SHRANJEVANJU JE PRIŠLO DO NAPAKE!\n'
                   'Preberite napako in poskusite znova ali se posvetujte z asistentom.\n'
                   '-------------------------------------------------------------------\n')
        print(message)
        traceback.print_exc()
        print(message)
        sys.exit(1)
    else:
        print('Rešitve so shranjene.')
        update_attempts(Check.parts, response)
        if 'update' in response:
            print('Updating file... ', end="")
            backup_filename = backup(filename)
            with open(__file__, 'w', encoding='utf-8') as f:
                f.write(response['update'])
            print('Previous file has been renamed to {0}.'.format(backup_filename))
            print('If the file did not refresh in your editor, close and reopen it.')
    Check.summarize()

if __name__ == '__main__':
    _validate_current_file()
