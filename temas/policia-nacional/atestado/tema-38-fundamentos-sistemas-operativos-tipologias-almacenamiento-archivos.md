# TEMA 38 · FUNDAMENTOS DE SISTEMAS OPERATIVOS: FUNCIONES DE UN SISTEMA OPERATIVO. TIPOLOGÍAS: MS-DOS, UNIX, LINUX, WINDOWS Y MACOS. SISTEMAS OPERATIVOS MÓVILES: IOS Y ANDROID. SISTEMAS DE ALMACENAMIENTO. SISTEMAS DE ARCHIVOS.

**Policía Nacional · Método VIGOR · ATESTADO**
**Versión de contenido:** 1.0.0
**Estado editorial:** approved_internal · **Publicación:** not_published

# Mapa del tema

El Tema 38 se estudia en diez partes: fundamentos; funciones; MS-DOS; UNIX/POSIX; Linux; Windows; macOS; iOS y Android; sistemas de almacenamiento; y sistemas de archivos.

# Contenido

## 01. Alcance oficial del Tema 38

### Lógica del bloque

Para dominar **alcance oficial del tema 38**, aplica esta regla: El programa exige fundamentos y funciones de los sistemas operativos. El anclaje principal es **diez áreas de estudio**.

### Hechos examinables

- El programa exige fundamentos y funciones de los sistemas operativos. <!-- FACT:PN-T38-F001 -->
- Las tipologías expresamente citadas son MS-DOS, UNIX, Linux, Windows y macOS. <!-- FACT:PN-T38-F002 -->
- El epígrafe incorpora los sistemas operativos móviles iOS y Android. <!-- FACT:PN-T38-F003 -->
- El programa se completa con sistemas de almacenamiento y sistemas de archivos. <!-- FACT:PN-T38-F004 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: Las tipologías expresamente citadas son MS-DOS, UNIX, Linux, Windows y macOS.
- **Contraste útil:** Contraste: El epígrafe incorpora los sistemas operativos móviles iOS y Android.

### Trampas de examen

- **Incorrecto:** El Tema 38 se limita al manejo de Windows.
- **Incorrecto:** Las tecnologías móviles y los sistemas de archivos quedan fuera del epígrafe.

<!-- VISUAL PENDIENTE: t38-01-alcance-oficial-del-tema-38.webp -->

:::hablemos-claro
El programa exige fundamentos y funciones de los sistemas operativos.
:::

:::en-la-calle
Al seguir el arranque desde el hardware hasta el núcleo, El programa exige fundamentos y funciones de los sistemas operativos.
:::

:::lo-que-cae
Prioriza **diez áreas de estudio** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: CONVOCATORIA-PN-2026-T38 -->

## 02. Hardware, software y firmware

### Lógica del bloque

Para dominar **hardware, software y firmware**, aplica esta regla: El hardware reúne los componentes físicos que ejecutan, almacenan o transfieren información. El anclaje principal es **tres capas del sistema**.

### Hechos examinables

- El hardware reúne los componentes físicos que ejecutan, almacenan o transfieren información. <!-- FACT:PN-T38-F005 -->
- El software es el conjunto de instrucciones y datos que se ejecutan sobre el hardware. <!-- FACT:PN-T38-F006 -->
- El firmware es software estrechamente ligado a un dispositivo y almacenado normalmente en memoria no volátil. <!-- FACT:PN-T38-F007 -->
- El sistema operativo coordina hardware, aplicaciones, datos y usuarios sin confundirse con ninguno de ellos. <!-- FACT:PN-T38-F008 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: El software es el conjunto de instrucciones y datos que se ejecutan sobre el hardware.
- **Contraste útil:** Contraste: El firmware es software estrechamente ligado a un dispositivo y almacenado normalmente en memoria no volátil.

### Trampas de examen

- **Incorrecto:** El firmware es un periférico físico sin código.
- **Incorrecto:** Toda aplicación forma parte del núcleo del sistema operativo.

<!-- VISUAL PENDIENTE: t38-02-hardware-software-y-firmware.webp -->

:::hablemos-claro
El hardware reúne los componentes físicos que ejecutan, almacenan o transfieren información.
:::

:::en-la-calle
Al seguir el arranque desde el hardware hasta el núcleo, El hardware reúne los componentes físicos que ejecutan, almacenan o transfieren información.
:::

:::lo-que-cae
Prioriza **tres capas del sistema** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: LINUX-KERNEL-T38 -->

## 03. Arquitectura de programa almacenado

### Lógica del bloque

Para dominar **arquitectura de programa almacenado**, aplica esta regla: En una arquitectura de programa almacenado, instrucciones y datos se conservan en memoria accesible al procesador. El anclaje principal es **instrucciones y datos en memoria**.

### Hechos examinables

- En una arquitectura de programa almacenado, instrucciones y datos se conservan en memoria accesible al procesador. <!-- FACT:PN-T38-F009 -->
- La unidad de control obtiene y decodifica instrucciones, y coordina su ejecución. <!-- FACT:PN-T38-F010 -->
- La ALU realiza operaciones aritméticas y lógicas requeridas por las instrucciones. <!-- FACT:PN-T38-F011 -->
- Los buses y controladores permiten intercambiar direcciones, datos y señales de control entre componentes. <!-- FACT:PN-T38-F012 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: La unidad de control obtiene y decodifica instrucciones, y coordina su ejecución.
- **Contraste útil:** Contraste: La ALU realiza operaciones aritméticas y lógicas requeridas por las instrucciones.

### Trampas de examen

- **Incorrecto:** La ALU almacena permanentemente todos los archivos del usuario.
- **Incorrecto:** El procesador ejecuta programas sin leer instrucciones ni datos de memoria.

<!-- VISUAL PENDIENTE: t38-03-arquitectura-de-programa-almacenado.webp -->

:::hablemos-claro
En una arquitectura de programa almacenado, instrucciones y datos se conservan en memoria accesible al procesador.
:::

:::en-la-calle
Al seguir el arranque desde el hardware hasta el núcleo, En una arquitectura de programa almacenado, instrucciones y datos se conservan en memoria accesible al procesador.
:::

:::lo-que-cae
Prioriza **instrucciones y datos en memoria** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: LINUX-KERNEL-T38 -->

## 04. CPU, núcleos, hilos y caché

### Lógica del bloque

Para dominar **cpu, núcleos, hilos y caché**, aplica esta regla: La CPU ejecuta instrucciones y puede integrar uno o varios núcleos de procesamiento. El anclaje principal es **capacidad de ejecución**.

### Hechos examinables

- La CPU ejecuta instrucciones y puede integrar uno o varios núcleos de procesamiento. <!-- FACT:PN-T38-F013 -->
- Un núcleo físico no es idéntico a un hilo lógico ofrecido por el hardware. <!-- FACT:PN-T38-F014 -->
- Los registros guardan operandos, direcciones y estado inmediato de la ejecución. <!-- FACT:PN-T38-F015 -->
- La memoria caché reduce la latencia media al conservar datos e instrucciones próximos al procesador. <!-- FACT:PN-T38-F016 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: Un núcleo físico no es idéntico a un hilo lógico ofrecido por el hardware.
- **Contraste útil:** Contraste: Los registros guardan operandos, direcciones y estado inmediato de la ejecución.

### Trampas de examen

- **Incorrecto:** Un hilo lógico es siempre otro procesador físico independiente.
- **Incorrecto:** La caché sustituye al almacenamiento persistente del equipo.

<!-- VISUAL PENDIENTE: t38-il-04-cpu-nucleos-hilos-y-cache.webp -->

:::hablemos-claro
La CPU ejecuta instrucciones y puede integrar uno o varios núcleos de procesamiento.
:::

:::en-la-calle
Al seguir el arranque desde el hardware hasta el núcleo, La CPU ejecuta instrucciones y puede integrar uno o varios núcleos de procesamiento.
:::

:::lo-que-cae
Prioriza **capacidad de ejecución** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: LINUX-KERNEL-T38 -->

## 05. Jerarquía de memoria

### Lógica del bloque

Para dominar **jerarquía de memoria**, aplica esta regla: Registros y cachés son muy rápidos y de capacidad limitada frente a la memoria principal. El anclaje principal es **velocidad, capacidad y persistencia**.

### Hechos examinables

- Registros y cachés son muy rápidos y de capacidad limitada frente a la memoria principal. <!-- FACT:PN-T38-F017 -->
- La RAM mantiene temporalmente código y datos en uso y pierde normalmente su contenido sin alimentación. <!-- FACT:PN-T38-F018 -->
- El almacenamiento secundario conserva información de forma no volátil. <!-- FACT:PN-T38-F019 -->
- La memoria virtual no convierte el almacenamiento en RAM física ni elimina su diferencia de velocidad. <!-- FACT:PN-T38-F020 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: La RAM mantiene temporalmente código y datos en uso y pierde normalmente su contenido sin alimentación.
- **Contraste útil:** Contraste: El almacenamiento secundario conserva información de forma no volátil.

### Trampas de examen

- **Incorrecto:** La RAM es un almacenamiento no volátil equivalente a un SSD.
- **Incorrecto:** La memoria virtual aumenta físicamente los módulos RAM instalados.

<!-- VISUAL PENDIENTE: t38-il-05-jerarquia-de-memoria.webp -->

:::hablemos-claro
Registros y cachés son muy rápidos y de capacidad limitada frente a la memoria principal.
:::

:::en-la-calle
Al seguir el arranque desde el hardware hasta el núcleo, Registros y cachés son muy rápidos y de capacidad limitada frente a la memoria principal.
:::

:::lo-que-cae
Prioriza **velocidad, capacidad y persistencia** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: LINUX-KERNEL-T38 -->

## 06. Bit, byte y prefijos de capacidad

### Lógica del bloque

Para dominar **bit, byte y prefijos de capacidad**, aplica esta regla: El bit es una unidad binaria y el byte agrupa ocho bits. El anclaje principal es **b frente a B y decimal frente a binario**.

### Hechos examinables

- El bit es una unidad binaria y el byte agrupa ocho bits. <!-- FACT:PN-T38-F021 -->
- La b minúscula suele representar bits y la B mayúscula bytes. <!-- FACT:PN-T38-F022 -->
- Los prefijos SI kB, MB y GB usan potencias de mil. <!-- FACT:PN-T38-F023 -->
- Los prefijos binarios KiB, MiB y GiB usan potencias de 1024 y no deben confundirse con los prefijos SI. <!-- FACT:PN-T38-F024 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: La b minúscula suele representar bits y la B mayúscula bytes.
- **Contraste útil:** Contraste: Los prefijos SI kB, MB y GB usan potencias de mil.

### Trampas de examen

- **Incorrecto:** Un byte contiene 1024 bits.
- **Incorrecto:** KB y KiB son símbolos rigurosamente equivalentes en cualquier contexto.

<!-- VISUAL PENDIENTE: t38-06-bit-byte-y-prefijos-de-capacidad.webp -->

:::hablemos-claro
El bit es una unidad binaria y el byte agrupa ocho bits.
:::

:::en-la-calle
Al seguir el arranque desde el hardware hasta el núcleo, El bit es una unidad binaria y el byte agrupa ocho bits.
:::

:::lo-que-cae
Prioriza **b frente a B y decimal frente a binario** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: NVME-SPEC-T38 -->

## 07. Entrada, salida y periféricos

### Lógica del bloque

Para dominar **entrada, salida y periféricos**, aplica esta regla: Un dispositivo de entrada aporta datos o señales al sistema. El anclaje principal es **dirección del flujo de información**.

### Hechos examinables

- Un dispositivo de entrada aporta datos o señales al sistema. <!-- FACT:PN-T38-F025 -->
- Un dispositivo de salida presenta o transmite resultados del sistema. <!-- FACT:PN-T38-F026 -->
- Un mismo dispositivo puede realizar funciones de entrada y salida. <!-- FACT:PN-T38-F027 -->
- El sistema operativo accede a los periféricos mediante controladores y mecanismos de entrada/salida. <!-- FACT:PN-T38-F028 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: Un dispositivo de salida presenta o transmite resultados del sistema.
- **Contraste útil:** Contraste: Un mismo dispositivo puede realizar funciones de entrada y salida.

### Trampas de examen

- **Incorrecto:** Todo periférico es exclusivamente de entrada o exclusivamente de salida.
- **Incorrecto:** Las aplicaciones controlan el hardware sin mediación del sistema operativo.

<!-- VISUAL PENDIENTE: t38-07-entrada-salida-y-perifericos.webp -->

:::hablemos-claro
Un dispositivo de entrada aporta datos o señales al sistema.
:::

:::en-la-calle
Al seguir el arranque desde el hardware hasta el núcleo, Un dispositivo de entrada aporta datos o señales al sistema.
:::

:::lo-que-cae
Prioriza **dirección del flujo de información** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: LINUX-KERNEL-T38 -->

## 08. Arranque: firmware, cargador y núcleo

### Lógica del bloque

Para dominar **arranque: firmware, cargador y núcleo**, aplica esta regla: El firmware inicializa componentes básicos y localiza un mecanismo de arranque. El anclaje principal es **cadena de arranque**.

### Hechos examinables

- El firmware inicializa componentes básicos y localiza un mecanismo de arranque. <!-- FACT:PN-T38-F029 -->
- El cargador de arranque prepara el entorno y transfiere el control al núcleo del sistema operativo. <!-- FACT:PN-T38-F030 -->
- El núcleo inicializa subsistemas como memoria, planificación, dispositivos y sistema de archivos raíz. <!-- FACT:PN-T38-F031 -->
- El arranque seguro añade verificaciones de integridad o autenticidad, pero no es sinónimo de cifrado de todos los datos. <!-- FACT:PN-T38-F032 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: El cargador de arranque prepara el entorno y transfiere el control al núcleo del sistema operativo.
- **Contraste útil:** Contraste: El núcleo inicializa subsistemas como memoria, planificación, dispositivos y sistema de archivos raíz.

### Trampas de examen

- **Incorrecto:** El cargador de arranque comienza después de cerrar el sistema operativo.
- **Incorrecto:** Arranque seguro y cifrado completo del almacenamiento son la misma función.

<!-- VISUAL PENDIENTE: t38-08-arranque-firmware-cargador-y-nucleo.webp -->

:::hablemos-claro
El firmware inicializa componentes básicos y localiza un mecanismo de arranque.
:::

:::en-la-calle
Al seguir el arranque desde el hardware hasta el núcleo, El firmware inicializa componentes básicos y localiza un mecanismo de arranque.
:::

:::lo-que-cae
Prioriza **cadena de arranque** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: APPLE-PLATFORM-SECURITY-T38 -->

## 09. Sistema operativo como gestor de recursos

### Lógica del bloque

Para dominar **sistema operativo como gestor de recursos**, aplica esta regla: El sistema operativo administra procesador, memoria, dispositivos y almacenamiento. El anclaje principal es **abstracción y arbitraje**.

### Hechos examinables

- El sistema operativo administra procesador, memoria, dispositivos y almacenamiento. <!-- FACT:PN-T38-F033 -->
- Proporciona abstracciones que evitan que cada aplicación gestione directamente el hardware. <!-- FACT:PN-T38-F034 -->
- Arbitra recursos compartidos para reducir conflictos entre programas y usuarios. <!-- FACT:PN-T38-F035 -->
- Ofrece servicios comunes para ejecutar aplicaciones y conservar información. <!-- FACT:PN-T38-F036 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: Proporciona abstracciones que evitan que cada aplicación gestione directamente el hardware.
- **Contraste útil:** Contraste: Arbitra recursos compartidos para reducir conflictos entre programas y usuarios.

### Trampas de examen

- **Incorrecto:** La única función del sistema operativo es mostrar ventanas.
- **Incorrecto:** Cada aplicación debe asignarse por sí sola la memoria física y los dispositivos.

<!-- VISUAL PENDIENTE: t38-09-sistema-operativo-como-gestor-de-recursos.webp -->

:::hablemos-claro
El sistema operativo administra procesador, memoria, dispositivos y almacenamiento.
:::

:::en-la-calle
Al observar cómo el sistema reparte CPU, memoria y dispositivos, El sistema operativo administra procesador, memoria, dispositivos y almacenamiento.
:::

:::lo-que-cae
Prioriza **abstracción y arbitraje** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: LINUX-KERNEL-T38 -->

## 10. Núcleo, modo usuario y llamadas al sistema

### Lógica del bloque

Para dominar **núcleo, modo usuario y llamadas al sistema**, aplica esta regla: El núcleo ejecuta funciones privilegiadas y mantiene el control de recursos críticos. El anclaje principal es **frontera de privilegios**.

### Hechos examinables

- El núcleo ejecuta funciones privilegiadas y mantiene el control de recursos críticos. <!-- FACT:PN-T38-F037 -->
- Las aplicaciones ordinarias se ejecutan normalmente con privilegios restringidos en modo usuario. <!-- FACT:PN-T38-F038 -->
- Una llamada al sistema solicita al núcleo un servicio mediante una interfaz definida. <!-- FACT:PN-T38-F039 -->
- Separar privilegios limita el daño directo que puede causar un proceso de usuario defectuoso. <!-- FACT:PN-T38-F040 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: Las aplicaciones ordinarias se ejecutan normalmente con privilegios restringidos en modo usuario.
- **Contraste útil:** Contraste: Una llamada al sistema solicita al núcleo un servicio mediante una interfaz definida.

### Trampas de examen

- **Incorrecto:** Una llamada al sistema cambia permanentemente cualquier programa a modo núcleo.
- **Incorrecto:** El modo usuario permite ejecutar sin control todas las instrucciones privilegiadas.

<!-- VISUAL PENDIENTE: t38-il-10-nucleo-modo-usuario-y-llamadas-al-sistema.webp -->

:::hablemos-claro
El núcleo ejecuta funciones privilegiadas y mantiene el control de recursos críticos.
:::

:::en-la-calle
Al observar cómo el sistema reparte CPU, memoria y dispositivos, El núcleo ejecuta funciones privilegiadas y mantiene el control de recursos críticos.
:::

:::lo-que-cae
Prioriza **frontera de privilegios** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: MS-WINDOWS-INTERNALS-T38 -->

## 11. Programa, proceso e imagen ejecutable

### Lógica del bloque

Para dominar **programa, proceso e imagen ejecutable**, aplica esta regla: Un programa es código y datos preparados para ejecutarse. El anclaje principal es **código frente a ejecución**.

### Hechos examinables

- Un programa es código y datos preparados para ejecutarse. <!-- FACT:PN-T38-F041 -->
- Un proceso es una instancia en ejecución con estado y recursos asociados. <!-- FACT:PN-T38-F042 -->
- Varias instancias del mismo programa pueden originar procesos distintos. <!-- FACT:PN-T38-F043 -->
- El sistema identifica y administra procesos sin confundirlos con el archivo ejecutable que los inició. <!-- FACT:PN-T38-F044 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: Un proceso es una instancia en ejecución con estado y recursos asociados.
- **Contraste útil:** Contraste: Varias instancias del mismo programa pueden originar procesos distintos.

### Trampas de examen

- **Incorrecto:** Un proceso es únicamente el archivo guardado en disco.
- **Incorrecto:** Un programa solo puede tener una instancia en ejecución.

<!-- VISUAL PENDIENTE: t38-11-programa-proceso-e-imagen-ejecutable.webp -->

:::hablemos-claro
Un programa es código y datos preparados para ejecutarse.
:::

:::en-la-calle
Al observar cómo el sistema reparte CPU, memoria y dispositivos, Un programa es código y datos preparados para ejecutarse.
:::

:::lo-que-cae
Prioriza **código frente a ejecución** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: POSIX-2024-T38 -->

## 12. Estados y ciclo de vida de un proceso

### Lógica del bloque

Para dominar **estados y ciclo de vida de un proceso**, aplica esta regla: Un proceso listo puede ejecutar cuando el planificador le asigne procesador. El anclaje principal es **listo, ejecución y espera**.

### Hechos examinables

