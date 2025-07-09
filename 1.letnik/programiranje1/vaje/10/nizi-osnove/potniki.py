# =============================================================================
# Potniki
#
# Nizi so v resnici le tabele znakov, zato večina funkcij, ki jih uporabljamo na
# tabelah, deluje tudi na nizih, po njih iščemo enako, tudi zanke delujejo na
# enak način. Obstaja pa kar nekaj funkcij, ki so uporabne
# posebno za nize.
# =====================================================================@028271=
# 1. podnaloga
# Številka EMŠO je sestavljena iz trinajstih števk v obliki DDMMLLL50NNNX, pri čemer je
# DDMMLLL rojstni datum, 50 je koda registra, NNN je zaporedna številka in X kontrolna številka.
# Trimestna številka, NNN, je med 000 in 499 za moške ter med 500 in 999 za ženske.
# 
# Napišite funkcijo `spol(EMSO)`, ki za EMŠO podan v nizu, vrne 'Ženska', če pripada ženski in
# 'Moški', če pripada moškemu.
# 
# Še en namig: če želimo seštevati ali primerjati števila, zapisana kot niz, jih moramo najprej
# spremeniti iz niza v število. Pomagajte si s funkcijama `int(niz)` ali `float(niz)`.
# 
# Primer:
# 
#     >>> spol("0505913509174")
#     'Ženska'
#     >>> spol("0306963500562")
#     'Moški'
# =============================================================================
def spol(EMSO):
    """pregleda emso in pove ali je zenska ali moski"""
    zenska = "56789"
    moski = "01234"
    for stevilo in EMSO[9:10]:
        if stevilo in zenska:
            return "Ženska"
        elif stevilo in moski:
            return "Moški"
# =====================================================================@028272=
# 2. podnaloga
# Za okroglo mizo sedijo gosti. Nekateri so srečni, drugi ne.
# Konkretno: srečni so moški, ki sedijo med dvema ženskama in ženske, ki sedijo med dvema moškima.
# Razpored gostov podamo s tabelo njihovih številk EMŠO.
# 
# Napiši funkcijo `stevilo_srecnezev(razpored)`, ki prejme takšno tabelo in vrne število srečnih gostov.
# 
# Pazi:
# Ker je miza okrogla, sedi prvi gost poleg zadnjega. Če sedita moški in ženska sama za okroglo mizo, 
# seveda nista srečneža.
# 
# Primer:
# 
#     >>> stevilo_srecnezev(['0903912505707', '0110913506472', '2009956506012','1102946502619', '1902922506199', '2602930503913',
#                            '0204940508783','1602960505003', '0207959502025', '0207962509545'])
#     4
#     >>> stevilo_srecnezev(['0702948501362', '1505987508785'])
#     0
# =============================================================================
def stevilo_srecnezev(razpored):
    '''
        vrne stevilo srecnih gostov
    '''
    stevilo = 0
    if len(razpored) < 3:
        return 0
    razpored.append(razpored[0])
    for oseba in range(len(razpored)-2):
        a = spol(razpored[oseba])
        b = spol(razpored[oseba+1])
        c = spol(razpored[oseba+2])
        soseda = a + c
        if b not in soseda:
            stevilo += 1
    return stevilo
    # če nimamo vsaj tri osebe, ni srečnih!

    # generiramo vse možne trojke - indeks naj označuje srednjega

          # pregledamo trojko, če je srečna
# =====================================================================@028273=
# 3. podnaloga
# Sestavite funkcijo `zapravljivci(tabela)`, ki za tabelo nizov oblike
# `"ime;priimek;EMŠO;zapravljen denar"` vrne `'Moški'`, če so več denarja
# zapravili moški, če so moški in ženske zapravili enako, vrne `'Neodločeno'`, sicer pa
# `'Ženske'`.
# 
# Pomagajte si z metodo `split()`, ki ob klicu `'juhuhuhu'.split('u') vrne
#   `['j','h', 'h', 'h']`.
# 
#     >>> zapravljivci(["Janez;Novak;0306963500562;44.32",
#                       "Janica;Zupanc Košir;0505913509174;54.33"])
#     'Ženske'
# =============================================================================
def zapravljivci(tabela):
    """vrne niz, ki pove kdo je vec zapravil"""
    slovar = dict()
    for niz in tabela:
        niz.split(";")
        oseba = spol(niz[2]) # pove ali je ženska ali moški
        # slovar, ki ima za ključ spol, za vrednost pa denar
        slovar[oseba] += niz[-1]
    vsota_z = 0
    vsota_m = 0
    for spol, denar in slovar.items():
        if spol == "Ženska":
            vsota_z += denar
        else:
            vsota_m += denar
    if vsota_z > vsota_m:
        return "Ženske"
    if vsota_m > vsota_z:
        return "Moški"
    else:
        return "Nedoločeno"
