# =============================================================================
# Zbiranje osebnih podatkov
#
# V nekem podjetju zbirajo podatke o osebah, ki brskajo po medmrežju.
# Podatki so shranjeni v slovarjih (en slovar za vsako osebo). Ključ v
# takem slovarju je _lastnost_, vrednosti pa _podatek_ o tej lastnosti
# za določeno osebo. Primeri takšnih slovarjev:
# 
#     oseba1 = {'ime': 'Božidar', 'telefon': '031918211',
#               'obiskane spletne strani': ['facebook.com', 'google.com']}
#     oseba2 = {'naslov': 'Dunajska 105', 'številka noge': 42,
#               'prijatelji': ['Marko', 'Ana']}
# =====================================================================@028408=
# 1. podnaloga
# Sestavite funkcijo `podatek(oseba, lastnost)`, ki vrne podatek o
# lastnosti `lastnost`, ki ga imamo v slovarju `oseba`. Funkcija naj vrne
# `None`, če se ta podatek v slovarju ne nahaja. Primer:
# 
#     >>> podatek({'ime': 'Božidar', 'naslov': 'Dunajska 105'}, 'naslov')
#     'Dunajska 105'
#     >>> podatek({'ime': 'Božidar', 'naslov': 'Dunajska 105'}, 'prijatelji')
#     None
# 
# Pri tem ne smeš uporabiti get!
# =============================================================================
def podatek(oseba, lastnost):
    """vrne podatek lastnosti, ki ga imamo v slovarju oseba"""
    for kljuc in oseba:
        if lastnost == kljuc:
            return oseba[kljuc]
        else:
            None
# =====================================================================@028409=
# 2. podnaloga
# Sestavite funkcijo `get_podatek(oseba, lastnost)`, ki vrne podatek o
# lastnosti `lastnost`, ki ga imamo v slovarju `oseba`. Funkcija naj vrne
# `None`, če se ta podatek v slovarju ne nahaja. Primer:
# 
#     >>> get_podatek({'ime': 'Božidar', 'naslov': 'Dunajska 105'}, 'naslov')
#     'Dunajska 105'
#     >>> get_podatek({'ime': 'Božidar', 'naslov': 'Dunajska 105'}, 'prijatelji')
#     None
# 
# Pri tem si nujno pomagajte z metodo `get`
# =============================================================================
def get_podatek(oseba, lastnost):
    """vrne podatek o lastnosti, ki ga imamo v slovarju oseba"""
    for kljuc in oseba:
        if kljuc == lastnost:
            return oseba.get(kljuc, None)
# =====================================================================@028410=
# 3. podnaloga
# Za osebi `oseba1` in `oseba2` pravimo, da se _ujemata_ v lastnosti
# `lastnost`, če za obe osebi poznamo podatka o tej lastnosti in sta
# podatka enaka. Če pa za obe osebi poznamo podatka in sta podatka
# različna, pa pravimo, da se osebi _razlikujeta_ v lastnosti `lastnost`.
# Na primer, osebi
# 
#     oseba1 = {'ime': 'Janez', 'priimek': 'Novak'}
#     oseba2 = {'ime': 'Jože', 'priimek': 'Novak', 'starost': 20}
# 
# se ujemata v lastnosti `'priimek'` in razlikujeta v lastnosti `'ime'`.
# (V lastnosti `'starost'` se niti ne ujemata niti ne razlikujeta.)
# 
# Sestavite funkcijo `ujemanje(oseba1, oseba2)`, ki pove, v koliko
# lastnostih se osebi `oseba1` in `oseba2` ujemata in v koliko lastnostih
# se razlikujeta. Rezultat naj funkcija vrne kot nabor z dvema elementoma.
# Primer:
# 
#     >>> ujemanje({'ime': 'Janez', 'priimek': 'Novak'},
#                  {'ime': 'Jože', 'priimek': 'Novak', 'starost': 20})
#     (1, 1)
# =============================================================================
def ujemanje(oseba1, oseba2):
    """pove v koliko lastnostih se oseba1 in oseba2 ujemata in v koliko razlikujeta"""
    ujemata = 0
    razlikujeta = 0
    for lastnost1 in oseba1:
        for lastnost2 in oseba2:
            if lastnost1 == lastnost2:
                if oseba1.get(lastnost1, None) == oseba2.get(lastnost2, None):
                    ujemata += 1
                else:
                    razlikujeta += 1
    return (ujemata, razlikujeta)
