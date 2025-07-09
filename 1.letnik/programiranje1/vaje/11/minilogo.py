# =============================================================================
# MiniLogo
#
# MiniLogo je okrnjena izvedba programskega jezika Logo, ki premore le
# štiri ukaze: `F`, `B`, `R` in `L`. S temi štirimi ukazi upravljamo
# želvo. Želva se nahaja v ravnini, ki je opremljena z običajnim
# koordinatnim sistemom (prva koordinata narašča proti desni, druga
# koordinata pa narašča navzgor). Želva se na začetku nahaja v točki
# $(0, 0)$ in gleda navzgor (proti "severu"). Z ukazom `F` želvi povemo,
# naj naredi en korak naprej (v tisti smeri, kamor je trenutno obrnjena).
# Z ukazom `B` povemo, naj naredi želva korak nazaj. Ukaz `R` pomeni, naj
# se želva zavrti v desno (tj. v smeri urinega kazalca) za 90°. Ukaz `L` pa
# pomeni, naj se želva zavrti za 90° v levo (tj. v nasprotni smeri urinega
# kazalca).
# 
# Program, ki upravlja z želvo, je torej niz v katerem nastopajo zgornji
# štirje znaki. Primer: `'FFLFRFRFFFLBRBLBBLF'`.
# =====================================================================@028309=
# 1. podnaloga
# Sestavite funkcijo `kam_pa_kam(ukazi)`, ki kot argument dobi niz
# `ukazi`. Ta niz vsebuje ukaze za želvo, kot je opisano zgoraj. Funkcija
# naj izračuna in vrne koordinati tiste točke, kjer se želva ustavi.
# 
#     >>> kam_pa_kam('LFF')
#     (-2, 0)
#     >>> kam_pa_kam('FRFLFRFLFRFLFRF')
#     (4, 4)
# =============================================================================
def kam_pa_kam(ukazi):
    """vrne koordinate tiste tocke, kjer se zelva ustavi"""
    smer = [(0,1), (1,0), (0,-1), (-1,0)]
    polozaj_x = 0
    polozaj_y = 0
    indeksi_smeri = 0
    for ukaz in ukazi:
        if ukaz == "R":
            indeksi_smeri = (indeksi_smeri + 1) % 4
        if ukaz == "L":
            indeksi_smeri = (indeksi_smeri - 1) % 4
        if ukaz == "F":
            polozaj_x += smer[indeksi_smeri][0]
            polozaj_y += smer[indeksi_smeri][1]
        if ukaz == "B":
            polozaj_x -= smer[indeksi_smeri][0]
            polozaj_y -= smer[indeksi_smeri][1]
    return (polozaj_x, polozaj_y)
# =====================================================================@028310=
# 2. podnaloga
# Sestavite funkcijo `pot_zelve(ukazi)`, ki kot argument dobi niz `ukazi`.
# Funkcija naj vrne tabelo točk (tj. urejenih parov koordinat), ki naj
# predstavlja pot, ki jo prepotuje želva.
# 
#     >>> pot_zelve('LFF')
#     [(0, 0), (-1, 0), (-2, 0)]
#     >>> pot_zelve('RFRFRFRF')
#     [(0, 0), (1, 0), (1, -1), (0, -1), (0, 0)]
# 
# Želva vedno začne svoj pohod v točki $(0, 0)$ obrnjena proti "severu".
# Pot (tj. tabela, ki jo funkcija vrne) bo vedno vsebovala en element več,
# kot je skupno število znakov `'F'` in `'B'` v nizu ukaz.
# =============================================================================
def pot_zelve(ukazi):
    """vrne posamezne koordinate zelvjih korakov"""
    pot = [(0,0),]
    smer = [(0,1), (1,0), (0,-1), (-1,0)]
    polozaj_x = 0
    polozaj_y = 0
    indeksi_smeri = 0
    for ukaz in ukazi:
        if ukaz == "R":
            indeksi_smeri = (indeksi_smeri + 1) % 4
        if ukaz == "L":
            indeksi_smeri = (indeksi_smeri - 1) % 4
        if ukaz == "F":
            polozaj_x += smer[indeksi_smeri][0]
            polozaj_y += smer[indeksi_smeri][1]
            pot.append((polozaj_x,polozaj_y))
        if ukaz == "B":
            polozaj_x -= smer[indeksi_smeri][0]
            polozaj_y -= smer[indeksi_smeri][1]
            pot.append((polozaj_x,polozaj_y))
    return pot