# =====================================================================@028274=
# 4. podnaloga
# Potniki letalske družbe SLED si lahko privoščijo tudi internetno povezavo. Čeprav ne
# vemo, kateri potniki bodo to storitev koristili, moramo za vse pripraviti
# uporabniška imena in gesla.
# Uporabniško ime sestavimo tako, da skupaj zložimo
# *prve tri črke imena in priimka* in *številko za spol* (1 za ženske, 2 za moške)
# Geslo pa je sestavljeno iz *zadnje črke imena in priimka* in *2. in predzadnjega števila EMŠO številke.*
# 
# Definirajte funkcijo `internet(potnik)`, ki potniku, podanemu z nizom kot prej določi
# uporabniško ime in geslo. Funkcija naj vrne par dveh nizov (uporabniško ime, geslo).
# 
# Primer:
# 
#     >>> internet("Janica;Zupanc Košir;0505913509174;54.33")
#     ("JanZup1", "ar57")
#     >>> internet("Janez;Novak;0306963500562;44.32")
#     ("JanNov2","zk36")
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
        Check.current_part['token'] = 'eyJ1c2VyIjo2NDgzLCJwYXJ0IjoyODI3MX0:1mxsCx:qpI1B2uaGLmwaoK_r0pR4kdTY_M'
        try:
            pravilno1 = True
            if 'emso[10' in Check.current_part['solution'] and \
               'EMSO[10' in Check.current_part['solution']:
                Check.error('Pazite na indekse. Kot v tabelah, tudi pri nizih začnemo šteti mesta z 0. Spomnite se video gradiva.')
                pravilno1 = False
            if pravilno1 and spol("0505913509174") != 'Ženska':
                Check.error('Super, nekaj testov ste že prestali, vendar za EMŠO 0505913509174 vaša funkcija vrne '
                            '"Moški" namesto "Ženska". Za ženski EMŠO je število med 500 in 999, funkcija pa mora vrniti "Ženska".')
                pravilno1 = False
            elif pravilno1 and spol("0505913500174") != "Moški":
                Check.error('Super, nekaj testov ste že prestali, vendar za EMŠO 0505913500174 vaša funkcija vrne '
                            '"Ženska" namesto "Moški". '
                            'Za moški EMŠO je število med 0 in 499, funkcija pa mora vrniti "Moški".')
                pravilno1 = False
            elif pravilno1 and spol("0306963505002") != "Ženska":
                Check.error('Super, nekaj testov ste že prestali, vendar za EMŠO 0306963505002 vaša funkcija vrne '
                            '"Moški" namesto "Ženska". Pazite, kako postavite mejo, števila nad vključno 500 so za ženske')
                pravilno1 = False
            elif pravilno1 and spol("0306963504994") != "Moški":
                Check.error('Super, nekaj testov ste že prestali, vendar za EMŠO 0306963504994 vaša funkcija vrne '
                            '"Ženska" namesto "Moški". Pazite, kako postavite mejo, do števila 499 so moški.')
                pravilno1 = False
            elif pravilno1 and not Check.equal('spol("0505963503565")', "Moški") or \
                 not Check.equal('spol("0306963500562")', "Moški") or \
                 not Check.equal('spol("0305003506562")', "Ženska") or \
                 not Check.equal('spol("0306963508562")', "Ženska"):
                pravilno1 = False
            if pravilno1:
                Check.feedback("Odlično vam gre, uspešno ste rešili prvo podnalogo.\n" \
                               "Ne pozabite si ogledati še uradne rešitve.")
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjo2NDgzLCJwYXJ0IjoyODI3Mn0:1mxsCx:tEmLbohVKVq9GAbtW3-BaFCppLY'
        try:
            Check.equal("""stevilo_srecnezev(['0903912505707', '0110913506472', '2009956506012','1102946502619', '1902922506199', '2602930503913', '0204940508783','1602960505003', '0207959502025', '0207962509545'])""", 4) and \
            Check.equal("""stevilo_srecnezev(['1012947507186', '0506929507291', '3107910505475','1109984500497', '0510960506179', '0307978501042', '1607944505399','1706954501918', '1305934508423', '1406967504211'])""", 7) and \
            Check.equal("""stevilo_srecnezev(['0503973503512', '3004964501773', '1005933505567','2905936507573', '0712966507144'])""", 0)and \
            Check.equal("""stevilo_srecnezev(['0702948501362', '1505987508785'])""", 0) and \
            Check.equal("""stevilo_srecnezev(['2807955501835', '1604923501254','0601925504908'])""", 0) and \
            Check.equal("""stevilo_srecnezev(['2807955501835'])""", 0) and \
            Check.equal("""stevilo_srecnezev(['2807955001835'])""", 0) and \
            Check.equal("""stevilo_srecnezev([])""", 0)
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjo2NDgzLCJwYXJ0IjoyODI3M30:1mxsCx:3Aje-1cxFYHvjPEP7YSyYLWerUQ'
        try:
            pravilno2 = True
            resitev = Check.current_part["solution"]
            if "int(" not in resitev and "float(" not in resitev:
                Check.error("Če želimo seštevati ali primerjati števila, zapisana kot niz, jih moramo najprej\n "
                            "spremeniti iz niza v število. Pomagajte si s funkcijama int(niz) ali float(niz).")
            if not Check.equal('zapravljivci(["Janez;Novak;0306963500562;44.32", "Janica;Zupanc Košir;0505913509174;54.33"])', 'Ženske'):
                Check.error('Preverite, ali ste pravilno postavili pogoje za primerjavo zneskov, in ali pravilno prištevate.')
                pravilno2 = False
            elif not Check.equal('zapravljivci(["Janez;Novak;0306963500562;44.32"])', 'Moški'):
                Check.error('Preverite, ali ste pravilno postavili pogoje za primerjavo zneskov, in ali pravilno prištevate.')
                pravilno2 = False
            elif not Check.equal('zapravljivci([])', 'Neodločeno') or \
                    not Check.equal('zapravljivci(["Janez;Novak;0306963500562;44.32", "Janica;Zupanc Košir;0505913509174;44.32"])', 'Neodločeno'):
                pravilno2 = False
                Check.error("Pazite na neodločene primere.")
            if not Check.equal("""zapravljivci(["Janez;Novak;0306963500562;44.28",
                            "Janja;Novak;0306963507562;144.32",
                            "Štefan;Novak;0306963500565;10.00",
                            "Anja;Novak;0306963508562;134.3",
                            "Lojze;Novak;0306963504562;44.32"])""", 'Ženske'):
                pravilno2 = False
            if not pravilno2:
                if 'split' not in resitev:
                    Check.error("Lahko si pomagate z metodo split kot je opisana v navodilu naloge. Zaporedje znakov v oklepaju "
                                "pove, kje naj se niz pretrga na posamezne dele, ki se bodo zložili v tabelo. Do njih lahko potem "
                                "dostopate z iskanjem po indeksih v tabeli.")
                if 'spol(' not in resitev:
                    Check.error("V pomoč vam je lahko tudi funkcija iz prejšnje naloge.")
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjo2NDgzLCJwYXJ0IjoyODI3NH0:1mxsCx:VWJaAjcDan81lGa_XzTGSK-eGOg'
        try:
            pravilno3 = True
            if "[-1]" not in Check.current_part['solution']:
                Check.error("Za iskanje zadnjih znakov v nizih uporabljajte [-1]. Poglejte si še enkrat video, da boste bolje razumeli indeksiranje.")
                pravilno3 = False
            
            (resitev_ime, resitev_geslo) = internet("Janez;Novak;0306963500562;44,32")
            
            if resitev_geslo[2] == '0':
                Check.equal('internet("Janez;Novak;0306963500562;44.32")', ("JanNov2", "zk36"))
                Check.error('Preverite, če ste pravilno indeksirali. Poglejte si še enkrat video, da boste bolje razumeli kaj se dogaja.')
                pravilno3 = False
            elif resitev_geslo[3] == '2':
                Check.equal('internet("Janez;Novak;0306963500562;44.32")', ("JanNov2", "zk36"))
                Check.error('Preverite, če ste pravilno indeksirali predzadnji znak številke EMŠO. Kadar indekse štejemo z zadnje strani, '
                            'prvi indeks ni -0, ampak -1. Poglejte si še enkrat video, da boste bolje razumeli kaj se dogaja.')
                pravilno3 = False
            elif resitev_ime[-1] == '1':
                Check.equal('internet("Janez;Novak;0306963500562;44.32")', ("JanNov2", "zk36"))
                Check.error('Nekaj je narobe z določanjem spola iz EMŠO številke. Pomagajte si s funkcijo iz prve naloge.')
                pravilno3 = False
            if not Check.equal('internet("Janez;Novak;0306963500562;44.32")', ("JanNov2", "zk36")) or \
               not Check.equal('internet("Janica;Zupanc Košir;0505913509174;54.33")', ("JanZup1", "ar57")):
                pravilno3 = False
            
            if pravilno1 & pravilno2 & pravilno3:
                Check.feedback("Odlično, rešili ste to nalogo. Sedaj ste pripravljeni na naslednji izziv.")
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