# =====================================================================@028411=
# 4. podnaloga
# Dva različna slovarja `oseba1` in `oseba2` lahko predstavljata isto
# osebo. To se zgodi, če se slovarja ne razlikujeta v več kot 1 lastnosti
# in se ujemata vsaj v 3 lastnostih ali če sta v obeh slovarjih lastnosti
# `ime` in `priimek` enaki. Na primer, slovarja
# 
#     oseba1 = {'ime': 'Janez', 'priimek': 'Novak', 'telefon': '031123234',
#               'starost': 90}
#     oseba2 = {'ime': 'Janez', 'priimek': 'Novak', 'davčna': '43424140'}
# 
# predstavljata isto osebo, prav tako slovarja
# 
#     oseba1 = {'ime': 'Janez', 'priimek': 'Novak', 'telefon': '031123234',
#               'starost': 90, davčna': '43424140'}
#     oseba2 = {'ime': 'Luka', 'priimek': 'Novak', 'starost': 90,
#               'davčna': '43424140', 'telefon': '031123234'}
# 
# Sestavite funkcijo `ista(oseba1, oseba2)`, ki preveri, ali slovarja
# predstavljata isto osebo. Na primer, za zgornja primera mora funkcija
# vrniti `True`.
# =============================================================================
def ista(oseba1, oseba2):
    """preveri ali slovarja predstavljata isto osebo"""
    delno = ujemanje(oseba1, oseba2)
    if delno[0] >= 3 and delno[1] <= 1:
        return True
    if "ime" in oseba1 and "ime" in oseba2 and "priimek" in oseba1 and "priimek" in oseba2:
        return oseba1['ime'] == oseba2['ime'] and oseba1['priimek'] == oseba2['priimek']
    else:
        return False
# =====================================================================@028412=
# 5. podnaloga
# V seznamu slovarjev, ki predstavljajo osebe, se lahko zgodi, da več
# slovarjev predstavlja isto osebo (isto v smislu prejšnje podnaloge).
# V takem primeru pravimo, da so ti slovarji _podvojeni_.
# 
# Sestavite funkcijo `podvojeni(seznam_oseb)`, ki vrne seznam vseh podvojenih
# slovarjev iz seznama `seznam_oseb`. Slovarji naj bodo razvrščeni v istem vrstnem
# redu kot v seznamu `seznam_oseb`. Primer:
# 
#     >>> podvojeni([{'ime': 'Jan', 'priimek': 'Dan', 'naslov': 'Jadranska 21'},
#                    {'ime': 'Jan', 'priimek': 'Dan', 'naslov': 'Jadranska 19'},
#                    {'ime': 'Žan', 'priimek': 'Dan', 'naslov': 'Jadranska 21'},
#                    {'ime': 'Žan', 'priimek': 'Noč', 'naslov': 'Jamova 25'}])
#     [{'ime': 'Jan', 'priimek': 'Dan', 'naslov': 'Jadranska 21'},
#      {'ime': 'Jan', 'priimek': 'Dan', 'naslov': 'Jadranska 19'}]
# =============================================================================
def st_podvojitev(oseba, seznam_oseb):
    st_podvojitev = 0
    for seznam in seznam_oseb:
        if ista(seznam, oseba):
            st_podvojitev += 1
    return st_podvojitev

