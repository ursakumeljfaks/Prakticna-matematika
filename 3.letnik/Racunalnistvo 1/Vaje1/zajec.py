# =============================================================================
# Zajec
#
# Jože goji zajce. V zadnjih letih so se tako namnožili, da si Jože enostavno
# ne more več zapomniti vseh. Zato potrebuje primeren informacijski sistem. V
# pomoč mu sestavite razred, ki bo vseboval vse potrebne podatke o vsakem
# zajcu.
# =====================================================================@038249=
# 1. podnaloga
# Sestavite razred `Zajec` s konstruktorjem `__init__(self, teza, starost)`, ki
# predstavlja zajca z dano težo in starostjo. Lastnosti `teza` in `starost` naj
# bodo definirane kot `property`, saj zajci z negativno težo in starostjo ne
# obstajajo. Takšnim zajcom nastavite težo oz. starost na 0 (in se
# pretvarjajte, da obstajajo zajci brez teže).
# =============================================================================
class Zajec:
    
    @property
    def teza(self):
        return self._teza
        
    @teza.setter
    def teza(self, vrednost):
        self._teza = max(0, vrednost)
        
    @property
    def starost(self):
        return self._starost
        
    @starost.setter
    def starost(self, vrednost):
        self._starost = max(0, vrednost)

    def __init__(self, teza, starost):
        self.teza = teza
        self.starost = starost
        
        
# =====================================================================@038250=
# 2. podnaloga
# Sestavite metodo `nahrani(self, hrana)`, kjer je argument `hrana` teža hrane,
# ki jo damo zajcu. Pri hranjenju se teža zajca poveča za 30 % teže hrane, ki
# jo zajec poje. Zgled:
# 
#     >>> z = Zajec(5, 2)
#     >>> z.nahrani(2)
#     >>> z.teza
#     5.6
# =============================================================================
class Zajec(Zajec):
    def nahrani(self, hrana):
        poveca = hrana * 0.3
        self.teza += poveca
# =====================================================================@038251=
# 3. podnaloga
# Sestavite metodo `__str__(self)`, ki vrne predstavitev razreda `Zajec` z
# nizom oblike `'Zajec težak X kg, star Y let.'`.
# 
# Primer:
# 
#     >>> z = Zajec(5, 2)
#     >>> print(z)
#     'Zajec težak 5 kg, star 2 let.'
# 
# _Opomba_: Funkcija `print` na svojem argumentu pokliče metodo `__str__` in
# izpiše niz, ki ga ta metoda vrne. Metoda `__str__` običajno vrne razumljiv
# opis objekta, ki naj bi ga razumeli tudi ne-programerji.
# =============================================================================
class Zajec(Zajec):
    def __str__(self):
        return f"Zajec težak {self.teza} kg, star {self.starost} let."
# =====================================================================@038252=
# 4. podnaloga
# Sestavite še metodo `__repr__`, ki vrne predstavitev razreda `Zajec` kot niz
# oblike `'Zajec(X, Y)'`, kjer je `X` teža, `Y` pa starost zajca.
# 
# Primer:
# 
#     >>> z = Zajec(5, 2)
#     >>> z
#     Zajec(5, 2)
# 
# _Opomba_: Če v interaktivni konzoli pokličemo nek objekt, se izpiše niz, ki
# ga vrne klic metode `__repr__` na tem objektu. Priporočilo je, da je niz, ki
# ga vrne metoda `__repr__`, veljavna programska koda v Pythonu, ki ustvari
# identično kopijo objekta.
# =============================================================================
class Zajec(Zajec):
    def __repr__(self):
        return f"Zajec({self.teza}, {self.starost})"
# =====================================================================@038253=
# 5. podnaloga
# Sestavite metodo `__lt__(self, drugi)`, ki dva zajca primerja med sabo.
# Metoda naj vrne `True`, če je prvi zajec manjši od drugega in `False` sicer.
# 
# Manjši zajec je tisti, ki je lažji. Če pa imata zajca enako maso, je manjši
# tisti, ki je mlajši (tj. ima manjše število let).
# 
#     >>> Zajec(5, 3) < Zajec(6, 2)
#     True
#     >>> Zajec(3, 1) < Zajec(2, 2)
#     False
#     >>> Zajec(4, 3) < Zajec(4, 2)
#     False
# =============================================================================
class Zajec(Zajec):
    def __lt__(self, drugi):
        if self.teza == drugi.teza:
            return self.starost < drugi.starost
        elif self.teza < drugi.teza:
            return True
        else:
            return False