# =====================================================================@028311=
# 3. podnaloga
# Sestavite funkcijo sled_zelve(ukazi), ki kot argument dobi niz `ukazi`.
# Funkcija naj vrne tabelo `sled`, ki predstavlja sled želve (tj. tabela
# vseh koordinat, ki jih želva vsaj enkrat obišče na svoji poti). Sled se
# od poti razlikuje v tem, da se nobena točka v tabeli `sled` ne sme
# pojaviti več kot enkrat. Pozor: točke, ki jih želva obišče prej, se
# morajo tudi v tabeli `sled` pojaviti prej.
# 
#     >>> sled_zelve('FFFBBFFFBBFFFBB')
#     [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5)]
#     >>> sled_zelve('FBRFBRFBRFBRFBFB')
#     [(0, 0), (0, 1), (1, 0), (0, -1), (-1, 0)]
# =============================================================================
def sled_zelve(ukazi):
    """vrne tabelo sled, ki predstavlja sled zelve"""
    pot = pot_zelve(ukazi)
    sled = []
    for ukaz in pot:
        if ukaz not in sled:
            sled.append(ukaz)
    return sled
# =====================================================================@028312=
# 4. podnaloga
# Želve, ki živijo v neposredni bližini Černobila, lahko korakajo samo
# _nazaj_ in se obračajo samo v _levo_. Kljub temu pa se izkaže, da lahko
# tudi "handicapirana" želva prehodi čisto vsako pot, ki jo lahko prehodijo
# običajne želve. Sestavite funkcijo `mutant(pot)`, ki kot argument dobi
# tabelo `pot`, ki predstavlja _veljavno_ pot želve, ki se začne v točki
# $(0, 0)$. Funkcija naj vrne niz ukazov `ukazi`, ki sme vsebovati le znaka
# 'L' in 'B'. Želva, ki bo začela svojo pot v točki $(0, 0)$ obrnjena proti
# "severu" in bo sledila tem ukazom, bo prehodila natančno tisto pot, ki je
# podana kot argument funkcije.
# 
#     >>> mutant([(0, 0), (-1, 0), (-2, 0)])
#     'LLLBB'
#     >>> mutant([(0, 0), (1, 0), (1, -1), (0, -1)])
#     'LBLLLBLLLB'
# 
# Niz, ki ga vrne funkcija `mutant`, ne sme vsebovati odvečnih rotacij.
# =============================================================================





































































































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
        Check.current_part['token'] = 'eyJ1c2VyIjo2NDgzLCJwYXJ0IjoyODMwOX0:1n1ny7:vV5I7Sf8KcvqQYWiEox2FDqxRd8'
        try:
            test_data = [
                ("kam_pa_kam('LFF')", (-2, 0)),
                ("kam_pa_kam('RFRFRFRF')", (0, 0)),
                ("kam_pa_kam('BBBBBBBBBB')", (0, -10)),
                ("kam_pa_kam('FRFLFRFLFRFLFRF')", (4, 4)),
                ("kam_pa_kam('BFFFLBFFFLFLBFFFLLBF')", (0, 1)),
                ("kam_pa_kam('')", (0, 0)),
                ("kam_pa_kam('BBRBFBRBFBBFFBBLRLFFFBBFRFFFLBBFFFFFBRLFRRFBFBFRLB')", (4, -3)),
            ]
            for td in test_data:
                if not Check.equal(*td):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjo2NDgzLCJwYXJ0IjoyODMxMH0:1n1ny7:84mc7kV3_r6jMtRbW1IoawdFJEM'
        try:
            test_data = [
                ("pot_zelve('LFF')", [(0, 0), (-1, 0), (-2, 0)]),
                ("pot_zelve('RFRFRFRF')", [(0, 0), (1, 0), (1, -1), (0, -1), (0, 0)]),
                ("pot_zelve('BBBBBBBBBB')", [(0, 0), (0, -1), (0, -2), (0, -3), (0, -4), (0, -5), (0, -6), (0, -7), (0, -8), (0, -9), (0, -10)]),
                ("pot_zelve('FRFLFRFLFRFLFRF')", [(0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (2, 3), (3, 3), (3, 4), (4, 4)]),
                ("pot_zelve('BFFFLBFFFLFLBFFFLLBF')", [(0, 0), (0, -1), (0, 0), (0, 1), (0, 2), (1, 2), (0, 2), (-1, 2), (-2, 2), (-2, 1), (-3, 1), (-2, 1), (-1, 1), (0, 1), (1, 1), (0, 1)]),
                ("pot_zelve('')", [(0, 0)]),
                ("pot_zelve('BBRBFBRBFBBFFBBLRLFFFBBFRFFFLBBFFFFFBRLFRRFBFBFRLB')",
                 [(0, 0), (0, -1), (0, -2), (-1, -2), (0, -2), (-1, -2), (-1, -1), (-1, -2), (-1, -1), (-1, 0), (-1, -1), (-1, -2), (-1, -1),
                  (-1, 0), (0, 0), (1, 0), (2, 0), (1, 0), (0, 0), (1, 0), (1, -1), (1, -2), (1, -3), (0, -3), (-1, -3), (0, -3), (1, -3), (2, -3),
                  (3, -3), (4, -3), (3, -3), (4, -3), (3, -3), (4, -3), (3, -3), (4, -3), (3, -3), (4, -3)]),
            ]
            for td in test_data:
                if not Check.equal(*td):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjo2NDgzLCJwYXJ0IjoyODMxMX0:1n1ny7:YikbKNwQSu-788WZ3Kj3AyHJRFo'
        try:
            test_data = [
                ("sled_zelve('FBRFBRFBRFBRFBFB')", [(0, 0), (0, 1), (1, 0), (0, -1), (-1, 0)]),
                ("sled_zelve('FFFBBFFFBBFFFBB')", [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5)]),
                ("sled_zelve('LFF')", [(0, 0), (-1, 0), (-2, 0)]),
                ("sled_zelve('RFRFRFRF')", [(0, 0), (1, 0), (1, -1), (0, -1)]),
                ("sled_zelve('BBBBBBBBBB')", [(0, 0), (0, -1), (0, -2), (0, -3), (0, -4), (0, -5), (0, -6), (0, -7), (0, -8), (0, -9), (0, -10)]),
                ("sled_zelve('FRFLFRFLFRFLFRF')", [(0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (2, 3), (3, 3), (3, 4), (4, 4)]),
                ("sled_zelve('BFFFLBFFFLFLBFFFLLBF')", [(0, 0), (0, -1), (0, 1), (0, 2), (1, 2), (-1, 2), (-2, 2), (-2, 1), (-3, 1), (-1, 1), (1, 1)]),
                ("sled_zelve('')", [(0, 0)]),
                ("sled_zelve('BBRBFBRBFBBFFBBLRLFFFBBFRFFFLBBFFFFFBRLFRRFBFBFRLB')",
                 [(0, 0), (0, -1), (0, -2), (-1, -2), (-1, -1), (-1, 0), (1, 0), (2, 0), (1, -1),
                  (1, -2), (1, -3), (0, -3), (-1, -3), (2, -3), (3, -3), (4, -3)]),
            ]
            for td in test_data:
                if not Check.equal(*td):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjo2NDgzLCJwYXJ0IjoyODMxMn0:1n1ny7:Vyi_u5j-03lkxIm4JZBdVHcIOSk'
        try:
            test_data = [
                ("mutant([(0, 0), (-1, 0), (-2, 0)])", 'LLLBB'),
                ("mutant([(0, 0), (1, 0), (1, -1), (0, -1)])", 'LBLLLBLLLB'),
                ("mutant([(0, 0)])", ''),
                ("mutant([(0, 0), (1, 0), (1, -1), (0, -1), (0, 0)])", 'LBLLLBLLLBLLLB'),
                ("mutant([(0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (2, 3), (3, 3), (3, 4), (4, 4)])", 'LLBLLLBLBLLLBLBLLLBLBLLLB'),
                ("mutant([(0, 0), (0, -1), (0, 0), (0, 1), (0, 2), (1, 2), (0, 2), (-1, 2), (-2, 2), (-2, 1), (-3, 1), (-2, 1), (-1, 1), (0, 1), (1, 1), (0, 1)])", 'BLLBBBLLLBLLBBBLBLLLBLLBBBBLLB'),
                ("mutant([(0, 0), (0, -1), (0, -2), (-1, -2), (0, -2), (-1, -2), (-1, -1), (-1, -2), (-1, -1), (-1, 0), (-1, -1), (-1, -2), (-1, -1), (-1, 0), (0, 0), (1, 0), (2, 0), (1, 0), (0, 0), (1, 0), (1, -1), (1, -2), (1, -3), (0, -3), (-1, -3), (0, -3), (1, -3), (2, -3), (3, -3), (4, -3), (3, -3), (4, -3), (3, -3), (4, -3), (3, -3), (4, -3), (3, -3), (4, -3)])",
                 'BBLLLBLLBLLBLLLBLLBLLBBLLBBLLBBLLLBBBLLBBLLBLLLBBBLLLBBLLBBBBBLLBLLBLLBLLBLLBLLBLLBLLB'),
            ]
            for td in test_data:
                if not Check.equal(*td):
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