- Un proceso listo puede ejecutar cuando el planificador le asigne procesador. <!-- FACT:PN-T38-F045 -->
- Un proceso en ejecución está usando una CPU o núcleo lógico en ese instante. <!-- FACT:PN-T38-F046 -->
- Un proceso bloqueado o en espera aguarda un evento o recurso antes de continuar. <!-- FACT:PN-T38-F047 -->
- La terminación libera o transfiere los recursos conforme a las reglas del sistema. <!-- FACT:PN-T38-F048 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: Un proceso en ejecución está usando una CPU o núcleo lógico en ese instante.
- **Contraste útil:** Contraste: Un proceso bloqueado o en espera aguarda un evento o recurso antes de continuar.

### Trampas de examen

- **Incorrecto:** Un proceso bloqueado consume necesariamente CPU de forma continua.
- **Incorrecto:** El estado listo significa que el proceso ya terminó.

<!-- VISUAL PENDIENTE: t38-il-12-estados-y-ciclo-de-vida-de-un-proceso.webp -->

:::hablemos-claro
Un proceso listo puede ejecutar cuando el planificador le asigne procesador.
:::

:::en-la-calle
Al observar cómo el sistema reparte CPU, memoria y dispositivos, Un proceso listo puede ejecutar cuando el planificador le asigne procesador.
:::

:::lo-que-cae
Prioriza **listo, ejecución y espera** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: POSIX-2024-T38 -->

## 13. Hilos y recursos compartidos

### Lógica del bloque

Para dominar **hilos y recursos compartidos**, aplica esta regla: Un hilo es una secuencia de ejecución planificable dentro de un proceso. El anclaje principal es **unidad de ejecución dentro del proceso**.

### Hechos examinables

- Un hilo es una secuencia de ejecución planificable dentro de un proceso. <!-- FACT:PN-T38-F049 -->
- Los hilos de un proceso comparten habitualmente el espacio de direcciones y otros recursos. <!-- FACT:PN-T38-F050 -->
- Cada hilo conserva contexto propio, como registros y pila de ejecución. <!-- FACT:PN-T38-F051 -->
- Compartir memoria facilita cooperación, pero exige sincronización frente a accesos concurrentes. <!-- FACT:PN-T38-F052 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: Los hilos de un proceso comparten habitualmente el espacio de direcciones y otros recursos.
- **Contraste útil:** Contraste: Cada hilo conserva contexto propio, como registros y pila de ejecución.

### Trampas de examen

- **Incorrecto:** Cada hilo tiene siempre un espacio de direcciones completamente aislado.
- **Incorrecto:** Los hilos eliminan cualquier riesgo de carrera sobre datos compartidos.

<!-- VISUAL PENDIENTE: t38-13-hilos-y-recursos-compartidos.webp -->

:::hablemos-claro
Un hilo es una secuencia de ejecución planificable dentro de un proceso.
:::

:::en-la-calle
Al observar cómo el sistema reparte CPU, memoria y dispositivos, Un hilo es una secuencia de ejecución planificable dentro de un proceso.
:::

:::lo-que-cae
Prioriza **unidad de ejecución dentro del proceso** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: MS-WINDOWS-INTERNALS-T38 -->

## 14. Planificación de CPU

### Lógica del bloque

Para dominar **planificación de cpu**, aplica esta regla: El planificador decide qué tarea ejecutable utiliza la CPU en cada momento. El anclaje principal es **elección de la siguiente tarea**.

### Hechos examinables

- El planificador decide qué tarea ejecutable utiliza la CPU en cada momento. <!-- FACT:PN-T38-F053 -->
- La política puede considerar prioridad, equidad, latencia, plazos o consumo energético. <!-- FACT:PN-T38-F054 -->
- El cambio de contexto sustituye el estado de ejecución de una tarea por el de otra. <!-- FACT:PN-T38-F055 -->
- Una mayor prioridad no implica necesariamente monopolio ilimitado del procesador. <!-- FACT:PN-T38-F056 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: La política puede considerar prioridad, equidad, latencia, plazos o consumo energético.
- **Contraste útil:** Contraste: El cambio de contexto sustituye el estado de ejecución de una tarea por el de otra.

### Trampas de examen

- **Incorrecto:** El planificador solo interviene cuando se apaga el equipo.
- **Incorrecto:** El cambio de contexto convierte dos procesos en uno.

<!-- VISUAL PENDIENTE: t38-14-planificacion-de-cpu.webp -->

:::hablemos-claro
El planificador decide qué tarea ejecutable utiliza la CPU en cada momento.
:::

:::en-la-calle
Al observar cómo el sistema reparte CPU, memoria y dispositivos, El planificador decide qué tarea ejecutable utiliza la CPU en cada momento.
:::

:::lo-que-cae
Prioriza **elección de la siguiente tarea** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: LINUX-KERNEL-T38 -->

## 15. Multiprogramación, multitarea y multiprocesamiento

### Lógica del bloque

Para dominar **multiprogramación, multitarea y multiprocesamiento**, aplica esta regla: La multiprogramación mantiene varios trabajos preparados para aprovechar mejor la CPU. El anclaje principal es **concurrencia frente a paralelismo**.

### Hechos examinables

- La multiprogramación mantiene varios trabajos preparados para aprovechar mejor la CPU. <!-- FACT:PN-T38-F057 -->
- La multitarea alterna o distribuye la ejecución de varias tareas de forma gestionada. <!-- FACT:PN-T38-F058 -->
- El multiprocesamiento utiliza más de una unidad de procesamiento. <!-- FACT:PN-T38-F059 -->
- La concurrencia permite progresos solapados; el paralelismo implica ejecución simultánea real. <!-- FACT:PN-T38-F060 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: La multitarea alterna o distribuye la ejecución de varias tareas de forma gestionada.
- **Contraste útil:** Contraste: El multiprocesamiento utiliza más de una unidad de procesamiento.

### Trampas de examen

- **Incorrecto:** Toda concurrencia exige dos procesadores físicos.
- **Incorrecto:** Multitarea y multiprocesamiento significan exactamente lo mismo.

<!-- VISUAL PENDIENTE: t38-15-multiprogramacion-multitarea-y-multiprocesamiento.webp -->

:::hablemos-claro
La multiprogramación mantiene varios trabajos preparados para aprovechar mejor la CPU.
:::

:::en-la-calle
Al observar cómo el sistema reparte CPU, memoria y dispositivos, La multiprogramación mantiene varios trabajos preparados para aprovechar mejor la CPU.
:::

:::lo-que-cae
Prioriza **concurrencia frente a paralelismo** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: LINUX-KERNEL-T38 -->

## 16. Sincronización y condiciones de carrera

### Lógica del bloque

Para dominar **sincronización y condiciones de carrera**, aplica esta regla: Existe condición de carrera cuando el resultado depende de un orden no controlado entre ejecuciones concurrentes. El anclaje principal es **ordenar accesos compartidos**.

### Hechos examinables

- Existe condición de carrera cuando el resultado depende de un orden no controlado entre ejecuciones concurrentes. <!-- FACT:PN-T38-F061 -->
- La exclusión mutua protege secciones críticas frente a accesos simultáneos incompatibles. <!-- FACT:PN-T38-F062 -->
- Semáforos, mutex y otros mecanismos coordinan tareas con propiedades diferentes. <!-- FACT:PN-T38-F063 -->
- Un interbloqueo puede surgir cuando varias tareas esperan recursos retenidos entre sí. <!-- FACT:PN-T38-F064 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: La exclusión mutua protege secciones críticas frente a accesos simultáneos incompatibles.
- **Contraste útil:** Contraste: Semáforos, mutex y otros mecanismos coordinan tareas con propiedades diferentes.

### Trampas de examen

- **Incorrecto:** Un mutex incrementa la velocidad eliminando toda espera posible.
- **Incorrecto:** Interbloqueo significa que una tarea ya ha terminado correctamente.

<!-- VISUAL PENDIENTE: t38-il-16-sincronizacion-y-condiciones-de-carrera.webp -->

:::hablemos-claro
Existe condición de carrera cuando el resultado depende de un orden no controlado entre ejecuciones concurrentes.
:::

:::en-la-calle
Al observar cómo el sistema reparte CPU, memoria y dispositivos, Existe condición de carrera cuando el resultado depende de un orden no controlado entre ejecuciones concurrentes.
:::

:::lo-que-cae
Prioriza **ordenar accesos compartidos** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: LINUX-KERNEL-T38 -->

## 17. Comunicación entre procesos

### Lógica del bloque

Para dominar **comunicación entre procesos**, aplica esta regla: La comunicación entre procesos permite intercambiar datos o señales entre ejecuciones separadas. El anclaje principal es **IPC**.

### Hechos examinables

- La comunicación entre procesos permite intercambiar datos o señales entre ejecuciones separadas. <!-- FACT:PN-T38-F065 -->
- Tuberías, colas, memoria compartida, señales y sockets son mecanismos de IPC. <!-- FACT:PN-T38-F066 -->
- La memoria compartida puede ser eficiente, pero requiere coordinación de acceso. <!-- FACT:PN-T38-F067 -->
- Un socket puede comunicar procesos del mismo equipo o de equipos distintos según su dominio y protocolo. <!-- FACT:PN-T38-F068 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: Tuberías, colas, memoria compartida, señales y sockets son mecanismos de IPC.
- **Contraste útil:** Contraste: La memoria compartida puede ser eficiente, pero requiere coordinación de acceso.

### Trampas de examen

- **Incorrecto:** IPC significa que todos los procesos comparten automáticamente toda la RAM.
- **Incorrecto:** Las tuberías son dispositivos físicos de almacenamiento.

<!-- VISUAL PENDIENTE: t38-17-comunicacion-entre-procesos.webp -->

:::hablemos-claro
La comunicación entre procesos permite intercambiar datos o señales entre ejecuciones separadas.
:::

:::en-la-calle
Al observar cómo el sistema reparte CPU, memoria y dispositivos, La comunicación entre procesos permite intercambiar datos o señales entre ejecuciones separadas.
:::

:::lo-que-cae
Prioriza **IPC** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: POSIX-2024-T38 -->

## 18. Gestión de memoria

### Lógica del bloque

Para dominar **gestión de memoria**, aplica esta regla: El sistema operativo asigna memoria a procesos y recupera regiones cuando dejan de utilizarse. El anclaje principal es **asignación, protección y recuperación**.

### Hechos examinables

- El sistema operativo asigna memoria a procesos y recupera regiones cuando dejan de utilizarse. <!-- FACT:PN-T38-F069 -->
- La protección de memoria evita accesos no autorizados entre espacios de direcciones. <!-- FACT:PN-T38-F070 -->
- La traducción de direcciones permite separar la visión virtual del proceso de la ubicación física. <!-- FACT:PN-T38-F071 -->
- La fragmentación puede ser interna o externa y no describe necesariamente archivos del disco. <!-- FACT:PN-T38-F072 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: La protección de memoria evita accesos no autorizados entre espacios de direcciones.
- **Contraste útil:** Contraste: La traducción de direcciones permite separar la visión virtual del proceso de la ubicación física.

### Trampas de examen

- **Incorrecto:** Todos los procesos escriben libremente en la memoria de los demás.
- **Incorrecto:** Fragmentación de memoria y fragmentación de archivos son siempre el mismo fenómeno.

<!-- VISUAL PENDIENTE: t38-18-gestion-de-memoria.webp -->

:::hablemos-claro
El sistema operativo asigna memoria a procesos y recupera regiones cuando dejan de utilizarse.
:::

:::en-la-calle
Al observar cómo el sistema reparte CPU, memoria y dispositivos, El sistema operativo asigna memoria a procesos y recupera regiones cuando dejan de utilizarse.
:::

:::lo-que-cae
Prioriza **asignación, protección y recuperación** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: LINUX-KERNEL-T38 -->

## 19. Memoria virtual y paginación

### Lógica del bloque

Para dominar **memoria virtual y paginación**, aplica esta regla: La memoria virtual proporciona a cada proceso un espacio de direcciones abstracto. El anclaje principal es **páginas virtuales y marcos físicos**.

### Hechos examinables

- La memoria virtual proporciona a cada proceso un espacio de direcciones abstracto. <!-- FACT:PN-T38-F073 -->
- La paginación divide el espacio virtual y la memoria física en unidades gestionables. <!-- FACT:PN-T38-F074 -->
- Una falta de página ocurre cuando la traducción o el contenido requerido no está disponible como necesita la CPU. <!-- FACT:PN-T38-F075 -->
- El intercambio con almacenamiento es mucho más lento que acceder a RAM y su uso excesivo degrada el rendimiento. <!-- FACT:PN-T38-F076 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: La paginación divide el espacio virtual y la memoria física en unidades gestionables.
- **Contraste útil:** Contraste: Una falta de página ocurre cuando la traducción o el contenido requerido no está disponible como necesita la CPU.

### Trampas de examen

- **Incorrecto:** Una falta de página demuestra siempre un fallo físico del disco.
- **Incorrecto:** El intercambio es más rápido que la memoria RAM.

<!-- VISUAL PENDIENTE: t38-il-19-memoria-virtual-y-paginacion.webp -->

:::hablemos-claro
La memoria virtual proporciona a cada proceso un espacio de direcciones abstracto.
:::

:::en-la-calle
Al observar cómo el sistema reparte CPU, memoria y dispositivos, La memoria virtual proporciona a cada proceso un espacio de direcciones abstracto.
:::

:::lo-que-cae
Prioriza **páginas virtuales y marcos físicos** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: LINUX-KERNEL-T38 -->

## 20. Gestión de archivos y directorios

### Lógica del bloque

Para dominar **gestión de archivos y directorios**, aplica esta regla: El sistema operativo ofrece operaciones para crear, abrir, leer, escribir, renombrar y eliminar archivos. El anclaje principal es **nombres, rutas y metadatos**.

### Hechos examinables

- El sistema operativo ofrece operaciones para crear, abrir, leer, escribir, renombrar y eliminar archivos. <!-- FACT:PN-T38-F077 -->
- Los directorios organizan nombres y referencias dentro de una jerarquía. <!-- FACT:PN-T38-F078 -->
- Los metadatos describen propiedades como tipo, tamaño, marcas temporales, propietario o permisos. <!-- FACT:PN-T38-F079 -->
- Eliminar una referencia de directorio no equivale necesariamente a sobrescribir de inmediato los datos físicos. <!-- FACT:PN-T38-F080 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: Los directorios organizan nombres y referencias dentro de una jerarquía.
- **Contraste útil:** Contraste: Los metadatos describen propiedades como tipo, tamaño, marcas temporales, propietario o permisos.

### Trampas de examen

- **Incorrecto:** Un directorio contiene únicamente los bytes de todos sus archivos concatenados.
- **Incorrecto:** Borrar un archivo garantiza por sí solo la destrucción física inmediata de todos sus datos.

<!-- VISUAL PENDIENTE: t38-20-gestion-de-archivos-y-directorios.webp -->

:::hablemos-claro
El sistema operativo ofrece operaciones para crear, abrir, leer, escribir, renombrar y eliminar archivos.
:::

:::en-la-calle
Al observar cómo el sistema reparte CPU, memoria y dispositivos, El sistema operativo ofrece operaciones para crear, abrir, leer, escribir, renombrar y eliminar archivos.
:::

:::lo-que-cae
Prioriza **nombres, rutas y metadatos** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: POSIX-2024-T38 -->

## 21. Dispositivos, controladores y entrada/salida

### Lógica del bloque

Para dominar **dispositivos, controladores y entrada/salida**, aplica esta regla: Un controlador traduce operaciones del sistema a interacciones adecuadas con un dispositivo. El anclaje principal es **abstracción del dispositivo**.

### Hechos examinables

- Un controlador traduce operaciones del sistema a interacciones adecuadas con un dispositivo. <!-- FACT:PN-T38-F081 -->
- Las interrupciones permiten notificar eventos sin sondear continuamente todos los dispositivos. <!-- FACT:PN-T38-F082 -->
- El almacenamiento en búfer suaviza diferencias de velocidad entre productores y consumidores. <!-- FACT:PN-T38-F083 -->
- La cola de entrada/salida permite ordenar y combinar peticiones según la política del sistema. <!-- FACT:PN-T38-F084 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: Las interrupciones permiten notificar eventos sin sondear continuamente todos los dispositivos.
- **Contraste útil:** Contraste: El almacenamiento en búfer suaviza diferencias de velocidad entre productores y consumidores.

### Trampas de examen

- **Incorrecto:** Un controlador es siempre una pieza física conectada por USB.
- **Incorrecto:** Una interrupción obliga a reinstalar el sistema operativo.

<!-- VISUAL PENDIENTE: t38-21-dispositivos-controladores-y-entrada-salida.webp -->

:::hablemos-claro
Un controlador traduce operaciones del sistema a interacciones adecuadas con un dispositivo.
:::

:::en-la-calle
Al observar cómo el sistema reparte CPU, memoria y dispositivos, Un controlador traduce operaciones del sistema a interacciones adecuadas con un dispositivo.
:::

:::lo-que-cae
Prioriza **abstracción del dispositivo** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: MS-WINDOWS-INTERNALS-T38 -->

## 22. Interfaz de línea de comandos, shell y GUI

### Lógica del bloque

Para dominar **interfaz de línea de comandos, shell y gui**, aplica esta regla: Una interfaz de línea de comandos recibe instrucciones textuales. El anclaje principal es **dos formas de interacción**.

### Hechos examinables

- Una interfaz de línea de comandos recibe instrucciones textuales. <!-- FACT:PN-T38-F085 -->
- Una shell interpreta órdenes y puede combinar programas mediante redirecciones y tuberías. <!-- FACT:PN-T38-F086 -->
- Una interfaz gráfica utiliza ventanas, iconos, menús y otros controles visuales. <!-- FACT:PN-T38-F087 -->
- CLI y GUI pueden coexistir y utilizar los mismos servicios del sistema operativo. <!-- FACT:PN-T38-F088 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: Una shell interpreta órdenes y puede combinar programas mediante redirecciones y tuberías.
- **Contraste útil:** Contraste: Una interfaz gráfica utiliza ventanas, iconos, menús y otros controles visuales.

### Trampas de examen

- **Incorrecto:** Todo sistema con GUI carece de shell y terminal.
- **Incorrecto:** La shell es el núcleo físico del procesador.

<!-- VISUAL PENDIENTE: t38-il-22-interfaz-de-linea-de-comandos-shell-y-gui.webp -->

:::hablemos-claro
Una interfaz de línea de comandos recibe instrucciones textuales.
:::

:::en-la-calle
Al observar cómo el sistema reparte CPU, memoria y dispositivos, Una interfaz de línea de comandos recibe instrucciones textuales.
:::

:::lo-que-cae
Prioriza **dos formas de interacción** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: POSIX-2024-T38 -->

## 23. Usuarios, autenticación y autorización

### Lógica del bloque

Para dominar **usuarios, autenticación y autorización**, aplica esta regla: La autenticación comprueba una identidad declarada. El anclaje principal es **identidad antes que permiso**.

### Hechos examinables

- La autenticación comprueba una identidad declarada. <!-- FACT:PN-T38-F089 -->
- La autorización decide qué acciones puede realizar una identidad autenticada. <!-- FACT:PN-T38-F090 -->
- Las cuentas, grupos y roles permiten asignar privilegios sin concederlos de forma indiscriminada. <!-- FACT:PN-T38-F091 -->
- El principio de mínimo privilegio limita cada usuario o proceso a los permisos necesarios. <!-- FACT:PN-T38-F092 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: La autorización decide qué acciones puede realizar una identidad autenticada.
- **Contraste útil:** Contraste: Las cuentas, grupos y roles permiten asignar privilegios sin concederlos de forma indiscriminada.

### Trampas de examen

- **Incorrecto:** Autenticación y autorización son términos idénticos.
- **Incorrecto:** Mínimo privilegio significa conceder derechos administrativos a todas las aplicaciones.

