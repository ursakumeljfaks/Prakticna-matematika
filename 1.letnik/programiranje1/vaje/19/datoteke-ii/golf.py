# =============================================================================
# Golf
#
# Na vsakem zanimivem igrišču za golf so ovire: jezero, pesek, ...
# 
# `Jezero` je krog, podan kot trojica `(x,y,r)`. `x` in `y` sta koordinati središča,
# `r` pa polmer.
# `Pesek` je pravokotnik, podan kot četverica`(x1,y1,x2,y2)`. Predpostaviš lahko, da
# so to po vrsti koordinate levega spodnjega in desnega zgornjega oglišča.
# Vse koordinate računamo na tri decimalke.
# =====================================================================@028453=
# 1. podnaloga
# Na datoteki imamo zapisane podatke o posameznih udarcih v obliki polarnih koordinat (kot
# je podan v stopinjah).
# V vsaki vrstici sta zapisani celi števili `r` in `fi`, ločeni s presledkom.
# Napišite funkcijo `datoteka_polozajev(vhod, izhod)`, ki naj prebere datoteko `vhod` in
# ustvari novo datoteko `izhod` tako, da je v vsaki vrstici zapisan njen trenutni položaj
# (v obliki decimalnih števil, zaokroženih na 3 decimalna mesta)
# in ločenih s presledkom. V ta namen uporabite formatiranje s pomočjo metode _format_.
# Začetni položaj naj bo v točki `(0,0)`.
# =============================================================================
from math import *
def datoteka_polozajev(vhod, izhod):
    '''Iz seznama udarcev, podanih v polarnih koordinatah, na datoteko zapiše
       kartezične koordinate položaja točk'''
    x,y = 0,0
    with open(izhod, "w") as dat2:
        with open(vhod, "r") as dat1:
            for vrstica in dat1:
                r, fi = vrstica.split(" ")
                x += cos(float(fi)*pi/180)*float(r)
                y += sin(float(fi)*pi/180)*float(r)
                print("{0:.3f}".format(x), "{0:.3f}".format(y), file=dat2)
# =====================================================================@028454=
# 2. podnaloga
# Podan je seznam položajev žogic po posameznem udarcu in seznam, katerega vsak element
# je nabor, ki podaja jezero ali pesek. Napišite metodo `se_izogne(pot, ovire)`, ki pove, ali
# se pot v celoti izogne oviram. Pazi: jezero je podano z naborom treh, pesek pa z naborom štirih števil.
# 
# Najprej napišite metodi `je_v_jezeru(zogica, jezero)` in `je_v_pesku(zogica, pesek)`, ki
# povesta, ali je žogica v jezeru ali v pesku. Žogica je podana kot par `(x,y)`, torej "nima dimenzije".
# =============================================================================
def je_v_jezeru(zogica, jezero):
    """Ali se je zogica znasla v jezeru(krogu)?"""
    x1, y1 = zogica
    x2, y2, r = jezero
    razdalja = (x1-x2)**2 + (y1-y2)**2
    return razdalja <= r**2 #ali je znotraj kroga?

def je_v_pesku(zogica, pesek):
    """Ali se je zogica znasla v pesku(kvadratu)?"""
    x0, y0 = zogica
    x1,y1,x2,y2 = pesek
    return x1 <= x0 <= x2 and y1 <= y0 <= y2

def se_izogne(pot, ovire):
    for delna_pot in pot:
        for ovira in ovire:
            if len(ovira)==3 and je_v_jezeru(delna_pot, ovira): #len(ovira)==3 preveri ali imamo res potrebne 3 podatke
                return False
            elif len(ovira)==4 and je_v_pesku(delna_pot, ovira):
                return False
    return True
