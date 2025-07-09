# =============================================================================
# Datumi
#
# Koledar, ki ga trenutno uporabljamo v zahodnem svetu, se imenuje
# [gregorijanski koledar](http://sl.wikipedia.org/wiki/Gregorijanski_koledar).
# Pri tej nalogi bomo implementirali razred `Datum`, ki bo omogočal
# predstavitev datumov v gregorijanskem koledarju in računanje z njimi.
# =====================================================================@038197=
# 1. podnaloga
# Sestavite funkcijo `je_prestopno(leto)`, ki preveri, ali je dano `leto`
# prestopno (po gregorijanskem koledarju). Zgled:
# 
#     >>> je_prestopno(2004)
#     True
#     >>> je_prestopno(1900)
#     False
# =============================================================================
def je_prestopno(leto):
    return (leto % 4 == 0 and leto % 100 != 0) or leto % 400 == 0
# =====================================================================@038198=
# 2. podnaloga
# Sestavite funkcijo `stevilo_dni(leto)`, ki vrne število dni v danem letu.
# Zgled:
# 
#     >>> stevilo_dni(2015)
#     365
#     >>> stevilo_dni(2016)
#     366
# 
# _Nasvet_: Uporabite funkcijo `je_prestopno`.
# =============================================================================
def stevilo_dni(leto):
    return 366 if je_prestopno(leto) else 365
# =====================================================================@038199=
# 3. podnaloga
# Sestavite funkcijo `dolzine_mesecev(leto)`, ki vrne seznam dolžine 12, ki ima
# za elemente števila dni po posameznih mesecih v danem letu. Zgled:
# 
#     >>> dolzine_mesecev(2015)
#     [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# =============================================================================
def dolzine_mesecev(leto):
    dnevi = [0] * 12
    for i in range(7):
        if i % 2 == 0:
            dnevi[i] = 31
        else:
            dnevi[i] = 30
        if je_prestopno(leto):
            dnevi[1] = 29
        else:
            dnevi[1] = 28
    
    for i in range(7, 12):
        if i % 2 == 0:
            dnevi[i] = 30
        else:
            dnevi[i] = 31
        
    return dnevi
        
# =====================================================================@038200=
# 4. podnaloga
# Definirajte razred `Datum`, s katerim predstavimo datum. Najprej sestavite
# konstruktor `__init__(self, dan, mesec, leto)`. Nastali objekt naj ima
# atribute `dan`, `mesec` in `leto`. Zgled:
# 
#     >>> d = Datum(8, 2, 1849)
#     >>> d.dan
#     8
#     >>> d.mesec
#     2
#     >>> d.leto
#     1849
# =============================================================================
class Datum:
    def __init__(self, dan, mesec, leto):
        self.dan = dan
        self.mesec = mesec
        self.leto = leto
# =====================================================================@038201=
# 5. podnaloga
# Sestavite metodo `__str__(self)`, ki predstavi datum v obliki
# `'dan. mesec. leto'`. Zgled:
# 
#     >>> d = Datum(8, 2, 1849)
#     >>> print(d)
#     8. 2. 1849
# =============================================================================
class Datum(Datum):
    def __str__(self):
        return f"{self.dan}. {self.mesec}. {self.leto}"
# =====================================================================@038202=
# 6. podnaloga
# Sestavite še metodo `__repr__(self)`, ki vrne niz oblike
# `'Datum(dan, mesec, leto)'`. Zgled:
# 
#     >>> d = Datum(8, 2, 1849)
#     >>> d
#     Datum(8, 2, 1849)
# =============================================================================
class Datum(Datum):
    def __repr__(self):
        return f"Datum({self.dan}, {self.mesec}, {self.leto})"
# =====================================================================@038203=
# 7. podnaloga
# Sestavite metodo `je_veljaven(self)`, ki preveri, ali je datum veljaven.
# Zgled:
# 
#     >>> d1 = Datum(8, 2, 1849)
#     >>> d1.je_veljaven()
#     True
#     >>> d2 = Datum(5, 14, 2014)
#     >>> d2.je_veljaven()
#     False
# =============================================================================
class Datum(Datum):
    def je_veljaven(self):
        return (1 <= self.mesec <= 12) and (0 < self.leto) and (1 <= self.dan <= dolzine_mesecev(self.leto)[self.mesec - 1])
# =====================================================================@038204=
# 8. podnaloga
# Sestavite metodo `__lt__(self, other)`, ki datum primerja z drugim datumom
# (metoda naj vrne `True`, če je prvi datum manjši, in `False`, če ni).
# 
# Ta metod omogoča, da lahko datume primerjamo kar z operatorjema `<` in `>`.
# Na primer:
# 
#     >>> Datum(31, 12, 1999) < Datum(1, 1, 2000)
#     True
# =============================================================================
class Datum(Datum):
    def __lt__(self, other):
        if self.leto < other.leto:
            return True
        elif self.leto > other.leto:
            return False
        else:
            if self.mesec < other.mesec:
                return True
            elif self.mesec > other.mesec:
                return False
            else:
                return self.dan < other.dan
            