<!-- VISUAL PENDIENTE: t38-23-usuarios-autenticacion-y-autorizacion.webp -->

:::hablemos-claro
La autenticación comprueba una identidad declarada.
:::

:::en-la-calle
Al observar cómo el sistema reparte CPU, memoria y dispositivos, La autenticación comprueba una identidad declarada.
:::

:::lo-que-cae
Prioriza **identidad antes que permiso** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: APPLE-PLATFORM-SECURITY-T38 -->

## 24. Protección, aislamiento y auditoría

### Lógica del bloque

Para dominar **protección, aislamiento y auditoría**, aplica esta regla: El aislamiento de procesos reduce accesos directos entre aplicaciones. El anclaje principal es **prevenir, contener y registrar**.

### Hechos examinables

- El aislamiento de procesos reduce accesos directos entre aplicaciones. <!-- FACT:PN-T38-F093 -->
- Los permisos y controles de acceso protegen objetos según identidad y política. <!-- FACT:PN-T38-F094 -->
- El registro de eventos permite reconstruir actividad, aunque no evita por sí solo un incidente. <!-- FACT:PN-T38-F095 -->
- Actualizaciones, firma de código, cifrado y copias de seguridad resuelven riesgos distintos y se complementan. <!-- FACT:PN-T38-F096 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: Los permisos y controles de acceso protegen objetos según identidad y política.
- **Contraste útil:** Contraste: El registro de eventos permite reconstruir actividad, aunque no evita por sí solo un incidente.

### Trampas de examen

- **Incorrecto:** Un registro de auditoría impide automáticamente todos los ataques.
- **Incorrecto:** Cifrar datos hace innecesarias las actualizaciones y las copias de seguridad.

<!-- VISUAL PENDIENTE: t38-24-proteccion-aislamiento-y-auditoria.webp -->

:::hablemos-claro
El aislamiento de procesos reduce accesos directos entre aplicaciones.
:::

:::en-la-calle
Al observar cómo el sistema reparte CPU, memoria y dispositivos, El aislamiento de procesos reduce accesos directos entre aplicaciones.
:::

:::lo-que-cae
Prioriza **prevenir, contener y registrar** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: APPLE-PLATFORM-SECURITY-T38 -->

## 25. Errores, excepciones y recuperación

### Lógica del bloque

Para dominar **errores, excepciones y recuperación**, aplica esta regla: El sistema operativo gestiona excepciones del procesador y errores comunicados por hardware o software. El anclaje principal es **fallar sin perder el control**.

### Hechos examinables

- El sistema operativo gestiona excepciones del procesador y errores comunicados por hardware o software. <!-- FACT:PN-T38-F097 -->
- Un fallo de una aplicación no debería comprometer por diseño todo el sistema. <!-- FACT:PN-T38-F098 -->
- La recuperación puede incluir reintentos, terminación controlada, reparación del sistema de archivos o restauración. <!-- FACT:PN-T38-F099 -->
- La tolerancia a fallos reduce impacto, pero no convierte ningún sistema en infalible. <!-- FACT:PN-T38-F100 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: Un fallo de una aplicación no debería comprometer por diseño todo el sistema.
- **Contraste útil:** Contraste: La recuperación puede incluir reintentos, terminación controlada, reparación del sistema de archivos o restauración.

### Trampas de examen

- **Incorrecto:** Toda excepción obliga a formatear el almacenamiento.
- **Incorrecto:** Tolerancia a fallos significa que no pueden producirse pérdidas.

<!-- VISUAL PENDIENTE: t38-25-errores-excepciones-y-recuperacion.webp -->

:::hablemos-claro
El sistema operativo gestiona excepciones del procesador y errores comunicados por hardware o software.
:::

:::en-la-calle
Al observar cómo el sistema reparte CPU, memoria y dispositivos, El sistema operativo gestiona excepciones del procesador y errores comunicados por hardware o software.
:::

:::lo-que-cae
Prioriza **fallar sin perder el control** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: LINUX-KERNEL-T38 -->

## 26. MS-DOS: naturaleza y contexto histórico

### Lógica del bloque

Para dominar **ms-dos: naturaleza y contexto histórico**, aplica esta regla: MS-DOS es una familia histórica de sistemas operativos de disco desarrollada para ordenadores personales compatibles. El anclaje principal es **DOS para ordenadores personales**.

### Hechos examinables

- MS-DOS es una familia histórica de sistemas operativos de disco desarrollada para ordenadores personales compatibles. <!-- FACT:PN-T38-F101 -->
- Su interacción característica es textual mediante un intérprete de comandos. <!-- FACT:PN-T38-F102 -->
- Las versiones clásicas fueron diseñadas para entornos de recursos muy limitados frente a sistemas actuales. <!-- FACT:PN-T38-F103 -->
- Estudiar MS-DOS sirve para comprender rutas, unidades, comandos y FAT, no para presentarlo como plataforma moderna segura. <!-- FACT:PN-T38-F104 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: Su interacción característica es textual mediante un intérprete de comandos.
- **Contraste útil:** Contraste: Las versiones clásicas fueron diseñadas para entornos de recursos muy limitados frente a sistemas actuales.

### Trampas de examen

- **Incorrecto:** MS-DOS es una distribución actual de Linux.
- **Incorrecto:** MS-DOS fue diseñado como sistema móvil táctil.

<!-- VISUAL PENDIENTE: t38-26-ms-dos-naturaleza-y-contexto-historico.webp -->

:::hablemos-claro
MS-DOS es una familia histórica de sistemas operativos de disco desarrollada para ordenadores personales compatibles.
:::

:::en-la-calle
Al trabajar en una consola histórica de MS-DOS, MS-DOS es una familia histórica de sistemas operativos de disco desarrollada para ordenadores personales compatibles.
:::

:::lo-que-cae
Prioriza **DOS para ordenadores personales** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: MS-DOS-SOURCE-T38 -->

## 27. Arquitectura y límites clásicos de MS-DOS

### Lógica del bloque

Para dominar **arquitectura y límites clásicos de ms-dos**, aplica esta regla: El MS-DOS clásico trabajaba sobre la arquitectura x86 en modo real de sus primeras generaciones. El anclaje principal es **entorno real y protección limitada**.

### Hechos examinables

- El MS-DOS clásico trabajaba sobre la arquitectura x86 en modo real de sus primeras generaciones. <!-- FACT:PN-T38-F105 -->
- Carecía del aislamiento y la protección de memoria propios de sistemas modernos. <!-- FACT:PN-T38-F106 -->
- Su modelo habitual era monousuario y de una tarea principal, aunque existieron técnicas y extensiones residentes. <!-- FACT:PN-T38-F107 -->
- Los programas accedían al sistema mediante servicios de DOS, BIOS y, en ciertos casos, acceso directo al hardware. <!-- FACT:PN-T38-F108 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: Carecía del aislamiento y la protección de memoria propios de sistemas modernos.
- **Contraste útil:** Contraste: Su modelo habitual era monousuario y de una tarea principal, aunque existieron técnicas y extensiones residentes.

### Trampas de examen

- **Incorrecto:** MS-DOS proporcionaba aislamiento de procesos equivalente al de un sistema moderno.
- **Incorrecto:** MS-DOS clásico exigía varios usuarios simultáneos con permisos POSIX.

<!-- VISUAL PENDIENTE: t38-27-arquitectura-y-limites-clasicos-de-ms-dos.webp -->

:::hablemos-claro
El MS-DOS clásico trabajaba sobre la arquitectura x86 en modo real de sus primeras generaciones.
:::

:::en-la-calle
Al trabajar en una consola histórica de MS-DOS, El MS-DOS clásico trabajaba sobre la arquitectura x86 en modo real de sus primeras generaciones.
:::

:::lo-que-cae
Prioriza **entorno real y protección limitada** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: MS-DOS-SOURCE-T38 -->

## 28. Intérprete y comandos de MS-DOS

### Lógica del bloque

Para dominar **intérprete y comandos de ms-dos**, aplica esta regla: COMMAND.COM actuaba como intérprete de comandos en versiones clásicas de MS-DOS. El anclaje principal es **COMMAND.COM y utilidades**.

### Hechos examinables

- COMMAND.COM actuaba como intérprete de comandos en versiones clásicas de MS-DOS. <!-- FACT:PN-T38-F109 -->
- Los comandos internos formaban parte del intérprete y los externos residían en archivos ejecutables separados. <!-- FACT:PN-T38-F110 -->
- DIR, CD, COPY, DEL y REN representan operaciones habituales sobre archivos y directorios. <!-- FACT:PN-T38-F111 -->
- La existencia histórica de un comando no garantiza idéntica sintaxis o comportamiento en la consola de Windows actual. <!-- FACT:PN-T38-F112 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: Los comandos internos formaban parte del intérprete y los externos residían en archivos ejecutables separados.
- **Contraste útil:** Contraste: DIR, CD, COPY, DEL y REN representan operaciones habituales sobre archivos y directorios.

### Trampas de examen

- **Incorrecto:** Todo comando de MS-DOS era un archivo externo independiente.
- **Incorrecto:** PowerShell y COMMAND.COM son el mismo intérprete.

<!-- VISUAL PENDIENTE: t38-28-interprete-y-comandos-de-ms-dos.webp -->

:::hablemos-claro
COMMAND.COM actuaba como intérprete de comandos en versiones clásicas de MS-DOS.
:::

:::en-la-calle
Al trabajar en una consola histórica de MS-DOS, COMMAND.COM actuaba como intérprete de comandos en versiones clásicas de MS-DOS.
:::

:::lo-que-cae
Prioriza **COMMAND.COM y utilidades** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: MS-DOS-SOURCE-T38 -->

## 29. Unidades, rutas y nombres en MS-DOS

### Lógica del bloque

Para dominar **unidades, rutas y nombres en ms-dos**, aplica esta regla: MS-DOS identifica habitualmente volúmenes mediante letras seguidas de dos puntos. El anclaje principal es **letra, dos puntos y barra inversa**.

### Hechos examinables

- MS-DOS identifica habitualmente volúmenes mediante letras seguidas de dos puntos. <!-- FACT:PN-T38-F113 -->
- La barra inversa separa componentes de ruta y la raíz se representa desde la unidad activa. <!-- FACT:PN-T38-F114 -->
- El directorio actual puede ser distinto en cada unidad según el entorno DOS. <!-- FACT:PN-T38-F115 -->
- Las primeras convenciones FAT usaron nombres cortos 8.3; las extensiones posteriores no deben proyectarse sin fecha sobre todas las versiones. <!-- FACT:PN-T38-F116 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: La barra inversa separa componentes de ruta y la raíz se representa desde la unidad activa.
- **Contraste útil:** Contraste: El directorio actual puede ser distinto en cada unidad según el entorno DOS.

### Trampas de examen

- **Incorrecto:** La barra inclinada es el único separador de rutas aceptado por el MS-DOS clásico.
- **Incorrecto:** El esquema 8.3 permite cualquier longitud de nombre sin extensión.

<!-- VISUAL PENDIENTE: t38-29-unidades-rutas-y-nombres-en-ms-dos.webp -->

:::hablemos-claro
MS-DOS identifica habitualmente volúmenes mediante letras seguidas de dos puntos.
:::

:::en-la-calle
Al trabajar en una consola histórica de MS-DOS, MS-DOS identifica habitualmente volúmenes mediante letras seguidas de dos puntos.
:::

:::lo-que-cae
Prioriza **letra, dos puntos y barra inversa** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: MS-DOS-SOURCE-T38 -->

## 30. MS-DOS, FAT y arranque

### Lógica del bloque

Para dominar **ms-dos, fat y arranque**, aplica esta regla: MS-DOS utilizó variantes de FAT para organizar archivos en volúmenes. El anclaje principal es **sistema de disco histórico**.

### Hechos examinables

- MS-DOS utilizó variantes de FAT para organizar archivos en volúmenes. <!-- FACT:PN-T38-F117 -->
- El sector de arranque y los archivos del sistema participaban en la carga de versiones clásicas. <!-- FACT:PN-T38-F118 -->
- La tabla FAT registra cadenas de clústeres y estado de asignación. <!-- FACT:PN-T38-F119 -->
- FAT aporta compatibilidad y sencillez, pero no ofrece el modelo de permisos y diario de NTFS o ext4. <!-- FACT:PN-T38-F120 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: El sector de arranque y los archivos del sistema participaban en la carga de versiones clásicas.
- **Contraste útil:** Contraste: La tabla FAT registra cadenas de clústeres y estado de asignación.

### Trampas de examen

- **Incorrecto:** FAT incorpora por diseño permisos ACL y diario transaccional equivalentes a NTFS.
- **Incorrecto:** El arranque de MS-DOS comienza ejecutando una aplicación gráfica de usuario.

<!-- VISUAL PENDIENTE: t38-il-30-ms-dos-fat-y-arranque.webp -->

:::hablemos-claro
MS-DOS utilizó variantes de FAT para organizar archivos en volúmenes.
:::

:::en-la-calle
Al trabajar en una consola histórica de MS-DOS, MS-DOS utilizó variantes de FAT para organizar archivos en volúmenes.
:::

:::lo-que-cae
Prioriza **sistema de disco histórico** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: MS-DOS-SOURCE-T38 -->

## 31. UNIX: origen y principios

### Lógica del bloque

Para dominar **unix: origen y principios**, aplica esta regla: UNIX nació como una familia de sistemas multiusuario y multitarea. El anclaje principal es **multiusuario, multitarea y composición**.

### Hechos examinables

- UNIX nació como una familia de sistemas multiusuario y multitarea. <!-- FACT:PN-T38-F121 -->
- Su diseño favorece herramientas pequeñas que pueden combinarse mediante interfaces comunes. <!-- FACT:PN-T38-F122 -->
- La jerarquía de archivos parte de una raíz única. <!-- FACT:PN-T38-F123 -->
- El término UNIX no debe usarse como sinónimo automático de cualquier sistema parecido a Unix. <!-- FACT:PN-T38-F124 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: Su diseño favorece herramientas pequeñas que pueden combinarse mediante interfaces comunes.
- **Contraste útil:** Contraste: La jerarquía de archivos parte de una raíz única.

### Trampas de examen

- **Incorrecto:** UNIX identifica cualquier sistema que tenga una terminal.
- **Incorrecto:** UNIX fue concebido como sistema monousuario sin procesos concurrentes.

<!-- VISUAL PENDIENTE: t38-31-unix-origen-y-principios.webp -->

:::hablemos-claro
UNIX nació como una familia de sistemas multiusuario y multitarea.
:::

:::en-la-calle
Al recorrer un sistema UNIX o compatible con POSIX, UNIX nació como una familia de sistemas multiusuario y multitarea.
:::

:::lo-que-cae
Prioriza **multiusuario, multitarea y composición** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: POSIX-2024-T38 -->

## 32. Núcleo, shell y utilidades UNIX

### Lógica del bloque

Para dominar **núcleo, shell y utilidades unix**, aplica esta regla: El núcleo gestiona procesos, memoria, dispositivos y sistemas de archivos. El anclaje principal es **tres niveles funcionales**.

### Hechos examinables

- El núcleo gestiona procesos, memoria, dispositivos y sistemas de archivos. <!-- FACT:PN-T38-F125 -->
- La shell interpreta el lenguaje de órdenes y lanza programas. <!-- FACT:PN-T38-F126 -->
- Las utilidades realizan tareas concretas y se coordinan mediante archivos, argumentos, tuberías y redirecciones. <!-- FACT:PN-T38-F127 -->
- La shell es un programa de usuario y no debe confundirse con el núcleo. <!-- FACT:PN-T38-F128 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: La shell interpreta el lenguaje de órdenes y lanza programas.
- **Contraste útil:** Contraste: Las utilidades realizan tareas concretas y se coordinan mediante archivos, argumentos, tuberías y redirecciones.

### Trampas de examen

- **Incorrecto:** El núcleo UNIX es la ventana del terminal que escribe el usuario.
- **Incorrecto:** Las utilidades solo pueden ejecutarse dentro del código del kernel.

<!-- VISUAL PENDIENTE: t38-32-nucleo-shell-y-utilidades-unix.webp -->

:::hablemos-claro
El núcleo gestiona procesos, memoria, dispositivos y sistemas de archivos.
:::

:::en-la-calle
Al recorrer un sistema UNIX o compatible con POSIX, El núcleo gestiona procesos, memoria, dispositivos y sistemas de archivos.
:::

:::lo-que-cae
Prioriza **tres niveles funcionales** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: POSIX-2024-T38 -->

## 33. Jerarquía, raíz y montaje en UNIX

### Lógica del bloque

Para dominar **jerarquía, raíz y montaje en unix**, aplica esta regla: La barra inclinada representa la raíz y separa componentes de una ruta POSIX. El anclaje principal es **un árbol de nombres**.

### Hechos examinables

- La barra inclinada representa la raíz y separa componentes de una ruta POSIX. <!-- FACT:PN-T38-F129 -->
- Una ruta absoluta parte de la raíz y una relativa se interpreta desde el directorio de trabajo. <!-- FACT:PN-T38-F130 -->
- Montar incorpora un sistema de archivos en un punto de la jerarquía. <!-- FACT:PN-T38-F131 -->
- Los dispositivos pueden exponerse mediante archivos especiales sin que dispositivo y archivo ordinario sean idénticos. <!-- FACT:PN-T38-F132 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: Una ruta absoluta parte de la raíz y una relativa se interpreta desde el directorio de trabajo.
- **Contraste útil:** Contraste: Montar incorpora un sistema de archivos en un punto de la jerarquía.

### Trampas de examen

- **Incorrecto:** Cada volumen UNIX necesita obligatoriamente una letra de unidad.
- **Incorrecto:** Montar un sistema de archivos copia todos sus datos al directorio de montaje.

<!-- VISUAL PENDIENTE: t38-33-jerarquia-raiz-y-montaje-en-unix.webp -->

:::hablemos-claro
La barra inclinada representa la raíz y separa componentes de una ruta POSIX.
:::

:::en-la-calle
Al recorrer un sistema UNIX o compatible con POSIX, La barra inclinada representa la raíz y separa componentes de una ruta POSIX.
:::

:::lo-que-cae
Prioriza **un árbol de nombres** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: POSIX-2024-T38 -->

## 34. Procesos UNIX: fork, exec y wait

### Lógica del bloque

Para dominar **procesos unix: fork, exec y wait**, aplica esta regla: fork crea un nuevo proceso a partir del contexto del proceso llamante. El anclaje principal es **crear, reemplazar y esperar**.

### Hechos examinables

- fork crea un nuevo proceso a partir del contexto del proceso llamante. <!-- FACT:PN-T38-F133 -->
- exec sustituye la imagen del proceso por un nuevo programa sin crear por sí solo otro proceso. <!-- FACT:PN-T38-F134 -->
- wait permite recoger el estado de terminación de procesos hijos. <!-- FACT:PN-T38-F135 -->
- La combinación fork y exec explica un patrón clásico de lanzamiento de programas en sistemas UNIX. <!-- FACT:PN-T38-F136 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: exec sustituye la imagen del proceso por un nuevo programa sin crear por sí solo otro proceso.
- **Contraste útil:** Contraste: wait permite recoger el estado de terminación de procesos hijos.

### Trampas de examen

- **Incorrecto:** exec duplica siempre el proceso y conserva ejecutándose el programa anterior.
- **Incorrecto:** wait convierte un proceso hijo en hilo del padre.

<!-- VISUAL PENDIENTE: t38-34-procesos-unix-fork-exec-y-wait.webp -->

:::hablemos-claro
fork crea un nuevo proceso a partir del contexto del proceso llamante.
:::

:::en-la-calle
Al recorrer un sistema UNIX o compatible con POSIX, fork crea un nuevo proceso a partir del contexto del proceso llamante.
:::

:::lo-que-cae
Prioriza **crear, reemplazar y esperar** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: POSIX-2024-T38 -->

## 35. Usuarios, grupos y permisos POSIX

### Lógica del bloque