# =====================================================================@028455=
# 3. podnaloga
# Napišite metodo `kje_je_zogica(datoteka, zacetek, ovire)`, ki
# vrne vektor od začenega do končnega položaja ali None,
# če žogica kdaj vmes pade v oviro.
# Posamezni udarci so v polarnih koordinatah zapisani na datoteko, začetek pa je
# podan kot par `(x,y)`.
# =============================================================================
def kje_je_zogica(datoteka, zacetek, ovire):
    """Napiše vektor potovanja zogice"""
    x, y = zacetek
    #x_kopija, y_kopija = zacetek
    sez_tock = []
    with open(datoteka, "r") as dat:
        for vrstica in dat:
            r, fi = vrstica.split(" ")
            x += cos(float(fi)*pi/180)*float(r)
            y += sin(float(fi)*pi/180)*float(r)
            sez_tock.append((x,y))
    if not se_izogne(sez_tock, ovire):
        return None
    else:
        return (round(x-zacetek[0], 3),round(y-zacetek[0],3)) 




































































































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
        Check.current_part['token'] = 'eyJwYXJ0IjoyODQ1MywidXNlciI6NjQ4M30:1nU4SI:z3D0AySkQSnXb6ozJXDH-3d4s7Y'
        try:
            def _makefile1(fname, ponovitev):
                with open(fname, "w") as f:
                    for i in range(ponovitev):
                        print("1 90", file=f)
                        print("2 -30", file=f)
                        print("2 210", file=f)
                        print("1 90", file=f)
            
            
            def _makefile2(fname, ponovitev):
                with open(fname, "w") as f:
                    for i in range(ponovitev):
                        print("0.000 1.000", file=f)
                        print("1.732 0.000", file=f)
                        print("0.000 -1.000", file=f)
                        print("0.000 0.000", file=f)
            
            
            def _istedatoteke(ena, dva):
                with open(ena) as f1, open(dva) as f2:
                    vrste1 = f1.read().strip()
                    vrste2 = f2.read().strip()
                    if vrste1 == vrste2:
                        return True
                    else:
                        print("Izhodna datoteka vsebuje naslednje vrstice: ")
                        print(vrste1)
                        print("Morala pa bi vsebovati naslednje vrstice: ")
                        print(vrste2)
            
            
            def _removefiles(*ime):
                import os
            
                for i in ime:
                    os.remove(i)
            
            
            _makefile1("_3d.in", 1)
            _makefile2("_3do.out", 1)
            datoteka_polozajev("_3d.in", "_3d.out")
            if not _istedatoteke("_3d.out", "_3do.out"):
                Check.error("Izhodna datoteka je napačna")
            _makefile1("_3d1.in", 2)
            _makefile2("_3do1.out", 2)
            datoteka_polozajev("_3d1.in", "_3d1.out")
            if not _istedatoteke("_3d1.out", "_3do1.out"):
                Check.error("Izhodna datoteka je napačna")
            _removefiles("_3d.in", "_3do.out", "_3d.out", "_3d1.in", "_3do1.out", "_3d1.out")
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJwYXJ0IjoyODQ1NCwidXNlciI6NjQ4M30:1nU4SI:dHQbh5RcIhMR5WSpaMLtjiTGi1A'
        try:
            Check.equal("se_izogne([(0,0),(1,2),(3,4)],[(2,3,4),(1,1,2,2)])", False)
            Check.equal("se_izogne([(1,1),(1,2),(3,4)],[(2,3,14),(1,1,2,2)])", False)
            Check.equal("se_izogne([(0,0),(0,1)],[(2,3,1),(1,1,2,2)])", True)
            Check.equal("se_izogne([(0,0),(1,2),(3,4)],[(2,3,1),(2,2,3,3)])", True)
            Check.equal("se_izogne([(1,1),(1,2),(3,4)],[(1,1,1),(1,1,2,2)])", False)
            Check.equal("se_izogne([(1,1),(1,2),(3,4)],[(0,0,1),(1,1,2,2)])", False)
            Check.equal("se_izogne([(0,2),(1,2),(3,4)],[(0,0,1),(1,1,2,2)])", False)
            Check.equal("se_izogne([(0,2),(1,3),(3,4)],[(0,0,1),(1,1,2,2)])", True)
            Check.equal("se_izogne([(0,2),(1,3),(3,4),(0,2),(1,3),(3,4)],[(0,0,1),(1,1,2,2)])", True)
            Check.equal("se_izogne([(0,2)],[(0,0,1),(1,1,2,2)])", True)
            Check.equal("se_izogne([(0,2),(1,3),(3,4),(0,2),(1,3),(3,4)],[])", True)
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJwYXJ0IjoyODQ1NSwidXNlciI6NjQ4M30:1nU4SI:PME9gNoXOfHfTVCbqdf4nKrEfvA'
        try:
            def _makefile1(fname, n):
                with open(fname, "w") as f:
                    poteze = [
                        "1 90",
                        "2 -30",
                        "2 210",
                        "1 90",
                        "1 90",
                        "2 -30",
                        "2 210",
                        "1 90",
                        "1 90",
                        "2 -30",
                        "2 210",
                        "1 90",
                    ]
                    for i in range(min(n, len(poteze))):
                        print(poteze[i], file=f)
            
            
            _makefile1("_kje1.in", 4)
            _makefile1("_kje2.in", 1)
            _makefile1("_kje3.in", 12)
            _makefile1("_kje4.in", 11)
            _makefile1("_kje5.in", 10)
            Check.equal('kje_je_zogica("_kje1.in",(0,0), [(2,3,4),(1,1,2,2)])', None)
            Check.equal('kje_je_zogica("_kje1.in",(0,0), [(2,3,1),(2,2,3,3)])', (0, 0))
            Check.equal('kje_je_zogica("_kje2.in",(0,0), [(2,3,1),(1,1,2,2)])', (0, 1))
            Check.equal('kje_je_zogica("_kje2.in",(0,0), [(0,0,2),(2,2,3,3)])', None)
            Check.equal('kje_je_zogica("_kje3.in",(0,0), [(2,3,4),(1,1,2,2)])', None)
            Check.equal('kje_je_zogica("_kje3.in",(0,0), [(0,0,0.5),(1,1,2,2)])', None)
            Check.equal('kje_je_zogica("_kje3.in",(0,0), [(0,0,0.5),(-1,-1,2,2)])', None)
            Check.equal('kje_je_zogica("_kje3.in",(0,0), [(2,3,1),(2,2,3,3)])', (0, 0))
            Check.equal('kje_je_zogica("_kje3.in",(0,0), [(2,3,1),(1,1,3,3)])', (0, 0))
            Check.equal('kje_je_zogica("_kje4.in",(0,0), [(2,3,1),(2,2,3,3)])', (0, -1))
            Check.equal('kje_je_zogica("_kje4.in",(0,0), [(2,3,1),(1,1,3,3)])', (0, -1))
            Check.equal('kje_je_zogica("_kje5.in",(0,0), [(2,3,1),(1,1,3,3)])', (1.732, 0.0))
            _removefiles("_kje1.in", "_kje2.in", "_kje3.in", "_kje4.in", "_kje5.in")
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
