# =============================================================================
# Bančni račun
#
# Pri reševanju te naloge (razen prvih dveh) uporabljamo tudi "rezanje" (slicing). 
# Npr. s tab[1:] dobimo tabelo, ki je enaka tabeli tab, le da nima prvega elementa.
# =====================================================================@028248=
# 1. podnaloga
# V tabeli imamo podatke o prilivih in odlivih s tekočega računa.
# Pozitivna števila predstavljajo priliv (polog denarja),
# negativna pa dvig.
# Vsak element tabele predstavlja en dan.
# Če na nek dan ni prilivov ali dvigov, je vrednost v tabeli 0.
# Privzemite, da je na začetku stanje na računu 0.
# 
# Sestavite funkcijo `koncno_stanje(spremembe)`, ki iz dane tabele
# prilivov in odlivov izračuna končno stanje.
# 
# Pri rešitvi ne uporabi zanke neposredno v kodi te funkcije.
# =============================================================================
def koncno_stanje(spremembe):
    """vrne stanje na racunu"""
    return sum(spremembe)
# =====================================================================@028249=
# 2. podnaloga
# Sestavite funkcijo `stanja(spremembe)`, ki iz dane tabele
# prilivov in odlivov ustvari tabelo vmesnih stanj na računu.
# Privzemite, da je na začetku stanje na računu 0. To naj bo prva "sprememba" v tabeli
# 
#      >>> stanja([10, -5, 20, -6])
#      [0, 10, 5, 25, 19]
# =============================================================================
def stanja(spremembe):
    """sestavi tabelo vmesnih stanj na racunu"""
    stanje = 0
    tabela = [0]
    for stevilo in spremembe:
        stanje += stevilo
        tabela.append(stanje)
    return tabela
# =====================================================================@028250=
# 3. podnaloga
# Sestavite funkcijo `ekstrema(spremembe)`, ki pri danih spremembah
# stanja poišče vrednosti, ko je bilo stanje na računu najnižje oziroma
# najvišje. Pri tem seveda zanemari začetno stanje 0 (uporabi rezanje)
# in prepostavi, da je prišlo do vsaj ene spremembe
# 
# Stanji naj vrne v obliki nabora.
# 
#      >>> ekstrema([10, -5, 20, -6])
#      (5, 25)
# 
# Rešitev poišči brez uporabe zank neposredno v kodi te funkcije.
# _Namig_: Pomagaj si s funkcijami iz prejšnjih nalog.
# =============================================================================
def ekstrema(spremembe):
    """poisce vrednosti, ko je bilo stanje na racunu najnizje oz. najvisje"""
    tabela = stanja(spremembe)
    najmanjsa = tabela[1]
    najvisja = tabela[1]
    for vrednost in tabela[1:]:
        if vrednost < najmanjsa:
            najmanjsa = vrednost
        elif vrednost > najvisja:
            najvisja = vrednost
    return (najmanjsa, najvisja)
# =====================================================================@028251=
# 4. podnaloga
# Sestavite funkcijo `kdaj_ekstrema(spremembe)`, ki pri danih spremembah
# stanja poišče število dni od začetka, ko je bilo stanje na računu najnižje oziroma
# najvišje.  Rezultat naj vrne v obliki nabora.
# 
# 
#      >>> kdaj_ekstrema([10, -5, 20, -6])
#      (2, 3)
# 
# Rešitev poišči brez uporabe zank neposredno v kodi te funkcije.
# _Namig_: Pomagaj si s funkcijami iz prejšnjih nalog ter z metodo `index`.
# =============================================================================
def kdaj_ekstrema(spremembe):
    """poisce stevilo dni od zacetka, ko je bilo stanje na racunu najnizje oz. najvisje"""
    tabela = stanja(spremembe)[1:]
    najmanjsa = tabela.index(min(tabela)) + 1
    najvecja = tabela.index(max(tabela)) + 1
    return (najmanjsa, najvecja)
