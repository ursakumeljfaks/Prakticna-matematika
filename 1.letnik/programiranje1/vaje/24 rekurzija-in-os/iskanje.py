# =============================================================================
# Iskanje
#
# Za preverjanje nalog v imenik/mapo, kjer imate rešitve, skopirajte
# *[ZIP datoteko](http://naslokar.fmf.uni-lj.si/FMF/testneDatoteke/mapa1.zip)*
# in jo razširite (v mapo, v kateri se nahaja
# pythonova datoteka z nalogami).
# 
# Namig: naloge se vam splača reševati tako, da najprej definirate delovanje
# funkcij v trenutni mapi, potem pa jih rekurzino pokličete še na vseh podmapah.
# Uporabljajte relativne poti.
# =====================================================================@030216=
# 1. podnaloga
# Sestavi funkcijo `poisci_velike(pot_do_mape, velikost)`,
# ki vrne seznam polnih imen datotek v dani mapi in njenih podmapah,
# katerih velikost je večja ali enaka dani vrednosti. Če je mapa prazna,
# naj funkcija vrne prazen seznam.
# 
#         >>> poisci_velike('mapa_1', 2000)
#         ['mapa_1\\mapa_1_1\\jovo_datoteka.txt', 'mapa_1\\mapa_1_3_abc\\bn_datoteka_556.txt']
# =============================================================================
import os

def poisci_velike(pot_do_mape, velikost):
    """vrne seznam polnih imen datotek v dani mapi in podmapah, katerih velikost je večja ali enaka dani vrednosti"""
    seznam_map = []
    for dat in os.listdir(pot_do_mape):
        pot = os.path.join(pot_do_mape, dat)
        if os.path.isfile(pot):
            if os.path.getsize(pot) >= velikost:
                seznam_map.append(pot)
        elif os.path.isdir(pot):
            seznam_map.extend(poisci_velike(pot, velikost))
    return seznam_map
# =====================================================================@030217=
# 2. podnaloga
# Sestavi funkcijo `poisci_poti(pot_do_mape,ime_datoteke)`, ki
# vrne seznam vseh poti, ki vodijo do dane datoteke.
# 
#          >>> poisci_poti('mapa_1', 'z_datoteka_1_2_e.txt')
#          ['mapa_1\\z_datoteka_1_2_e.txt', 'mapa_1\\mapa_1_1\\z_datoteka_1_2_e.txt']
# =============================================================================
def poisci_poti(pot_do_mape, ime_datoteke):
    """vrne seznam vseh poti, ki vodijo do dane datoteke"""
    seznam_poti = []
    for dat in os.listdir(pot_do_mape):
        pot = os.path.join(pot_do_mape, dat)
        if os.path.isfile(pot) == os.path.join(pot_do_mape, ime_datoteke):
            seznam_poti.append(os.path.join(pot_do_mape, ime_datoteke))
        else:
            seznam_poti.extend(poisci_poti(pot, ime_datoteke))
    return seznam_poti
# =====================================================================@030218=
# 3. podnaloga
# Sestavi funkcijo `najstevilcnejsa(pot_do_mape)`, ki v izbrani mapi (in njenih
# podmapah) poišče mapo, ki vsebuje največ datotek (štejemo samo datoteke v
# mapi, ne tudi v podmapah, saj je drugače naloga nesmiselna). Funkcija naj vrne
# ime iskane mape (skupaj s potjo) ter število datotek v tej mapi. Če je mapa
# prazna, naj funkcija vrne `(None, 0)`.
# 
#       >>> najstevilcnejsa('mapa_1')
#       ('mapa_1\\mapa_1_1', 4)
#       >>> najstevilcnejsa('mapa_1\\mapa_1_2')
#       (None, 0)
# =============================================================================

# =====================================================================@030219=
# 4. podnaloga
# Poišči vse najnovejše datoteke.
# 
# Sestavi funkcijo `poisci_najnovejse(pot_do_mape)`, ki v izbrani mapi
# (in njenih podmapah) poišče datoteke, ki so bile zadnje spremenjene.
# Funkcija naj vrne tabelo imen teh datotek (skupaj s potjo).
# 
#         >>> poisci_najnovejse('mapa_1')
#         ['mapa_1\\z_datoteka_1_2_e.txt', 'mapa_1\\mapa_1_1\\z_datoteka_1_2_e.txt', 'mapa_1\\mapa_1_3_abc\\arrested.txt']
# =============================================================================

