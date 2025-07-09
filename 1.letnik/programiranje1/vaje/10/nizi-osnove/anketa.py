# =============================================================================
# Anketa
#
# Podjetje SLED je med svojimi potniki izvedlo anketo o zadovoljstvu s storitvami.
# Za večino vprašanj analiza ni bila težavna, pri vprašanjih, kjer so potniki lahko
# prosto odgovarjali pa so se odločili, da v odgovorih preštejejo pojavitve besede
# odlično in na ta način ocenijo, kako zadovoljni so bili potniki z njihovimi uslugami.
# =====================================================================@028279=
# 1. podnaloga
# Sestavite funkcijo `odlicno(niz)`, ki prešteje vse pojavitve oblik besede
# odlično (odlično, odlična, odlični, odlične, odličen. namig: iščite po skupnem
# korenu teh besed), tudi če je beseda zapisana z veliko začetnico. Pomagate si
# lahko z metodo `niz.count(podniz)`, in/ali metodo `niz.title()`, ki vsem besedam v nizu
# spremeni prvo črko v veliko začetnico.
# 
#       >>> odlicno("hgfkj odlično Odlične sjhosk odlični")
#       >>> 3
# =============================================================================
def odlicno(niz):
    """presteje vse pojavitve besede odlicno"""
    niz = niz.lower()
    return niz.count("odlič")
# =====================================================================@028280=
# 2. podnaloga
# Pri vprašanju, kjer so lahko potniki prosto zapisali svoje mnenje o uslugah,
# je eden izmed potnikov zapisal zelo pozitivno kritiko, ki bi jo radi objavili
# na spletni strani, vendar pa je ime podjetja vedno pisal Sled, namesto SLED.
# 
# Sestavite funkcijo `popravi_sled(besedilo),` ki vrne besedilo, kjer so vsi
# zapisi besede 'Sled' zamenjani z besedo 'SLED'.
# Ta funkcija lahko zamenja tudi kakšno besedo, ki `'Sled'` vsebuje kot del
# besede (npr. Slediti), zato naj funcija vrne tudi tabelo indeksov, na
# katerih je popravljala besede.
# 
# Na primer:
# 
#     >>> popravi_sled("Let z družbo Sled mi je bil v veliko veselje.")
#     ("Let z družbo SLED mi je bil v veliko veselje.", [13])
#     >>> popravi_sled("Sledil sem stevardesi Sleda.")
#     ("SLEDil sem stevardesi SLEDa.", [0, 22])
# 
# Namig: pomagate si lahko z metodama `niz.upper()` ali `niz.lower()`, ki niz
# pretvorita v velike oz. male črke.
# =============================================================================
def popravi_sled(besedilo):
    """vrne besedilo, kjer so vsi zapisi besede Sled zamenjani z besedo SLED"""
    for beseda in besedilo:
        if beseda == "Sled":
            bededa == "SLED"