Para dominar **usuarios, grupos y permisos posix**, aplica esta regla: Los permisos clásicos distinguen lectura, escritura y ejecución. El anclaje principal es **propietario, grupo y otros**.

### Hechos examinables

- Los permisos clásicos distinguen lectura, escritura y ejecución. <!-- FACT:PN-T38-F137 -->
- Las clases tradicionales son propietario, grupo y otros. <!-- FACT:PN-T38-F138 -->
- En un directorio, lectura, escritura y ejecución tienen efectos diferentes de los que tienen sobre un archivo ordinario. <!-- FACT:PN-T38-F139 -->
- El usuario con privilegios administrativos no elimina la necesidad de aplicar mínimo privilegio. <!-- FACT:PN-T38-F140 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: Las clases tradicionales son propietario, grupo y otros.
- **Contraste útil:** Contraste: En un directorio, lectura, escritura y ejecución tienen efectos diferentes de los que tienen sobre un archivo ordinario.

### Trampas de examen

- **Incorrecto:** El permiso de ejecución en un directorio significa reproducir su contenido multimedia.
- **Incorrecto:** Conceder lectura a un archivo concede automáticamente administración del sistema.

<!-- VISUAL PENDIENTE: t38-il-35-usuarios-grupos-y-permisos-posix.webp -->

:::hablemos-claro
Los permisos clásicos distinguen lectura, escritura y ejecución.
:::

:::en-la-calle
Al recorrer un sistema UNIX o compatible con POSIX, Los permisos clásicos distinguen lectura, escritura y ejecución.
:::

:::lo-que-cae
Prioriza **propietario, grupo y otros** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: POSIX-2024-T38 -->

## 36. Tuberías, redirecciones y descriptores

### Lógica del bloque

Para dominar **tuberías, redirecciones y descriptores**, aplica esta regla: La entrada estándar, la salida estándar y el error estándar son flujos diferenciados. El anclaje principal es **conectar flujos**.

### Hechos examinables

- La entrada estándar, la salida estándar y el error estándar son flujos diferenciados. <!-- FACT:PN-T38-F141 -->
- Una tubería conecta normalmente la salida de un proceso con la entrada de otro. <!-- FACT:PN-T38-F142 -->
- La redirección cambia el origen o destino de un flujo sin modificar necesariamente el programa. <!-- FACT:PN-T38-F143 -->
- Un descriptor de archivo es un identificador de proceso para un archivo abierto u otro objeto de entrada/salida. <!-- FACT:PN-T38-F144 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: Una tubería conecta normalmente la salida de un proceso con la entrada de otro.
- **Contraste útil:** Contraste: La redirección cambia el origen o destino de un flujo sin modificar necesariamente el programa.

### Trampas de examen

- **Incorrecto:** Una tubería guarda permanentemente todos los datos como copia de seguridad.
- **Incorrecto:** Entrada estándar y error estándar son siempre el mismo descriptor.

<!-- VISUAL PENDIENTE: t38-il-36-tuberias-redirecciones-y-descriptores.webp -->

:::hablemos-claro
La entrada estándar, la salida estándar y el error estándar son flujos diferenciados.
:::

:::en-la-calle
Al recorrer un sistema UNIX o compatible con POSIX, La entrada estándar, la salida estándar y el error estándar son flujos diferenciados.
:::

:::lo-que-cae
Prioriza **conectar flujos** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: POSIX-2024-T38 -->

## 37. POSIX, UNIX y sistemas tipo Unix

### Lógica del bloque

Para dominar **posix, unix y sistemas tipo unix**, aplica esta regla: POSIX define interfaces y comportamientos portables para sistemas compatibles. El anclaje principal es **estándar, marca y parentesco**.

### Hechos examinables

- POSIX define interfaces y comportamientos portables para sistemas compatibles. <!-- FACT:PN-T38-F145 -->
- UNIX es también una marca y una especificación de conformidad gestionada por The Open Group. <!-- FACT:PN-T38-F146 -->
- Un sistema tipo Unix puede compartir diseño e interfaces sin estar certificado como UNIX. <!-- FACT:PN-T38-F147 -->
- IBM AIX es un sistema operativo UNIX orientado principalmente a servidores y entornos empresariales. <!-- FACT:PN-T38-F148 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: UNIX es también una marca y una especificación de conformidad gestionada por The Open Group.
- **Contraste útil:** Contraste: Un sistema tipo Unix puede compartir diseño e interfaces sin estar certificado como UNIX.

### Trampas de examen

- **Incorrecto:** POSIX es un sistema operativo comercial concreto.
- **Incorrecto:** Todo sistema tipo Unix está certificado automáticamente con la marca UNIX.

<!-- VISUAL PENDIENTE: t38-37-posix-unix-y-sistemas-tipo-unix.webp -->

:::hablemos-claro
POSIX define interfaces y comportamientos portables para sistemas compatibles.
:::

:::en-la-calle
Al recorrer un sistema UNIX o compatible con POSIX, POSIX define interfaces y comportamientos portables para sistemas compatibles.
:::

:::lo-que-cae
Prioriza **estándar, marca y parentesco** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: POSIX-2024-T38 -->

## 38. Linux: núcleo y distribuciones

### Lógica del bloque

Para dominar **linux: núcleo y distribuciones**, aplica esta regla: Linux designa estrictamente el núcleo iniciado por el proyecto de Linus Torvalds. El anclaje principal es **kernel frente a sistema completo**.

### Hechos examinables

- Linux designa estrictamente el núcleo iniciado por el proyecto de Linus Torvalds. <!-- FACT:PN-T38-F149 -->
- Una distribución combina el núcleo con bibliotecas, herramientas, instalador, repositorios y políticas propias. <!-- FACT:PN-T38-F150 -->
- Distintas distribuciones pueden usar el mismo núcleo con componentes y ciclos de soporte diferentes. <!-- FACT:PN-T38-F151 -->
- GNU/Linux es una denominación usada cuando se destaca la combinación del núcleo Linux con herramientas GNU. <!-- FACT:PN-T38-F152 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: Una distribución combina el núcleo con bibliotecas, herramientas, instalador, repositorios y políticas propias.
- **Contraste útil:** Contraste: Distintas distribuciones pueden usar el mismo núcleo con componentes y ciclos de soporte diferentes.

### Trampas de examen

- **Incorrecto:** Linux es una única distribución con una sola interfaz y gestor de paquetes.
- **Incorrecto:** El núcleo Linux incluye necesariamente todas las aplicaciones de escritorio.

<!-- VISUAL PENDIENTE: t38-38-linux-nucleo-y-distribuciones.webp -->

:::hablemos-claro
Linux designa estrictamente el núcleo iniciado por el proyecto de Linus Torvalds.
:::

:::en-la-calle
Al administrar procesos y permisos en Linux, Linux designa estrictamente el núcleo iniciado por el proyecto de Linus Torvalds.
:::

:::lo-que-cae
Prioriza **kernel frente a sistema completo** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: LINUX-KERNEL-T38 -->

## 39. Arquitectura del núcleo Linux

### Lógica del bloque

Para dominar **arquitectura del núcleo linux**, aplica esta regla: Linux se describe habitualmente como un núcleo monolítico con capacidad modular. El anclaje principal es **núcleo monolítico modular**.

### Hechos examinables

- Linux se describe habitualmente como un núcleo monolítico con capacidad modular. <!-- FACT:PN-T38-F153 -->
- Servicios fundamentales como planificación, memoria y VFS se ejecutan en espacio de núcleo. <!-- FACT:PN-T38-F154 -->
- Los módulos permiten incorporar funcionalidad al núcleo sin recompilarlo íntegramente en muchos casos. <!-- FACT:PN-T38-F155 -->
- Monolítico no significa que todo el software del sistema se ejecute en modo núcleo. <!-- FACT:PN-T38-F156 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: Servicios fundamentales como planificación, memoria y VFS se ejecutan en espacio de núcleo.
- **Contraste útil:** Contraste: Los módulos permiten incorporar funcionalidad al núcleo sin recompilarlo íntegramente en muchos casos.

### Trampas de examen

- **Incorrecto:** Un núcleo monolítico impide cargar módulos.
- **Incorrecto:** Todas las aplicaciones Linux se ejecutan con privilegios de kernel.

<!-- VISUAL PENDIENTE: t38-39-arquitectura-del-nucleo-linux.webp -->

:::hablemos-claro
Linux se describe habitualmente como un núcleo monolítico con capacidad modular.
:::

:::en-la-calle
Al administrar procesos y permisos en Linux, Linux se describe habitualmente como un núcleo monolítico con capacidad modular.
:::

:::lo-que-cae
Prioriza **núcleo monolítico modular** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: LINUX-KERNEL-T38 -->

## 40. VFS y jerarquía Linux

### Lógica del bloque

Para dominar **vfs y jerarquía linux**, aplica esta regla: VFS proporciona una interfaz común para que coexistan distintos sistemas de archivos. El anclaje principal es **una interfaz para varios sistemas de archivos**.

### Hechos examinables

- VFS proporciona una interfaz común para que coexistan distintos sistemas de archivos. <!-- FACT:PN-T38-F157 -->
- La jerarquía Linux integra volúmenes y sistemas virtuales bajo una raíz. <!-- FACT:PN-T38-F158 -->
- Los inodos representan objetos y metadatos en sistemas que usan ese modelo. <!-- FACT:PN-T38-F159 -->
- Una entrada de directorio relaciona un nombre con un objeto; nombre e inodo no son la misma cosa. <!-- FACT:PN-T38-F160 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: La jerarquía Linux integra volúmenes y sistemas virtuales bajo una raíz.
- **Contraste útil:** Contraste: Los inodos representan objetos y metadatos en sistemas que usan ese modelo.

### Trampas de examen

- **Incorrecto:** VFS obliga a formatear todos los volúmenes como ext4.
- **Incorrecto:** El nombre de archivo se almacena siempre dentro del inodo como único identificador.

<!-- VISUAL PENDIENTE: t38-40-vfs-y-jerarquia-linux.webp -->

:::hablemos-claro
VFS proporciona una interfaz común para que coexistan distintos sistemas de archivos.
:::

:::en-la-calle
Al administrar procesos y permisos en Linux, VFS proporciona una interfaz común para que coexistan distintos sistemas de archivos.
:::

:::lo-que-cae
Prioriza **una interfaz para varios sistemas de archivos** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: LINUX-KERNEL-T38 -->

## 41. Procesos y pseudo-sistema /proc

### Lógica del bloque

Para dominar **procesos y pseudo-sistema /proc**, aplica esta regla: /proc expone información de procesos y estructuras internas mediante una interfaz de sistema de archivos. El anclaje principal es **vista dinámica del núcleo**.

### Hechos examinables

- /proc expone información de procesos y estructuras internas mediante una interfaz de sistema de archivos. <!-- FACT:PN-T38-F161 -->
- Muchas entradas de /proc se generan dinámicamente y no son archivos persistentes en disco. <!-- FACT:PN-T38-F162 -->
- Los identificadores numéricos de proceso aparecen como directorios bajo /proc cuando procede. <!-- FACT:PN-T38-F163 -->
- Modificar parámetros mediante interfaces de /proc o sysctl exige conocer permisos, alcance y riesgo. <!-- FACT:PN-T38-F164 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: Muchas entradas de /proc se generan dinámicamente y no son archivos persistentes en disco.
- **Contraste útil:** Contraste: Los identificadores numéricos de proceso aparecen como directorios bajo /proc cuando procede.

### Trampas de examen

- **Incorrecto:** Todo contenido de /proc se conserva en el disco después de apagar.
- **Incorrecto:** /proc es una carpeta ordinaria de documentos personales.

<!-- VISUAL PENDIENTE: t38-il-41-procesos-y-pseudo-sistema-proc.webp -->

:::hablemos-claro
/proc expone información de procesos y estructuras internas mediante una interfaz de sistema de archivos.
:::

:::en-la-calle
Al administrar procesos y permisos en Linux, /proc expone información de procesos y estructuras internas mediante una interfaz de sistema de archivos.
:::

:::lo-que-cae
Prioriza **vista dinámica del núcleo** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: LINUX-KERNEL-T38 -->

## 42. Propiedad, permisos y privilegios en Linux

### Lógica del bloque

Para dominar **propiedad, permisos y privilegios en linux**, aplica esta regla: Los procesos actúan con identidades y grupos que condicionan sus permisos. El anclaje principal es **UID, GID y capacidades**.

### Hechos examinables

- Los procesos actúan con identidades y grupos que condicionan sus permisos. <!-- FACT:PN-T38-F165 -->
- root es la cuenta administrativa tradicional, pero los sistemas pueden delegar privilegios de forma controlada. <!-- FACT:PN-T38-F166 -->
- sudo ejecuta una orden conforme a una política; no convierte toda la sesión en root necesariamente. <!-- FACT:PN-T38-F167 -->
- Las capacidades de Linux pueden dividir privilegios tradicionalmente concentrados en root. <!-- FACT:PN-T38-F168 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: root es la cuenta administrativa tradicional, pero los sistemas pueden delegar privilegios de forma controlada.
- **Contraste útil:** Contraste: sudo ejecuta una orden conforme a una política; no convierte toda la sesión en root necesariamente.

### Trampas de examen

- **Incorrecto:** sudo concede a cualquier usuario todos los privilegios sin política.
- **Incorrecto:** Las capacidades Linux son permisos rwx de un archivo ordinario.

<!-- VISUAL PENDIENTE: t38-42-propiedad-permisos-y-privilegios-en-linux.webp -->

:::hablemos-claro
Los procesos actúan con identidades y grupos que condicionan sus permisos.
:::

:::en-la-calle
Al administrar procesos y permisos en Linux, Los procesos actúan con identidades y grupos que condicionan sus permisos.
:::

:::lo-que-cae
Prioriza **UID, GID y capacidades** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: POSIX-2024-T38 -->

## 43. Servicios, demonios y arranque en Linux

### Lógica del bloque

Para dominar **servicios, demonios y arranque en linux**, aplica esta regla: Un demonio es un proceso que presta servicios en segundo plano. El anclaje principal es **procesos de larga duración**.

### Hechos examinables

- Un demonio es un proceso que presta servicios en segundo plano. <!-- FACT:PN-T38-F169 -->
- El sistema de inicio y gestor de servicios arranca, supervisa y detiene unidades según configuración. <!-- FACT:PN-T38-F170 -->
- systemd es común en muchas distribuciones, pero no define por sí solo a Linux. <!-- FACT:PN-T38-F171 -->
- El núcleo inicia el primer proceso de espacio de usuario conforme al sistema configurado. <!-- FACT:PN-T38-F172 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: El sistema de inicio y gestor de servicios arranca, supervisa y detiene unidades según configuración.
- **Contraste útil:** Contraste: systemd es común en muchas distribuciones, pero no define por sí solo a Linux.

### Trampas de examen

- **Incorrecto:** Todo sistema Linux utiliza obligatoriamente systemd.
- **Incorrecto:** Un demonio es malware por definición.

<!-- VISUAL PENDIENTE: t38-43-servicios-demonios-y-arranque-en-linux.webp -->

:::hablemos-claro
Un demonio es un proceso que presta servicios en segundo plano.
:::

:::en-la-calle
Al administrar procesos y permisos en Linux, Un demonio es un proceso que presta servicios en segundo plano.
:::

:::lo-que-cae
Prioriza **procesos de larga duración** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: LINUX-KERNEL-T38 -->

## 44. Software libre, código abierto y licencias

### Lógica del bloque

Para dominar **software libre, código abierto y licencias**, aplica esta regla: El código del núcleo Linux se distribuye principalmente bajo GPLv2. El anclaje principal es **libertades y condiciones jurídicas**.

### Hechos examinables

- El código del núcleo Linux se distribuye principalmente bajo GPLv2. <!-- FACT:PN-T38-F173 -->
- Código abierto describe disponibilidad del código bajo una licencia, no ausencia de derechos de autor. <!-- FACT:PN-T38-F174 -->
- Software libre se refiere a libertades de uso, estudio, modificación y redistribución conforme a la licencia. <!-- FACT:PN-T38-F175 -->
- Gratuidad, código abierto y software libre son conceptos relacionados, pero no equivalentes. <!-- FACT:PN-T38-F176 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: Código abierto describe disponibilidad del código bajo una licencia, no ausencia de derechos de autor.
- **Contraste útil:** Contraste: Software libre se refiere a libertades de uso, estudio, modificación y redistribución conforme a la licencia.

### Trampas de examen

- **Incorrecto:** Código abierto significa que no existe licencia ni autor.
- **Incorrecto:** Todo software gratuito permite modificar y redistribuir su código.

<!-- VISUAL PENDIENTE: t38-44-software-libre-codigo-abierto-y-licencias.webp -->

:::hablemos-claro
El código del núcleo Linux se distribuye principalmente bajo GPLv2.
:::

:::en-la-calle
Al administrar procesos y permisos en Linux, El código del núcleo Linux se distribuye principalmente bajo GPLv2.
:::

:::lo-que-cae
Prioriza **libertades y condiciones jurídicas** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: LINUX-KERNEL-T38 -->

## 45. Windows y la familia Windows NT

### Lógica del bloque

Para dominar **windows y la familia windows nt**, aplica esta regla: Las versiones modernas de escritorio y servidor de Windows pertenecen a la familia Windows NT. El anclaje principal es **arquitectura NT moderna**.

### Hechos examinables

- Las versiones modernas de escritorio y servidor de Windows pertenecen a la familia Windows NT. <!-- FACT:PN-T38-F177 -->
- Windows separa componentes de modo usuario y modo núcleo. <!-- FACT:PN-T38-F178 -->
- El ejecutivo y el núcleo cooperan con controladores y la capa de abstracción de hardware. <!-- FACT:PN-T38-F179 -->
- La compatibilidad con aplicaciones históricas no convierte Windows actual en MS-DOS. <!-- FACT:PN-T38-F180 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: Windows separa componentes de modo usuario y modo núcleo.
- **Contraste útil:** Contraste: El ejecutivo y el núcleo cooperan con controladores y la capa de abstracción de hardware.

### Trampas de examen

- **Incorrecto:** Windows actual se ejecuta como una interfaz gráfica sobre MS-DOS.
- **Incorrecto:** La familia Windows NT carece de separación entre usuario y núcleo.

<!-- VISUAL PENDIENTE: t38-45-windows-y-la-familia-windows-nt.webp -->

:::hablemos-claro
Las versiones modernas de escritorio y servidor de Windows pertenecen a la familia Windows NT.
:::

:::en-la-calle
Al usar Explorer, servicios o seguridad en Windows, Las versiones modernas de escritorio y servidor de Windows pertenecen a la familia Windows NT.
:::

:::lo-que-cae
Prioriza **arquitectura NT moderna** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: MS-WINDOWS-INTERNALS-T38 -->

## 46. Procesos, hilos y servicios en Windows

### Lógica del bloque

Para dominar **procesos, hilos y servicios en windows**, aplica esta regla: Windows planifica hilos dentro del contexto de procesos. El anclaje principal es **objetos ejecutables y servicios**.

### Hechos examinables

- Windows planifica hilos dentro del contexto de procesos. <!-- FACT:PN-T38-F181 -->
- Un servicio es un programa administrado por el Service Control Manager y puede ejecutarse sin sesión interactiva. <!-- FACT:PN-T38-F182 -->
- El Administrador de tareas permite observar aplicaciones, procesos y consumo, pero no sustituye al planificador. <!-- FACT:PN-T38-F183 -->
- Finalizar un proceso puede perder trabajo o afectar servicios dependientes. <!-- FACT:PN-T38-F184 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: Un servicio es un programa administrado por el Service Control Manager y puede ejecutarse sin sesión interactiva.
- **Contraste útil:** Contraste: El Administrador de tareas permite observar aplicaciones, procesos y consumo, pero no sustituye al planificador.

### Trampas de examen

- **Incorrecto:** El Administrador de tareas asigna manualmente cada instrucción a la CPU.
- **Incorrecto:** Todo servicio necesita una ventana abierta y un usuario escribiendo.

