# =============================================================================
# Ednina, dvojina, množina
# =====================================================================@028160=
# 1. podnaloga
# Napiši funkcijo `fin_stanje(stanje)`, ki kot argument sprejme količino denarja
# na bančnem računu, podano v evrih (celih) in slovničnemu številu
# ustrezno vrne opis (kot niz) finančnega stanja.
# 
#      >>> fin_stanje(1)
#      Stanje: 1 evro.
#      >>> fin_stanje(1002)
#      Stanje: 1002 evra.
#      >>> fin_stanje(-203)
#      Stanje: -203 evri.
#      >>> fin_stanje(215)
#      Stanje: 215 evrov.
# 
# Primer, če je vneseno stanje večje ali enako 1000000 evrov:
# 
#      >>> fin_stanje(1000002)
#      Tajkun!
# 
# Primer, če je vneseno stanje nižje od -300 evrov: 
# 
#      >>> fin_stanje(-302)
#      Ti si navadna zguba!
# =============================================================================
def fin_stanje(stanje):
    """vrne stanje na racunu"""
    if abs(stanje) % 10 == 2 and abs(stanje) % 100 < 10 and stanje > -300:
        return "Stanje: " + str(stanje) + " evra."
    if abs(stanje) % 10 == 3 and abs(stanje) % 100 < 10 and stanje > -300:
        return "Stanje: " + str(stanje) + " evri."
    if abs(stanje) % 10 == 1 and abs(stanje) % 100 < 10 and stanje > -300:
        return "Stanje: " + str(stanje) + " evro."
    if abs(stanje) % 10 == 4 and abs(stanje) % 100 < 10 and stanje > -300:
        return "Stanje: " + str(stanje) + " evri."
    if stanje < 1000000:
        "Stanje: " + str(stanje) + " evrov."
    if stanje >= 1000000:
        return "Tajkun!"
    if stanje < -300:
        return "Ti si navadna zguba!"
    else:
        return "Stanje: " + str(stanje) + " evrov."
# =====================================================================@028161=
# 2. podnaloga
# Sestavi funkcijo `st_ljudi(n)`, ki kot argument sprejme poljubno naravno
# število in nato v slovnično pravilni obliki vrne opis števila ljudi
# v dvorani kulturnega doma (glej zglede). Dvorana sprejme največ 500 ljudi. Podatki so simeslni, torej
# celo število, večje ali enako 0.
# Primer za n=0:
# 
#      Dvorana je prazna.
# 
# Primer za n=1:
# 
#      V dvorani je 1 človek.
# 
# Primer za n=303:
# 
#      V dvorani so 303 ljudje.
# 
# Primer za n=500:
# 
#      Dvorana je polna.
# 
# Primer za n=502:
# 
#      Dvorana je polna. Zunaj sta ostala 2 človeka.
# =============================================================================
def st_ljudi(n):
    """vrne koliko ljudi je v dvorani"""
    if n == 500:
        return "Dvorana je polna."
    if n < 500:
        if n == 1:
            return "V dvorani je " + str(n) + " človek."
        elif n == 2 or n % 100 == 2:
            return "V dvorani sta " + str(n) + " človeka."
        elif n == 3 or n == 4:
            return "V dvorani so " + str(n) + " ljudje."
        elif n % 100 == 1:
            return "V dvorani je " + str(n) + " človek."
        elif n % 100 == 3 or n % 100 == 4:
            return "V dvorani so " + str(n) + " ljudje."
        elif n == 0:
            return "Dvorana je prazna."
        else:
            return "V dvorani je " + str(n) + " ljudi."
    if n > 500:
        if n % 100 == 1:
            return "Dvorana je polna. Zunaj je ostal " + str(n-500) + " človek."
        if n % 100 == 2:
            return "Dvorana je polna. Zunaj sta ostala " + str(n-500) + " človeka."
        if n % 100 == 3:
            return "Dvorana je polna. Zunaj so ostali " + str(n-500) + " ljudje."
        if n % 100 == 4:
            return "Dvorana je polna. Zunaj so ostali " + str(n-500) + " ljudje."
        else:
            return "Dvorana je polna. Zunaj je ostalo " + str(n-500) + " ljudi."