# =====================================================================@030220=
# 5. podnaloga
# Poišči najnovejšo datoteko.
# 
# Sestavi funkcijo `poisci_najnovejso_abeceda(pot_do_mape)`, ki v izbrani mapi
# (in njenih podmapah) poišče datoteko, ki je bila zadnja spremenjena, in
# vrne njeno polno ime (skupaj s potjo). Če je takih datotek več, naj funkcija
# vrne ime datoteke, ki je prva po abecedi.
# 
#         >>> poisci_najnovejso_abeceda('mapa_1')
#         'mapa_1\\mapa_1_1\\z_datoteka_1_2_e.txt'
# =============================================================================

# =====================================================================@030221=
# 6. podnaloga
# Poišči največjo datoteko.
# 
# Sestavi funkcijo `najvecja(pot_do_mape)`, ki v izbrani mapi (in njenih
# podmapah) poišče največjo datoteko. Funkcija naj vrne par, ki ga sestavljata
# po abecedi zadnje ime take datoteke (skupaj s potjo) in njena velikost.
# 
#        >>> najvecja('mapa_1')
#        ('mapa_1\\mapa_1_3_abc\\bn_datoteka_556.txt', 6120)
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
        Check.current_part['token'] = 'eyJwYXJ0IjozMDIxNiwidXNlciI6NjQ4M30:1niDJy:kNqXDCX3VSlrk724TkRQQ12OyjU'
        try:
            test_data = [
                (
                    (['mapa_1'], 500), 
                    [['mapa_1', 'datoteka_1_1_abcd.txt'],
                     ['mapa_1', 'z_datoteka_1_2_e.txt'],
                     ['mapa_1', 'mapa_1_1', '32_datoteka.txt'],
                     ['mapa_1', 'mapa_1_1', 'ar_datoteka_jk.txt'],
                     ['mapa_1', 'mapa_1_1', 'jovo_datoteka.txt'],
                     ['mapa_1', 'mapa_1_1', 'z_datoteka_1_2_e.txt'],
                     ['mapa_1', 'mapa_1_3_abc', 'arrested.txt'],
                     ['mapa_1', 'mapa_1_3_abc', 'bn_datoteka_556.txt']]
                ),
                (
                    (['mapa_1'], 2000), 
                    [['mapa_1', 'mapa_1_1', 'jovo_datoteka.txt'],
                     ['mapa_1', 'mapa_1_3_abc', 'bn_datoteka_556.txt']]
                )
            ]
            
            for test_in, test_out in test_data:
                # zdruzi pot do vhodne datoteke
                # test_path = os.path.join(*test_in)
                test_path = os.path.join(*test_in[0])
                test_file = test_in[1]
                res = poisci_velike(test_path, test_file)
                if res is None or test_out is None:
                    if res != test_out:
                        Check.error(f"poisci_velike({test_path}, {test_file}) vrne {res} namesto {test_out}.")
                else:
                    res = sorted(res)
                    test_out = sorted([os.path.join(*path) for path in test_out])
                    if res != test_out:
                        Check.error(f"sorted(poisci_velike({test_path}, {test_file})) vrne {res} namesto {test_out}.")
            
            # stari testi delujejo le na Windowsih
            # seznam1 = ['mapa_1\\datoteka_1_1_abcd.txt',
            #            'mapa_1\\z_datoteka_1_2_e.txt',
            #            'mapa_1\\mapa_1_1\\32_datoteka.txt',
            #            'mapa_1\\mapa_1_1\\ar_datoteka_jk.txt',
            #            'mapa_1\\mapa_1_1\\jovo_datoteka.txt',
            #            'mapa_1\\mapa_1_1\\z_datoteka_1_2_e.txt',
            #            'mapa_1\\mapa_1_3_abc\\arrested.txt',
            #            'mapa_1\\mapa_1_3_abc\\bn_datoteka_556.txt']
            # seznam2 = ['mapa_1\\mapa_1_1\\jovo_datoteka.txt',
            #            'mapa_1\\mapa_1_3_abc\\bn_datoteka_556.txt']
            
            # test_data = [
            #     ("poisci_velike('mapa_1', 500)", seznam1),
            #     ("poisci_velike('mapa_1', 2000)", seznam2)
            # ]
            # for td in test_data:
            #     if not Check.equal(*td):
            #         break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJwYXJ0IjozMDIxNywidXNlciI6NjQ4M30:1niDJy:yqXMnfHUd2K7I2civVfHw9Fu--4'
        try:
            # Testi neodvisni od OS
            test_data = [
                (
                    (['mapa_1'], "z_datoteka_1_2_e.txt"), 
                    [['mapa_1', 'z_datoteka_1_2_e.txt'], ['mapa_1','mapa_1_1', 'z_datoteka_1_2_e.txt']]
                ),
                (
                    (['mapa_1'], "nova_datoteka.txt"), 
                    [['mapa_1','mapa_1_1', 'gh_mapa_zadnja', "nova_datoteka.txt"]]
                )
            ]
            
            for test_in, test_out in test_data:
                # zdruzi pot do vhodne datoteke
                test_path = os.path.join(*test_in[0])
                test_file = test_in[1]
                res = poisci_poti(test_path, test_file)
                if res is None or test_out is None:
                    if res != test_out:
                        Check.error(f"poisci_poti({test_path}, {test_file}) vrne {res} namesto {test_out}.")
                else:
                    res = sorted(res)
                    test_out = sorted([os.path.join(*path) for path in test_out])
                    if res != test_out:
                        Check.error(f"sorted(poisci_poti({test_path}, {test_file})) vrne {res} namesto {test_out}.")
            
            # seznam1 = ['mapa_1\\z_datoteka_1_2_e.txt',
            #            'mapa_1\\mapa_1_1\\z_datoteka_1_2_e.txt']
            # seznam2 = ['mapa_1\\mapa_1_1\\gh_mapa_zadnja\\nova_datoteka.txt']
            
            # test_data = [
            #     ("poisci_poti('mapa_1', 'z_datoteka_1_2_e.txt')", seznam1),
            #     ("poisci_poti('mapa_1', 'nova_datoteka.txt')", seznam2)
            # ]
            # for td in test_data:
            #     if not Check.equal(*td):
            #         break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJwYXJ0IjozMDIxOCwidXNlciI6NjQ4M30:1niDJy:Gp2Bpi3rkKjGxTIW_sulxUfVxAQ'
        try:
            test_data = [
                (
                    ['mapa_1'], 
                    (['mapa_1','mapa_1_1'], 4)),
                (
                    ['mapa_1', 'mapa_1_2'], 
                    (None, 0)),
            ]
            
            
            for test_in, test_out in test_data:
                # zdruzi pot do vhodne datoteke
                test_path = os.path.join(*test_in)
                res = najstevilcnejsa(test_path)
                if res[0] is None or test_out[0] is None:
                    if res != test_out:
                        Check.error(f"najstevilcnejsa({test_path}) vrne {res} namesto {test_out}.")
                else:
                    res_files = res[0]
                    files = os.path.join(*test_out[0])
                    test_out = (files, test_out[1])
                    if res != test_out:
                        Check.error(f"sorted(najstevilcnejsa({test_path})) vrne {res} namesto {test_out}.")
            
            
            # test_data = [
            #     ("najstevilcnejsa('mapa_1')", (f"{os.path.join('mapa_1', 'mapa_1_1')}", 4)),
            #     ("najstevilcnejsa('mapa_1\\mapa_1_2')", (None, 0))
            # ]
            # for td in test_data:
            #     if not Check.equal(*td):
            #         break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJwYXJ0IjozMDIxOSwidXNlciI6NjQ4M30:1niDJy:lezHTI4AJbaKvHalMXwRd-oLv7U'
        try:
            Check.feedback("Funkcija poisci_najnovejse nima testov - za pravilnost rešitve poskrbite sami.")
            
            # Testi neodvisni od OS
            # test_data = [
            #     (
            #         ['mapa_1'], 
            #         [
            #             ['mapa_1','z_datoteka_1_2_e.txt'], 
            #             ['mapa_1', 'mapa_1_1', 'z_datoteka_1_2_e.txt'], 
            #             ['mapa_1', 'mapa_1_3_abc', 'arrested.txt']
            #         ]),
            #     (
            #         ['mapa_1', 'mapa_1_1', 'gh_mapa_zadnja'],  
            #         [['mapa_1', 'mapa_1_1', 'gh_mapa_zadnja', 'test_datoteka.txt']]),
            # ]
            
            # for test_in, test_out in test_data:
            #     # zdruzi pot do vhodne datoteke
            #     test_path = os.path.join(*test_in)
            #     res = poisci_najnovejse(test_path)
            #     if res is None or test_out is None:
            #         if res != test_out:
            #             Check.error(f"poisci_najnovejse({test_path}) vrne {res} namesto {test_out}.")
            #     else:
            #         res = sorted(res)
            #         test_out = sorted([os.path.join(*path) for path in test_out])
            #         if res != test_out:
            #             Check.error(f"sorted(poisci_najnovejse({test_path})) vrne {res} namesto {test_out}.")
            
            # Stari testi delujejo le na Windowsih
            # seznam1 = ['mapa_1\\z_datoteka_1_2_e.txt',
            #            'mapa_1\\mapa_1_1\\z_datoteka_1_2_e.txt',
            #            'mapa_1\\mapa_1_3_abc\\arrested.txt']
            # seznam2 = ['mapa_1\\mapa_1_1\\gh_mapa_zadnja\\test_datoteka.txt']
            
            # test_data = [
            #     ("poisci_najnovejse('mapa_1')", seznam1),
            #     ("poisci_najnovejse('mapa_1\\mapa_1_1\\gh_mapa_zadnja')", seznam2)
            # ]
            # for td in test_data:
            #     if not Check.equal(*td):
            #         break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJwYXJ0IjozMDIyMCwidXNlciI6NjQ4M30:1niDJy:bLh2s6Icwh3ZB3KEJcy3bC--dJg'
        try:
            Check.feedback("Funkcija poisci_najnovejso_abeceda nima testov - za pravilnost rešitve poskrbite sami.")
            # test_data = [
            #     (['mapa_1'], ['mapa_1', 'mapa_1_1', 'z_datoteka_1_2_e.txt']),
            #     (['mapa_1', 'mapa_1_1', 'gh_mapa_zadnja'], ['mapa_1', 'mapa_1_1', 'gh_mapa_zadnja', 'test_datoteka.txt']),
            # ]
            
            # for test_in, test_out in test_data:
            #     # zdruzi pot do vhodne datoteke
            #     test_path = os.path.join(*test_in)
            #     res = poisci_najnovejso_abeceda(test_path)
            #     test_out = os.path.join(*test_out)
            #     if res != test_out:
            #         Check.error(f"poisci_najnovejso_abeceda({test_path}) vrne {res} namesto {test_out}.")
            
            # test_data = [
            #     ("poisci_najnovejso_abeceda('mapa_1')",
            #      'mapa_1\\mapa_1_1\\z_datoteka_1_2_e.txt'),
            #     ("poisci_najnovejso_abeceda('mapa_1\\mapa_1_1\\gh_mapa_zadnja')",
            #      'mapa_1\\mapa_1_1\\gh_mapa_zadnja\\test_datoteka.txt')
            # ]
            # for td in test_data:
            #     if not Check.equal(*td):
            #         break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJwYXJ0IjozMDIyMSwidXNlciI6NjQ4M30:1niDJy:Bv-oPlMut6ot7DfsPfcE_2wMP18'
        try:
            test_data = [
                (['mapa_1'], (['mapa_1', 'mapa_1_3_abc', 'bn_datoteka_556.txt'], 6120)),
                (['mapa_1', 'mapa_1_1'], (['mapa_1', 'mapa_1_1', 'jovo_datoteka.txt'], 6120)),
                (['mapa_1', 'mapa_1_1', 'gh_mapa_zadnja'], (['mapa_1', 'mapa_1_1', 'gh_mapa_zadnja', 'test_datoteka.txt'], 272)),
            ]
            
            for test_in, test_out in test_data:
                # zdruzi pot do vhodne datoteke
                test_path = os.path.join(*test_in)
                test_out = os.path.join(*test_out[0]), test_out[1]
                res = najvecja(test_path)
                
                if res != test_out:
                    Check.error(f"najvecja({test_path}) vrne {res} namesto {test_out}.")
                    break
            
            
            # stari testi delujejo le na windowsih
            # test_data = [
            #     ("najvecja('mapa_1')",
            #      ('mapa_1\\mapa_1_3_abc\\bn_datoteka_556.txt', 6120)),
            #     ("najvecja('mapa_1\\mapa_1_1')",
            #      ('mapa_1\\mapa_1_1\\jovo_datoteka.txt', 6120)),
            #     ("najvecja('mapa_1\\mapa_1_1\\gh_mapa_zadnja')",
            #      ('mapa_1\\mapa_1_1\\gh_mapa_zadnja\\test_datoteka.txt', 272))
            # ]
            # for td in test_data:
            #     if not Check.equal(*td):
            #         break
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