<!-- VISUAL PENDIENTE: t38-46-procesos-hilos-y-servicios-en-windows.webp -->

:::hablemos-claro
Windows planifica hilos dentro del contexto de procesos.
:::

:::en-la-calle
Al usar Explorer, servicios o seguridad en Windows, Windows planifica hilos dentro del contexto de procesos.
:::

:::lo-que-cae
Prioriza **objetos ejecutables y servicios** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: MS-WINDOWS-INTERNALS-T38 -->

## 47. Registro de Windows

### Lógica del bloque

Para dominar **registro de windows**, aplica esta regla: El Registro almacena configuración estructurada del sistema, usuarios y aplicaciones. El anclaje principal es **base jerárquica de configuración**.

### Hechos examinables

- El Registro almacena configuración estructurada del sistema, usuarios y aplicaciones. <!-- FACT:PN-T38-F185 -->
- Claves y valores forman una jerarquía lógica distinta de la jerarquía ordinaria de archivos. <!-- FACT:PN-T38-F186 -->
- Editar el Registro puede afectar al funcionamiento y requiere copia o procedimiento de recuperación adecuado. <!-- FACT:PN-T38-F187 -->
- No toda configuración de Windows vive en el Registro: también existen archivos, bases y servicios de configuración. <!-- FACT:PN-T38-F188 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: Claves y valores forman una jerarquía lógica distinta de la jerarquía ordinaria de archivos.
- **Contraste útil:** Contraste: Editar el Registro puede afectar al funcionamiento y requiere copia o procedimiento de recuperación adecuado.

### Trampas de examen

- **Incorrecto:** El Registro es una carpeta NTFS que solo contiene documentos de texto.
- **Incorrecto:** Todas las preferencias de cualquier aplicación se almacenan obligatoriamente en el Registro.

<!-- VISUAL PENDIENTE: t38-il-47-registro-de-windows.webp -->

:::hablemos-claro
El Registro almacena configuración estructurada del sistema, usuarios y aplicaciones.
:::

:::en-la-calle
Al usar Explorer, servicios o seguridad en Windows, El Registro almacena configuración estructurada del sistema, usuarios y aplicaciones.
:::

:::lo-que-cae
Prioriza **base jerárquica de configuración** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: MS-WINDOWS-INTERNALS-T38 -->

## 48. Explorer, CMD y PowerShell

### Lógica del bloque

Para dominar **explorer, cmd y powershell**, aplica esta regla: El Explorador de archivos es una interfaz gráfica para navegar y gestionar objetos del sistema de archivos. El anclaje principal es **interfaces distintas**.

### Hechos examinables

- El Explorador de archivos es una interfaz gráfica para navegar y gestionar objetos del sistema de archivos. <!-- FACT:PN-T38-F189 -->
- CMD interpreta el lenguaje de comandos tradicional de Windows. <!-- FACT:PN-T38-F190 -->
- PowerShell trabaja con comandos y objetos y no es una simple copia de COMMAND.COM. <!-- FACT:PN-T38-F191 -->
- Las tres interfaces pueden realizar operaciones semejantes mediante modelos y sintaxis diferentes. <!-- FACT:PN-T38-F192 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: CMD interpreta el lenguaje de comandos tradicional de Windows.
- **Contraste útil:** Contraste: PowerShell trabaja con comandos y objetos y no es una simple copia de COMMAND.COM.

### Trampas de examen

- **Incorrecto:** PowerShell es el nombre moderno de MS-DOS.
- **Incorrecto:** El Explorador de archivos es el núcleo de Windows.

<!-- VISUAL PENDIENTE: t38-il-48-explorer-cmd-y-powershell.webp -->

:::hablemos-claro
El Explorador de archivos es una interfaz gráfica para navegar y gestionar objetos del sistema de archivos.
:::

:::en-la-calle
Al usar Explorer, servicios o seguridad en Windows, El Explorador de archivos es una interfaz gráfica para navegar y gestionar objetos del sistema de archivos.
:::

:::lo-que-cae
Prioriza **interfaces distintas** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: MS-WINDOWS-INTERNALS-T38 -->

## 49. Cuentas, UAC y controles de acceso

### Lógica del bloque

Para dominar **cuentas, uac y controles de acceso**, aplica esta regla: Windows asocia procesos a tokens que recogen identidad, grupos y privilegios. El anclaje principal es **elevación controlada**.

### Hechos examinables

- Windows asocia procesos a tokens que recogen identidad, grupos y privilegios. <!-- FACT:PN-T38-F193 -->
- Las ACL especifican qué identidades pueden realizar determinadas operaciones sobre un objeto. <!-- FACT:PN-T38-F194 -->
- UAC ayuda a separar el uso ordinario de las operaciones que requieren elevación. <!-- FACT:PN-T38-F195 -->
- Aceptar una elevación no concede permisos permanentes e ilimitados a todos los procesos. <!-- FACT:PN-T38-F196 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: Las ACL especifican qué identidades pueden realizar determinadas operaciones sobre un objeto.
- **Contraste útil:** Contraste: UAC ayuda a separar el uso ordinario de las operaciones que requieren elevación.

### Trampas de examen

- **Incorrecto:** UAC es un antivirus que analiza cada archivo.
- **Incorrecto:** Una ACL solo indica el tamaño máximo de un volumen.

<!-- VISUAL PENDIENTE: t38-49-cuentas-uac-y-controles-de-acceso.webp -->

:::hablemos-claro
Windows asocia procesos a tokens que recogen identidad, grupos y privilegios.
:::

:::en-la-calle
Al usar Explorer, servicios o seguridad en Windows, Windows asocia procesos a tokens que recogen identidad, grupos y privilegios.
:::

:::lo-que-cae
Prioriza **elevación controlada** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: MS-WINDOWS-INTERNALS-T38 -->

## 50. Unidades, rutas y atributos en Windows

### Lógica del bloque

Para dominar **unidades, rutas y atributos en windows**, aplica esta regla: Windows representa habitualmente volúmenes mediante letras, aunque también admite puntos de montaje en carpetas. El anclaje principal es **letras y barras inversas**.

### Hechos examinables

- Windows representa habitualmente volúmenes mediante letras, aunque también admite puntos de montaje en carpetas. <!-- FACT:PN-T38-F197 -->
- La barra inversa separa componentes en rutas Win32 habituales. <!-- FACT:PN-T38-F198 -->
- Oculto, sistema y solo lectura son atributos; no equivalen por sí solos a permisos de acceso. <!-- FACT:PN-T38-F199 -->
- Mostrar archivos ocultos es una opción de visualización y no elimina automáticamente sus restricciones de acceso. <!-- FACT:PN-T38-F200 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: La barra inversa separa componentes en rutas Win32 habituales.
- **Contraste útil:** Contraste: Oculto, sistema y solo lectura son atributos; no equivalen por sí solos a permisos de acceso.

### Trampas de examen

- **Incorrecto:** Un archivo oculto no puede ser mostrado por ninguna configuración de usuario.
- **Incorrecto:** El atributo solo lectura concede permisos de administrador.

<!-- VISUAL PENDIENTE: t38-50-unidades-rutas-y-atributos-en-windows.webp -->

:::hablemos-claro
Windows representa habitualmente volúmenes mediante letras, aunque también admite puntos de montaje en carpetas.
:::

:::en-la-calle
Al usar Explorer, servicios o seguridad en Windows, Windows representa habitualmente volúmenes mediante letras, aunque también admite puntos de montaje en carpetas.
:::

:::lo-que-cae
Prioriza **letras y barras inversas** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: MS-NTFS-T38 -->

## 51. Actualización, cifrado y recuperación en Windows

### Lógica del bloque

Para dominar **actualización, cifrado y recuperación en windows**, aplica esta regla: Windows Update distribuye correcciones y cambios, pero exige gestión de reinicios y compatibilidad. El anclaje principal es **defensas complementarias**.

### Hechos examinables

- Windows Update distribuye correcciones y cambios, pero exige gestión de reinicios y compatibilidad. <!-- FACT:PN-T38-F201 -->
- BitLocker cifra volúmenes y protege datos en reposo conforme a su configuración. <!-- FACT:PN-T38-F202 -->
- EFS cifra archivos compatibles en NTFS y no es lo mismo que cifrar todo el volumen. <!-- FACT:PN-T38-F203 -->
- Los puntos de restauración, copias de seguridad y recuperación de archivos cubren supuestos diferentes. <!-- FACT:PN-T38-F204 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: BitLocker cifra volúmenes y protege datos en reposo conforme a su configuración.
- **Contraste útil:** Contraste: EFS cifra archivos compatibles en NTFS y no es lo mismo que cifrar todo el volumen.

### Trampas de examen

- **Incorrecto:** BitLocker sustituye las copias de seguridad frente a borrado accidental.
- **Incorrecto:** EFS y BitLocker son nombres distintos para una función idéntica en todo contexto.

<!-- VISUAL PENDIENTE: t38-51-actualizacion-cifrado-y-recuperacion-en-windows.webp -->

:::hablemos-claro
Windows Update distribuye correcciones y cambios, pero exige gestión de reinicios y compatibilidad.
:::

:::en-la-calle
Al usar Explorer, servicios o seguridad en Windows, Windows Update distribuye correcciones y cambios, pero exige gestión de reinicios y compatibilidad.
:::

:::lo-que-cae
Prioriza **defensas complementarias** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: MS-NTFS-T38 -->

## 52. macOS, Darwin y XNU

### Lógica del bloque

Para dominar **macos, darwin y xnu**, aplica esta regla: macOS es el sistema operativo de escritorio de Apple y se apoya en Darwin. El anclaje principal es **capas del sistema Apple**.

### Hechos examinables

- macOS es el sistema operativo de escritorio de Apple y se apoya en Darwin. <!-- FACT:PN-T38-F205 -->
- XNU es el núcleo utilizado por macOS y combina componentes Mach con elementos BSD y controladores I/O Kit. <!-- FACT:PN-T38-F206 -->
- macOS ofrece interfaces UNIX y una interfaz gráfica propia. <!-- FACT:PN-T38-F207 -->
- Compartir componentes con iOS no convierte ambos sistemas en productos idénticos. <!-- FACT:PN-T38-F208 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: XNU es el núcleo utilizado por macOS y combina componentes Mach con elementos BSD y controladores I/O Kit.
- **Contraste útil:** Contraste: macOS ofrece interfaces UNIX y una interfaz gráfica propia.

### Trampas de examen

- **Incorrecto:** macOS utiliza el núcleo de Windows NT.
- **Incorrecto:** macOS e iOS son exactamente el mismo sistema con distinto fondo de pantalla.

<!-- VISUAL PENDIENTE: t38-52-macos-darwin-y-xnu.webp -->

:::hablemos-claro
macOS es el sistema operativo de escritorio de Apple y se apoya en Darwin.
:::

:::en-la-calle
Al gestionar aplicaciones y volúmenes en macOS, macOS es el sistema operativo de escritorio de Apple y se apoya en Darwin.
:::

:::lo-que-cae
Prioriza **capas del sistema Apple** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: APPLE-PLATFORM-SECURITY-T38 -->

## 53. Aqua, Finder y Terminal

### Lógica del bloque

Para dominar **aqua, finder y terminal**, aplica esta regla: Aqua designa el entorno gráfico característico de macOS. El anclaje principal es **GUI y línea de comandos**.

### Hechos examinables

- Aqua designa el entorno gráfico característico de macOS. <!-- FACT:PN-T38-F209 -->
- Finder permite navegar y gestionar archivos, aplicaciones y volúmenes. <!-- FACT:PN-T38-F210 -->
- Terminal proporciona acceso a una shell y utilidades de línea de comandos. <!-- FACT:PN-T38-F211 -->
- Usar Finder o Terminal no cambia por sí solo los permisos efectivos del usuario. <!-- FACT:PN-T38-F212 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: Finder permite navegar y gestionar archivos, aplicaciones y volúmenes.
- **Contraste útil:** Contraste: Terminal proporciona acceso a una shell y utilidades de línea de comandos.

### Trampas de examen

- **Incorrecto:** Finder es el núcleo XNU.
- **Incorrecto:** Abrir Terminal concede automáticamente privilegios administrativos.

<!-- VISUAL PENDIENTE: t38-il-53-aqua-finder-y-terminal.webp -->

:::hablemos-claro
Aqua designa el entorno gráfico característico de macOS.
:::

:::en-la-calle
Al gestionar aplicaciones y volúmenes en macOS, Aqua designa el entorno gráfico característico de macOS.
:::

:::lo-que-cae
Prioriza **GUI y línea de comandos** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: APPLE-PLATFORM-SECURITY-T38 -->

## 54. Aplicaciones, paquetes y sandbox en macOS

### Lógica del bloque

Para dominar **aplicaciones, paquetes y sandbox en macos**, aplica esta regla: Una aplicación macOS puede presentarse como un paquete que Finder muestra como una unidad lógica. El anclaje principal es **aplicación como paquete**.

### Hechos examinables

- Una aplicación macOS puede presentarse como un paquete que Finder muestra como una unidad lógica. <!-- FACT:PN-T38-F213 -->
- El paquete contiene ejecutables y recursos organizados conforme a convenciones de la plataforma. <!-- FACT:PN-T38-F214 -->
- El sandbox restringe recursos accesibles a una aplicación según sus permisos y entitlements. <!-- FACT:PN-T38-F215 -->
- La firma de código aporta autenticidad e integridad, pero no demuestra que una aplicación sea segura en cualquier circunstancia. <!-- FACT:PN-T38-F216 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: El paquete contiene ejecutables y recursos organizados conforme a convenciones de la plataforma.
- **Contraste útil:** Contraste: El sandbox restringe recursos accesibles a una aplicación según sus permisos y entitlements.

### Trampas de examen

- **Incorrecto:** Un paquete de aplicación es un único byte indivisible.
- **Incorrecto:** Una firma válida garantiza la ausencia absoluta de vulnerabilidades.

<!-- VISUAL PENDIENTE: t38-54-aplicaciones-paquetes-y-sandbox-en-macos.webp -->

:::hablemos-claro
Una aplicación macOS puede presentarse como un paquete que Finder muestra como una unidad lógica.
:::

:::en-la-calle
Al gestionar aplicaciones y volúmenes en macOS, Una aplicación macOS puede presentarse como un paquete que Finder muestra como una unidad lógica.
:::

:::lo-que-cae
Prioriza **aplicación como paquete** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: APPLE-PLATFORM-SECURITY-T38 -->

## 55. APFS en macOS

### Lógica del bloque

Para dominar **apfs en macos**, aplica esta regla: APFS es el sistema de archivos predeterminado en macOS moderno y en otras plataformas Apple. El anclaje principal es **copy-on-write y contenedores**.

### Hechos examinables

- APFS es el sistema de archivos predeterminado en macOS moderno y en otras plataformas Apple. <!-- FACT:PN-T38-F217 -->
- APFS fue diseñado con especial atención a almacenamiento Flash y SSD. <!-- FACT:PN-T38-F218 -->
- Sus contenedores permiten compartir espacio entre varios volúmenes. <!-- FACT:PN-T38-F219 -->
- Copy-on-write, clonación y snapshots son funciones distintas aunque relacionadas. <!-- FACT:PN-T38-F220 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: APFS fue diseñado con especial atención a almacenamiento Flash y SSD.
- **Contraste útil:** Contraste: Sus contenedores permiten compartir espacio entre varios volúmenes.

### Trampas de examen

- **Incorrecto:** APFS reserva obligatoriamente una partición física fija e incomunicada para cada volumen.
- **Incorrecto:** Clonar un archivo en APFS siempre copia inmediatamente todos sus bloques.

<!-- VISUAL PENDIENTE: t38-55-apfs-en-macos.webp -->

:::hablemos-claro
APFS es el sistema de archivos predeterminado en macOS moderno y en otras plataformas Apple.
:::

:::en-la-calle
Al gestionar aplicaciones y volúmenes en macOS, APFS es el sistema de archivos predeterminado en macOS moderno y en otras plataformas Apple.
:::

:::lo-que-cae
Prioriza **copy-on-write y contenedores** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: APPLE-APFS-T38 -->

## 56. Rutas, volúmenes y sensibilidad a mayúsculas

### Lógica del bloque

Para dominar **rutas, volúmenes y sensibilidad a mayúsculas**, aplica esta regla: macOS usa una jerarquía de rutas con barra inclinada y una raíz única. El anclaje principal es **nombre lógico y configuración**.

### Hechos examinables

- macOS usa una jerarquía de rutas con barra inclinada y una raíz única. <!-- FACT:PN-T38-F221 -->
- Los volúmenes se montan dentro de esa jerarquía y Finder puede presentarlos con nombres amigables. <!-- FACT:PN-T38-F222 -->
- APFS admite variantes sensibles y no sensibles a mayúsculas según el formato elegido. <!-- FACT:PN-T38-F223 -->
- No debe suponerse una misma sensibilidad a mayúsculas para todos los volúmenes macOS. <!-- FACT:PN-T38-F224 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: Los volúmenes se montan dentro de esa jerarquía y Finder puede presentarlos con nombres amigables.
- **Contraste útil:** Contraste: APFS admite variantes sensibles y no sensibles a mayúsculas según el formato elegido.

### Trampas de examen

- **Incorrecto:** Todo volumen macOS se identifica exclusivamente por una letra.
- **Incorrecto:** APFS obliga siempre a distinguir archivo de Archivo en cualquier instalación.

<!-- VISUAL PENDIENTE: t38-56-rutas-volumenes-y-sensibilidad-a-mayusculas.webp -->

:::hablemos-claro
macOS usa una jerarquía de rutas con barra inclinada y una raíz única.
:::

:::en-la-calle
Al gestionar aplicaciones y volúmenes en macOS, macOS usa una jerarquía de rutas con barra inclinada y una raíz única.
:::

:::lo-que-cae
Prioriza **nombre lógico y configuración** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: APPLE-APFS-T38 -->

## 57. FileVault y volumen de sistema firmado

### Lógica del bloque

Para dominar **filevault y volumen de sistema firmado**, aplica esta regla: FileVault protege datos en reposo mediante cifrado de volumen conforme a la plataforma. El anclaje principal es **confidencialidad frente a integridad**.

### Hechos examinables

- FileVault protege datos en reposo mediante cifrado de volumen conforme a la plataforma. <!-- FACT:PN-T38-F225 -->
- El volumen de sistema firmado protege la integridad del contenido del sistema mediante una cadena verificable. <!-- FACT:PN-T38-F226 -->
- Cifrado e integridad responden a amenazas diferentes. <!-- FACT:PN-T38-F227 -->
- Perder una clave o credencial de recuperación puede impedir acceder a datos cifrados. <!-- FACT:PN-T38-F228 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: El volumen de sistema firmado protege la integridad del contenido del sistema mediante una cadena verificable.
- **Contraste útil:** Contraste: Cifrado e integridad responden a amenazas diferentes.

### Trampas de examen

- **Incorrecto:** El volumen de sistema firmado cifra automáticamente todos los documentos del usuario.
- **Incorrecto:** FileVault permite recuperar datos sin clave ni credencial bajo cualquier circunstancia.

<!-- VISUAL PENDIENTE: t38-57-filevault-y-volumen-de-sistema-firmado.webp -->

:::hablemos-claro
FileVault protege datos en reposo mediante cifrado de volumen conforme a la plataforma.
:::

:::en-la-calle
Al gestionar aplicaciones y volúmenes en macOS, FileVault protege datos en reposo mediante cifrado de volumen conforme a la plataforma.
:::

:::lo-que-cae
Prioriza **confidencialidad frente a integridad** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: APPLE-PLATFORM-SECURITY-T38 -->

## 58. Rasgos de los sistemas operativos móviles

### Lógica del bloque