# =====================================================================@038205=
# 9. podnaloga
# Sestavite metodo `__eq__(self, other)`, ki datum primerja z drugim datumom
# (metoda naj vrne `True`, če sta datuma enaka, in `False`, če nista).
# 
# Ta metoda omogoča, da lahko datume primerjamo kar z operatorjema `==` in
# `!=`. Na primer:
# 
#     >>> Datum(31, 12, 1999) != Datum(1, 1, 2000)
#     True
# =============================================================================
class Datum(Datum):
    def __eq__(self, other):
        return (self.dan == other.dan) and (self.mesec == other.mesec) and (self.leto == other.leto)
# =====================================================================@038206=
# 10. podnaloga
# Sestavite metodo `dan_v_letu(self)`, ki izračuna, koliko dni je minilo od
# začetka leta do danega datuma. Zgled:
# 
#     >>> d = Datum(1, 11, 2014)
#     >>> d.dan_v_letu()
#     305
# 
# _Nasvet_: Ali si lahko kako pomagate s funkcijo `dolzine_mesecev`?
# =============================================================================
class Datum(Datum):
    def dan_v_letu(self):
        st = 0
        for i in range(self.mesec-1):
            st += dolzine_mesecev(self.leto)[i]
        st += self.dan
        return st
# =====================================================================@038207=
# 11. podnaloga
# Sestavite metodo `razlika(self, other)`, ki kot argument dobi še en objekt
# razreda `Datum` in vrne število dni med datumoma. Dobra rešitev deluje _brez_
# uporabe zanke po vseh letih med danima datuma (ima časovno zahtevnost
# $O(1)$). Zgled:
# 
#     >>> d1 = Datum(1, 11, 2014)
#     >>> d2 = Datum(14, 10, 2014)
#     >>> d1.razlika(d2)
#     18
# 
# Namig: Najprej sestavite pomožno metodo `dni_od_zacetka(self)`, ki izračuna,
# koliko dni je minilo od "začetka štetja" (`leto==0`, `mesec=1`, `dan=1`).
# Razliko v dnevih med `self` in `other` lahko nato preprosto izračunate z
# metodo `dni_od_zacetka`. 
# 
# Opomba: Gregorijanski koledar seveda ni bil v veljavi leta 0, ampak za
# potrebe računanja se lahko pretvarjamo, da ga je uporabljal tudi Julij Cezar.
# =============================================================================
class Datum(Datum):
    def dni_od_zacetka(self):
        st = 0
        for i in range(self.leto - 1):
            st += stevilo_dni(i)
        for i in range(self.mesec - 1):
            st += dolzine_mesecev(self.leto)[i]
        st += self.dan
        return st 

    def razlika(self, other):
        return self.dni_od_zacetka() - other.dni_od_zacetka()
