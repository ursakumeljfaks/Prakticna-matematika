# =============================================================================
# Kompleksna števila II
# =====================================================================@038262=
# 1. podnaloga
# Sestavljen je razred KompleksnoStevilo z metodama `__init__(self, re, im)`,
# lastnostima `im` in`re ter `__repr__(self)`.
# Realni del kompleksnega števila je shranjen v spremenljivki 
# `_re`, imaginarni pa v `_im`. Metoda `__repr__(self)` predstavi kompleksno 
# število z nizom oblike `KompleksnoStevilo(re, im)`.
# 
# Zgled:
# 
#     >>> u = KompleksnoStevilo(3, 4)
#     >>> u
#     KompleksnoStevilo(3, 4)
# 
# Žal so se vrstice v kodi zamešale. uredi jih v pravilni vrstni red. Razen
# spreminanja vrstnega reda ne naredi nobene druge spremembe
# =============================================================================
class KompleksnoStevilo:
    def __init__(self, re, im):
        '''konstruktor, ki sprejme dve stevili za realni in imaginarni del'''
        self.re = re
        self.im = im

    @property
    def re(self):
        return self._re

    @re.setter
    def re(self, vr):
        self._re = vr

    @property
    def im(self):
        return self._im
    
    @im.setter
    def im(self, vr):
        self._im = vr


    def __repr__(self):
        '''Kompleksno stevilo predstavi z nizom oblike 'KompleksnoStevilo(re, im)' '''
        niz = 'KompleksnoStevilo(' + str(self.re) + ', ' + str(self.im) + ')'
        return niz

# =====================================================================@038263=
# 2. podnaloga
# Razredu dodaj metodo `__str__(self)`, ki kompleksno stevilo predstavi z nizom
#  oblike npr. `3 + 4i`
# Pri tem bodi pozoren da:
# ◦ Če je realni ali imaginarni del števila enak `0`, naj bo v nizu njegov člen 
# izpuščen (npr. namesto `2 + 0i` pišemo samo `2`).
# ◦ Če je imaginarni del števila enak `1`, namesto `1i` pišemo samo `i`. Če je 
# enak `-1`namesto `-1i` pišemo `-i`.
# ◦ Če je imaginarni del števila negativen, njegov predznak zamenja `+`. Torej, 
# namesto `2 + (-3)i` pišemo kar `2 – 3i`. Če je realni del enak `0` med predznakom 
# `-` in nadaljevanjem ni presledka. Torej namesto `- 3i` pišemo `-3i`.
# 
# Zgled:
# 
#     >>> u = KompleksnoStevilo(3, 4)
#     >>> print(u)
#     3 + 4i
#     >>> v = KompleksnoStevilo(2, 0)
#     >>> print(v)
#     2
#     >>> w = KompleksnoStevilo(0, -4)
#     >>> print(w)
#     -4i
#     >>> w = KompleksnoStevilo(0, 1)
#     >>> print(w)
#     i
#     >>> y = KompleksnoStevilo(-2, -6)
#     >>> print(y)
#     -2 - 6i
#     >>> z = KompleksnoStevilo(0, 0)
#     >>> print(z)
#     0
#     
# Opozorilo: To in vse ostale podnaloge
# začnite s `class KompleksnoStevilo(KompleksnoStevilo)`
# =============================================================================
class KompleksnoStevilo(KompleksnoStevilo):
    def __str__(self):
        if self._im == 0:
            return f"{self.re}"
        if self._re == 0:
            if self._im == -1:
                izpis = "-i"
            elif self._im == 1:
                izpis = "i"
            else:
                izpis = f"{self.im}i"
        else:
            izpis = f"{self._re} "
            if self._im < -1:
                izpis += f"- {-self.im}i"
            elif self._im == -1:
                izpis += "- i"
            elif self._im == 1:
                izpis += "i"
            else:
                izpis += f"+ {self.im}i"
        return izpis