Para dominar **rasgos de los sistemas operativos móviles**, aplica esta regla: Un sistema móvil gestiona recursos limitados, batería, conectividad radio, sensores y ciclo de vida de aplicaciones. El anclaje principal es **energía, radio, sensores y aplicaciones**.

### Hechos examinables

- Un sistema móvil gestiona recursos limitados, batería, conectividad radio, sensores y ciclo de vida de aplicaciones. <!-- FACT:PN-T38-F229 -->
- La interfaz táctil es habitual, pero no define por sí sola la arquitectura del sistema. <!-- FACT:PN-T38-F230 -->
- Las aplicaciones se aíslan y reciben permisos conforme al modelo de la plataforma. <!-- FACT:PN-T38-F231 -->
- Suspender o terminar procesos en segundo plano permite gestionar energía y memoria. <!-- FACT:PN-T38-F232 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: La interfaz táctil es habitual, pero no define por sí sola la arquitectura del sistema.
- **Contraste útil:** Contraste: Las aplicaciones se aíslan y reciben permisos conforme al modelo de la plataforma.

### Trampas de examen

- **Incorrecto:** Un sistema móvil mantiene todas las aplicaciones ejecutándose sin límites.
- **Incorrecto:** La presencia de pantalla táctil convierte cualquier firmware en Android o iOS.

<!-- VISUAL PENDIENTE: t38-58-rasgos-de-los-sistemas-operativos-moviles.webp -->

:::hablemos-claro
Un sistema móvil gestiona recursos limitados, batería, conectividad radio, sensores y ciclo de vida de aplicaciones.
:::

:::en-la-calle
Al comparar aislamiento y almacenamiento en iOS y Android, Un sistema móvil gestiona recursos limitados, batería, conectividad radio, sensores y ciclo de vida de aplicaciones.
:::

:::lo-que-cae
Prioriza **energía, radio, sensores y aplicaciones** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: ANDROID-ARCH-T38 -->

## 59. iOS: arquitectura y ecosistema

### Lógica del bloque

Para dominar **ios: arquitectura y ecosistema**, aplica esta regla: iOS es el sistema operativo de Apple para iPhone. El anclaje principal es **plataforma móvil Apple**.

### Hechos examinables

- iOS es el sistema operativo de Apple para iPhone. <!-- FACT:PN-T38-F233 -->
- Comparte bases tecnológicas con otras plataformas Apple, incluido XNU y APFS. <!-- FACT:PN-T38-F234 -->
- El sistema integra frameworks de alto nivel sobre servicios y núcleo protegidos. <!-- FACT:PN-T38-F235 -->
- El ecosistema controla instalación, firma y ejecución de aplicaciones mediante políticas de plataforma. <!-- FACT:PN-T38-F236 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: Comparte bases tecnológicas con otras plataformas Apple, incluido XNU y APFS.
- **Contraste útil:** Contraste: El sistema integra frameworks de alto nivel sobre servicios y núcleo protegidos.

### Trampas de examen

- **Incorrecto:** iOS está basado en el núcleo Windows NT.
- **Incorrecto:** iOS permite ejecutar cualquier binario sin firma ni política.

<!-- VISUAL PENDIENTE: t38-59-ios-arquitectura-y-ecosistema.webp -->

:::hablemos-claro
iOS es el sistema operativo de Apple para iPhone.
:::

:::en-la-calle
Al comparar aislamiento y almacenamiento en iOS y Android, iOS es el sistema operativo de Apple para iPhone.
:::

:::lo-que-cae
Prioriza **plataforma móvil Apple** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: APPLE-PLATFORM-SECURITY-T38 -->

## 60. Sandbox, entitlements y permisos en iOS

### Lógica del bloque

Para dominar **sandbox, entitlements y permisos en ios**, aplica esta regla: Las aplicaciones de terceros se ejecutan en sandbox con un contenedor propio. El anclaje principal es **acceso explícitamente mediado**.

### Hechos examinables

- Las aplicaciones de terceros se ejecutan en sandbox con un contenedor propio. <!-- FACT:PN-T38-F237 -->
- Los entitlements declaran capacidades autorizadas para un binario firmado. <!-- FACT:PN-T38-F238 -->
- El acceso a datos sensibles se media mediante servicios y permisos del sistema. <!-- FACT:PN-T38-F239 -->
- Conceder un permiso concreto no elimina el resto de límites del sandbox. <!-- FACT:PN-T38-F240 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: Los entitlements declaran capacidades autorizadas para un binario firmado.
- **Contraste útil:** Contraste: El acceso a datos sensibles se media mediante servicios y permisos del sistema.

### Trampas de examen

- **Incorrecto:** Un entitlement es una contraseña escrita por el usuario.
- **Incorrecto:** Permitir acceso a la cámara concede acceso irrestricto a todos los archivos del sistema.

<!-- VISUAL PENDIENTE: t38-60-sandbox-entitlements-y-permisos-en-ios.webp -->

:::hablemos-claro
Las aplicaciones de terceros se ejecutan en sandbox con un contenedor propio.
:::

:::en-la-calle
Al comparar aislamiento y almacenamiento en iOS y Android, Las aplicaciones de terceros se ejecutan en sandbox con un contenedor propio.
:::

:::lo-que-cae
Prioriza **acceso explícitamente mediado** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: APPLE-PLATFORM-SECURITY-T38 -->

## 61. iOS, APFS y Data Protection

### Lógica del bloque

Para dominar **ios, apfs y data protection**, aplica esta regla: iOS utiliza APFS y mecanismos de Data Protection para proteger datos. El anclaje principal es **claves por archivo y clases**.

### Hechos examinables

- iOS utiliza APFS y mecanismos de Data Protection para proteger datos. <!-- FACT:PN-T38-F241 -->
- Los archivos pueden asociarse a clases que condicionan cuándo son accesibles. <!-- FACT:PN-T38-F242 -->
- Las claves por archivo o extensión se integran con la jerarquía criptográfica del dispositivo. <!-- FACT:PN-T38-F243 -->
- El estado bloqueado del dispositivo y la disponibilidad de credenciales influyen en el acceso según la clase. <!-- FACT:PN-T38-F244 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: Los archivos pueden asociarse a clases que condicionan cuándo son accesibles.
- **Contraste útil:** Contraste: Las claves por archivo o extensión se integran con la jerarquía criptográfica del dispositivo.

### Trampas de examen

- **Incorrecto:** Todos los archivos iOS usan una única clave pública sin relación con el bloqueo.
- **Incorrecto:** APFS impide asignar políticas de protección diferentes a los archivos.

<!-- VISUAL PENDIENTE: t38-61-ios-apfs-y-data-protection.webp -->

:::hablemos-claro
iOS utiliza APFS y mecanismos de Data Protection para proteger datos.
:::

:::en-la-calle
Al comparar aislamiento y almacenamiento en iOS y Android, iOS utiliza APFS y mecanismos de Data Protection para proteger datos.
:::

:::lo-que-cae
Prioriza **claves por archivo y clases** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: APPLE-PLATFORM-SECURITY-T38 -->

## 62. Android: capas de arquitectura

### Lógica del bloque

Para dominar **android: capas de arquitectura**, aplica esta regla: Android se apoya en un kernel Linux adaptado a las necesidades de la plataforma. El anclaje principal es **kernel, HAL, runtime y framework**.

### Hechos examinables

- Android se apoya en un kernel Linux adaptado a las necesidades de la plataforma. <!-- FACT:PN-T38-F245 -->
- La HAL ofrece interfaces normalizadas entre componentes superiores e implementaciones de hardware. <!-- FACT:PN-T38-F246 -->
- El runtime y las bibliotecas nativas prestan servicios de ejecución y funciones básicas. <!-- FACT:PN-T38-F247 -->
- El framework de aplicaciones expone servicios de alto nivel a las aplicaciones. <!-- FACT:PN-T38-F248 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: La HAL ofrece interfaces normalizadas entre componentes superiores e implementaciones de hardware.
- **Contraste útil:** Contraste: El runtime y las bibliotecas nativas prestan servicios de ejecución y funciones básicas.

### Trampas de examen

- **Incorrecto:** Android es una distribución de escritorio idéntica a cualquier GNU/Linux.
- **Incorrecto:** La HAL sustituye completamente al kernel Linux.

<!-- VISUAL PENDIENTE: t38-62-android-capas-de-arquitectura.webp -->

:::hablemos-claro
Android se apoya en un kernel Linux adaptado a las necesidades de la plataforma.
:::

:::en-la-calle
Al comparar aislamiento y almacenamiento en iOS y Android, Android se apoya en un kernel Linux adaptado a las necesidades de la plataforma.
:::

:::lo-que-cae
Prioriza **kernel, HAL, runtime y framework** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: ANDROID-ARCH-T38 -->

## 63. Android Runtime y Binder

### Lógica del bloque

Para dominar **android runtime y binder**, aplica esta regla: Android Runtime ejecuta código de aplicaciones y gestiona aspectos de su entorno. El anclaje principal es **ejecución e IPC**.

### Hechos examinables

- Android Runtime ejecuta código de aplicaciones y gestiona aspectos de su entorno. <!-- FACT:PN-T38-F249 -->
- Binder es el mecanismo principal de comunicación entre procesos en Android. <!-- FACT:PN-T38-F250 -->
- Los servicios del sistema exponen operaciones a procesos clientes mediante interfaces controladas. <!-- FACT:PN-T38-F251 -->
- IPC no significa que todas las aplicaciones compartan el mismo proceso o memoria. <!-- FACT:PN-T38-F252 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: Binder es el mecanismo principal de comunicación entre procesos en Android.
- **Contraste útil:** Contraste: Los servicios del sistema exponen operaciones a procesos clientes mediante interfaces controladas.

### Trampas de examen

- **Incorrecto:** Binder es un sistema de archivos para tarjetas SD.
- **Incorrecto:** Todas las aplicaciones Android se ejecutan dentro de un único proceso común.

<!-- VISUAL PENDIENTE: t38-63-android-runtime-y-binder.webp -->

:::hablemos-claro
Android Runtime ejecuta código de aplicaciones y gestiona aspectos de su entorno.
:::

:::en-la-calle
Al comparar aislamiento y almacenamiento en iOS y Android, Android Runtime ejecuta código de aplicaciones y gestiona aspectos de su entorno.
:::

:::lo-que-cae
Prioriza **ejecución e IPC** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: ANDROID-ARCH-T38 -->

## 64. Aislamiento y permisos en Android

### Lógica del bloque

Para dominar **aislamiento y permisos en android**, aplica esta regla: Android asigna identidades y aislamientos a las aplicaciones para separar sus datos y procesos. El anclaje principal es **UID y sandbox por aplicación**.

### Hechos examinables

- Android asigna identidades y aislamientos a las aplicaciones para separar sus datos y procesos. <!-- FACT:PN-T38-F253 -->
- Los permisos controlan el acceso a funciones o datos protegidos. <!-- FACT:PN-T38-F254 -->
- SELinux refuerza el control de acceso obligatorio en la plataforma. <!-- FACT:PN-T38-F255 -->
- Instalar una aplicación no concede necesariamente todos los permisos sensibles solicitados. <!-- FACT:PN-T38-F256 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: Los permisos controlan el acceso a funciones o datos protegidos.
- **Contraste útil:** Contraste: SELinux refuerza el control de acceso obligatorio en la plataforma.

### Trampas de examen

- **Incorrecto:** Todas las aplicaciones Android comparten UID y directorio privado.
- **Incorrecto:** SELinux es una tienda de aplicaciones.

<!-- VISUAL PENDIENTE: t38-64-aislamiento-y-permisos-en-android.webp -->

:::hablemos-claro
Android asigna identidades y aislamientos a las aplicaciones para separar sus datos y procesos.
:::

:::en-la-calle
Al comparar aislamiento y almacenamiento en iOS y Android, Android asigna identidades y aislamientos a las aplicaciones para separar sus datos y procesos.
:::

:::lo-que-cae
Prioriza **UID y sandbox por aplicación** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: ANDROID-ARCH-T38 -->

## 65. Almacenamiento y cifrado en Android

### Lógica del bloque

Para dominar **almacenamiento y cifrado en android**, aplica esta regla: El cifrado basado en archivos permite proteger archivos con claves que pueden desbloquearse de forma independiente. El anclaje principal es **datos de dispositivo y de credencial**.

### Hechos examinables

- El cifrado basado en archivos permite proteger archivos con claves que pueden desbloquearse de forma independiente. <!-- FACT:PN-T38-F257 -->
- Direct Boot distingue almacenamiento disponible antes y después de desbloquear credenciales. <!-- FACT:PN-T38-F258 -->
- El almacenamiento interno privado de una aplicación no equivale al almacenamiento compartido. <!-- FACT:PN-T38-F259 -->
- El acceso al almacenamiento compartido está condicionado por versión, permisos y políticas como scoped storage. <!-- FACT:PN-T38-F260 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: Direct Boot distingue almacenamiento disponible antes y después de desbloquear credenciales.
- **Contraste útil:** Contraste: El almacenamiento interno privado de una aplicación no equivale al almacenamiento compartido.

### Trampas de examen

- **Incorrecto:** Direct Boot deja descifrados todos los datos privados antes de autenticarse.
- **Incorrecto:** Almacenamiento compartido significa que cualquier aplicación puede leerlo todo sin control.

<!-- VISUAL PENDIENTE: t38-65-almacenamiento-y-cifrado-en-android.webp -->

:::hablemos-claro
El cifrado basado en archivos permite proteger archivos con claves que pueden desbloquearse de forma independiente.
:::

:::en-la-calle
Al comparar aislamiento y almacenamiento en iOS y Android, El cifrado basado en archivos permite proteger archivos con claves que pueden desbloquearse de forma independiente.
:::

:::lo-que-cae
Prioriza **datos de dispositivo y de credencial** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: ANDROID-STORAGE-T38 -->

## 66. Comparación entre iOS y Android

### Lógica del bloque

Para dominar **comparación entre ios y android**, aplica esta regla: iOS y Android gestionan aplicaciones, memoria, dispositivos, energía, permisos y almacenamiento. El anclaje principal es **mismos fines, arquitecturas distintas**.

### Hechos examinables

- iOS y Android gestionan aplicaciones, memoria, dispositivos, energía, permisos y almacenamiento. <!-- FACT:PN-T38-F261 -->
- iOS utiliza tecnologías Apple como XNU y APFS; Android utiliza un kernel Linux y la arquitectura AOSP. <!-- FACT:PN-T38-F262 -->
- Ambos aíslan aplicaciones, aunque sus mecanismos, distribución y políticas no son idénticos. <!-- FACT:PN-T38-F263 -->
- Las diferencias de versión y fabricante impiden convertir una observación concreta en regla universal de Android. <!-- FACT:PN-T38-F264 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: iOS utiliza tecnologías Apple como XNU y APFS; Android utiliza un kernel Linux y la arquitectura AOSP.
- **Contraste útil:** Contraste: Ambos aíslan aplicaciones, aunque sus mecanismos, distribución y políticas no son idénticos.

### Trampas de examen

- **Incorrecto:** iOS y Android comparten el mismo núcleo y sistema de archivos por definición.
- **Incorrecto:** Todos los dispositivos Android ejecutan exactamente la misma versión sin modificaciones.

<!-- VISUAL PENDIENTE: t38-il-66-comparacion-entre-ios-y-android.webp -->

:::hablemos-claro
iOS y Android gestionan aplicaciones, memoria, dispositivos, energía, permisos y almacenamiento.
:::

:::en-la-calle
Al comparar aislamiento y almacenamiento en iOS y Android, iOS y Android gestionan aplicaciones, memoria, dispositivos, energía, permisos y almacenamiento.
:::

:::lo-que-cae
Prioriza **mismos fines, arquitecturas distintas** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: APPLE-PLATFORM-SECURITY-T38 -->

## 67. Memoria y almacenamiento: clasificación

### Lógica del bloque

Para dominar **memoria y almacenamiento: clasificación**, aplica esta regla: La memoria de trabajo y el almacenamiento persistente cumplen funciones diferentes. El anclaje principal es **volátil frente a no volátil**.

### Hechos examinables

- La memoria de trabajo y el almacenamiento persistente cumplen funciones diferentes. <!-- FACT:PN-T38-F265 -->
- Un medio volátil pierde normalmente su contenido al faltar alimentación; uno no volátil lo conserva. <!-- FACT:PN-T38-F266 -->
- Almacenamiento local, extraíble y remoto describen ubicación o conexión, no un único tipo físico. <!-- FACT:PN-T38-F267 -->
- Capacidad, latencia, rendimiento, durabilidad, coste y disponibilidad son compromisos distintos. <!-- FACT:PN-T38-F268 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: Un medio volátil pierde normalmente su contenido al faltar alimentación; uno no volátil lo conserva.
- **Contraste útil:** Contraste: Almacenamiento local, extraíble y remoto describen ubicación o conexión, no un único tipo físico.

### Trampas de examen

- **Incorrecto:** Toda memoria es persistente y todo almacenamiento es volátil.
- **Incorrecto:** El dispositivo con más capacidad es necesariamente el más rápido y fiable.

<!-- VISUAL PENDIENTE: t38-67-memoria-y-almacenamiento-clasificacion.webp -->

:::hablemos-claro
La memoria de trabajo y el almacenamiento persistente cumplen funciones diferentes.
:::

:::en-la-calle
Al elegir un medio, interfaz o esquema de particiones, La memoria de trabajo y el almacenamiento persistente cumplen funciones diferentes.
:::

:::lo-que-cae
Prioriza **volátil frente a no volátil** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: NVME-SPEC-T38 -->

## 68. Discos magnéticos HDD

### Lógica del bloque

Para dominar **discos magnéticos hdd**, aplica esta regla: Un HDD almacena datos mediante dominios magnéticos en platos giratorios. El anclaje principal es **platos y cabezales**.

### Hechos examinables

- Un HDD almacena datos mediante dominios magnéticos en platos giratorios. <!-- FACT:PN-T38-F269 -->
- El posicionamiento mecánico introduce latencia de búsqueda y rotación. <!-- FACT:PN-T38-F270 -->
- El acceso secuencial suele resultar menos costoso que muchos accesos aleatorios dispersos. <!-- FACT:PN-T38-F271 -->
- Golpes, vibración y desgaste mecánico son riesgos relevantes, aunque no los únicos. <!-- FACT:PN-T38-F272 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: El posicionamiento mecánico introduce latencia de búsqueda y rotación.
- **Contraste útil:** Contraste: El acceso secuencial suele resultar menos costoso que muchos accesos aleatorios dispersos.

### Trampas de examen

- **Incorrecto:** Un HDD carece de partes móviles y usa exclusivamente memoria NAND.
- **Incorrecto:** Desfragmentar un HDD elimina la necesidad de copias de seguridad.

<!-- VISUAL PENDIENTE: t38-il-68-discos-magneticos-hdd.webp -->

:::hablemos-claro
Un HDD almacena datos mediante dominios magnéticos en platos giratorios.
:::

:::en-la-calle
Al elegir un medio, interfaz o esquema de particiones, Un HDD almacena datos mediante dominios magnéticos en platos giratorios.
:::

:::lo-que-cae
Prioriza **platos y cabezales** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: MS-STORAGE-T38 -->

## 69. Unidades de estado sólido SSD

### Lógica del bloque

Para dominar **unidades de estado sólido ssd**, aplica esta regla: Un SSD almacena datos normalmente en memoria flash no volátil y carece de platos y cabezales. El anclaje principal es **memoria flash y controlador**.

### Hechos examinables

- Un SSD almacena datos normalmente en memoria flash no volátil y carece de platos y cabezales. <!-- FACT:PN-T38-F273 -->
- El controlador gestiona traducción de direcciones, corrección de errores y distribución de escrituras. <!-- FACT:PN-T38-F274 -->
- La amplificación de escritura y el desgaste condicionan la vida útil de la flash. <!-- FACT:PN-T38-F275 -->
- TRIM permite al sistema informar de bloques que ya no contienen datos útiles, si toda la cadena lo admite. <!-- FACT:PN-T38-F276 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: El controlador gestiona traducción de direcciones, corrección de errores y distribución de escrituras.
- **Contraste útil:** Contraste: La amplificación de escritura y el desgaste condicionan la vida útil de la flash.