# =====================================================================@028162=
# 3. podnaloga
# Sestavite program, ki prebere naravno število `n` in nato izpiše niz oblike
# 
#     Koliko imaš limon? 103
#     Imaš 103 limone.
#     Koliko imaš limon? 0
#     Imaš 0 limon.
# 
# pri čemer mora biti seveda vse pravilno sklanjano.
# =============================================================================
n = int(input("Koliko imaš limon? "))
if n == 0:
    print("Imaš " + str(n) + " limon.")
elif n % 100 == 1:
    print("Imaš " + str(n) + " limono.")
elif n % 100 == 2:
    print("Imaš " + str(n) + " limoni.")
elif n % 100 == 3 or n % 100 == 4:
    print("Imaš " + str(n) + " limone.")
else:
    print("Imaš " + str(n) + " limon.")




































































































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
        Check.current_part['token'] = 'eyJ1c2VyIjo2NDgzLCJwYXJ0IjoyODE2MH0:1mxbtm:z_7L1Nr42v6mQznZ1VW0cpfBeB0'
        try:
            s = Check.current_part['solution']
            sw = re.sub('[ \n]', '', s)
            
            if "):\"" not in sw and "):'" not in sw:
                Check.error("Ne pozabi na opis funkcije.")
            elif not fin_stanje.__doc__ or fin_stanje.__doc__ == "" or not fin_stanje.__doc__.strip():
                Check.error("Opis funkcije ne sme biti prazen.")
                
            Check.equal("""fin_stanje(0)""", 'Stanje: 0 evrov.') and \
            Check.equal("""fin_stanje(1)""", 'Stanje: 1 evro.') and \
            Check.equal("""fin_stanje(2)""", 'Stanje: 2 evra.') and \
            Check.equal("""fin_stanje(3)""", 'Stanje: 3 evri.') and \
            Check.equal("""fin_stanje(103)""", 'Stanje: 103 evri.') and \
            Check.equal("""fin_stanje(113)""", 'Stanje: 113 evrov.') and \
            Check.equal("""fin_stanje(-3)""", 'Stanje: -3 evri.') and \
            Check.equal("""fin_stanje(-4)""", 'Stanje: -4 evri.') and \
            Check.equal("""fin_stanje(-5)""", 'Stanje: -5 evrov.') and \
            Check.equal("""fin_stanje(-300)""", 'Stanje: -300 evrov.') and \
            Check.equal("""fin_stanje(-101)""", 'Stanje: -101 evro.') and \
            Check.equal("""fin_stanje(202)""", 'Stanje: 202 evra.') and \
            Check.equal("""fin_stanje(222)""", 'Stanje: 222 evrov.') and \
            Check.equal("""fin_stanje(16232)""", 'Stanje: 16232 evrov.') and \
            Check.equal("""fin_stanje(404)""", 'Stanje: 404 evri.') and \
            Check.equal("""fin_stanje(555)""", 'Stanje: 555 evrov.') and \
            Check.equal("""fin_stanje(1000000)""", 'Tajkun!') and \
            Check.equal("""fin_stanje(999999)""", 'Stanje: 999999 evrov.') and \
            Check.equal("""fin_stanje(-300)""", 'Stanje: -300 evrov.') and \
            Check.equal("""fin_stanje(-301)""", 'Ti si navadna zguba!') and \
            Check.equal("""fin_stanje(-30108)""", 'Ti si navadna zguba!')
            Check.secret("""fin_stanje(30108)""") 
            Check.secret("""fin_stanje(1081)""")
            Check.secret("""fin_stanje(-108)""")
            Check.secret("""fin_stanje(1083)""")
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjo2NDgzLCJwYXJ0IjoyODE2MX0:1mxbtm:MRI4s9VDKT5xU4kI3Ot0t946fAA'
        try:
            s = Check.current_part['solution']
            sw = re.sub('[ \n]', '', s)
            
            if "):\"" not in sw and "):'" not in sw:
                Check.error("Ne pozabi na opis funkcije.")
            elif not st_ljudi.__doc__ or st_ljudi.__doc__ == "" or not st_ljudi.__doc__.strip():
                Check.error("Opis funkcije ne sme biti prazen.")
                
            Check.equal("""st_ljudi(0)""", 'Dvorana je prazna.') and \
            Check.equal("""st_ljudi(1)""",'V dvorani je 1 človek.') and \
            Check.equal("""st_ljudi(2)""",'V dvorani sta 2 človeka.') and \
            Check.equal("""st_ljudi(3)""",'V dvorani so 3 ljudje.') and \
            Check.equal("""st_ljudi(4)""",'V dvorani so 4 ljudje.') and \
            Check.equal("""st_ljudi(5)""",'V dvorani je 5 ljudi.') and \
            Check.equal("""st_ljudi(10)""",'V dvorani je 10 ljudi.') and \
            Check.equal("""st_ljudi(101)""",'V dvorani je 101 človek.') and \
            Check.equal("""st_ljudi(202)""",'V dvorani sta 202 človeka.') and \
            Check.equal("""st_ljudi(303)""",'V dvorani so 303 ljudje.') and \
            Check.equal("""st_ljudi(404)""",'V dvorani so 404 ljudje.') and \
            Check.equal("""st_ljudi(499)""",'V dvorani je 499 ljudi.') and \
            Check.equal("""st_ljudi(500)""",'Dvorana je polna.') and \
            Check.equal("""st_ljudi(501)""",'Dvorana je polna. Zunaj je ostal 1 človek.') and \
            Check.equal("""st_ljudi(602)""",'Dvorana je polna. Zunaj sta ostala 102 človeka.') and \
            Check.equal("""st_ljudi(703)""",'Dvorana je polna. Zunaj so ostali 203 ljudje.') and \
            Check.equal("""st_ljudi(804)""",'Dvorana je polna. Zunaj so ostali 304 ljudje.') and \
            Check.equal("""st_ljudi(905)""",'Dvorana je polna. Zunaj je ostalo 405 ljudi.')
            Check.secret("""st_ljudi(30108)""")
            Check.secret("""st_ljudi(11)""")
            Check.secret("""st_ljudi(108)""")
            Check.secret("""st_ljudi(1083)""")
            Check.secret("""st_ljudi(81)""")
            Check.secret("""st_ljudi(108)""")
            Check.secret("""st_ljudi(102)""")
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjo2NDgzLCJwYXJ0IjoyODE2Mn0:1mxbtm:E5IHgt3DUN84h4s-HrfW0uLP66g'
        try:
            test_data = [
                ('1', 'o', ''),
                ('101', 'o', 'Pri 101 je enaka končnica kot pri 1.'),
                ('11', '', 'Pri 11 pa je končnica drugačna kot pri 1, razmisli, kakšno je pravilo - odvisno bo tako od desetic kot od enic.'),
                ('111', '', 'Pri 111 je končnica enaka kot pri 11.'),
                ('2', 'i', ''),
                ('3', 'e', ''),
                ('13', '', 'Pri 3, 13, 103 in 113 je logika enaka kot pri 1, 11, 101 in 111 ;)'),
                ('103', 'e', 'Pri 3, 13, 103 in 113 je logika enaka kot pri 1, 11, 101 in 111 ;)'),
                ('4', 'e', ''),
                ('5', '', ''),
                ('17', '', ''),
                ('1267', '', ''),
                ('202', 'i', ''),
            
            ]
            
            for vhod, izhod, namig in test_data:
                with Check.input([vhod]):
                    pravilno = Check.output(
                        Check.current_part['solution'],
                        ['Koliko imaš limon? ' + vhod,
                         "Imaš {0} limon{1}.".format(vhod, izhod),
                        ]
                    )
                    if not pravilno:
                        if namig is not '':
                            Check.error(namig)
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