def podvojeni(seznam_oseb):
    """vrne seznamvseh podvojenih slovarjev iz seznama seznam_oseb"""
    nov_seznam = []
    for seznam in seznam_oseb:
        if st_podvojitev(seznam, seznam_oseb) >= 2:
            nov_seznam.append(seznam)
    return nov_seznam
        




































































































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
        request = urllib.request.Request(url, data=data, headers=headers)
        # This is a workaround because some clients (and not macOS ones!) report
        # <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: certificate has expired (_ssl.c:1129)>
        import ssl
        context = ssl._create_unverified_context()
        response = urllib.request.urlopen(request, context=context)
        # When the issue is resolved, the following should be used
        # response = urllib.request.urlopen(request)
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
        Check.current_part['token'] = 'eyJwYXJ0IjoyODQwOCwidXNlciI6NjQ4M30:1nKkYH:2JpNiucpEjXb6g2gW8aN5Ofo0MM'
        try:
            if '.get' in Check.current_part['solution']:
                Cheeck.error('Uporaba metode get ni dovoljena!')
            
            test_data = [
                ({'ime': 'Božidar', 'naslov': 'Dunajska 105'}, 'naslov', 'Dunajska 105'),
                ({'ime': 'Božidar', 'naslov': 'Dunajska 105'}, 'prijatelji', None),
                ({'ime': 'Anja', 'barva oči': 'zelena', 'obsegi': [82, 58, 82], 'IP': '193.77.34.1'}, 'IP', '193.77.34.1'),
            ]
            for oseba, lastnost, vrednost in test_data:
                if not Check.equal("podatek({0}, '{1}')".format(oseba, lastnost), vrednost):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJwYXJ0IjoyODQwOSwidXNlciI6NjQ4M30:1nKkYH:lvcPSPGfpzohuAT_608Zp5DEc-U'
        try:
            if '.get' not in Check.current_part['solution']:
                Cheeck.error('Obvezna je uporaba metode get!')
            
            test_data = [
                ({'ime': 'Božidar', 'naslov': 'Dunajska 105'}, 'naslov', 'Dunajska 105'),
                ({'ime': 'Božidar', 'naslov': 'Dunajska 105'}, 'prijatelji', None),
                ({'ime': 'Anja', 'barva oči': 'zelena', 'obsegi': [82, 58, 82], 'IP': '193.77.34.1'}, 'IP', '193.77.34.1'),
            ]
            for oseba, lastnost, vrednost in test_data:
                if not Check.equal("get_podatek({0}, '{1}')".format(oseba, lastnost), vrednost):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJwYXJ0IjoyODQxMCwidXNlciI6NjQ4M30:1nKkYH:aCXJbvBj3xLyZ2_bKjr_aKRD7cs'
        try:
            test_data = [
                ({'ime': 'Janez', 'priimek': 'Novak'},
                 {'ime': 'Jože', 'priimek': 'Novak', 'starost': 20},
                 (1, 1)),
                ({'ime': 'Božidar', 'telefon': '031918211', 'obiskane spletne strani': ['facebook.com', 'google.com']},
                 {'naslov': 'Dunajska 105', 'številka noge': 42, 'obiskane spletne strani': ['facebook.com', 'google.com']},
                 (1, 0)),
            ]
            for oseba1, oseba2, vrednost in test_data:
                if not Check.equal("ujemanje({0}, {1})".format(oseba1, oseba2), vrednost):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJwYXJ0IjoyODQxMSwidXNlciI6NjQ4M30:1nKkYH:B88a4TDOeqgOKhDBhGEXtXohSqk'
        try:
            test_data = [
                ({'ime': 'Žak', 'priimek': 'Koc'},
                 {'ime': 'Žak', 'priimek': 'Koc', 'starost': 100}, True),
                ({'ime': 'Žan', 'priimek': 'Noč', 'starost': 4},
                 {'ime': 'Jan', 'priimek': 'Noč', 'starost': 4}, False),
                ({'ime': 'Pak', 'starost': 60, 'prijatelji': {'Žak', 'Mak'}, 'naslov': 'Jadranska 21'},
                 {'starost': 60, 'prijatelji': {'Žak', 'Mak'}, 'naslov': 'Jadranska 21'}, True),
                ({'starost': 30, 'ime': 'Joža'},
                 {'starost': 30, 'ime': 'Joža'}, False),
                ({'starost': 20, 'ime': 'Joža', 'naslov': 'Jadranska 21', 'stan': 'samski', 'otroci': 9},
                 {'starost': 20, 'ime': 'Joža', 'naslov': 'Jadranska 19', 'stan': 'samski', 'otroci': 10}, False),
            ]
            for oseba1, oseba2, vrednost in test_data:
                if not Check.equal("ista({0}, {1})".format(oseba1, oseba2), vrednost):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJwYXJ0IjoyODQxMiwidXNlciI6NjQ4M30:1nKkYH:ZQ7PtuUgTUnfCuNCHiZytfGA7WY'
        try:
            test_data = [
                ([{'ime': 'Jan', 'priimek': 'Dan', 'naslov': 'Jadranska 21'},
                  {'ime': 'Jan', 'priimek': 'Dan', 'naslov': 'Jadranska 19'},
                  {'ime': 'Žan', 'priimek': 'Dan', 'naslov': 'Jadranska 21'}],
                 [{'ime': 'Jan', 'priimek': 'Dan', 'naslov': 'Jadranska 21'},
                  {'ime': 'Jan', 'priimek': 'Dan', 'naslov': 'Jadranska 19'}]),
                ([{'ime': 'Žan', 'priimek': 'Noč', 'starost': 4},
                  {'ime': 'Jan', 'priimek': 'Noč', 'starost': 4},
                  {'ime': 'Pak', 'starost': 60, 'prijatelji': {'Žak', 'Mak'}, 'naslov': 'Jadranska 21'},
                  {'starost': 60, 'prijatelji': {'Žak', 'Mak'}, 'naslov': 'Jadranska 21'},
                  {'starost': 30, 'ime': 'Joža'},
                  {'starost': 30, 'ime': 'Joža'}],
                 [{'ime': 'Pak', 'starost': 60, 'prijatelji': {'Žak', 'Mak'}, 'naslov': 'Jadranska 21'},
                  {'starost': 60, 'prijatelji': {'Žak', 'Mak'}, 'naslov': 'Jadranska 21'}]),
            ]
            for s, vrednost in test_data:
                if not Check.equal("podvojeni({0})".format(s), vrednost):
                    break
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