### Trampas de examen

- **Incorrecto:** Un SSD no puede fallar porque no tiene piezas mecánicas.
- **Incorrecto:** TRIM sobrescribe de forma certificada todo archivo eliminado.

<!-- VISUAL PENDIENTE: t38-69-unidades-de-estado-solido-ssd.webp -->

:::hablemos-claro
Un SSD almacena datos normalmente en memoria flash no volátil y carece de platos y cabezales.
:::

:::en-la-calle
Al elegir un medio, interfaz o esquema de particiones, Un SSD almacena datos normalmente en memoria flash no volátil y carece de platos y cabezales.
:::

:::lo-que-cae
Prioriza **memoria flash y controlador** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: NVME-SPEC-T38 -->

## 70. SATA, NVMe y factores de forma

### Lógica del bloque

Para dominar **sata, nvme y factores de forma**, aplica esta regla: SATA es una interfaz y protocolo de almacenamiento usado por HDD y SSD. El anclaje principal es **protocolo no es forma física**.

### Hechos examinables

- SATA es una interfaz y protocolo de almacenamiento usado por HDD y SSD. <!-- FACT:PN-T38-F277 -->
- NVMe define comunicación del host con almacenamiento no volátil mediante transportes compatibles. <!-- FACT:PN-T38-F278 -->
- M.2 describe un factor de forma y conector; una unidad M.2 puede usar protocolos diferentes. <!-- FACT:PN-T38-F279 -->
- Un SSD no es automáticamente NVMe y una unidad NVMe no se define únicamente por su forma física. <!-- FACT:PN-T38-F280 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: NVMe define comunicación del host con almacenamiento no volátil mediante transportes compatibles.
- **Contraste útil:** Contraste: M.2 describe un factor de forma y conector; una unidad M.2 puede usar protocolos diferentes.

### Trampas de examen

- **Incorrecto:** M.2 y NVMe son términos rigurosamente sinónimos.
- **Incorrecto:** SATA solo puede conectar discos magnéticos.

<!-- VISUAL PENDIENTE: t38-70-sata-nvme-y-factores-de-forma.webp -->

:::hablemos-claro
SATA es una interfaz y protocolo de almacenamiento usado por HDD y SSD.
:::

:::en-la-calle
Al elegir un medio, interfaz o esquema de particiones, SATA es una interfaz y protocolo de almacenamiento usado por HDD y SSD.
:::

:::lo-que-cae
Prioriza **protocolo no es forma física** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: NVME-SPEC-T38 -->

## 71. Medios ópticos y extraíbles

### Lógica del bloque

Para dominar **medios ópticos y extraíbles**, aplica esta regla: CD, DVD y Blu-ray almacenan información mediante estructuras ópticas leídas por una unidad compatible. El anclaje principal es **soporte y unidad separados**.

### Hechos examinables

- CD, DVD y Blu-ray almacenan información mediante estructuras ópticas leídas por una unidad compatible. <!-- FACT:PN-T38-F281 -->
- Los formatos pueden ser de solo lectura, grabables una vez o regrabables. <!-- FACT:PN-T38-F282 -->
- Una memoria USB integra almacenamiento flash y un controlador mediante una interfaz USB. <!-- FACT:PN-T38-F283 -->
- Extraíble no significa inmune a corrupción, pérdida física o malware. <!-- FACT:PN-T38-F284 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: Los formatos pueden ser de solo lectura, grabables una vez o regrabables.
- **Contraste útil:** Contraste: Una memoria USB integra almacenamiento flash y un controlador mediante una interfaz USB.

### Trampas de examen

- **Incorrecto:** Todo disco óptico es regrabable ilimitadamente.
- **Incorrecto:** Una memoria USB es segura por el hecho de poder retirarse.

<!-- VISUAL PENDIENTE: t38-71-medios-opticos-y-extraibles.webp -->

:::hablemos-claro
CD, DVD y Blu-ray almacenan información mediante estructuras ópticas leídas por una unidad compatible.
:::

:::en-la-calle
Al elegir un medio, interfaz o esquema de particiones, CD, DVD y Blu-ray almacenan información mediante estructuras ópticas leídas por una unidad compatible.
:::

:::lo-que-cae
Prioriza **soporte y unidad separados** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: MS-STORAGE-T38 -->

## 72. Sectores, bloques y clústeres

### Lógica del bloque

Para dominar **sectores, bloques y clústeres**, aplica esta regla: Un sector es una unidad direccionable del dispositivo o de su interfaz lógica. El anclaje principal es **unidades de capas distintas**.

### Hechos examinables

- Un sector es una unidad direccionable del dispositivo o de su interfaz lógica. <!-- FACT:PN-T38-F285 -->
- Un bloque es una unidad utilizada por capas del sistema o del sistema de archivos. <!-- FACT:PN-T38-F286 -->
- Un clúster o unidad de asignación agrupa sectores para asignar espacio a archivos en determinados sistemas. <!-- FACT:PN-T38-F287 -->
- Sector, bloque, página y clúster no deben usarse como sinónimos universales. <!-- FACT:PN-T38-F288 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: Un bloque es una unidad utilizada por capas del sistema o del sistema de archivos.
- **Contraste útil:** Contraste: Un clúster o unidad de asignación agrupa sectores para asignar espacio a archivos en determinados sistemas.

### Trampas de examen

- **Incorrecto:** Un clúster es siempre un ordenador conectado a una red.
- **Incorrecto:** Sector, bloque y página tienen tamaño idéntico en cualquier sistema.

<!-- VISUAL PENDIENTE: t38-72-sectores-bloques-y-clusteres.webp -->

:::hablemos-claro
Un sector es una unidad direccionable del dispositivo o de su interfaz lógica.
:::

:::en-la-calle
Al elegir un medio, interfaz o esquema de particiones, Un sector es una unidad direccionable del dispositivo o de su interfaz lógica.
:::

:::lo-que-cae
Prioriza **unidades de capas distintas** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: LINUX-EXT4-T38 -->

## 73. Particiones, volúmenes, MBR y GPT

### Lógica del bloque

Para dominar **particiones, volúmenes, mbr y gpt**, aplica esta regla: Una partición divide lógicamente el espacio de un dispositivo conforme a una tabla. El anclaje principal es **estructura física y lógica**.

### Hechos examinables

- Una partición divide lógicamente el espacio de un dispositivo conforme a una tabla. <!-- FACT:PN-T38-F289 -->
- Un volumen es una unidad lógica que el sistema puede formatear y montar, y no siempre coincide uno a uno con una partición. <!-- FACT:PN-T38-F290 -->
- MBR es un esquema histórico con limitaciones de tamaño y número de particiones primarias. <!-- FACT:PN-T38-F291 -->
- GPT usa identificadores GUID, admite más particiones y se asocia habitualmente con UEFI. <!-- FACT:PN-T38-F292 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: Un volumen es una unidad lógica que el sistema puede formatear y montar, y no siempre coincide uno a uno con una partición.
- **Contraste útil:** Contraste: MBR es un esquema histórico con limitaciones de tamaño y número de particiones primarias.

### Trampas de examen

- **Incorrecto:** GPT limita todos los discos a cuatro particiones primarias.
- **Incorrecto:** Partición, volumen y sistema de archivos son exactamente la misma capa.

<!-- VISUAL PENDIENTE: t38-73-particiones-volumenes-mbr-y-gpt.webp -->

:::hablemos-claro
Una partición divide lógicamente el espacio de un dispositivo conforme a una tabla.
:::

:::en-la-calle
Al elegir un medio, interfaz o esquema de particiones, Una partición divide lógicamente el espacio de un dispositivo conforme a una tabla.
:::

:::lo-que-cae
Prioriza **estructura física y lógica** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: MS-STORAGE-T38 -->

## 74. RAID, redundancia y copia de seguridad

### Lógica del bloque

Para dominar **raid, redundancia y copia de seguridad**, aplica esta regla: RAID combina unidades para obtener rendimiento, capacidad o redundancia según el nivel. El anclaje principal es **rendimiento o continuidad no son backup**.

### Hechos examinables

- RAID combina unidades para obtener rendimiento, capacidad o redundancia según el nivel. <!-- FACT:PN-T38-F293 -->
- RAID 0 distribuye datos sin redundancia y aumenta el impacto del fallo de una unidad. <!-- FACT:PN-T38-F294 -->
- RAID 1 mantiene copias espejo y sacrifica capacidad útil. <!-- FACT:PN-T38-F295 -->
- RAID no sustituye una copia de seguridad independiente frente a borrado, corrupción o ataque. <!-- FACT:PN-T38-F296 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: RAID 0 distribuye datos sin redundancia y aumenta el impacto del fallo de una unidad.
- **Contraste útil:** Contraste: RAID 1 mantiene copias espejo y sacrifica capacidad útil.

### Trampas de examen

- **Incorrecto:** RAID 0 conserva una copia completa en cada disco.
- **Incorrecto:** Un espejo protege automáticamente frente a borrar por error un archivo.

<!-- VISUAL PENDIENTE: t38-il-74-raid-redundancia-y-copia-de-seguridad.webp -->

:::hablemos-claro
RAID combina unidades para obtener rendimiento, capacidad o redundancia según el nivel.
:::

:::en-la-calle
Al elegir un medio, interfaz o esquema de particiones, RAID combina unidades para obtener rendimiento, capacidad o redundancia según el nivel.
:::

:::lo-que-cae
Prioriza **rendimiento o continuidad no son backup** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: MS-STORAGE-T38 -->

## 75. Concepto y funciones del sistema de archivos

### Lógica del bloque

Para dominar **concepto y funciones del sistema de archivos**, aplica esta regla: Un sistema de archivos define cómo se organizan, nombran y localizan datos y metadatos en un soporte o espacio lógico. El anclaje principal es **nombres, espacio y metadatos**.

### Hechos examinables

- Un sistema de archivos define cómo se organizan, nombran y localizan datos y metadatos en un soporte o espacio lógico. <!-- FACT:PN-T38-F297 -->
- Gestiona asignación de espacio, directorios y operaciones sobre archivos. <!-- FACT:PN-T38-F298 -->
- Puede incorporar permisos, diario, compresión, cifrado, cuotas o instantáneas según su diseño. <!-- FACT:PN-T38-F299 -->
- El sistema de archivos no es el dispositivo físico ni la tabla de particiones. <!-- FACT:PN-T38-F300 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: Gestiona asignación de espacio, directorios y operaciones sobre archivos.
- **Contraste útil:** Contraste: Puede incorporar permisos, diario, compresión, cifrado, cuotas o instantáneas según su diseño.

### Trampas de examen

- **Incorrecto:** Formatear cambia físicamente un HDD en SSD.
- **Incorrecto:** La tabla GPT es un sistema de archivos que almacena documentos.

<!-- VISUAL PENDIENTE: t38-75-concepto-y-funciones-del-sistema-de-archivos.webp -->

:::hablemos-claro
Un sistema de archivos define cómo se organizan, nombran y localizan datos y metadatos en un soporte o espacio lógico.
:::

:::en-la-calle
Al formatear, montar o proteger un volumen, Un sistema de archivos define cómo se organizan, nombran y localizan datos y metadatos en un soporte o espacio lógico.
:::

:::lo-que-cae
Prioriza **nombres, espacio y metadatos** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: LINUX-KERNEL-T38 -->

## 76. Archivos, directorios y metadatos

### Lógica del bloque

Para dominar **archivos, directorios y metadatos**, aplica esta regla: El contenido de un archivo se distingue de los metadatos que lo describen. El anclaje principal es **contenido separado de descripción**.

### Hechos examinables

- El contenido de un archivo se distingue de los metadatos que lo describen. <!-- FACT:PN-T38-F301 -->
- Un directorio asocia nombres con objetos del sistema de archivos. <!-- FACT:PN-T38-F302 -->
- Las marcas temporales pueden registrar distintos eventos y su significado depende del sistema. <!-- FACT:PN-T38-F303 -->
- Extensión, tipo real y aplicación asociada son conceptos relacionados, pero no idénticos. <!-- FACT:PN-T38-F304 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: Un directorio asocia nombres con objetos del sistema de archivos.
- **Contraste útil:** Contraste: Las marcas temporales pueden registrar distintos eventos y su significado depende del sistema.

### Trampas de examen

- **Incorrecto:** Cambiar la extensión transforma siempre el contenido al nuevo formato.
- **Incorrecto:** Un directorio es solo una etiqueta visual sin estructura almacenada.

<!-- VISUAL PENDIENTE: t38-76-archivos-directorios-y-metadatos.webp -->

:::hablemos-claro
El contenido de un archivo se distingue de los metadatos que lo describen.
:::

:::en-la-calle
Al formatear, montar o proteger un volumen, El contenido de un archivo se distingue de los metadatos que lo describen.
:::

:::lo-que-cae
Prioriza **contenido separado de descripción** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: LINUX-KERNEL-T38 -->

## 77. Rutas absolutas, relativas y resolución de nombres

### Lógica del bloque

Para dominar **rutas absolutas, relativas y resolución de nombres**, aplica esta regla: Una ruta absoluta se resuelve desde una raíz o designador completo del sistema. El anclaje principal es **punto de partida**.

### Hechos examinables

- Una ruta absoluta se resuelve desde una raíz o designador completo del sistema. <!-- FACT:PN-T38-F305 -->
- Una ruta relativa se interpreta desde el directorio de trabajo u otro contexto definido. <!-- FACT:PN-T38-F306 -->
- Los componentes especiales punto y doble punto representan respectivamente el directorio actual y su padre en entornos compatibles. <!-- FACT:PN-T38-F307 -->
- Los separadores, nombres reservados y sensibilidad a mayúsculas dependen del sistema y de su configuración. <!-- FACT:PN-T38-F308 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: Una ruta relativa se interpreta desde el directorio de trabajo u otro contexto definido.
- **Contraste útil:** Contraste: Los componentes especiales punto y doble punto representan respectivamente el directorio actual y su padre en entornos compatibles.

### Trampas de examen

- **Incorrecto:** Toda ruta relativa empieza obligatoriamente en la raíz.
- **Incorrecto:** Windows, POSIX y macOS aplican siempre idénticas reglas de nombres.

<!-- VISUAL PENDIENTE: t38-77-rutas-absolutas-relativas-y-resolucion-de-nombres.webp -->

:::hablemos-claro
Una ruta absoluta se resuelve desde una raíz o designador completo del sistema.
:::

:::en-la-calle
Al formatear, montar o proteger un volumen, Una ruta absoluta se resuelve desde una raíz o designador completo del sistema.
:::

:::lo-que-cae
Prioriza **punto de partida** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: POSIX-2024-T38 -->

## 78. Asignación de espacio y fragmentación interna

### Lógica del bloque

Para dominar **asignación de espacio y fragmentación interna**, aplica esta regla: El sistema de archivos asigna espacio en unidades que pueden ser mayores que los datos finales de un archivo. El anclaje principal es **unidades de asignación**.

### Hechos examinables

- El sistema de archivos asigna espacio en unidades que pueden ser mayores que los datos finales de un archivo. <!-- FACT:PN-T38-F309 -->
- El espacio no aprovechado dentro de la última unidad asignada es fragmentación interna. <!-- FACT:PN-T38-F310 -->
- Unidades mayores reducen ciertas estructuras de gestión, pero pueden desperdiciar más espacio con archivos pequeños. <!-- FACT:PN-T38-F311 -->
- La elección de tamaño de unidad depende del sistema, volumen y carga de trabajo. <!-- FACT:PN-T38-F312 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: El espacio no aprovechado dentro de la última unidad asignada es fragmentación interna.
- **Contraste útil:** Contraste: Unidades mayores reducen ciertas estructuras de gestión, pero pueden desperdiciar más espacio con archivos pequeños.

### Trampas de examen

- **Incorrecto:** Una unidad de asignación mayor siempre ahorra espacio con archivos pequeños.
- **Incorrecto:** Fragmentación interna significa que el archivo está dividido en varios directorios.

<!-- VISUAL PENDIENTE: t38-78-asignacion-de-espacio-y-fragmentacion-interna.webp -->

:::hablemos-claro
El sistema de archivos asigna espacio en unidades que pueden ser mayores que los datos finales de un archivo.
:::

:::en-la-calle
Al formatear, montar o proteger un volumen, El sistema de archivos asigna espacio en unidades que pueden ser mayores que los datos finales de un archivo.
:::

:::lo-que-cae
Prioriza **unidades de asignación** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: LINUX-EXT4-T38 -->

## 79. Montaje, letras y puntos de montaje

### Lógica del bloque

Para dominar **montaje, letras y puntos de montaje**, aplica esta regla: Montar conecta un sistema de archivos con un punto accesible de la jerarquía. El anclaje principal es **hacer accesible un volumen**.

### Hechos examinables

- Montar conecta un sistema de archivos con un punto accesible de la jerarquía. <!-- FACT:PN-T38-F313 -->
- Los sistemas tipo Unix usan puntos de montaje dentro de un árbol único. <!-- FACT:PN-T38-F314 -->
- Windows usa habitualmente letras, pero también puede montar volúmenes en carpetas. <!-- FACT:PN-T38-F315 -->
- Desmontar de forma segura permite completar escrituras pendientes antes de retirar un medio. <!-- FACT:PN-T38-F316 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: Los sistemas tipo Unix usan puntos de montaje dentro de un árbol único.
- **Contraste útil:** Contraste: Windows usa habitualmente letras, pero también puede montar volúmenes en carpetas.

### Trampas de examen

- **Incorrecto:** Montar copia el contenido completo del volumen a la RAM.
- **Incorrecto:** Windows solo puede acceder a volúmenes mediante letras y nunca mediante carpetas.

<!-- VISUAL PENDIENTE: t38-79-montaje-letras-y-puntos-de-montaje.webp -->

:::hablemos-claro
Montar conecta un sistema de archivos con un punto accesible de la jerarquía.
:::

:::en-la-calle
Al formatear, montar o proteger un volumen, Montar conecta un sistema de archivos con un punto accesible de la jerarquía.
:::

:::lo-que-cae
Prioriza **hacer accesible un volumen** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: POSIX-2024-T38 -->

## 80. Formateo, borrado y recuperación

### Lógica del bloque

Para dominar **formateo, borrado y recuperación**, aplica esta regla: Formatear crea o renueva estructuras de un sistema de archivos en un volumen. El anclaje principal es **crear estructuras no es destruir con certeza**.

### Hechos examinables

- Formatear crea o renueva estructuras de un sistema de archivos en un volumen. <!-- FACT:PN-T38-F317 -->
- El formato rápido suele reconstruir metadatos esenciales sin verificar ni sobrescribir todo el soporte. <!-- FACT:PN-T38-F318 -->
- Eliminar o formatear no garantiza por sí solo un borrado irrecuperable. <!-- FACT:PN-T38-F319 -->
- El borrado seguro depende del medio, cifrado, controlador y procedimiento de sanitización. <!-- FACT:PN-T38-F320 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: El formato rápido suele reconstruir metadatos esenciales sin verificar ni sobrescribir todo el soporte.
- **Contraste útil:** Contraste: Eliminar o formatear no garantiza por sí solo un borrado irrecuperable.

### Trampas de examen

- **Incorrecto:** Un formato rápido sobrescribe necesariamente cada celda del dispositivo.
- **Incorrecto:** Eliminar una entrada de directorio certifica la destrucción física instantánea.

<!-- VISUAL PENDIENTE: t38-80-formateo-borrado-y-recuperacion.webp -->

:::hablemos-claro
Formatear crea o renueva estructuras de un sistema de archivos en un volumen.
:::

:::en-la-calle
Al formatear, montar o proteger un volumen, Formatear crea o renueva estructuras de un sistema de archivos en un volumen.
:::