# =====================================================================@028252=
# 5. podnaloga
# Sestavite funkcijo `razlika(spremembe, i, j)`, ki poišče razliko
# stanj med dnevoma z indeksom `i` in `j`. Na dan 0 je bilo seveda stanje 0.
# 
#      >>> razlika([10, -5, 20, -6], 1, 3)
#      15
#      >>> razlika([10, -5, 20, -6], 1, 2)
#      -5
# 
# Predpostavite lahko, da je `i` manjši ali enak `j`.
# Rešitev poišči brez uporabe zank neposredno v kodi te funkcije.
# Tu potrebuješ rezanje!
# =============================================================================
def razlika(spremembe, i, j):
    """razlika stanj med dnevoma z indeksom i in j"""
    return sum(spremembe[i:j])
# =====================================================================@028253=
# 6. podnaloga
# Sestavite funkcijo `najvecja_razlika(spremembe)`, ki poišče največji
# relativni priliv. Z drugimi besedami, poišče največjo vrednost, ki jo
# zavzame vsota poljubne strnjene podtabele.
# Tako na primer `najvecja_razlika([10, -13, 3, 20, -2, 5])` vrne
# 3 + 20 - 2 + 5 = 26.
# Če je tabela `spremembe` prazna, naj funkcija vrne `None`.
# 
# Namig: verjetno bo potrebno preveriti vse možne podtabele!
# =============================================================================
def najvecja_razlika(spremembe):
    """poisce najvecjo vrednost, ki jo zavzame vsota poljubne strnjene podtabele"""
    if spremembe == []:
        return None




































































































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
        Check.current_part['token'] = 'eyJ1c2VyIjo2NDgzLCJwYXJ0IjoyODI0OH0:1mxbwz:xN_7rM4Kgfo1B4NXgtKWPU7HofI'
        try:
            res = Check.current_part["solution"]
            sw = re.sub('[ \n]', '', res)
            
            if "):\"" not in sw and "):'" not in sw:
                Check.error("Ne pozabi na opis funkcije.")
            elif not koncno_stanje.__doc__ or koncno_stanje.__doc__ == "" or not koncno_stanje.__doc__.strip():
                Check.error("Opis funkcije ne sme biti prazen.")  
            elif 'for ' in res or 'while ' in res or 'while(' in res:
                Check.error('Rekli smo brez zanke!')
            else:
                if not Check.equal('koncno_stanje([1, 2, 3])', 6) and \
                Check.equal('koncno_stanje([1, -5, -20, 30])', 6) and \
                Check.equal('koncno_stanje([1, -5, -20, -30])', -54) and \
                Check.equal('koncno_stanje([0])', 0) and \
                Check.equal('koncno_stanje([])', 0) and \
                Check.equal('koncno_stanje([10, -5, 20, -6])', 19) :
                    if 'sum' not in res:
                        Check.feedback('Verjetno bo potrebno uporabiti funkcijo sum')
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjo2NDgzLCJwYXJ0IjoyODI0OX0:1mxbwz:MhIzWjDRm3nHbKhkxh5bz4KgXww'
        try:
            res = Check.current_part["solution"]
            sw = re.sub('[ \n]', '', res)
            
            if "):\"" not in sw and "):'" not in sw:
                Check.error("Ne pozabi na opis funkcije.")
            elif not stanja.__doc__ or stanja.__doc__ == "" or not stanja.__doc__.strip():
                Check.error("Opis funkcije ne sme biti prazen.")
            else:
                Check.equal('stanja([1, 2, 3])', [0, 1, 3, 6]) and \
                Check.equal('stanja([1, -5, -20, 30])', [0, 1, -4, -24, 6]) and \
                Check.equal('stanja([0])', [0, 0]) and \
                Check.equal('stanja([])', [0]) and \
                Check.equal('stanja([10, -5, 20, -6])', [0, 10, 5, 25, 19])
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjo2NDgzLCJwYXJ0IjoyODI1MH0:1mxbwz:tRXv1w-UBTD1f-m9XWJxdjUcsPU'
        try:
            res = Check.current_part["solution"]
            sw = re.sub('[ \n]', '', res)
            
            if "):\"" not in sw and "):'" not in sw:
                Check.error("Ne pozabi na opis funkcije.")
            elif not ekstrema.__doc__ or ekstrema.__doc__ == "" or not ekstrema.__doc__.strip():
                Check.error("Opis funkcije ne sme biti prazen.")
            else:
                Check.equal('ekstrema([1, 2, 3])', (1, 6)) and \
                Check.equal('ekstrema([1, -5, -20, 30])', (-24, 6)) and \
                Check.equal('ekstrema([2])', (2, 2)) and \
                Check.equal('ekstrema([10, -5, 20, -6])', (5, 25))
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjo2NDgzLCJwYXJ0IjoyODI1MX0:1mxbwz:sE78WHhY5KcGXIIOBD58atLXCPo'
        try:
            res = Check.current_part["solution"]
            sw = re.sub('[ \n]', '', res)
            
            if "):\"" not in sw and "):'" not in sw:
                Check.error("Ne pozabi na opis funkcije.")
            elif not kdaj_ekstrema.__doc__ or kdaj_ekstrema.__doc__ == "" or not kdaj_ekstrema.__doc__.strip():
                Check.error("Opis funkcije ne sme biti prazen.")
            elif 'for ' in res or 'while ' in res or 'while(' in res:
                Check.error('Nalogo reši brez uporabe zank!')
                Check.feedback('Poskusi s funkcijo index')
            else:
                Check.equal('kdaj_ekstrema([1, 2, 3])', (1, 3)) and \
                Check.equal('kdaj_ekstrema([1, -5, -20, 30])', (3, 4)) and \
                Check.equal('kdaj_ekstrema([2])', (1, 1)) and \
                Check.equal('kdaj_ekstrema([10, -5, 20, -6])', (2, 3))
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjo2NDgzLCJwYXJ0IjoyODI1Mn0:1mxbwz:DRUxHdkSQZLttaGRZ8Oo5zCIssk'
        try:
            sw = re.sub('[ \n]', '', res)
            
            if "):\"" not in sw and "):'" not in sw:
                Check.error("Ne pozabi na opis funkcije.")
            elif not razlika.__doc__ or razlika.__doc__ == "" or not razlika.__doc__.strip():
                Check.error("Opis funkcije ne sme biti prazen.")
            else:
                Check.equal('razlika([1, 2, 3], 2, 3)', 3) and \
                Check.equal('razlika([1, -5, -20, 30], 0, 4)', 6) and \
                Check.equal('razlika([10, -5, 20, -6], 1, 2)', -5) and \
                Check.equal('razlika([10, -5, 20, -6], 2, 4)', 14)
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjo2NDgzLCJwYXJ0IjoyODI1M30:1mxbwz:qZ0PpLcWYrA4lyFuOfSGy9thWzQ'
        try:
            sw = re.sub('[ \n]', '', res)
            
            if "):\"" not in sw and "):'" not in sw:
                Check.error("Ne pozabi na opis funkcije.")
            elif not najvecja_razlika.__doc__ or najvecja_razlika.__doc__ == "" or not najvecja_razlika.__doc__.strip():
                Check.error("Opis funkcije ne sme biti prazen.")
            else:
                Check.equal('najvecja_razlika([10, -13, 3, 20, -2, 5])', 26) and \
                Check.equal('najvecja_razlika([12, 3, 5, -10, -8, 7, 11, -30, 6, 8, -40])', 20) and \
                Check.equal('najvecja_razlika([8, -6, 10, -14, 13, -5, 7, -9, 18, -3, 2])', 24) and \
                Check.equal('najvecja_razlika([1, 2, 3])', 6) and \
                Check.equal('najvecja_razlika([])', None) and \
                Check.equal('najvecja_razlika([-1])', -1) and \
                Check.equal('najvecja_razlika([1, -5, -20, 30])', 30) and \
                Check.equal('najvecja_razlika([10, -5, 20, -6])', 25)
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
