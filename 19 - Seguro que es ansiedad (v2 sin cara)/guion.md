# Guion 19 (v2 del 18, sin cara)

Mismo tema que el 18 («¿Y si no era ansiedad?»), otro guion: versión B para prueba A/B. Sin la cara de Karen: 100 % animación a dos tintas con personaje ilustrado y voz clonada. Guion escrito por el editor y aprobado por Eduardo el 27 oct 2026; falta que Karen lo revise.

**Voz:** clonada de Karen (ElevenLabs `sSQiAF9Uq1K3xnyvFi8w`), modelo **Eleven v3 con Audio Tags** y silencios recortados a 0.35 s (`voz.py --modelo v3 --max-silencio 0.35`), aprobada el 30 oct 2026. Antes llevó la voz provisional de Fernando y luego la de Karen en v2.

**Texto para la voz (con tags):** `[pause]` tras «aun así…», `[sighs]` en «Intentas calmarte», `[curious]` antes de «Antes de buscar», `[softly]` antes de «solo se ve a alguien nerviosa» y `[warmly]` antes de «Cuéntame en comentarios». Los tags no salen en subtítulos.

## Guion

Llevas años diciendo «tengo ansiedad» y, aun así… algo no cuadra. Intentas calmarte y lo que te pasa sigue ahí. Antes de buscar más ansiedad, vale la pena hacerte otra pregunta.

La ansiedad se mueve por el miedo: tu mente se adelanta a lo que podría salir mal. En el TDAH no hace falta ningún miedo. Lo que cuesta es sostener la atención, frenar impulsos y organizarte. Y a veces lo que parece perfeccionismo es una estrategia: revisar, anotar y controlar todo para no perderte.

Hay tres pistas para mirar. Primera: ¿desde cuándo? El TDAH y el autismo no aparecen de un día para otro, vienen desde la infancia. Segunda: ¿dónde pasa? En casa, en la escuela y en el trabajo, no solo cuando estás bajo estrés. Tercera: ¿a quién más en tu familia se parece? Son rasgos hereditarios.

Muchas mujeres aprenden a disimular tan bien que, por fuera, solo se ve a alguien nerviosa. Y claro, todo esto puede convivir con la ansiedad.

Ninguna de estas pistas es un diagnóstico. Lo que sí ayuda es una evaluación con pruebas estandarizadas que ordene tu historia. Este video orienta y no diagnostica. ¿Cuál de las tres pistas te hizo pensar? Cuéntame en comentarios.

## Tabla de elementos aprobada (estilo dos tintas)

Segundos de la voz provisional con la que se armó (sin los 0.2 s de portada); con la voz de Karen se trasladan con `warp.json` (ver el README del método).

| Segundo | Escena | Personaje |
|---|---|---|
| 0–4.65 | Gancho «Años diciendo "tengo ansiedad" y algo no cuadra», rótulo con cédula, burbuja «?» | Duda |
| 4.7–12.45 | Nube «tengo ansiedad» que se revienta, ramas a «con miedo» / «sin miedo», «¿Y si es otra cosa?» | Preocupada → Tranquila |
| 12.6–17.45 | «Ansiedad: se mueve por el miedo», camino de «hoy» a «¿y si sale mal?» | — |
| 17.6–24.95 | «TDAH: no hace falta ningún miedo», tarjetas Atención / Impulsos / Organización | — |
| 25.1–32.25 | «Perfeccionismo: a veces es una estrategia», tablero Revisar / Anotar / Controlar | — |
| 32.3–34.25 | «3 pistas» con tres nodos | — |
| 34.3–41.45 | Pista 1 «¿Desde cuándo?»: línea de la infancia a hoy | — |
| 41.6–47.55 | Pista 2 «¿Dónde pasa?»: casa, escuela y trabajo con palomita | — |
| 47.6–52.25 | Pista 3 «¿A quién se parece?»: árbol familiar | — |
| 52.3–57.05 | «Sesgo en mujeres: aprenden a disimular», «Por fuera, solo se ve a alguien nerviosa» | Sonrisa → Preocupada (tiembla) |
| 57.1–60.15 | Diagrama Ansiedad / TDAH-autismo, «Pueden convivir» | — |
| 60.3–67.65 | «Las pistas no son un diagnóstico», tablero «Evaluación» | — |
| 67.9–75.6 | Aviso, «¿Cuál de las 3 pistas te hizo pensar?», 1 2 3, web | Sonrisa |

Transición de línea con nodo hecha a mano entre escenas. Fuente del render: `.claude/skills/videos-karen/v2-sin-cara/ejemplo-19/`.