# =====================================================================@028281=
# 3. podnaloga
# S prejšnjo funkcijo so imeli še vedno preveč dela pri ročnem popravljanju,
# zato so vas prosili, da še malo izboljšate funkcijo iz prejšnje naloge
# (poimenujte jo `boljse_popravi_sled`),
# da bo še preverila, kaj sledi nizu 'Sled'. Kadar mu sledi katera izmed končnic
# 'u', 'a', 'om', 'ov', 'ovi', 'ovem', 'ova', 'ovo', 'ove', 'ovim', 'ovega', 'ovemu',
# dodajte za besedo SLED vezaj in končnico (Sledovi -> SLED-ovi). Če stoji beseda Sled samostojno,
# popravite kot prej, če pa ji sledi katerakoli druga končnica, pustite Sled tak kot je.
# 
# Bodite pozorni tudi na ločila, tu si lahko pomagate z metodo `niz.isalpha()`, ki vrne
# `True`, če so v nizu le črke, v nasprotnem primeru pa vrne `False`. Namig: če vam
# to dela težave definirajte nov niz `znak`, v katerega si shranite ločilo.
# 
# V indeksih naj bodo shranjena mesta začetkov popravljenih besed v popravljenem besedilu.
# 
#     >>> boljse_popravi_sled("Let z družbo Sled mi je bil v veliko veselje.")
#     ("Let z družbo SLED mi je bil v veliko veselje.", [13])
#     >>> boljse_popravi_sled("Sledov pilot je super.")
#     ("SLED-ov pilot je super.", [0])
#     >>> boljse_popravi_sled("Sledil sem Sledovi stevardesi.")
#     ("Sledil sem SLED-ovi stevardesi.", [11])
# 
# Namig: lahko si pomagate z razbitjem
# besedila na besede (ni nujno, da se naloge lotite tako, obstaja veliko različnih poti).
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
        Check.current_part['token'] = 'eyJ1c2VyIjo2NDgzLCJwYXJ0IjoyODI3OX0:1mxsCx:b2p-1AkhNkySn5VoxUi4ojM8ug4'
        try:
            pravilno = True
            
            if ".count" not in Check.current_part['solution']:
                Check.feedback("Lahko si pomagate z metodo count, šlo bo veliko lažje.")
            if odlicno("odlično") != 1:
                Check.equal('odlicno("odlično")', 1)
                Check.error('Verjetno ste se nekje zatipkali.')
                pravilno = False
            elif odlicno("Odlično") != 1:
                Check.equal('odlicno("Odlično")', 1)
                Check.error('Ne pozabite na velike začetnice.')
                pravilno = False
            elif not Check.equal('odlicno("123")', 0) or \
                not Check.equal('odlicno("")', 0):
                pravilno = False
            
            elif odlicno("odlična odličen odlične odlični") != 4 or\
                 odlicno("Odlična Odličen Odlične Odlični") != 4:
                Check.equal('odlicno("odlična odličen odlične odlični")', 4)
                Check.equal('odlicno("Odlična Odličen Odlične Odlični")', 4)
                Check.error('Poskusite poiskati boljši skupni koren.')
                pravilno = False
            elif not Check.equal('odlicno("hgfkjodličnoOdličnesjhoskodlični")', 3) or \
                 not Check.equal('odlicno("hgfkjodločnoOdličnesjhoskodlični")', 2):
                pravilno = False
            
            if pravilno:
                Check.feedback("No tole ste pa res odlično rešili.")
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjo2NDgzLCJwYXJ0IjoyODI4MH0:1mxsCx:DF66X9zrBVT6EF87SxK20osgK9E'
        try:
            (tekst, indeks) = popravi_sled("Sled")
            if (tekst, indeks) == ("Sled", [0]):
                if popravi_sled("g Sled")[0] == "g SLED":
                    Check.error('Preverite, ali se niz res bere od začetka. Morda začne z indeksom 1 namesto 0.')
                else:
                    Check.error('Vaša koda ne najde nobene pojavitve besede "Sled". Morda ' \
                                'ste se zatipkali, ali pa kakšna funkcija deluje malo drugače, kot si predstavljate.')
            elif tekst in {'SSLEDled', 'SLEDled', 'SSLED', 'SLEDSled', 'SLEDed', 'SLEDd'}:
                Check.error('Vaša funkcija "Sled" popravi v {0}. Pazite, da ne dodate nobene' \
                            ' izmed starih črk nazaj v nov niz.'.format(tekst))
            elif tekst != "SLED":
                Check.error('Namesto v "SLED" se "Sled" spremeni v {0}, '\
                            'poskusite prestaviti dodajanje črke ali besede prej v kodi.'.format(tekst))
            elif indeks == []:
                Check.error('Beseda "Sled" se dobro pretvori, vendar pa ste pozabili dodati indeks '
                            'v tabelo indeksov.')
            elif len(indeks) > 1:
                Check.error('Beseda "Sled" se dobro pretvori, vendar pa ste dodali malo preveč ' \
                            'indeksov. Najbolje, da indeks v tabelo dodajate le tam, kjer ' \
                            'začnete pisati popravljeno besedo "SLED". Dodali ste {0} '\
                            'namesto [0]'.format(indeks))
            else:
                if popravi_sled('sled') == ("SLED", [0]):
                    Check.error('Kadar se pojavi "sled" (z malo začetnico) tega ne popravljajte.')
                Check.equal('popravi_sled("Let z družbo Sled mi je bil v veliko veselje.")',
                        ("Let z družbo SLED mi je bil v veliko veselje.", [13]))
                Check.equal('popravi_sled("Sledil sem stevardesi Sleda.")', ("SLEDil sem stevardesi SLEDa.", [0, 22]))
                Check.equal('popravi_sled("To gotovo ni bil moj poslednji let z družbo Sled.")',
                            ("To gotovo ni bil moj poslednji let z družbo SLED.", [44]))
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjo2NDgzLCJwYXJ0IjoyODI4MX0:1mxsCx:yp0_GX-UYlOoUefh8PwSsYyBQWM'
        try:
            prekinjen = False
            koncnice = ['u', 'a', 'om', 'ov', 'ovi', 'ovem', 'ova', 'ovo',
                'ove', 'ovim', 'ovega', 'ovemu']
            (tekst, indeks) = boljse_popravi_sled("Sled")
            if tekst == "Sled":
                prekinjen = True
                if boljse_popravi_sled("g Sled")[0] == "g SLED":
                    Check.error('Preverite, ali se niz res bere od začetka. Morda začne z indeksom 1 namesto 0.')
                else:
                    Check.error('Vaša koda ne najde nobene pojavitve besede "Sled". Morda '
                                'ste se zatipkali, ali pa kakšna funkcija deluje malo drugače, kot si predstavljate.')
            if not prekinjen and tekst in {'SSLEDled', 'SLEDled', 'SSLED', 'SLEDSled', 'SLEDed', 'SLEDd'}:
                prekinjen = True
                Check.error('Vaša funkcija "Sled" popravi v {0}. Pazite, da ne dodate nobene' \
                            ' izmed starih črk nazaj v nov niz.'.format(tekst))
            if not prekinjen and tekst != "SLED":
                prekinjen = True
                Check.error('Namesto v "SLED" se vaš "Sled" spremeni v {0}. '\
                            'Poskusite prestaviti dodajanje črke ali besede prej v kodi.'.format(tekst)) and\
                Check.equal("boljse_popravi_sled('')[0]", '') and\
                Check.equal('boljse_popravi_sled("Let z družbo Sled mi je bil v veliko veselje.")[0]',
                        "Let z družbo SLED mi je bil v veliko veselje")
            if not prekinjen and indeks == []:
                prekinjen = True
                Check.error('Besedo "Sled" ste dobro pretvorili, vendar pa ste pozabili dodati indeks '
                            'v tabelo indeksov.')
            if not prekinjen and len(indeks) > 1:
                prekinjen = True
                Check.error('Besedo "Sled" ste dobro pretvorili, vendar pa ste dodali malo preveč ' \
                            'indeksov. Najbolje, da indeks v tabelo dodajate le tam, kjer ' \
                            'začnete pisati popravljeno besedo "SLED". Dodali ste {0} '\
                            'namesto [0]'.format(indeks))
            if not prekinjen and indeks != [0]:
                prekinjen = True
                Check.error('Besedo "Sled" ste dobro pretvorili, vendar pa ste dobili indeks {0}, namesto [0].'
                            'Preverite, če ste začeli s pravim indeksom.'.format(indeks))
            if not prekinjen:
                Check.feedback("Osnovni primeri odlično delujejo. Gremo naprej.")
            if not prekinjen and boljse_popravi_sled("Sledov pilot je super.")[0] != "SLED-ov pilot je super." :
                prekinjen = True
                Check.equal('boljse_popravi_sled("Sledov pilot je super.")[0]',
                        "SLED-ov pilot je super.")
                Check.error('Malo še popravite dodajanje vezaja v besede z izbranimi končnicami.')
            if not prekinjen :
                for koncnica in koncnice:
                    if boljse_popravi_sled("Sled{0}".format(koncnica))[0] != "SLED-{0}".format(koncnica):
                        prekinjen  = True
                        Check.equal('boljse_popravi_sled("Sled{0}")[0]'.format(koncnica),
                                "SLED-{0}".format(koncnica))
                        Check.error('Očitno, vam je nekaj končnic ušlo. Upam, da ne pišete if stavka za vsako posebej.')
                        break
            if not prekinjen and "SLED" == boljse_popravi_sled("Sledkjfh.")[0][:4]:
                prekinjen = True
                Check.equal('boljse_popravi_sled("Sledil sem Sledovi stevardesi.")[0]',
                        "Sledil sem SLED-ovi stevardesi.")
                Check.secret('boljse_popravi_sled("Sledkjfh.")[0]',
                        "Sledkjfh.")
                Check.error('Ne spremenite kar vseh pojavitev besede "Sled"')
            if not prekinjen and boljse_popravi_sled("To gotovo ni bil moj poslednji let z družbo Sled.")[0] != "To gotovo ni bil moj poslednji let z družbo SLED.":
                prekinjen = True
                Check.equal('boljse_popravi_sled("To gotovo ni bil moj poslednji let z družbo Sled.")[0]',
                        "To gotovo ni bil moj poslednji let z družbo SLED.")
                Check.error("Pazite na ločila, če so to 'končnica' besede Sled.")
            
            # preverimo še pravilnost indeksov:
            if not prekinjen:
                Check.feedback("Izgleda, da pravilno spreminjate besede. Poglejmo kako gredo indeksi.")
            if not prekinjen:
                testi = [('', [], "Kje dodajate indekse?"),
                         ("Sledil sem Sledovi stevardesi.", [11], "Vaš indeks je napačen. Ga pravilno povečujete? Pazite na presledke."),
                         ("Sledil sem stevardesi Sleda, ki me je odpeljala na Sledovo letalo. ", [22, 52],
                          "Vaš indeks je napačen. Ga pravilno povečujete? Pazite na ločila."),
                         ("Sledova letalska hrana je pač Sledova.", [0, 31], "Pazite, da dodate indekse v novem besedilu z vezajem.")]
                for (test, resitev, odziv) in testi:
                    #(tekst, indeks) = boljse_popravi_sled(test)
                    if boljse_popravi_sled(test)[1] != resitev:
                        print()
                        Check.equal("boljse_popravi_sled('{0}')[1]".format(test), resitev)
                        Check.error(odziv)
                        prekinjen = True
                        break
            if not prekinjen:
                if Check.equal('boljse_popravi_sled("Sledova letalska hrana je pač Sledova.")',
                           ("SLED-ova letalska hrana je pač SLED-ova.", [0, 31])):
                    Check.feedback("Uau, tole je pa bila naloga. Dokazali ste, da obvladate nize, čestitke!")
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