# =====================================================================@038264=
# 3. podnaloga
# Razširite razred tako, da podpira seštevanje dveh kompleksnih števil.
# Zgled:
# 
#      >>> KompleksnoStevilo(3, -2) + KompleksnoStevilo(2, 1)
#      KompleksnoStevilo(5, -1)
# =============================================================================
class KompleksnoStevilo(KompleksnoStevilo):
    def __add__(self, other):
        return KompleksnoStevilo(self.re + other.re, self.im + other.im)
# =====================================================================@038265=
# 4. podnaloga
# Razširite razred tako, da podpira seštevanje kompleksnih števil z decimalnimi
# in celimi števili. 
# Zgled:
# 
#      >>> str(KompleksnoStevilo(3, -2) + KompleksnoStevilo(2, 1))
#      5 - i
#      >>> str(KompleksnoStevilo(3, 2) + 4.5)
#      7.5 + 2i
#      >>> str(5 + KompleksnoStevilo(3, -2))
#      8 - 2i
#      >>> str("bla" + KompleksnoStevilo(3, -2))
#      ...TypeError('Kompleksnih števil ne znamo seštevati z objekti tipa str')
# =============================================================================

# =====================================================================@038266=
# 5. podnaloga
# Sestavite metodo `__mul__(self, other)`, ki vrne produkt dveh kompleksnih števil.
# Množenec na levi bo vedno tipa `KompleksnoStevilo`, množenec na desni pa je lahko
# tudi navadno število tipa `float` ali `int`.
# 
# Zgled:
# 
#     >>> KompleksnoStevilo(3, 4) * 2
#     KompleksnoStevilo(6, 8)
#     >>> KompleksnoStevilo(3, 4) * KompleksnoStevilo(2, -1)
#     KompleksnoStevilo(10, 2)
# =============================================================================

        
# =====================================================================@038267=
# 6. podnaloga
# Omogočite, da lahko med sabo poljubno množimo kompleksna, cela in decimalna
# števila.
# 
# Zgled:
# 
#     >>> d1 = KompleksnoStevilo(3, 4)
#     >>> d2 = KompleksnoStevilo(2, -1)
#     >>> d1 * d2
#     KompleksnoStevilo(10, 2)
#     >>> d1 * 3
#     KompleksnoStevilo(9, 12)
#     >>> 2.2 * d2
#     KompleksnoStevilo(4.4, -2.2)
#     >>> 7 * 3
#     21
# =============================================================================

