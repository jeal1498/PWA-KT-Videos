---
name: parte
description: Al decir «/parte» o «parte», saca de la conversación actual los 3 puntos (✓ Decidido, … Falta, ⏳ Pendiente), actualiza parte.md, lo sube a main y lo muestra. Solo lee sin cambiar si dicen «lee el parte».
---
**`/parte` o «parte» (por defecto = actualizar desde la conversación):**
1. `git pull`, lee `parte.md` y repasa esta conversación.
2. **Decidido:** agrega lo que Karen o Eduardo aprobaron o eligieron, o que quedó hecho y verificado (versión, enlace o dato concreto), con fecha y una línea cada uno. No repitas lo que ya está.
3. **Falta:** lo que todavía no se empieza. Quita lo que ya se cerró y agrega lo nuevo con responsable y fecha si la hay.
4. **Pendiente:** lo que se empezó y quedó a medias (dónde quedó y qué sigue). Lo terminado sale de aquí y pasa a «Decidido».
5. Pon la fecha de hoy y haz commit y push directo a `main` (o a la rama de la sesión, si se asignó una).
6. Muestra los 3 puntos en máximo 10 líneas, sin recapitular la conversación.

**«Lee el parte» (solo leer):** `git pull` y muestra `parte.md` en máximo 10 líneas, sin cambiar nada.

Reglas: una línea por punto; «Hecho» no es «Publicado» (solo lo marcan Karen o Eduardo); sin datos de pacientes.