:::lo-que-cae
Prioriza **crear estructuras no es destruir con certeza** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: MS-STORAGE-T38 -->

## 81. Diario, copy-on-write y comprobaciones

### Lógica del bloque

Para dominar **diario, copy-on-write y comprobaciones**, aplica esta regla: El journaling registra información de cambios para facilitar recuperación tras una interrupción. El anclaje principal es **mecanismos de consistencia diferentes**.

### Hechos examinables

- El journaling registra información de cambios para facilitar recuperación tras una interrupción. <!-- FACT:PN-T38-F321 -->
- Copy-on-write escribe cambios en nuevas ubicaciones antes de actualizar referencias. <!-- FACT:PN-T38-F322 -->
- Los checksums detectan determinadas alteraciones, pero no reparan cualquier daño por sí solos. <!-- FACT:PN-T38-F323 -->
- Ninguno de estos mecanismos sustituye una copia de seguridad independiente. <!-- FACT:PN-T38-F324 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: Copy-on-write escribe cambios en nuevas ubicaciones antes de actualizar referencias.
- **Contraste útil:** Contraste: Los checksums detectan determinadas alteraciones, pero no reparan cualquier daño por sí solos.

### Trampas de examen

- **Incorrecto:** Journaling conserva automáticamente versiones históricas completas de todos los archivos.
- **Incorrecto:** Un checksum corrige cualquier corrupción sin datos redundantes.

<!-- VISUAL PENDIENTE: t38-81-diario-copy-on-write-y-comprobaciones.webp -->

:::hablemos-claro
El journaling registra información de cambios para facilitar recuperación tras una interrupción.
:::

:::en-la-calle
Al formatear, montar o proteger un volumen, El journaling registra información de cambios para facilitar recuperación tras una interrupción.
:::

:::lo-que-cae
Prioriza **mecanismos de consistencia diferentes** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: LINUX-EXT4-T38 -->

## 82. FAT12, FAT16 y FAT32

### Lógica del bloque

Para dominar **fat12, fat16 y fat32**, aplica esta regla: Las variantes FAT se diferencian principalmente por el tamaño de sus entradas y la cantidad de clústeres direccionables. El anclaje principal es **tabla de asignación de archivos**.

### Hechos examinables

- Las variantes FAT se diferencian principalmente por el tamaño de sus entradas y la cantidad de clústeres direccionables. <!-- FACT:PN-T38-F325 -->
- FAT32 mantiene amplia compatibilidad, pero carece de permisos ACL y diario nativos comparables a NTFS. <!-- FACT:PN-T38-F326 -->
- FAT32 no admite archivos de tamaño igual o superior a 4 GiB por el campo de tamaño de 32 bits. <!-- FACT:PN-T38-F327 -->
- El límite práctico de creación de volúmenes puede depender de la herramienta y no solo del formato FAT32. <!-- FACT:PN-T38-F328 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: FAT32 mantiene amplia compatibilidad, pero carece de permisos ACL y diario nativos comparables a NTFS.
- **Contraste útil:** Contraste: FAT32 no admite archivos de tamaño igual o superior a 4 GiB por el campo de tamaño de 32 bits.

### Trampas de examen

- **Incorrecto:** FAT32 admite un archivo individual de cualquier tamaño.
- **Incorrecto:** FAT32 incorpora de forma nativa ACL, cifrado EFS y journaling.

<!-- VISUAL PENDIENTE: t38-82-fat12-fat16-y-fat32.webp -->

:::hablemos-claro
Las variantes FAT se diferencian principalmente por el tamaño de sus entradas y la cantidad de clústeres direccionables.
:::

:::en-la-calle
Al formatear, montar o proteger un volumen, Las variantes FAT se diferencian principalmente por el tamaño de sus entradas y la cantidad de clústeres direccionables.
:::

:::lo-que-cae
Prioriza **tabla de asignación de archivos** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: MS-EXFAT-T38 -->

## 83. exFAT

### Lógica del bloque

Para dominar **exfat**, aplica esta regla: exFAT es sucesor de FAT32 dentro de la familia FAT. El anclaje principal es **FAT ampliado para medios modernos**.

### Hechos examinables

- exFAT es sucesor de FAT32 dentro de la familia FAT. <!-- FACT:PN-T38-F329 -->
- Utiliza campos de 64 bits para tamaño de archivo y fue diseñado para archivos y dispositivos grandes. <!-- FACT:PN-T38-F330 -->
- Mantiene una estructura relativamente simple y orientada a medios extraíbles y flash. <!-- FACT:PN-T38-F331 -->
- La compatibilidad real depende de la versión del sistema y del dispositivo, no solo del nombre exFAT. <!-- FACT:PN-T38-F332 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: Utiliza campos de 64 bits para tamaño de archivo y fue diseñado para archivos y dispositivos grandes.
- **Contraste útil:** Contraste: Mantiene una estructura relativamente simple y orientada a medios extraíbles y flash.

### Trampas de examen

- **Incorrecto:** exFAT conserva el límite de archivo de FAT32.
- **Incorrecto:** exFAT ofrece por diseño todos los permisos y el diario de NTFS.

<!-- VISUAL PENDIENTE: t38-83-exfat.webp -->

:::hablemos-claro
exFAT es sucesor de FAT32 dentro de la familia FAT.
:::

:::en-la-calle
Al formatear, montar o proteger un volumen, exFAT es sucesor de FAT32 dentro de la familia FAT.
:::

:::lo-que-cae
Prioriza **FAT ampliado para medios modernos** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: MS-EXFAT-T38 -->

## 84. NTFS

### Lógica del bloque

Para dominar **ntfs**, aplica esta regla: NTFS es el sistema de archivos predeterminado de Windows moderno para volúmenes del sistema. El anclaje principal es **sistema predeterminado de Windows moderno**.

### Hechos examinables

- NTFS es el sistema de archivos predeterminado de Windows moderno para volúmenes del sistema. <!-- FACT:PN-T38-F333 -->
- Admite descriptores de seguridad y listas de control de acceso. <!-- FACT:PN-T38-F334 -->
- Incluye diario de metadatos y funciones como compresión, cuotas y cifrado EFS. <!-- FACT:PN-T38-F335 -->
- La compatibilidad de escritura desde otros sistemas debe comprobarse por versión y software; no es universal por definición. <!-- FACT:PN-T38-F336 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: Admite descriptores de seguridad y listas de control de acceso.
- **Contraste útil:** Contraste: Incluye diario de metadatos y funciones como compresión, cuotas y cifrado EFS.

### Trampas de examen

- **Incorrecto:** NTFS carece de permisos y solo admite nombres 8.3.
- **Incorrecto:** Cualquier sistema operativo escribe NTFS de forma nativa y completa sin condiciones.

<!-- VISUAL PENDIENTE: t38-84-ntfs.webp -->

:::hablemos-claro
NTFS es el sistema de archivos predeterminado de Windows moderno para volúmenes del sistema.
:::

:::en-la-calle
Al formatear, montar o proteger un volumen, NTFS es el sistema de archivos predeterminado de Windows moderno para volúmenes del sistema.
:::

:::lo-que-cae
Prioriza **sistema predeterminado de Windows moderno** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: MS-NTFS-T38 -->

## 85. ReFS y alcance comparado

### Lógica del bloque

Para dominar **refs y alcance comparado**, aplica esta regla: ReFS es un sistema de archivos de Microsoft orientado a resiliencia, integridad y escenarios de almacenamiento determinados. El anclaje principal es **integridad y cargas específicas**.

### Hechos examinables

- ReFS es un sistema de archivos de Microsoft orientado a resiliencia, integridad y escenarios de almacenamiento determinados. <!-- FACT:PN-T38-F337 -->
- ReFS y NTFS comparten algunas funciones, pero no son intercambiables en todos los escenarios. <!-- FACT:PN-T38-F338 -->
- La disponibilidad de ReFS depende de la edición, versión y tipo de volumen de Windows. <!-- FACT:PN-T38-F339 -->
- Que ReFS sea más reciente no lo convierte automáticamente en la mejor elección para cualquier equipo. <!-- FACT:PN-T38-F340 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: ReFS y NTFS comparten algunas funciones, pero no son intercambiables en todos los escenarios.
- **Contraste útil:** Contraste: La disponibilidad de ReFS depende de la edición, versión y tipo de volumen de Windows.

### Trampas de examen

- **Incorrecto:** ReFS reemplaza obligatoriamente a NTFS en toda instalación de Windows.
- **Incorrecto:** ReFS está disponible con idénticas funciones en cualquier edición y dispositivo.

<!-- VISUAL PENDIENTE: t38-85-refs-y-alcance-comparado.webp -->

:::hablemos-claro
ReFS es un sistema de archivos de Microsoft orientado a resiliencia, integridad y escenarios de almacenamiento determinados.
:::

:::en-la-calle
Al formatear, montar o proteger un volumen, ReFS es un sistema de archivos de Microsoft orientado a resiliencia, integridad y escenarios de almacenamiento determinados.
:::

:::lo-que-cae
Prioriza **integridad y cargas específicas** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: MS-NTFS-T38 -->

## 86. ext2, ext3 y ext4

### Lógica del bloque

Para dominar **ext2, ext3 y ext4**, aplica esta regla: ext2 no incorpora el diario que caracteriza a ext3. El anclaje principal es **evolución de la familia extended**.

### Hechos examinables

- ext2 no incorpora el diario que caracteriza a ext3. <!-- FACT:PN-T38-F341 -->
- ext3 añadió journaling manteniendo continuidad con ext2. <!-- FACT:PN-T38-F342 -->
- ext4 amplió capacidad y rendimiento mediante extents, asignación diferida y otras mejoras. <!-- FACT:PN-T38-F343 -->
- ext4 utiliza inodos, grupos de bloques y un diario gestionado con JBD2 cuando está habilitado. <!-- FACT:PN-T38-F344 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: ext3 añadió journaling manteniendo continuidad con ext2.
- **Contraste útil:** Contraste: ext4 amplió capacidad y rendimiento mediante extents, asignación diferida y otras mejoras.

### Trampas de examen

- **Incorrecto:** ext4 deriva de NTFS y usa la MFT de Windows.
- **Incorrecto:** ext2, ext3 y ext4 son nombres distintos sin diferencias funcionales.

<!-- VISUAL PENDIENTE: t38-86-ext2-ext3-y-ext4.webp -->

:::hablemos-claro
ext2 no incorpora el diario que caracteriza a ext3.
:::

:::en-la-calle
Al formatear, montar o proteger un volumen, ext2 no incorpora el diario que caracteriza a ext3.
:::

:::lo-que-cae
Prioriza **evolución de la familia extended** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: LINUX-EXT4-T38 -->

## 87. APFS y HFS+

### Lógica del bloque

Para dominar **apfs y hfs+**, aplica esta regla: HFS+ fue el sistema principal de macOS antes de APFS. El anclaje principal es **transición del ecosistema Apple**.

### Hechos examinables

- HFS+ fue el sistema principal de macOS antes de APFS. <!-- FACT:PN-T38-F345 -->
- APFS se convirtió en el sistema predeterminado de las plataformas Apple modernas. <!-- FACT:PN-T38-F346 -->
- APFS ofrece cifrado, snapshots, clonación y espacio compartido entre volúmenes. <!-- FACT:PN-T38-F347 -->
- La transición no significa que todos los soportes antiguos o externos se conviertan automáticamente a APFS. <!-- FACT:PN-T38-F348 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: APFS se convirtió en el sistema predeterminado de las plataformas Apple modernas.
- **Contraste útil:** Contraste: APFS ofrece cifrado, snapshots, clonación y espacio compartido entre volúmenes.

### Trampas de examen

- **Incorrecto:** HFS+ es el nombre antiguo de NTFS.
- **Incorrecto:** Instalar macOS convierte sin excepción cualquier unidad externa a APFS.

<!-- VISUAL PENDIENTE: t38-87-apfs-y-hfs.webp -->

:::hablemos-claro
HFS+ fue el sistema principal de macOS antes de APFS.
:::

:::en-la-calle
Al formatear, montar o proteger un volumen, HFS+ fue el sistema principal de macOS antes de APFS.
:::

:::lo-que-cae
Prioriza **transición del ecosistema Apple** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: APPLE-APFS-T38 -->

## 88. ISO 9660 y UDF

### Lógica del bloque

Para dominar **iso 9660 y udf**, aplica esta regla: ISO 9660 se diseñó para el intercambio de datos en medios ópticos de solo lectura. El anclaje principal es **sistemas para medios ópticos**.

### Hechos examinables

- ISO 9660 se diseñó para el intercambio de datos en medios ópticos de solo lectura. <!-- FACT:PN-T38-F349 -->
- UDF se utiliza en distintos medios ópticos y soporta casos más amplios y archivos mayores según versión. <!-- FACT:PN-T38-F350 -->
- Las extensiones de ISO 9660 pueden ampliar nombres y metadatos para plataformas concretas. <!-- FACT:PN-T38-F351 -->
- El sistema de archivos del medio y el tipo físico de disco son capas distintas. <!-- FACT:PN-T38-F352 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: UDF se utiliza en distintos medios ópticos y soporta casos más amplios y archivos mayores según versión.
- **Contraste útil:** Contraste: Las extensiones de ISO 9660 pueden ampliar nombres y metadatos para plataformas concretas.

### Trampas de examen

- **Incorrecto:** ISO 9660 es una interfaz física equivalente a SATA.
- **Incorrecto:** Todo Blu-ray utiliza obligatoriamente FAT32.

<!-- VISUAL PENDIENTE: t38-88-iso-9660-y-udf.webp -->

:::hablemos-claro
ISO 9660 se diseñó para el intercambio de datos en medios ópticos de solo lectura.
:::

:::en-la-calle
Al formatear, montar o proteger un volumen, ISO 9660 se diseñó para el intercambio de datos en medios ópticos de solo lectura.
:::

:::lo-que-cae
Prioriza **sistemas para medios ópticos** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: MS-STORAGE-T38 -->

## 89. Enlaces, permisos y sensibilidad a mayúsculas

### Lógica del bloque

Para dominar **enlaces, permisos y sensibilidad a mayúsculas**, aplica esta regla: Un enlace duro añade otra referencia al mismo objeto dentro de las restricciones del sistema de archivos. El anclaje principal es **semántica dependiente del sistema**.

### Hechos examinables

- Un enlace duro añade otra referencia al mismo objeto dentro de las restricciones del sistema de archivos. <!-- FACT:PN-T38-F353 -->
- Un enlace simbólico contiene una referencia de ruta y puede quedar roto si cambia su destino. <!-- FACT:PN-T38-F354 -->
- Los permisos pueden expresarse mediante bits clásicos, ACL u otros modelos. <!-- FACT:PN-T38-F355 -->
- La distinción entre mayúsculas y minúsculas depende del sistema de archivos, su formato y la capa que resuelve nombres. <!-- FACT:PN-T38-F356 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: Un enlace simbólico contiene una referencia de ruta y puede quedar roto si cambia su destino.
- **Contraste útil:** Contraste: Los permisos pueden expresarse mediante bits clásicos, ACL u otros modelos.

### Trampas de examen

- **Incorrecto:** Un enlace simbólico contiene siempre una copia completa e independiente del archivo.
- **Incorrecto:** Todos los sistemas de archivos tratan Archivo y archivo de forma idéntica.

<!-- VISUAL PENDIENTE: t38-89-enlaces-permisos-y-sensibilidad-a-mayusculas.webp -->

:::hablemos-claro
Un enlace duro añade otra referencia al mismo objeto dentro de las restricciones del sistema de archivos.
:::

:::en-la-calle
Al formatear, montar o proteger un volumen, Un enlace duro añade otra referencia al mismo objeto dentro de las restricciones del sistema de archivos.
:::

:::lo-que-cae
Prioriza **semántica dependiente del sistema** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: POSIX-2024-T38 -->

## 90. Elección del sistema de archivos

### Lógica del bloque

Para dominar **elección del sistema de archivos**, aplica esta regla: La elección debe considerar sistema operativo, tamaño de archivos, permisos, resiliencia, rendimiento y dispositivos de destino. El anclaje principal es **uso, compatibilidad y riesgo**.

### Hechos examinables

- La elección debe considerar sistema operativo, tamaño de archivos, permisos, resiliencia, rendimiento y dispositivos de destino. <!-- FACT:PN-T38-F357 -->
- FAT32 prioriza compatibilidad amplia con límites relevantes; exFAT amplía tamaños para medios compartidos. <!-- FACT:PN-T38-F358 -->
- NTFS y FAT, ext4 y APFS son ejemplos reales de sistemas de archivos de los ecosistemas Windows, Linux y Apple. <!-- FACT:PN-T38-F359 -->
- Ninguna tabla de compatibilidad es eterna: debe fecharse y comprobarse en las versiones concretas implicadas. <!-- FACT:PN-T38-F360 -->

### Ejemplos razonados

- **Aplicación correcta:** Aplicación: FAT32 prioriza compatibilidad amplia con límites relevantes; exFAT amplía tamaños para medios compartidos.
- **Contraste útil:** Contraste: NTFS y FAT, ext4 y APFS son ejemplos reales de sistemas de archivos de los ecosistemas Windows, Linux y Apple.

### Trampas de examen

- **Incorrecto:** Siempre existe un sistema de archivos óptimo para todos los dispositivos y usos.
- **Incorrecto:** La compatibilidad depende únicamente de la capacidad física del disco.

<!-- VISUAL PENDIENTE: t38-il-90-eleccion-del-sistema-de-archivos.webp -->

:::hablemos-claro
La elección debe considerar sistema operativo, tamaño de archivos, permisos, resiliencia, rendimiento y dispositivos de destino.
:::

:::en-la-calle
Al formatear, montar o proteger un volumen, La elección debe considerar sistema operativo, tamaño de archivos, permisos, resiliencia, rendimiento y dispositivos de destino.
:::

:::lo-que-cae
Prioriza **uso, compatibilidad y riesgo** y descarta respuestas que confundan hardware, proceso, interfaz, volumen o sistema de archivos.
:::

<!-- FUENTE: CONVOCATORIA-PN-2026-T38 -->

# Hablemos claro

:::hablemos-claro
Este tema tiene cuatro trampas maestras: confundir hardware con software; programa con proceso; dispositivo, partición, volumen y sistema de archivos; y producto histórico con versión actual. Antes de responder identifica la capa, la plataforma y si la afirmación depende de versión.
:::

# En la calle

:::en-la-calle
En una intervención, distinguir un archivo oculto de uno inaccesible, un volumen cifrado de una copia de seguridad o una unidad M.2 de un protocolo NVMe evita diagnósticos falsos y preserva mejor la evidencia.
:::

# Lo que cae

:::lo-que-cae
Prioriza funciones del sistema operativo; proceso, hilo y planificación; memoria virtual; kernel, shell y GUI; diferencias entre MS-DOS, UNIX, Linux, Windows, macOS, iOS y Android; HDD/SSD, SATA/NVMe, MBR/GPT; y FAT32, exFAT, NTFS, ext4 y APFS.
:::

# Ha caído

:::ha-caido
Se han localizado 9 referencias históricas del Tema 38. Permanecen ocultas y en cuarentena porque no existe plantilla oficial final verificable en el repositorio.
:::

## Fuentes legales, institucionales y primarias

- `CONVOCATORIA-PN-2026-T38`
- `MS-WINDOWS-INTERNALS-T38`
- `MS-NTFS-T38`
- `MS-EXFAT-T38`
- `MS-STORAGE-T38`
- `MS-DOS-SOURCE-T38`
- `POSIX-2024-T38`
- `LINUX-KERNEL-T38`
- `LINUX-EXT4-T38`
- `APPLE-PLATFORM-SECURITY-T38`
- `APPLE-APFS-T38`
- `ANDROID-ARCH-T38`
- `ANDROID-STORAGE-T38`
- `NVME-SPEC-T38`

---

*Academia En Vigor · El temario que nunca duerme · Tema 38 · v1.0.0 · Documento interno no publicado.*
