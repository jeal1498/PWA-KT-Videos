---
name: parte
description: Al decir «/parte» o «parte», saca de la conversación actual los 3 puntos (✓ Decidido, … Falta, ✗ No tocar), actualiza parte.md, lo sube y lo muestra. Solo lee sin cambiar si dicen «lee el parte».
---
**`/parte` o «parte» (por defecto = actualizar desde la conversación):**
1. `git pull`, lee `parte.md` y repasa esta conversación.
2. **✓ Decidido:** agrega lo que Karen o Eduardo confirmaron o que quedó hecho y verificado en esta conversación (versión, enlace o dato concreto, una línea cada uno). No repitas lo que ya está.
3. **… Falta:** deja lo pendiente, incluido lo que quedó a medias (dónde quedó y qué sigue). Quita lo que ya se cerró y agrega lo nuevo con su responsable y fecha si la hay.
4. **✗ No tocar:** conserva lo que hay; agrega solo lo que Karen o Eduardo prohíban en la conversación.
5. Pon la fecha de hoy en el título, haz commit y push directo a `main` (o a la rama de la sesión, si se asignó una).
6. Muestra los 3 puntos en máximo 10 líneas, sin recapitular la conversación.

**«Lee el parte» (solo leer):** `git pull` y muestra `parte.md` en máximo 10 líneas, sin cambiar nada.

Reglas: «Hecho» no es «Publicado» (solo lo marcan Karen o Eduardo); sin datos de pacientes.
