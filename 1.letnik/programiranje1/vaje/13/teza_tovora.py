# =============================================================================
# Teža tovora
#
# Mama Metka in ata Jože se selita. Naročila sta ljudi s selitvenega servisa,
# ki bodo njuno pohištvo s tovornjakom preselili na novo lokacijo.
# Podatke o tem, kakšen tovor bodo naložili na tovornjak in kolikšna je masa
# posameznih kosov tovora, si bodo tovornjakarji beležili v slovarju.
# 
# Na primer, slovar
# 
#       selitveni_tovor = {'televizor' : 17, 'postelja' : 100, 'miza' : 35, 'zofa': 40, 'omara': 17}
# 
# pove, da bodo na tovornjak naložili 17 kg težak televizor, 100 kg težko posteljo,
# 35 kg težko mizo, 40 kg težko zofo in 17 kg težko omaro.
# =====================================================================@028376=
# 1. podnaloga
# Sestavite funkcijo `teza_tovora(tovor)`, ki sprejme tak slovar in vrne skupno
# težo tovora. Zgled:
# 
#     >>> teza_tovora(selitveni_tovor)
#     209
# =============================================================================
def teza_tovora(tovor):
    """vrne tezo tovora"""
    vsota = 0
    for teza in tovor.values():
        vsota += teza
    return vsota
# =====================================================================@028377=
# 2. podnaloga
# Sestavite funkcijo `lahko_pelje(tovor, nosilnost)`, ki ugotovi, ali tovornjak
# z nosilnostjo `nosilnost` lahko pelje tovor, dan s slovarjem `tovor`. Zgled:
# 
#     >>> lahko_pelje(selitveni_tovor, 333)
#     True
# 
#     >>> lahko_pelje(selitveni_tovor, 208)
#     False
# =============================================================================
def lahko_pelje(tovor, nosilnost):
    """ali lahko tovornjak pelje tovor z nosilnostjo"""
    teza = teza_tovora(tovor)
    if teza <= nosilnost:
        return True
    else:
        return False
# =====================================================================@028378=
# 3. podnaloga
# Sestavite funkcijo `enaka_tovora(tovor1, tovor2)`, ki ugotovi, če sta
# tovora, podana v slovarjih `tovor1` in `tovor2` enaka! Tovora sta enaka, če
# vsebujeta iste predmete z isto težo. Zgled:
# 
#     tovor1 = {'zibelka': 15, 'namizna lučka': 2, 'kuhinjska posoda': 14}
#     tovor2 = {'kuhinjska posoda': 13, 'zibelka': 15, 'namizna lučka': 2}
#     tovor3 = {'kuhinjska posoda': 14, 'namizna lučka': 2, 'zibelka': 15}
# 
#     >>> enaka_tovora(tovor1, tovor3)
#     True
# 
#     >>> enaka_tovora(tovor1, tovor2)
#     False
# 
# Nalogo reši brez direktenga preverjanja slovarjev s tovor1 == tovor2.
# =============================================================================
def enaka_tovora(tovor1, tovor2):
    """ugotovi ali sta tovora enaka"""
    if tovor1.items() == tovor2.items():
        return True
    else:
        return False
# =====================================================================@028379=
# 4. podnaloga
# Sestavite funkcijo `ustrezen_tovor(tovor, min_teza, max_teza)`, ki "prečisti"
# slovar z danimi težami tako, da vrne slovar, v katerem so le tisti predmeti,
# katerih teža je med `min_teza` in `max_teza`. Zgled:
# 
#     >>> ustrezen_tovor(selitveni_tovor, 18, 100)
#     {'postelja' : 100, 'miza' : 35, 'zofa': 40}
# 
#     >>> ustrezen_tovor(selitveni_tovor, 41, 80)
#     {}
# =============================================================================
def ustrezen_tovor(tovor, min_teza, max_teza):
    """precisti slovar"""
    nov = dict()
    for kljuc, teza in tovor.items():
        if min_teza <= teza <= max_teza:
            nov[kljuc] = teza
    return nov
# =====================================================================@028380=
# 5. podnaloga
# Sestavite funkcijo `najkrajsi_opis(tovor)`, ki vrne po abecedi urejeno
# tabelo tistih predmetov, ki imajo najkrajši opis. Zgled:
# 
#     >>> najkrajsi_opis(selitveni_tovor)
#     ['miza', 'zofa']
# 
#     >>> najkrajsi_opis(dict())
#     []
# =============================================================================
def najkrajsi_opis(tovor):
    """vrne po abecedi urejeno tabelo tistih predmetov, ki imajo najkrajsi opis"""
    tabela = []
    for kljuc in tovor.keys():
        tabela.append(kljuc)
    najkrajsa = tabela[0]
    tab = []
    for beseda in tabela:
        if len(beseda) < len(najkrajsa):
            najkrajsa = beseda
            tab.append(najkrajsa)
    return sorted(tab)
