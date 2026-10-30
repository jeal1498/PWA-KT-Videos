# Estilo v2 sin cara: referencia

Leer cuando se arme la animación (`scenes.py` / `anim.js`) o la portada. Receta aprobada por Karen el 30 oct 2026 con el 19; no volver a proponer estilos ni voces salvo que lo pidan.

## Dos tintas
- Rellenos planos lavanda `#C6BCE2`, rosa `#F9DEE3`, arena `#F5E7D6`; contorno ciruela profundo `#2E2545` de 6 a 8 px; check verde `#10b77f`. Fondo ciruela con resplandor radial, viñeta y garabatos que se mecen.
- Trazo que vibra 12 veces por segundo: filtro `#rough` (`feTurbulence` + `feDisplacementMap`, escala 6). Los textos van **fuera** del filtro para que se lean limpios.
- Entradas con `elastic.out(1,0.55)`; líneas y ramas que se dibujan. Palabras clave como calcomanía: arena, −2.5°, sombra lavanda `7px 8px`.
- Transición entre escenas: la línea con nodo de la marca. Ninguna otra.

## Personaje
- Open Peeps de DiceBear (CC0), `seed: 'Mar'`, `head: long`, piel arena, ropa lavanda, trazo ciruela. Se generan con `scripts/avatares.cjs` (una vez por entorno: `npm i --prefix <dir> @dicebear/core@9.2.2 @dicebear/collection@9.2.2`).
- **Solo donde suma:** gancho, momentos emocionales y cierre (≈4 de 12 escenas). Cambia de cara en cada giro (cruce de 0.25 s). Sin manos: gestos con movimiento (asentir, negar, respirar, rebote).
- Caras: problema → `tired`, `hectic`, `concernedFear`; duda → `suspicious`, `solemn`, `serious`; «¡ah!» → `awe`, `driven`; solución → `calm`, `smile`, `smileBig`. **No usar `concerned` en el gancho** (boca abierta, asusta).
- Una clave por aparición (`sonrisa`, `sonrisa2`): el mismo avatar en dos escenas comparte ids de máscara y desaparece.
- No dibujar personajes a mano en SVG (salieron feos tres veces). El avatar de Karen (`assets/avatar-karen.cjs`) existe pero no se usa.

## Voz (Eleven v3)
- `voz.py guion.txt <trabajo> --modelo v3 --max-silencio 0.35`. Voz clonada de Karen `sSQiAF9Uq1K3xnyvFi8w` (por defecto). La clave `ELEVENLABS_API_KEY` no tiene speech-to-text.
- 4 a 6 tags solo en giros emocionales (`[pause]`, `[sighs]`, `[curious]`, `[softly]`, `[warmly]`). Nunca en la explicación clínica ni en el aviso; sin `[laughs]` ni `[excited]`. **No abrir con `[pause]`.**
- Cada toma de v3 sale distinta; si una gusta, guardarla. Duración real: ≈165 a 185 palabras → 62 a 72 s.
- Cambiar la voz de un video ya armado: regenerar, crear `warp.json` con pares `[inicio_viejo, inicio_nuevo]` y volver a correr `build.py` (así se hizo el 19; recuperable de git, ver `docs/README.md`).

## Escenas (lecciones 21 a 25)
- **Sin cuadros vacíos:** en cada escena entran elementos desde el principio (tarjetas atenuadas que se encienden al decirlas, burbujas que se sustituyen); nunca más de ≈1.5 s con solo el título. Revisar con `armar.sh --vistazo`, sobre todo justo después de cada título.
- No repetir en pantalla lo que ya dice el subtítulo.
- Objetos cotidianos reconocibles (llaves con aro, celular de pie, audífonos de diadema). Una estufa con perillas parece cara: olla encima y ventana de horno. Luna: path de Feather `M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z`.
- Trazos ciruela sobre fondo ciruela no se ven: usar arena.
- Subir los textos `.q` si tapan al avatar.

## Trampas de código
- En `build.py` no llamar `H` a una función propia (pisa `html as H`); usar `HD`.
- Grupos con `pop` dentro de otro `<g transform>` se desplazan: para elementos de contorno usar `fade`.
- Un `span.st` inline con `stick` no escala: animar `up` en un `div` contenedor.
- No hacer `replace` sobre `class="m1…"` si existen clases `m10`: rompe la clase.
- Para dibujar un trazo concreto con `draw`, darle clase propia (`.sl`), no `path:last-of-type`.
- Atributos SVG siempre entre comillas (`opacity=.55/>` deja el elemento abierto). Ids únicos en la página.
- GSAP: `fromTo` se muestra desde el cuadro 0; para algo posterior, `immediateRender:false`. Sin `Math.random` ni `Date.now`.
- `hyperframes check` a veces no abre el navegador («Browser session never ran»): basta `snapshot` y el render.

## Portada v2
- Tipográfica con ilustración, sin cuadro de Karen; todo entre y=300 y 1620 (`qc.py` lo revisa). Etiqueta: «Consejo para TDAH» o «Consejo de bienestar» si no habla de TDAH.
- Gancho de ≤25 caracteres, de la idea del guion. Revisar signos (salió «=» donde iba «≠»).
- Aprobadas: dos paneles «Por fuera / Por dentro» (23), reloj grande con flecha antihoraria (24), cocina con signos de interrogación (25).