# =====================================================================@038208=
# 12. podnaloga
# Sestavite metodo `dan_v_tednu(self)`, ki vrne številko dneva v tednu
# (1 = ponedeljek, 2 = torek, …, 7 = nedelja). Lahko si pomagate z
# [Zellerjevim obrazcem](http://en.wikipedia.org/wiki/Zeller's_congruence).
# Druga možnost je, da izračunate razliko med datumom `self` in nekim fiksnim
# datumom, za katerega že poznate dan v tednu. Zgled:
# 
#     >>> d = Datum(1, 11, 2014)
#     >>> d.dan_v_tednu()
#     6
# =============================================================================
class Datum(Datum): 
    def dan_v_tednu(self):
        m = (self.mesec + 1) if self.mesec < 3 else (self.mesec - 9)
        K = self.leto % 100
        J = self.leto // 100

        h = (self.dan + (13 * m + 1) // 5 + K + K // 4 + J // 4 + 5 * J) % 7        
        d = (h + 5) % 7 + 1
        return d
# =====================================================================@038209=
# 13. podnaloga
# Sestavite *statično* metodo `dan_v_letu_stat(leto, dan)`, ki za parametra
# dobi leto in zaporedno številko dneva v letu ter sestavi in vrne ustrezen
# datum. Zgled:
# 
#     >>> Datum.dan_v_letu_stat(2014, 305)
#     Datum(1, 11, 2014)
# =============================================================================






































































































# ============================================================================@
# fmt: off
"Če vam Python sporoča, da je v tej vrstici sintaktična napaka,"
"se napaka v resnici skriva v zadnjih vrsticah vaše kode."

"Kode od tu naprej NE SPREMINJAJTE!"

# isort: off
import json
import os
import re
import shutil
import sys
import traceback
import urllib.error
import urllib.request
import io
from contextlib import contextmanager


class VisibleStringIO(io.StringIO):
    def read(self, size=None):
        x = io.StringIO.read(self, size)
        print(x, end="")
        return x

    def readline(self, size=None):
        line = io.StringIO.readline(self, size)
        print(line, end="")
        return line


class Check:
    parts = None
    current_part = None
    part_counter = None

    @staticmethod
    def has_solution(part):
        return part["solution"].strip() != ""

    @staticmethod
    def initialize(parts):
        Check.parts = parts
        for part in Check.parts:
            part["valid"] = True
            part["feedback"] = []
            part["secret"] = []

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
        Check.current_part["feedback"].append(message.format(*args, **kwargs))

    @staticmethod
    def error(message, *args, **kwargs):
        Check.current_part["valid"] = False
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
            v = complex(
                Check.clean(x.real, digits, typed), Check.clean(x.imag, digits, typed)
            )
        elif t is list:
            v = list([Check.clean(y, digits, typed) for y in x])
        elif t is tuple:
            v = tuple([Check.clean(y, digits, typed) for y in x])
        elif t is dict:
            v = sorted(
                [
                    (Check.clean(k, digits, typed), Check.clean(v, digits, typed))
                    for (k, v) in x.items()
                ]
            )
        elif t is set:
            v = sorted([Check.clean(y, digits, typed) for y in x])
        else:
            v = x
        return (t, v) if typed else v

    @staticmethod
    def secret(x, hint=None, clean=None):
        clean = Check.get("clean", clean)
        Check.current_part["secret"].append((str(clean(x)), hint))

    @staticmethod
    def equal(expression, expected_result, clean=None, env=None, update_env=None):
        global_env = Check.init_environment(env=env, update_env=update_env)
        clean = Check.get("clean", clean)
        actual_result = eval(expression, global_env)
        if clean(actual_result) != clean(expected_result):
            Check.error(
                "Izraz {0} vrne {1!r} namesto {2!r}.",
                expression,
                actual_result,
                expected_result,
            )
            return False
        else:
            return True

    @staticmethod
    def approx(expression, expected_result, tol=1e-6, env=None, update_env=None):
        try:
            import numpy as np
        except ImportError:
            Check.error("Namestiti morate numpy.")
            return False
        if not isinstance(expected_result, np.ndarray):
            Check.error("Ta funkcija je namenjena testiranju za tip np.ndarray.")

        if env is None:
            env = dict()
        env.update({"np": np})
        global_env = Check.init_environment(env=env, update_env=update_env)
        actual_result = eval(expression, global_env)
        if type(actual_result) is not type(expected_result):
            Check.error(
                "Rezultat ima napačen tip. Pričakovan tip: {}, dobljen tip: {}.",
                type(expected_result).__name__,
                type(actual_result).__name__,
            )
            return False
        exp_shape = expected_result.shape
        act_shape = actual_result.shape
        if exp_shape != act_shape:
            Check.error(
                "Obliki se ne ujemata. Pričakovana oblika: {}, dobljena oblika: {}.",
                exp_shape,
                act_shape,
            )
            return False
        try:
            np.testing.assert_allclose(
                expected_result, actual_result, atol=tol, rtol=tol
            )
            return True
        except AssertionError as e:
            Check.error("Rezultat ni pravilen." + str(e))
            return False

    @staticmethod
    def run(statements, expected_state, clean=None, env=None, update_env=None):
        code = "\n".join(statements)
        statements = "  >>> " + "\n  >>> ".join(statements)
        global_env = Check.init_environment(env=env, update_env=update_env)
        clean = Check.get("clean", clean)
        exec(code, global_env)
        errors = []
        for x, v in expected_state.items():
            if x not in global_env:
                errors.append(
                    "morajo nastaviti spremenljivko {0}, vendar je ne".format(x)
                )
            elif clean(global_env[x]) != clean(v):
                errors.append(
                    "nastavijo {0} na {1!r} namesto na {2!r}".format(
                        x, global_env[x], v
                    )
                )
        if errors:
            Check.error("Ukazi\n{0}\n{1}.", statements, ";\n".join(errors))
            return False
        else:
            return True

    @staticmethod
    @contextmanager
    def in_file(filename, content, encoding=None):
        encoding = Check.get("encoding", encoding)
        with open(filename, "w", encoding=encoding) as f:
            for line in content:
                print(line, file=f)
        old_feedback = Check.current_part["feedback"][:]
        yield
        new_feedback = Check.current_part["feedback"][len(old_feedback) :]
        Check.current_part["feedback"] = old_feedback
        if new_feedback:
            new_feedback = ["\n    ".join(error.split("\n")) for error in new_feedback]
            Check.error(
                "Pri vhodni datoteki {0} z vsebino\n  {1}\nso se pojavile naslednje napake:\n- {2}",
                filename,
                "\n  ".join(content),
                "\n- ".join(new_feedback),
            )

    @staticmethod
    @contextmanager
    def input(content, visible=None):
        old_stdin = sys.stdin
        old_feedback = Check.current_part["feedback"][:]
        try:
            with Check.set_stringio(visible):
                sys.stdin = Check.get("stringio")("\n".join(content) + "\n")
                yield
        finally:
            sys.stdin = old_stdin
        new_feedback = Check.current_part["feedback"][len(old_feedback) :]
        Check.current_part["feedback"] = old_feedback
        if new_feedback:
            new_feedback = ["\n  ".join(error.split("\n")) for error in new_feedback]
            Check.error(
                "Pri vhodu\n  {0}\nso se pojavile naslednje napake:\n- {1}",
                "\n  ".join(content),
                "\n- ".join(new_feedback),
            )

    @staticmethod
    def out_file(filename, content, encoding=None):
        encoding = Check.get("encoding", encoding)
        with open(filename, encoding=encoding) as f:
            out_lines = f.readlines()
        equal, diff, line_width = Check.difflines(out_lines, content)
        if equal:
            return True
        else:
            Check.error(
                "Izhodna datoteka {0}\n  je enaka{1}  namesto:\n  {2}",
                filename,
                (line_width - 7) * " ",
                "\n  ".join(diff),
            )
            return False

    @staticmethod
    def output(expression, content, env=None, update_env=None):
        global_env = Check.init_environment(env=env, update_env=update_env)
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        too_many_read_requests = False
        try:
            exec(expression, global_env)
        except EOFError:
            too_many_read_requests = True
        finally:
            output = sys.stdout.getvalue().rstrip().splitlines()
            sys.stdout = old_stdout
        equal, diff, line_width = Check.difflines(output, content)
        if equal and not too_many_read_requests:
            return True
        else:
            if too_many_read_requests:
                Check.error("Program prevečkrat zahteva uporabnikov vnos.")
            if not equal:
                Check.error(
                    "Program izpiše{0}  namesto:\n  {1}",
                    (line_width - 13) * " ",
                    "\n  ".join(diff),
                )
            return False

    @staticmethod
    def difflines(actual_lines, expected_lines):
        actual_len, expected_len = len(actual_lines), len(expected_lines)
        if actual_len < expected_len:
            actual_lines += (expected_len - actual_len) * ["\n"]
        else:
            expected_lines += (actual_len - expected_len) * ["\n"]
        equal = True
        line_width = max(
            len(actual_line.rstrip())
            for actual_line in actual_lines + ["Program izpiše"]
        )
        diff = []
        for out, given in zip(actual_lines, expected_lines):
            out, given = out.rstrip(), given.rstrip()
            if out != given:
                equal = False
            diff.append(
                "{0} {1} {2}".format(
                    out.ljust(line_width), "|" if out == given else "*", given
                )
            )
        return equal, diff, line_width

    @staticmethod
    def init_environment(env=None, update_env=None):
        global_env = globals()
        if not Check.get("update_env", update_env):
            global_env = dict(global_env)
        global_env.update(Check.get("env", env))
        return global_env

    @staticmethod
    def generator(
        expression,
        expected_values,
        should_stop=None,
        further_iter=None,
        clean=None,
        env=None,
        update_env=None,
    ):
        from types import GeneratorType

        global_env = Check.init_environment(env=env, update_env=update_env)
        clean = Check.get("clean", clean)
        gen = eval(expression, global_env)
        if not isinstance(gen, GeneratorType):
            Check.error("Izraz {0} ni generator.", expression)
            return False

        try:
            for iteration, expected_value in enumerate(expected_values):
                actual_value = next(gen)
                if clean(actual_value) != clean(expected_value):
                    Check.error(
                        "Vrednost #{0}, ki jo vrne generator {1} je {2!r} namesto {3!r}.",
                        iteration,
                        expression,
                        actual_value,
                        expected_value,
                    )
                    return False
            for _ in range(Check.get("further_iter", further_iter)):
                next(gen)  # we will not validate it
        except StopIteration:
            Check.error("Generator {0} se prehitro izteče.", expression)
            return False

        if Check.get("should_stop", should_stop):
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
                print("{0}. podnaloga je brez rešitve.".format(i + 1))
            elif not part["valid"]:
                print("{0}. podnaloga nima veljavne rešitve.".format(i + 1))
            else:
                print("{0}. podnaloga ima veljavno rešitev.".format(i + 1))
            for message in part["feedback"]:
                print("  - {0}".format("\n    ".join(message.splitlines())))

    settings_stack = [
        {
            "clean": clean.__func__,
            "encoding": None,
            "env": {},
            "further_iter": 0,
            "should_stop": False,
            "stringio": VisibleStringIO,
            "update_env": False,
        }
    ]

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
        with Check.set(clean=(lambda x: clean(x, **kwargs)) if kwargs else clean):
            yield

    @staticmethod
    @contextmanager
    def set_environment(**kwargs):
        env = dict(Check.get("env"))
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
        if stringio is None or stringio is Check.get("stringio"):
            yield
        else:
            with Check.set(stringio=stringio):
                yield


def _validate_current_file():
    def extract_parts(filename):
        with open(filename, encoding="utf-8") as f:
            source = f.read()
        part_regex = re.compile(
            r"# =+@(?P<part>\d+)=\s*\n"  # beginning of header
            r"(\s*#( [^\n]*)?\n)+?"  # description
            r"\s*# =+\s*?\n"  # end of header
            r"(?P<solution>.*?)"  # solution
            r"(?=\n\s*# =+@)",  # beginning of next part
            flags=re.DOTALL | re.MULTILINE,
        )
        parts = [
            {"part": int(match.group("part")), "solution": match.group("solution")}
            for match in part_regex.finditer(source)
        ]
        # The last solution extends all the way to the validation code,
        # so we strip any trailing whitespace from it.
        parts[-1]["solution"] = parts[-1]["solution"].rstrip()
        return parts

    def backup(filename):
        backup_filename = None
        suffix = 1
        while not backup_filename or os.path.exists(backup_filename):
            backup_filename = "{0}.{1}".format(filename, suffix)
            suffix += 1
        shutil.copy(filename, backup_filename)
        return backup_filename

    def submit_parts(parts, url, token):
        submitted_parts = []
        for part in parts:
            if Check.has_solution(part):
                submitted_part = {
                    "part": part["part"],
                    "solution": part["solution"],
                    "valid": part["valid"],
                    "secret": [x for (x, _) in part["secret"]],
                    "feedback": json.dumps(part["feedback"]),
                }
                if "token" in part:
                    submitted_part["token"] = part["token"]
                submitted_parts.append(submitted_part)
        data = json.dumps(submitted_parts).encode("utf-8")
        headers = {"Authorization": token, "content-type": "application/json"}
        request = urllib.request.Request(url, data=data, headers=headers)
        # This is a workaround because some clients (and not macOS ones!) report
        # <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: certificate has expired (_ssl.c:1129)>
        import ssl

        context = ssl._create_unverified_context()
        response = urllib.request.urlopen(request, context=context)
        # When the issue is resolved, the following should be used
        # response = urllib.request.urlopen(request)
        return json.loads(response.read().decode("utf-8"))

    def update_attempts(old_parts, response):
        updates = {}
        for part in response["attempts"]:
            part["feedback"] = json.loads(part["feedback"])
            updates[part["part"]] = part
        for part in old_parts:
            valid_before = part["valid"]
            part.update(updates.get(part["part"], {}))
            valid_after = part["valid"]
            if valid_before and not valid_after:
                wrong_index = response["wrong_indices"].get(str(part["part"]))
                if wrong_index is not None:
                    hint = part["secret"][wrong_index][1]
                    if hint:
                        part["feedback"].append("Namig: {}".format(hint))

    filename = os.path.abspath(sys.argv[0])
    file_parts = extract_parts(filename)
    Check.initialize(file_parts)

    if Check.part():
        Check.current_part[
            "token"
        ] = "eyJwYXJ0IjozODE5NywidXNlciI6NjQ4M30:1qrCcB:qY-ctEeNgbaG6yj8UbgJ3FOxA9j4Y7xSN-w4_KypTF8"
        try:
            tests = [
                    ('je_prestopno(1900)', False),
                    ('je_prestopno(2000)', True),
                    ('je_prestopno(2004)', True),
                    ('je_prestopno(2011)', False)
                    ]
            
            for test in tests:
                if not Check.equal(*test):
                    break
            
            for leto in range(1900, 2100):
                Check.secret(je_prestopno(leto), leto)
        except:
            Check.error(
                "Testi sprožijo izjemo\n  {0}",
                "\n  ".join(traceback.format_exc().split("\n"))[:-2],
            )

    if Check.part():
        Check.current_part[
            "token"
        ] = "eyJwYXJ0IjozODE5OCwidXNlciI6NjQ4M30:1qrCcB:1NqyCRWxLLqq0zp9QNinSlPYZwJ7Y-YNPOGMotQnbuM"
        try:
            tests = [
                    ('stevilo_dni(1900)', 365),
                    ('stevilo_dni(2000)', 366),
                    ('stevilo_dni(2004)', 366),
                    ('stevilo_dni(2011)', 365),
                    ('stevilo_dni(2015)', 365),
                    ('stevilo_dni(2016)', 366)
                    ]
            
            for test in tests:
                if not Check.equal(*test):
                    break
            
            for leto in range(1900, 2100):
                Check.secret(stevilo_dni(leto), leto)
        except:
            Check.error(
                "Testi sprožijo izjemo\n  {0}",
                "\n  ".join(traceback.format_exc().split("\n"))[:-2],
            )

    if Check.part():
        Check.current_part[
            "token"
        ] = "eyJwYXJ0IjozODE5OSwidXNlciI6NjQ4M30:1qrCcB:hYxdBySYDSnfWSzeiTA44p6M9v82N0Ib0Ikbytm1E0s"
        try:
            tests = [
                    ('dolzine_mesecev(1900)', [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]),
                    ('dolzine_mesecev(2000)', [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]),
                    ('dolzine_mesecev(2004)', [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]),
                    ('dolzine_mesecev(2011)', [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])
                    ]
            
            for test in tests:
                if not Check.equal(*test):
                    break
            
            for leto in range(1900, 2100, 10):
                Check.secret(dolzine_mesecev(leto), leto)
        except:
            Check.error(
                "Testi sprožijo izjemo\n  {0}",
                "\n  ".join(traceback.format_exc().split("\n"))[:-2],
            )

    if Check.part():
        Check.current_part[
            "token"
        ] = "eyJwYXJ0IjozODIwMCwidXNlciI6NjQ4M30:1qrCcB:Cnhr1J73deMXDArStfeBpdRgk5dSrKZVtc8HaVKLkWo"
        try:
            tests = [
                    ('Datum(8, 2, 1849).dan', 8),
                    ('Datum(8, 2, 1849).mesec', 2),
                    ('Datum(8, 2, 1849).leto', 1849),
                    ('Datum(14, 12, 1982).dan', 14),
                    ('Datum(14, 12, 1982).mesec', 12),
                    ('Datum(14, 12, 1982).leto', 1982)
                    ]
            
            for test in tests:
                if not Check.equal(*test):
                    break
        except:
            Check.error(
                "Testi sprožijo izjemo\n  {0}",
                "\n  ".join(traceback.format_exc().split("\n"))[:-2],
            )

    if Check.part():
        Check.current_part[
            "token"
        ] = "eyJwYXJ0IjozODIwMSwidXNlciI6NjQ4M30:1qrCcB:b1PyahomTPar0YXRw2BJ8eAg2rVz3jIUqrnTox5cQ9M"
        try:
            tests = [
                    ('str(Datum(8, 2, 1849))', "8. 2. 1849"),
                    ('str(Datum(14, 12, 1982))', "14. 12. 1982"),
                    ('str(Datum(21, 12, 2012))', "21. 12. 2012")
                    ]
            
            for test in tests:
                if not Check.equal(*test):
                    break
        except:
            Check.error(
                "Testi sprožijo izjemo\n  {0}",
                "\n  ".join(traceback.format_exc().split("\n"))[:-2],
            )

    if Check.part():
        Check.current_part[
            "token"
        ] = "eyJwYXJ0IjozODIwMiwidXNlciI6NjQ4M30:1qrCcB:pPHaflSQrauCFiX9wl9JVzykGBSQHXXgxexhjd6V51E"
        try:
            tests = [
                    ('repr(Datum(8, 2, 1849))', "Datum(8, 2, 1849)"),
                    ('repr(Datum(14, 12, 1982))', "Datum(14, 12, 1982)"),
                    ('repr(Datum(21, 12, 2012))', "Datum(21, 12, 2012)")
                    ]
            
            for test in tests:
                if not Check.equal(*test):
                    break
        except:
            Check.error(
                "Testi sprožijo izjemo\n  {0}",
                "\n  ".join(traceback.format_exc().split("\n"))[:-2],
            )

    if Check.part():
        Check.current_part[
            "token"
        ] = "eyJwYXJ0IjozODIwMywidXNlciI6NjQ4M30:1qrCcB:yca55GjiGgPoB0tY_jvtoyiadSIxDD0Gmi9Cz-zwZQk"
        try:
            tests = [
                    ('Datum(8, 2, 1849).je_veljaven()', True),
                    ('Datum(5, 14, 2014).je_veljaven()', False),
                    ('Datum(14, 12, 1982).je_veljaven()', True),
                    ('Datum(31, 4, 2012).je_veljaven()', False),
                    ('Datum(5, 13, 2012).je_veljaven()', False),
                    ('Datum(29, 2, 2012).je_veljaven()', True),
                    ('Datum(29, 2, 2011).je_veljaven()', False)
                    ]
            
            for test in tests:
                if not Check.equal(*test):
                    break
        except:
            Check.error(
                "Testi sprožijo izjemo\n  {0}",
                "\n  ".join(traceback.format_exc().split("\n"))[:-2],
            )

    if Check.part():
        Check.current_part[
            "token"
        ] = "eyJwYXJ0IjozODIwNCwidXNlciI6NjQ4M30:1qrCcB:U5pebsBC0ACG-P9nKxFJtk0elTRXiTAxwWcGtfz-w20"
        try:
            tests = [
                    ('Datum(31, 12, 1999) < Datum(1, 1, 2000)', True),
                    ('Datum(31, 12, 1999) > Datum(1, 1, 2000)', False),
                    ('Datum(31, 12, 1999) < Datum(31, 12, 1999)', False),
                    ('Datum(31, 12, 1999) > Datum(31, 12, 1999)', False),
                    ('Datum(31, 3, 1999) < Datum(1, 4, 1999)', True),
                    ('Datum(31, 3, 1999) > Datum(1, 4, 1999)', False),
                    ('Datum(12, 7, 2014) > Datum(1, 2, 2015)', False),
                    ('Datum(12, 7, 2014) < Datum(1, 2, 2015)', True),
                    ('Datum(1, 7, 2014) < Datum(12, 2, 2014)', False),
                    ('Datum(1, 7, 2014) > Datum(12, 2, 2014)', True),
                    ('Datum(1, 7, 2014) > Datum(12, 7, 2014)', False),
                    ('Datum(12, 7, 2014) > Datum(1, 7, 2014)', True)
                    ]
            
            for test in tests:
                if not Check.equal(*test):
                    break
        except:
            Check.error(
                "Testi sprožijo izjemo\n  {0}",
                "\n  ".join(traceback.format_exc().split("\n"))[:-2],
            )

    if Check.part():
        Check.current_part[
            "token"
        ] = "eyJwYXJ0IjozODIwNSwidXNlciI6NjQ4M30:1qrCcB:uQZJHIEMrT__ME_oOgG2anx72SqmatsXMeuw6IPQy-8"
        try:
            tests = [
                    ('Datum(31, 12, 1999) == Datum(1, 1, 2000)', False),
                    ('Datum(31, 12, 1999) == Datum(31, 12, 1999)', True),
                    ('Datum(31, 3, 1999) != Datum(1, 4, 1999)', True),
                    ('Datum(2, 2, 2014) != Datum(1, 2, 2014)', True),
                    ('Datum(2, 2, 2014) == Datum(1, 2, 2014)', False),
                    ('Datum(2, 2, 2014) != Datum(2, 1, 2014)', True),
                    ('Datum(2, 2, 2014) == Datum(2, 1, 2014)', False),
                    ('Datum(2, 2, 2014) != Datum(2, 2, 2015)', True),
                    ('Datum(2, 2, 2014) == Datum(2, 2, 2015)', False)
                    ]
            
            for test in tests:
                if not Check.equal(*test):
                    break
        except:
            Check.error(
                "Testi sprožijo izjemo\n  {0}",
                "\n  ".join(traceback.format_exc().split("\n"))[:-2],
            )

    if Check.part():
        Check.current_part[
            "token"
        ] = "eyJwYXJ0IjozODIwNiwidXNlciI6NjQ4M30:1qrCcB:7m3qPVggTIWEdCVESzBJu7itQslihHRqIlBffw6YWFk"
        try:
            tests = [
                    ('Datum(1, 11, 2014).dan_v_letu()', 305),
                    ('Datum(28, 2, 2014).dan_v_letu()', 59),
                    ('Datum(1, 3, 2014).dan_v_letu()', 60),
                    ('Datum(31, 12, 2014).dan_v_letu()', 365),
                    ('Datum(28, 2, 2016).dan_v_letu()', 59),
                    ('Datum(29, 2, 2016).dan_v_letu()', 60),
                    ('Datum(1, 3, 2016).dan_v_letu()', 61),
                    ('Datum(31, 12, 2016).dan_v_letu()', 366),
                    ('Datum(1, 1, 2016).dan_v_letu()', 1),
                    ('Datum(14, 12, 1982).dan_v_letu()', 348),
                    ('Datum(31, 3, 2012).dan_v_letu()', 91),
                    ('Datum(31, 3, 2011).dan_v_letu()', 90),
                    ('Datum(1, 1, 2011).dan_v_letu()', 1)
                    ]
            
            for test in tests:
                if not Check.equal(*test):
                    break
        except:
            Check.error(
                "Testi sprožijo izjemo\n  {0}",
                "\n  ".join(traceback.format_exc().split("\n"))[:-2],
            )

    if Check.part():
        Check.current_part[
            "token"
        ] = "eyJwYXJ0IjozODIwNywidXNlciI6NjQ4M30:1qrCcB:EDXzlZAvxUqfa_5_GFnILBCAovkCJwfQDhPxTmLQqS0"
        try:
            tests = [
                    ('Datum(1, 11, 2014).razlika(Datum(14, 10, 2014))', 18),
                    ('Datum(14, 12, 1990).razlika(Datum(14, 12, 1982))', 2922),
                    ('Datum(31, 3, 2012).razlika(Datum(1, 4, 2011))', 365),
                    ('Datum(25, 6, 1991).razlika(Datum(10, 11, 2011))', -7443),
                    ('Datum(8, 2, 1849).razlika(Datum(3, 12, 1800))', 17599),
                    ('Datum(21, 1, 1994).razlika(Datum(17, 12, 2015))', -8000)
                    ]
            
            for test in tests:
                if not Check.equal(*test):
                    break
        except:
            Check.error(
                "Testi sprožijo izjemo\n  {0}",
                "\n  ".join(traceback.format_exc().split("\n"))[:-2],
            )

    if Check.part():
        Check.current_part[
            "token"
        ] = "eyJwYXJ0IjozODIwOCwidXNlciI6NjQ4M30:1qrCcB:QJxYsPhMCcq_7Un9mPXaPAFUXD4t9Fb3pqZIImbf2Ig"
        try:
            tests = [
                    ('Datum(14, 12, 1982).dan_v_tednu()', 2),
                    ('Datum(1, 1, 1982).dan_v_tednu()', 5),
                    ('Datum(1, 2, 1982).dan_v_tednu()', 1),
                    ('Datum(1, 3, 1982).dan_v_tednu()', 1),
                    ('Datum(1, 4, 1982).dan_v_tednu()', 4),
                    ('Datum(1, 5, 1982).dan_v_tednu()', 6),
                    ('Datum(1, 6, 1982).dan_v_tednu()', 2),
                    ('Datum(1, 7, 1982).dan_v_tednu()', 4),
                    ('Datum(1, 8, 1982).dan_v_tednu()', 7),
                    ('Datum(1, 9, 1982).dan_v_tednu()', 3),
                    ('Datum(1, 10, 1982).dan_v_tednu()', 5),
                    ('Datum(1, 11, 1982).dan_v_tednu()', 1),
                    ('Datum(1, 12, 1982).dan_v_tednu()', 3),
                    ('Datum(10, 11, 2011).dan_v_tednu()', 4),
                    ('Datum(9, 3, 1981).dan_v_tednu()', 1),
                    ('Datum(1, 11, 2014).dan_v_tednu()', 6),
                    ('Datum(2, 11, 2014).dan_v_tednu()', 7),
                    ('Datum(3, 11, 2014).dan_v_tednu()', 1),
                    ('Datum(4, 11, 2014).dan_v_tednu()', 2),
                    ('Datum(5, 11, 2014).dan_v_tednu()', 3),
                    ('Datum(6, 11, 2014).dan_v_tednu()', 4),
                    ('Datum(7, 11, 2014).dan_v_tednu()', 5),
                    ('Datum(29, 2, 2024).dan_v_tednu()', 4),
                    ('Datum(1, 3, 2024).dan_v_tednu()', 5),
                    ('Datum(2, 3, 2024).dan_v_tednu()', 6),
                    ('Datum(3, 3, 2024).dan_v_tednu()', 7),
                    ('Datum(4, 3, 2024).dan_v_tednu()', 1),
                    ('Datum(5, 3, 2024).dan_v_tednu()', 2),
                    ('Datum(6, 3, 2024).dan_v_tednu()', 3)
                    ]
            
            for test in tests:
                if not Check.equal(*test):
                    break
        except:
            Check.error(
                "Testi sprožijo izjemo\n  {0}",
                "\n  ".join(traceback.format_exc().split("\n"))[:-2],
            )

    if Check.part():
        Check.current_part[
            "token"
        ] = "eyJwYXJ0IjozODIwOSwidXNlciI6NjQ4M30:1qrCcB:TsgBtAczRrdrxquo4wSMBrKt1BYOgd9hLL290H-DQCQ"
        try:
            tests = [
                    ('Datum.dan_v_letu_stat(2014, 305)', Datum(1, 11, 2014)),
                    ('Datum.dan_v_letu_stat(2011, 1)', Datum(1, 1, 2011)),
                    ('Datum.dan_v_letu_stat(2012, 12)', Datum(12, 1, 2012)),
                    ('Datum.dan_v_letu_stat(2013, 123)', Datum(3, 5, 2013)),
                    ('Datum.dan_v_letu_stat(2014, 365)', Datum(31, 12, 2014)),
                    ('Datum.dan_v_letu_stat(2016, 366)', Datum(31, 12, 2016)),
                    ('Datum.dan_v_letu_stat(2016, 60)', Datum(29, 2, 2016)),
                    ('Datum.dan_v_letu_stat(2015, 60)', Datum(1, 3, 2015)),
                    ('Datum.dan_v_letu_stat(2015, 90)', Datum(31, 3, 2015)),
                    ('Datum.dan_v_letu_stat(2015, 91)', Datum(1, 4, 2015)),
                    ('Datum.dan_v_letu_stat(2015, 92)', Datum(2, 4, 2015)),
                    ('Datum.dan_v_letu_stat(2015, 120)', Datum(30, 4, 2015)),
                    ('Datum.dan_v_letu_stat(2015, 121)', Datum(1, 5, 2015)),
                    ('Datum.dan_v_letu_stat(2015, 304)', Datum(31, 10, 2015)),
                    ('Datum.dan_v_letu_stat(2015, 305)', Datum(1, 11, 2015))
                    ]
            
            for test in tests:
                if not Check.equal(*test):
                    break
        except:
            Check.error(
                "Testi sprožijo izjemo\n  {0}",
                "\n  ".join(traceback.format_exc().split("\n"))[:-2],
            )

    print("Shranjujem rešitve na strežnik... ", end="")
    try:
        url = "https://www.projekt-tomo.si/api/attempts/submit/"
        token = "Token 8386a0252615c3bd9fa483e87dba321eee45b936"
        response = submit_parts(Check.parts, url, token)
    except urllib.error.URLError:
        message = (
            "\n"
            "-------------------------------------------------------------------\n"
            "PRI SHRANJEVANJU JE PRIŠLO DO NAPAKE!\n"
            "Preberite napako in poskusite znova ali se posvetujte z asistentom.\n"
            "-------------------------------------------------------------------\n"
        )
        print(message)
        traceback.print_exc()
        print(message)
        sys.exit(1)
    else:
        print("Rešitve so shranjene.")
        update_attempts(Check.parts, response)
        if "update" in response:
            print("Updating file... ", end="")
            backup_filename = backup(filename)
            with open(__file__, "w", encoding="utf-8") as f:
                f.write(response["update"])
            print("Previous file has been renamed to {0}.".format(backup_filename))
            print("If the file did not refresh in your editor, close and reopen it.")
    Check.summarize()


if __name__ == "__main__":
    _validate_current_file()
