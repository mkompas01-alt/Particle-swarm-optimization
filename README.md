# Particle-swarm-optimization

Implementácia troch variantov PSO v Pythone. Cieľom je minimalizácia testovacích funkcií.

## Varianty

| Variant | w | c1, c2 | Topológia |
|---|---|---|---|
| 1 | 0.8 → 0.3 | 2 | globálna (hviezda) |
| 2 | 0.7 | 1.49618 | globálna (hviezda) |
| 3 | 0.7 | 1.49618 | kruhová |

Pri prvom variante sa zotrvačnosť lineárne znižuje podľa počtu vykonaných ohodnotení. Pri globálnej topológii sa častica riadi najlepším riešením celej populácie. Pri kruhovej topológii sa vyberá najlepšie riešenie z trojice: ľavý sused, samotná častica a pravý sused.

## Nastavenia

- NP = 40
- MAXFES = 20 000 (vrátane inicializácie)
- Dimenzia = 10
- vmax = 0.2 * (high - low)
- 10 behov každého variantu na každej funkcii, seedy 0 až 9

Rýchlosť je obmedzená v každej dimenzii. Častice môžu opustiť prehľadávanú oblasť, ich poloha sa neupravuje. Mimo oblasti sa účelová funkcia nevyhodnocuje a FES sa nezvyšuje.

## Testovacie funkcie

| Funkcia | Rozsah | Globálne minimum |
|---|---|---|
| Sphere | [-5.12, 5.12] | 0 v bode (0, ..., 0) |
| Rastrigin | [-5.12, 5.12] | 0 v bode (0, ..., 0) |
| Rosenbrock | [-5, 10] | 0 v bode (1, ..., 1) |

## Výsledky

Najlepšia a priemerná hodnota z 10 behov (nižšia hodnota je lepšia).

| Funkcia | Variant | Best | Avg |
|---|---|---:|---:|
| Sphere | 1 | 2.998111e-25 | 1.349570e-22 |
| Sphere | 2 | 8.224812e-33 | 1.719846e-30 |
| Sphere | 3 | 2.911675e-17 | 1.952192e-16 |
| Rastrigin | 1 | 2.001075 | 4.390551 |
| Rastrigin | 2 | 2.984877 | 8.059164 |
| Rastrigin | 3 | 3.979844 | 7.203259 |
| Rosenbrock | 1 | 0.4565611 | 4.160052 |
| Rosenbrock | 2 | 0.06105202 | 1.523569 |
| Rosenbrock | 3 | 0.2233918 | 2.866953 |

Všetky varianty ukončili testy pri 20 000 ohodnoteniach. Na funkcii Sphere sa všetky priblížili k nule. Na Rastriginovej funkcii dosiahol najlepší priemer variant 1 a na Rosenbrockovej variant 2. Výsledky platia pre zvolené nastavenia a počet behov, nie všeobecne pre všetky optimalizačné úlohy.