# =====================================================================@038268=
# 7. podnaloga
# Izven razreda KompleksnoStevilo sestavite funkcijo `vsota_kompleksnih`, ki
# sprejme tabelo kompleksnih števil in vrne vsoto številv tabeli.
# 
#     >>> kompleksna = [KompleksnoStevilo(0, 0), KompleksnoStevilo(3, 4), KompleksnoStevilo(2, 2)]
#     >>> vsota_kompleksnih(kompleksna)
#     KompleksnoStevilo(5, 6)
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
        ] = "eyJwYXJ0IjozODI2MiwidXNlciI6NjQ4M30:1qsShf:bihI-fXFY9pWjzxK6yM0ar3vUYvYM0UtiQNxyNQX8Hw"
        try:
            Check.equal('repr(KompleksnoStevilo(3, 4))', 'KompleksnoStevilo(3, 4)') and \
            Check.equal('repr(KompleksnoStevilo(1, 6))', 'KompleksnoStevilo(1, 6)') and \
            Check.equal('KompleksnoStevilo(0, 1).re', 0)
        except:
            Check.error(
                "Testi sprožijo izjemo\n  {0}",
                "\n  ".join(traceback.format_exc().split("\n"))[:-2],
            )

    if Check.part():
        Check.current_part[
            "token"
        ] = "eyJwYXJ0IjozODI2MywidXNlciI6NjQ4M30:1qsShf:zQTu3y2D0_VTxAGWERiJE2-g7PDsbqpmtY8FIxSb1RQ"
        try:
            Check.equal('str(KompleksnoStevilo(3, 4))', '3 + 4i') and \
            Check.equal('str(KompleksnoStevilo(2, 0))', '2') and \
            Check.equal('str(KompleksnoStevilo(-5, 0))', '-5') and \
            Check.equal('str(KompleksnoStevilo(0, 1))', 'i') and \
            Check.equal('str(KompleksnoStevilo(-2, -6))', '-2 - 6i')and \
            Check.equal('str(KompleksnoStevilo(0, 0))', '0')and \
            Check.equal('str(KompleksnoStevilo(-3, -4))', '-3 - 4i')and \
            Check.equal('str(KompleksnoStevilo(-3, 4))', '-3 + 4i')and \
            Check.equal('str(KompleksnoStevilo(0, -1))', '-i')and \
            Check.equal('str(KompleksnoStevilo(0, -4))', '-4i')and \
            Check.equal('str(KompleksnoStevilo(0, 8))', '8i')
        except:
            Check.error(
                "Testi sprožijo izjemo\n  {0}",
                "\n  ".join(traceback.format_exc().split("\n"))[:-2],
            )

    if Check.part():
        Check.current_part[
            "token"
        ] = "eyJwYXJ0IjozODI2NCwidXNlciI6NjQ4M30:1qsShf:OtjYwdQOoVFtlY6iVSjCTUUnYRArBzwdo4PQKS2blWw"
        try:
            Check.equal('str(KompleksnoStevilo(0, 0) + KompleksnoStevilo(0, 0))', '0')and \
            Check.equal('str(KompleksnoStevilo(1, 1) + KompleksnoStevilo(2, 2))', '3 + 3i')and \
            Check.equal('str(KompleksnoStevilo(-1, 1) + KompleksnoStevilo(2, -2))', '1 - i')and \
            Check.equal('str(KompleksnoStevilo(-4, 1) + KompleksnoStevilo(4, -2))', '-i')and \
            Check.equal('str(KompleksnoStevilo(0, 5) + KompleksnoStevilo(-6, 0))', '-6 + 5i')
        except:
            Check.error(
                "Testi sprožijo izjemo\n  {0}",
                "\n  ".join(traceback.format_exc().split("\n"))[:-2],
            )

    if Check.part():
        Check.current_part[
            "token"
        ] = "eyJwYXJ0IjozODI2NSwidXNlciI6NjQ4M30:1qsShf:3cldZ937Nw-d3aBR342rv2l9M2p5EJuEIuF2Q9ajZpQ"
        try:
            Check.equal('str(KompleksnoStevilo(0, 0) + KompleksnoStevilo(0, 0))', '0')and \
            Check.equal('str(KompleksnoStevilo(1, 1) + KompleksnoStevilo(2, 2))', '3 + 3i')and \
            Check.equal('str(10 + KompleksnoStevilo(0, 0))', '10')and \
            Check.equal('str(KompleksnoStevilo(1, 3) + 4.5)', '5.5 + 3i')and \
            Check.equal('str(KompleksnoStevilo(-1, 1) + KompleksnoStevilo(2, -2))', '1 - i')and \
            Check.equal('str(KompleksnoStevilo(-4, 1) + KompleksnoStevilo(4, -2))', '-i')and \
            Check.equal('str(KompleksnoStevilo(0, 5) + KompleksnoStevilo(-6, 0))', '-6 + 5i')
            try:
                x = 'bla' + KompleksnoStevilo(-1, 1)
                Check.error("'bla' + KompleksnoStevilo(-1, 1) mora sprožiti izjemo")
            except:
                pass
            try:
                x = KompleksnoStevilo(-1, 1) + (1, 2)
                Check.error("KompleksnoStevilo(-1, 1) + (1, 2) mora sprožiti izjemo")
            except:
                pass
            
            if not Check.run(["z1 = KompleksnoStevilo(-1, 1)", "z2 = KompleksnoStevilo(1, 1)",
                       "z3 = z1 + z2", "z3.im = 42", "x = z1.im", "y = z3.im"], 
                      {'x': 1, 'y': 42}) :
                          Check.feedback('Pozor, pri seštevanju se operanda ne smeta spremeniti!')
        except:
            Check.error(
                "Testi sprožijo izjemo\n  {0}",
                "\n  ".join(traceback.format_exc().split("\n"))[:-2],
            )

    if Check.part():
        Check.current_part[
            "token"
        ] = "eyJwYXJ0IjozODI2NiwidXNlciI6NjQ4M30:1qsShf:jmdVudKj-G6V5faYy4nafFUICsu1d7f15oZNW4SVUjk"
        try:
            Check.equal('str(KompleksnoStevilo(0, 0) * KompleksnoStevilo(0, 0))', '0')and \
            Check.equal('str(KompleksnoStevilo(1, 1) * KompleksnoStevilo(2, 2))', '4i')and \
            Check.equal('str(KompleksnoStevilo(-1, 1) * KompleksnoStevilo(1, -2))', '1 + 3i')and \
            Check.equal('str(KompleksnoStevilo(3, 4) * 2)', '6 + 8i')and \
            Check.equal('str(KompleksnoStevilo(3, 4) * KompleksnoStevilo(2, -1))', '10 + 5i')and \
            Check.equal('str(KompleksnoStevilo(0, 1) * KompleksnoStevilo(-1, 0))', '-i')
        except:
            Check.error(
                "Testi sprožijo izjemo\n  {0}",
                "\n  ".join(traceback.format_exc().split("\n"))[:-2],
            )

    if Check.part():
        Check.current_part[
            "token"
        ] = "eyJwYXJ0IjozODI2NywidXNlciI6NjQ4M30:1qsShf:teEbXPoyQsbEvHyRvTdYiX884Z-68Eoe81eGuVZqsro"
        try:
            Check.equal('str(KompleksnoStevilo(0, 0) * KompleksnoStevilo(0, 0))', '0') and \
            Check.equal('str(KompleksnoStevilo(1, 1) * KompleksnoStevilo(2, 2))', '4i')and \
            Check.equal('str(KompleksnoStevilo(-1, 1) * KompleksnoStevilo(1, -2))', '1 + 3i')and \
            Check.equal('str(KompleksnoStevilo(3, 4) * 2)', '6 + 8i')and \
            Check.equal('str(KompleksnoStevilo(3, 4) * KompleksnoStevilo(2, -1))', '10 + 5i')and \
            Check.equal('str(KompleksnoStevilo(0, 1) * KompleksnoStevilo(-1, 0))', '-i')
        except:
            Check.error(
                "Testi sprožijo izjemo\n  {0}",
                "\n  ".join(traceback.format_exc().split("\n"))[:-2],
            )

    if Check.part():
        Check.current_part[
            "token"
        ] = "eyJwYXJ0IjozODI2OCwidXNlciI6NjQ4M30:1qsShf:QQguS2WUySYGBmsofRARhVuf_NuKndHyDN1Hhnn_SP0"
        try:
            tabela=[]
            for i in range(15):
                tabela += [KompleksnoStevilo(2*i + 2, i-2)]
            Check.equal('str(vsota_kompleksnih({0}))'.format(tabela), '240 + 75i')
            
            Check.equal('str(vsota_kompleksnih([]))', '0')
            Check.equal('str(vsota_kompleksnih([KompleksnoStevilo(0, 0), KompleksnoStevilo(1, 1)]))', '1 + i')and \
            Check.equal('str(vsota_kompleksnih([KompleksnoStevilo(2, 1), KompleksnoStevilo(1, 2)]))', '3 + 3i')and \
            Check.equal('str(vsota_kompleksnih([KompleksnoStevilo(2, 1), KompleksnoStevilo(-1, -2)]))', '1 - i')
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
