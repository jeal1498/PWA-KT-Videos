---
name: guiones-karen
description: "Escribir guiones para los videos de Karen Trujillo, neuropsicóloga en Cancún (TDAH, autismo y bienestar): la v2 sin cara de un video ya hecho, temas nuevos o un guion para que ella grabe, en lotes para aprobar juntos. Úsala siempre que Eduardo o Karen pidan un guion, ideas de tema, «la siguiente v2», «el siguiente lote», un gancho nuevo o reescribir un texto de video, aunque no digan «guion». Para producir el video (voz, animación, portada, copy, guardar) usa videos-karen."
---

# Guiones de Karen

Un lote son 5 guiones (3 en el primer lote o si cambia la receta). Karen los aprueba **juntos** en un solo mensaje: es la aprobación 1 de 2 del flujo; la 2 es el lote terminado (skill `videos-karen`). Por eso cada guion tiene que llegar listo para producir.

## Antes de escribir
1. `git pull` y leer `docs/pendientes.md`: qué v2 faltan y qué fechas siguen.
2. `python3 -I .claude/skills/videos-karen/scripts/calendario.py fechas 10`: los días libres y si son **sin cara** (v2, voz clonada) o **con Karen** (ella graba).
3. Para cada v2, leer el `guion.md` del original y de las otras v2 del mismo tema para **no repetir gancho, ejemplos ni estructura**.
4. Elegir el orden de forma que dos videos del mismo tema no queden en días seguidos.

## Cómo es un buen guion
- **Público:** adultos que sospechan TDAH y madres y padres de hijos de 5 a 17 años. Trato de «tú», cálido, clínico y preciso, sin tecnicismos de más.
- **Largo:** 160 a 185 palabras sin tags (≈62 a 72 s con la voz de Karen en v3).
- **Estructura que funcionó:** escena cotidiana o pregunta en los primeros 3 s (sin abrir con silencio) → la idea en una frase → desarrollo con 3 o 4 ejemplos concretos o pasos → matiz clínico («si lleva años, en varios lugares y afecta tu vida, consúltalo con un profesional») → una acción para hoy → cierre con pregunta a la audiencia → «Este video orienta y no diagnostica.»
- **Formatos que le gustan:** guía práctica 1/2/3, mito y realidad, historia (escena → giro → qué hacer), «un síntoma, varias causas».
- **Prohibido:** «cura», promesas, «siempre», «todos», diagnosticar por video, culpar («eres flojo»), datos inventados presentados como reales, casos que identifiquen a alguien.
- **Gancho de portada:** ≤25 caracteres, sale de una frase del guion.

## Audio Tags (solo guiones sin cara, Eleven v3)
4 a 6 en total, solo en giros emocionales: `[curious]` en la pregunta del giro, `[sighs]` en la empatía, `[softly]` en lo más sensible y `[warmly]` en la invitación final. **Nunca** al principio ni en la explicación clínica o el aviso; sin `[laughs]` ni `[excited]`.

## Guion para que Karen grabe
Sin tags. Frases cortas que pueda decir de corrido, marcadas en bloques (gancho / idea / pasos / cierre) para que grabe por tomas. Decir el nombre exacto de los instrumentos (ADOS-2, WISC-V, CAARS-2, CONNERS-3). Las escenas gráficas se piensan con `plantillas/guion-pilares.md`.

## Entrega del lote (un solo mensaje)
Primero una tabla: `NN · fecha · sin cara/con Karen · tema (v2 del MM) · gancho recomendado`. Después, por video:

```
### NN · Título (v2 del MM)
Guion (con tags)
Gancho de portada: A (recomendado) · B · C
Escenas: 3 líneas con la idea visual de cada bloque
Cómo se diferencia del original: 2 líneas
Por confirmar con Karen: ejemplos o datos que ella no ha dicho
```
Cerrar con: «Responde "aprobado" o los cambios por número».

Con el lote aprobado, guardar cada guion en `<trabajo>/guion.txt` (texto con tags, para `voz.py`) y pasar a `videos-karen`. Si piden cambios en un guion, se rehace solo ese y se vuelve a mandar solo ese.
