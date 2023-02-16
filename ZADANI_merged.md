# Merged zadania projektov ISJ 2023 #

## Projekt 1 ##

> *[proj1.py](proj1.py); max. 5 bodov; zadané 15. februára, deadline 1. marca*

Stáhněte si soubor [isj_proj1_xnovak00.py](https://moodle.vut.cz/pluginfile.php/566708/mod_assign/introattachment/0/isj_proj1_xnovak00.py?forcedownload=1) a místo xnovak00 dejte do názvu svůj login.

Dopište definici regulárního výrazu inbetween (místo ...), aby odpovídal pozicím, na něž se má ve jménech typu *camelCaseName* vložit _ při převodu na *snake_case_name*. (3 body)

Dopište definici regulárního pat (místo ...), aby odpovídal buď jménu, před kterým je titul \[Pp\]rof. nebo \[Dd\]oc. a za ním následuje ", Ph.D.", nebo jinému případu. (2 body)
Oddělovačem je čárka, za kterou následuje alespoň jeden bílý znak.

Nic jiného v kódu neměňte (i kdyby se vám nelíbil nedostatek komentářů apod.).
Cvičné hodnocení můžete vyzkoušet v systému [http://isj.fit.vutbr.cz/upload](http://isj.fit.vutbr.cz/upload), ale pro získání bodů za projekt musíte výsledný skript (se správným názvem) odevzdat prostřednictví [úkolu v MOODLE](https://moodle.vut.cz/mod/assign/view.php?id=304668).

Myšlenka 2. příkladu je taková, že si máte vyzkoušet *["best trick ever"](http://www.rexegg.com/regex-best-trick.html)* z [přednášky](https://moodle.vut.cz/pluginfile.php/566693/mod_folder/content/0/isj_regex.ipynb?forcedownload=1) (je to prostě obdoba "Tarzan").

Máte vracet ze seznamu jmen s akademickými tituly ta, která možná někdo napsal neúplně (bez všech titulů za jménem a před jménem ).
Můžete to udělat tak, že jako první alternativu/alternativy napíšete to, co na výstupu být nemá, pokud bude potřeba, tak v "nezapamatované závorce" (?: ... ), a v druhé (poslední) uvedete výraz pro to, co vyjít má. Pouze normální závorka pak zůstane v iteraci pomocí `.findall`.

Regulární výraz má na konci vést k tomu, aby se jakýkoliv vstup, který má na začátku Prof|Doc a na konci , Ph.D., vyloučil. Ale ve skriptu je vše připraveno tak, abyste mohli snadno použít onen trik - to, co nechcete, napíšete jako první, a pak si pomocí závorky "posbíráte" to, co opravdu chcete.