# =====================================================================@028381=
# 6. podnaloga
# Sestavite funkcijo `najlazji_predmet(tovor)`, ki vrne po abecedi urejeno
# tabelo tistih predmetov, ki so najlažji. Zgled:
# 
#     >>> najlazji_predmet(selitveni_tovor)
#     ['omara', 'televizor']
# 
#     >>> najlazji_predmet(dict())
#     []
# =============================================================================
def najlazji_predmet(tovor):
    """vrne po abecedi urejeno tabelo tistih predmetov, ki so najlazji"""




































































































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
        Check.current_part['token'] = 'eyJ1c2VyIjo2NDgzLCJwYXJ0IjoyODM3Nn0:1n7FKI:wpdomh7qyn-pdgS46VItMtZoMV4'
        try:
            selitveni_tovor = {'televizor': 17, 'postelja': 100, 'miza': 35, 'zofa': 40, 'omara': 17}
            
            Check.equal(f"teza_tovora({selitveni_tovor})", 209) and \
            Check.equal("teza_tovora({'kuhinjska posoda': 14, 'namizna lučka': 2, 'zibelka': 15})", 31) and \
            Check.equal("teza_tovora({})", 0)
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjo2NDgzLCJwYXJ0IjoyODM3N30:1n7FKI:v2kVdh2g4I-8gD2y2p40YXUm8-g'
        try:
            Check.equal(f"lahko_pelje({selitveni_tovor}, 333)", True) and \
            Check.equal(f"lahko_pelje({selitveni_tovor}, 208)", False) and \
            Check.equal("lahko_pelje({}, 0)", True) and \
            Check.equal("lahko_pelje({}, 100)", True) and \
            Check.equal("lahko_pelje({'kavč':100}, 100)", True) and \
            Check.equal("lahko_pelje({'kavč':100, 'pivo':1}, 101)", True)
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjo2NDgzLCJwYXJ0IjoyODM3OH0:1n7FKI:-DJ1DVrzFDpC87AaPGCNG980wOE'
        try:
            sol = Check.current_part['solution']
            if re.search(r"tovor1\s*==\s*tovor2", sol):
                Check.error('To sicer deluje, ampak želimo rešitev brez neposrednega primerjanja slovarjev')
                
            tovor1 = {'zibelka': 15, 'namizna lučka': 2, 'kuhinjska posoda': 14}
            tovor2 = {'kuhinjska posoda': 13, 'zibelka': 15, 'namizna lučka': 2}
            tovor3 = {'kuhinjska posoda': 14, 'namizna lučka': 2, 'zibelka': 15}
            
            
            Check.equal("enaka_tovora({0}, {1})".format(tovor1, tovor3), True) and \
            Check.equal("enaka_tovora({0}, {1})".format(tovor1, tovor2), False) and \
            Check.equal("enaka_tovora({'televizor' : 17, 'zaboj piva' : 12, 'zofa' : 35},"
                        "{'televizor' : 17, 'zaboj piva' : 12, 'zofa' : 35})", True) and \
            Check.equal("enaka_tovora({}, {})", True) and \
            Check.equal("enaka_tovora({'televizor' : 17, 'zaboj piva' : 12, 'zofa' : 35},"
                        "{'zaboj piva' : 12, 'televizor' : 17, 'zofa' : 35})", True) and \
            Check.equal("enaka_tovora({'zaboj piva' : 12, 'zofa' : 35},"
                        "{'televizor' : 17, 'zaboj piva' : 12, 'zofa' : 35})", False)
            
            if not Check.equal(
                    "enaka_tovora({'zaboj piva' : 12, 'zofa' : 35}, {'zaboj piva' : 35, 'zofa' : 12})",
                    False
            ):
                Check.feedback("Samo enaka teža tovora ni dovolj!")
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjo2NDgzLCJwYXJ0IjoyODM3OX0:1n7FKI:hzSiGahY8fTYX9FAAhDO7JjVXME'
        try:
            Check.equal("ustrezen_tovor({0}, 18, 100)".format(selitveni_tovor),
                        {'postelja' : 100, 'miza' : 35, 'zofa': 40}) and \
            Check.equal("ustrezen_tovor({0}, 41, 80)".format(selitveni_tovor), {}) and \
            Check.equal("ustrezen_tovor({'televizor' : 17, 'zaboj piva' : 12, 'zofa' : 35}, 20, 100)",
                        {'zofa': 35}) and \
            Check.equal("ustrezen_tovor({'televizor' : 17, 'zaboj piva' : 12, 'zofa' : 35}, 10, 100)",
                        {'televizor': 17, 'zaboj piva': 12, 'zofa': 35}) and \
            Check.equal("ustrezen_tovor({'televizor' : 17, 'zaboj piva' : 12, 'zofa' : 35}, 10, 15)",
                        {'zaboj piva': 12})
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjo2NDgzLCJwYXJ0IjoyODM4MH0:1n7FKI:GHbciLafjMuO6204ClU8MaOKQlg'
        try:
            Check.equal("najkrajsi_opis({0})".format(selitveni_tovor), ['miza', 'zofa']) and \
            Check.equal("najkrajsi_opis(dict())", []) and \
            Check.equal("najkrajsi_opis({'televizor' : 17, 'zaboj piva' : 12, 'zofa' : 35})",
                        ['zofa']) and \
            Check.equal("najkrajsi_opis({'televizor' : 17, 'zaboj piva' : 12, 'zofa' : 35, 'ZOFA': 12})",
                        ['ZOFA', 'zofa'])
            
            Check.secret(najkrajsi_opis({'televizor': 17, 'zaboj piva': 12, 'zofa': 35, 'televizia': 17, \
                        'Zaboj piva': 12, 'sofa': 35, 'Televizor': 17, 'gajba pira': 12, 'kavč': 35}))
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjo2NDgzLCJwYXJ0IjoyODM4MX0:1n7FKI:SDno2Mdxq6Idx6mOx2lhHQMc41k'
        try:
            Check.equal("najlazji_predmet({0})".format(selitveni_tovor), ['omara', 'televizor']) and \
            Check.equal("najlazji_predmet(dict())", []) and \
            Check.equal("najlazji_predmet({'televizor' : 17, 'zaboj piva' : 12, 'zofa' : 35})",
                        ['zaboj piva'])
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