# =====================================================================@038254=
# 6. podnaloga
# Sestavite funkcijo `uredi(teze, starosti)`. Argumenta `teze` in `starosti`
# sta enako dolga seznama števil, kjer $i$-ti element predstavlja težo oz.
# starost $i$-tega zajca. Funkcija `uredi` naj ne bo znotraj razreda `Zajec`,
# saj ni objektna metoda, ampak je čisto običajna funkcija.
# 
# Funkcija naj ustvari seznam ustreznih primerkov razreda `Zajec`, ga uredi po
# velikosti glede na zgoraj opisano relacijo in ta seznam vrne kot rezultat.
# 
# **Namig:** metodo `__lt__` ste že definirali, torej jo Python lahko uporablja
# v svojih funkcijah.
# 
#     >>> l = uredi([5, 4, 4], [3, 2, 3])
#     >>> for z in l:
#     ...     print(z)
#     ...
#     Zajec težak 4 kg, star 2 let.
#     Zajec težak 4 kg, star 3 let.
#     Zajec težak 5 kg, star 3 let.
# =============================================================================
def uredi(teze, starosti):
    zajci = [Zajec(teza, starost) for teza, starost in zip(teze, starosti)]
    return sorted(zajci)





































































































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
        ] = "eyJwYXJ0IjozODI0OSwidXNlciI6NjQ4M30:1qsREw:NIzN5hcKRhZfrp1RcU83IWZqEvOd1nk8PH1rLypAVHc"
        try:
            if not isinstance(getattr(Zajec, 'teza'), property):
                Check.error('Teža zajca ni definirana kot `property`.')
            
            if not isinstance(getattr(Zajec, 'starost'), property):
                Check.error('Starost zajca ni definirana kot `property`.')
            
            test_data = [
                ('Zajec(5, 3).teza', 5),
                ('Zajec(5, 3).starost', 3),
                ('Zajec(7, 2).teza', 7),
                ('Zajec(7, 2).starost', 2),
                ('Zajec(-1, -3).starost', 0),
                ('Zajec(-6, -2).teza', 0),
            ]
            for td in test_data:
                if not Check.equal(*td):
                    break
            
            test_data = [
                (['a = Zajec(-5, -10)',
                  'a.teza = -2',
                  't = a.teza'],
                 {'t' : 0}),
                (['a = Zajec(-5, -10)',
                  'a.teza = 2',
                  't = a.teza'],
                 {'t' : 2}),
                (['a = Zajec(-5, -10)',
                  'a.starost = -2',
                  's = a.starost'],
                 {'s' : 0}),
                (['a = Zajec(-5, -10)',
                  'a.starost = 2',
                  's = a.starost'],
                 {'s' : 2})
            ]
            for td in test_data:
                if not Check.run(*td):
                    break
        except:
            Check.error(
                "Testi sprožijo izjemo\n  {0}",
                "\n  ".join(traceback.format_exc().split("\n"))[:-2],
            )

    if Check.part():
        Check.current_part[
            "token"
        ] = "eyJwYXJ0IjozODI1MCwidXNlciI6NjQ4M30:1qsREw:w1U7S0D7Yua7lO6phSS8BOt8DUSNVf6hEU8rJOy9F3A"
        try:
            Check.run(["z = Zajec(5, 2)", "z.nahrani(2)", "nova_teza = z.teza"],
                      {'nova_teza': 5.6})
            test_data = [
                (["z = Zajec(5, 2)", "z.nahrani(2)", "nova_teza = z.teza"],
                 {'nova_teza': 5.6}),
                (["z = Zajec(5, 2)", "z.nahrani(0)", "nova_teza = z.teza"],
                 {'nova_teza': 5}),
                (["z = Zajec(4, 2)", "z.nahrani(10)", "nova_teza = z.teza"],
                 {'nova_teza': 7}),
            ]
            for td in test_data:
                if not Check.run(*td):
                    break
        except:
            Check.error(
                "Testi sprožijo izjemo\n  {0}",
                "\n  ".join(traceback.format_exc().split("\n"))[:-2],
            )

    if Check.part():
        Check.current_part[
            "token"
        ] = "eyJwYXJ0IjozODI1MSwidXNlciI6NjQ4M30:1qsREw:Jf2PFe2GvZvWvz9RgBKT_56RcXyjXhCVd4pCYK8j9IQ"
        try:
            test_data = [
                ('str(Zajec(5, 2))', 'Zajec težak 5 kg, star 2 let.'),
                ('str(Zajec(10, 8))', 'Zajec težak 10 kg, star 8 let.'),
            ]
            for td in test_data:
                if not Check.equal(*td):
                    break
        except:
            Check.error(
                "Testi sprožijo izjemo\n  {0}",
                "\n  ".join(traceback.format_exc().split("\n"))[:-2],
            )

    if Check.part():
        Check.current_part[
            "token"
        ] = "eyJwYXJ0IjozODI1MiwidXNlciI6NjQ4M30:1qsREw:_nWgQC4jDOVEQ0h1PffLkQ1lvtIUdyHaudbO9rMuydM"
        try:
            test_data = [
                ('repr(Zajec(5, 2))', 'Zajec(5, 2)'),
                ('repr(Zajec(10, 8))', 'Zajec(10, 8)'),
            ]
            for td in test_data:
                if not Check.equal(*td):
                    break
        except:
            Check.error(
                "Testi sprožijo izjemo\n  {0}",
                "\n  ".join(traceback.format_exc().split("\n"))[:-2],
            )

    if Check.part():
        Check.current_part[
            "token"
        ] = "eyJwYXJ0IjozODI1MywidXNlciI6NjQ4M30:1qsREw:c-sJFBT8LAbyc670H6G3NhmXuSV2cYoHRvLydbFql_Y"
        try:
            Check.run(["z1 = Zajec(10, 10)", "z2 = Zajec(10, 11)", "z3 = Zajec(5, 15)",
                       "seznam = [z2, z1, z3]", "seznam.sort()", "urejeno = [(z.teza, z.starost) for z in seznam]"],
                      {'urejeno': [(5, 15), (10, 10), (10, 11)]})
        except:
            Check.error(
                "Testi sprožijo izjemo\n  {0}",
                "\n  ".join(traceback.format_exc().split("\n"))[:-2],
            )

    if Check.part():
        Check.current_part[
            "token"
        ] = "eyJwYXJ0IjozODI1NCwidXNlciI6NjQ4M30:1qsREw:pRnum8tDQcDi6wyhDvKMEq9YfX5J_UHqjYR3RnTb2jk"
        try:
            Check.run(["teze = [10, 10, 5]",  "starosti = [10, 11, 15]",
                       "seznam = uredi(teze, starosti)", "urejeno = [(z.teza, z.starost) for z in seznam]"],
                      {'urejeno': [(5, 15), (10, 10), (10, 11)]})
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
