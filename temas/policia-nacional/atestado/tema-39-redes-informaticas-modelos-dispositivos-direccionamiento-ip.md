# TEMA 39 · REDES INFORMÁTICAS: MODELO OSI Y MODELO TCP/IP. DISPOSITIVOS DE RED: HUBS, SWITCHES, ROUTERS, FIREWALL, SERVIDORES DHCP, SERVIDORES DNS Y SERVIDORES PROXY. DIRECCIONAMIENTO IP: CLASES DE REDES, IPV4 E IPV6.

**Policía Nacional · Método VIGOR · ATESTADO**
**Versión de contenido:** 1.0.0
**Estado editorial:** approved_internal · **Publicación:** not_published

# Mapa del tema

El Tema 39 se estudia en ocho partes: fundamentos; modelo OSI; modelo TCP/IP; hubs y switches; routers y firewall; DHCP, DNS y proxy; IPv4 y clases históricas; e IPv6.

# Contenido

## 01. Alcance oficial del Tema 39

### Lógica del bloque

Para dominar **alcance oficial del tema 39**, aplica esta regla: El programa exige estudiar los modelos OSI y TCP/IP. El anclaje principal es **tres núcleos oficiales**.

### Hechos examinables

- El programa exige estudiar los modelos OSI y TCP/IP. <!-- FACT:PN-T39-F001 -->
- El epígrafe enumera hubs, switches, routers, firewall y servidores DHCP, DNS y proxy. <!-- FACT:PN-T39-F002 -->
- El direccionamiento comprende clases de redes, IPv4 e IPv6. <!-- FACT:PN-T39-F003 -->
- Protocolos o técnicas auxiliares se incluyen solo cuando explican esos núcleos oficiales. <!-- FACT:PN-T39-F004 -->

### Ejemplos razonados

- **Aplicación correcta:** El epígrafe enumera hubs, switches, routers, firewall y servidores DHCP, DNS y proxy.
- **Contraste útil:** El direccionamiento comprende clases de redes, IPv4 e IPv6.

### Trampas de examen

- **Incorrecto:** El Tema 39 es un catálogo general de toda la ciberseguridad.
- **Incorrecto:** Las direcciones IP quedan fuera del epígrafe.

<!-- VISUAL:t39-01-alcance-oficial-del-tema-39.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-01-alcance-oficial-del-tema-39.webp" alt="Alcance oficial del Tema 39" width="820">
</p>
<p align="center"><em>Infografía: Alcance oficial del Tema 39.</em></p>

:::hablemos-claro
El programa exige estudiar los modelos OSI y TCP/IP.
:::

:::en-la-calle
Al identificar el alcance y la topología de una red, El programa exige estudiar los modelos OSI y TCP/IP.
:::

:::lo-que-cae
Prioriza **tres núcleos oficiales** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: CONVOCATORIA-PN-2026-T39 -->

## 02. Red, nodo, enlace y protocolo

### Lógica del bloque

Para dominar **red, nodo, enlace y protocolo**, aplica esta regla: Una red interconecta sistemas para intercambiar datos y compartir recursos. El anclaje principal es **cuatro piezas de una comunicación**.

### Hechos examinables

- Una red interconecta sistemas para intercambiar datos y compartir recursos. <!-- FACT:PN-T39-F005 -->
- Un nodo es un sistema o dispositivo que participa en la comunicación. <!-- FACT:PN-T39-F006 -->
- Un enlace es el medio lógico o físico que conecta nodos adyacentes. <!-- FACT:PN-T39-F007 -->
- Un protocolo define reglas y formatos compartidos para que las entidades se entiendan. <!-- FACT:PN-T39-F008 -->

### Ejemplos razonados

- **Aplicación correcta:** Un nodo es un sistema o dispositivo que participa en la comunicación.
- **Contraste útil:** Un enlace es el medio lógico o físico que conecta nodos adyacentes.

### Trampas de examen

- **Incorrecto:** Una red exige siempre acceso a Internet.
- **Incorrecto:** Un protocolo es el cable que une físicamente dos equipos.

<!-- VISUAL:t39-02-red-nodo-enlace-y-protocolo.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-02-red-nodo-enlace-y-protocolo.webp" alt="Red, nodo, enlace y protocolo" width="820">
</p>
<p align="center"><em>Infografía: Red, nodo, enlace y protocolo.</em></p>

:::hablemos-claro
Una red interconecta sistemas para intercambiar datos y compartir recursos.
:::

:::en-la-calle
Al identificar el alcance y la topología de una red, Una red interconecta sistemas para intercambiar datos y compartir recursos.
:::

:::lo-que-cae
Prioriza **cuatro piezas de una comunicación** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: RFC1122-HOSTS-T39 -->

## 03. LAN, MAN, WAN y PAN

### Lógica del bloque

Para dominar **lan, man, wan y pan**, aplica esta regla: Una LAN cubre normalmente un ámbito local bajo administración próxima. El anclaje principal es **alcance geográfico y funcional**.

### Hechos examinables

- Una LAN cubre normalmente un ámbito local bajo administración próxima. <!-- FACT:PN-T39-F009 -->
- Una WAN interconecta redes o sistemas a distancias amplias. <!-- FACT:PN-T39-F010 -->
- MAN describe un ámbito metropolitano y PAN una red personal de corto alcance. <!-- FACT:PN-T39-F011 -->
- La clasificación por alcance no determina por sí sola el protocolo, el medio ni la propiedad. <!-- FACT:PN-T39-F012 -->

### Ejemplos razonados

- **Aplicación correcta:** Una WAN interconecta redes o sistemas a distancias amplias.
- **Contraste útil:** MAN describe un ámbito metropolitano y PAN una red personal de corto alcance.

### Trampas de examen

- **Incorrecto:** Toda LAN usa exclusivamente cable Ethernet.
- **Incorrecto:** Una WAN pertenece necesariamente a una sola organización.

<!-- VISUAL:t39-03-lan-man-wan-y-pan.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-03-lan-man-wan-y-pan.webp" alt="LAN, MAN, WAN y PAN" width="820">
</p>
<p align="center"><em>Infografía: LAN, MAN, WAN y PAN.</em></p>

:::hablemos-claro
Una LAN cubre normalmente un ámbito local bajo administración próxima.
:::

:::en-la-calle
Al identificar el alcance y la topología de una red, Una LAN cubre normalmente un ámbito local bajo administración próxima.
:::

:::lo-que-cae
Prioriza **alcance geográfico y funcional** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: RFC1122-HOSTS-T39 -->

## 04. Topología física y topología lógica

### Lógica del bloque

Para dominar **topología física y topología lógica**, aplica esta regla: La topología física describe cómo se disponen enlaces y dispositivos. El anclaje principal es **forma frente a circulación**.

### Hechos examinables

- La topología física describe cómo se disponen enlaces y dispositivos. <!-- FACT:PN-T39-F013 -->
- La topología lógica describe cómo circula la información o se organiza el acceso. <!-- FACT:PN-T39-F014 -->
- Bus, anillo, estrella, árbol y malla son modelos de topología. <!-- FACT:PN-T39-F015 -->
- Una red puede presentar topología física y lógica diferentes. <!-- FACT:PN-T39-F016 -->

### Ejemplos razonados

- **Aplicación correcta:** La topología lógica describe cómo circula la información o se organiza el acceso.
- **Contraste útil:** Bus, anillo, estrella, árbol y malla son modelos de topología.

### Trampas de examen

- **Incorrecto:** La topología física y la lógica son siempre idénticas.
- **Incorrecto:** Estrella significa que cada nodo está conectado directamente a todos los demás.

<!-- VISUAL:t39-04-topologia-fisica-y-topologia-logica.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-04-topologia-fisica-y-topologia-logica.webp" alt="Topología física y topología lógica" width="820">
</p>
<p align="center"><em>Infografía: Topología física y topología lógica.</em></p>

:::hablemos-claro
La topología física describe cómo se disponen enlaces y dispositivos.
:::

:::en-la-calle
Al identificar el alcance y la topología de una red, La topología física describe cómo se disponen enlaces y dispositivos.
:::

:::lo-que-cae
Prioriza **forma frente a circulación** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: IEEE8023-ETHERNET-T39 -->

## 05. Conmutación, encaminamiento y servicios

### Lógica del bloque

Para dominar **conmutación, encaminamiento y servicios**, aplica esta regla: La conmutación Ethernet decide el reenvío local principalmente mediante direcciones MAC. El anclaje principal es **decidir en el nivel correcto**.

### Hechos examinables

- La conmutación Ethernet decide el reenvío local principalmente mediante direcciones MAC. <!-- FACT:PN-T39-F017 -->
- El encaminamiento IP decide el siguiente salto entre redes mediante prefijos IP. <!-- FACT:PN-T39-F018 -->
- DHCP asigna parámetros, DNS resuelve nombres y un proxy actúa como intermediario. <!-- FACT:PN-T39-F019 -->
- Un mismo equipo comercial puede reunir varias funciones sin volverlas equivalentes. <!-- FACT:PN-T39-F020 -->

### Ejemplos razonados

- **Aplicación correcta:** El encaminamiento IP decide el siguiente salto entre redes mediante prefijos IP.
- **Contraste útil:** DHCP asigna parámetros, DNS resuelve nombres y un proxy actúa como intermediario.

### Trampas de examen

- **Incorrecto:** Switch, router y DNS son tres nombres de la misma función.
- **Incorrecto:** Un router reenvía tramas locales únicamente por la dirección MAC de destino final.

<!-- VISUAL:t39-il-05-conmutacion-encaminamiento-y-servicios.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-il-05-conmutacion-encaminamiento-y-servicios.webp" alt="Conmutación, encaminamiento y servicios" width="820">
</p>
<p align="center"><em>Infografía: Conmutación, encaminamiento y servicios.</em></p>

:::hablemos-claro
La conmutación Ethernet decide el reenvío local principalmente mediante direcciones MAC.
:::

:::en-la-calle
Al identificar el alcance y la topología de una red, La conmutación Ethernet decide el reenvío local principalmente mediante direcciones MAC.
:::

:::lo-que-cae
Prioriza **decidir en el nivel correcto** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: RFC1812-ROUTERS-T39 -->

## 06. Encapsulación y unidades de datos

### Lógica del bloque

Para dominar **encapsulación y unidades de datos**, aplica esta regla: La encapsulación añade información de control al bajar por la pila. El anclaje principal es **cada capa añade su control**.

### Hechos examinables

- La encapsulación añade información de control al bajar por la pila. <!-- FACT:PN-T39-F021 -->
- La desencapsulación interpreta y retira esa información al recibir. <!-- FACT:PN-T39-F022 -->
- Los datos de aplicación se transportan dentro de unidades de capas inferiores. <!-- FACT:PN-T39-F023 -->
- Cabecera, carga útil y, cuando existe, tráiler cumplen funciones distintas. <!-- FACT:PN-T39-F024 -->

### Ejemplos razonados

- **Aplicación correcta:** La desencapsulación interpreta y retira esa información al recibir.
- **Contraste útil:** Los datos de aplicación se transportan dentro de unidades de capas inferiores.

### Trampas de examen

- **Incorrecto:** Cada capa borra las cabeceras de las capas superiores antes de transmitir.
- **Incorrecto:** La carga útil de una capa nunca contiene una unidad de otra capa.

<!-- VISUAL:t39-06-encapsulacion-y-unidades-de-datos.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-06-encapsulacion-y-unidades-de-datos.webp" alt="Encapsulación y unidades de datos" width="820">
</p>
<p align="center"><em>Infografía: Encapsulación y unidades de datos.</em></p>

:::hablemos-claro
La encapsulación añade información de control al bajar por la pila.
:::

:::en-la-calle
Al identificar el alcance y la topología de una red, La encapsulación añade información de control al bajar por la pila.
:::

:::lo-que-cae
Prioriza **cada capa añade su control** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: RFC1122-HOSTS-T39 -->

## 07. Finalidad del modelo OSI

### Lógica del bloque

Para dominar **finalidad del modelo osi**, aplica esta regla: OSI proporciona una base común para coordinar estándares de interconexión de sistemas abiertos. El anclaje principal es **referencia de siete capas**.

### Hechos examinables

- OSI proporciona una base común para coordinar estándares de interconexión de sistemas abiertos. <!-- FACT:PN-T39-F025 -->
- El modelo divide funciones de comunicación en siete capas. <!-- FACT:PN-T39-F026 -->
- OSI es un modelo de referencia y no una única pila obligatoria implementada literalmente. <!-- FACT:PN-T39-F027 -->
- Su separación facilita describir interoperabilidad y localizar fallos. <!-- FACT:PN-T39-F028 -->

### Ejemplos razonados

- **Aplicación correcta:** El modelo divide funciones de comunicación en siete capas.
- **Contraste útil:** OSI es un modelo de referencia y no una única pila obligatoria implementada literalmente.

### Trampas de examen

- **Incorrecto:** OSI es un sistema operativo de red.
- **Incorrecto:** Toda comunicación real implementa exactamente un protocolo por capa OSI.

<!-- VISUAL:t39-07-finalidad-del-modelo-osi.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-07-finalidad-del-modelo-osi.webp" alt="Finalidad del modelo OSI" width="820">
</p>
<p align="center"><em>Infografía: Finalidad del modelo OSI.</em></p>

:::hablemos-claro
OSI proporciona una base común para coordinar estándares de interconexión de sistemas abiertos.
:::

:::en-la-calle
Al aislar un fallo mediante el modelo OSI, OSI proporciona una base común para coordinar estándares de interconexión de sistemas abiertos.
:::

:::lo-que-cae
Prioriza **referencia de siete capas** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: ISO-7498-1-OSI-T39 -->

## 08. Capas, servicios, protocolos e interfaces

### Lógica del bloque

Para dominar **capas, servicios, protocolos e interfaces**, aplica esta regla: Una capa presta servicios a la capa superior y utiliza servicios de la inferior. El anclaje principal es **relaciones distintas**.

### Hechos examinables

- Una capa presta servicios a la capa superior y utiliza servicios de la inferior. <!-- FACT:PN-T39-F029 -->
- Un protocolo regula la comunicación entre entidades pares de una misma capa. <!-- FACT:PN-T39-F030 -->
- Una interfaz define cómo una capa accede a servicios de la capa adyacente. <!-- FACT:PN-T39-F031 -->
- Servicio y protocolo están relacionados, pero no son términos intercambiables. <!-- FACT:PN-T39-F032 -->

### Ejemplos razonados

- **Aplicación correcta:** Un protocolo regula la comunicación entre entidades pares de una misma capa.
- **Contraste útil:** Una interfaz define cómo una capa accede a servicios de la capa adyacente.

### Trampas de examen

- **Incorrecto:** Un servicio describe exclusivamente el formato de los mensajes entre pares.
- **Incorrecto:** Una interfaz conecta siempre dos ordenadores remotos.

<!-- VISUAL:t39-08-capas-servicios-protocolos-e-interfaces.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-08-capas-servicios-protocolos-e-interfaces.webp" alt="Capas, servicios, protocolos e interfaces" width="820">
</p>
<p align="center"><em>Infografía: Capas, servicios, protocolos e interfaces.</em></p>

:::hablemos-claro
Una capa presta servicios a la capa superior y utiliza servicios de la inferior.
:::

:::en-la-calle
Al aislar un fallo mediante el modelo OSI, Una capa presta servicios a la capa superior y utiliza servicios de la inferior.
:::

:::lo-que-cae
Prioriza **relaciones distintas** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: ISO-7498-1-OSI-T39 -->

## 09. Capa 1: física

### Lógica del bloque

Para dominar **capa 1: física**, aplica esta regla: La capa física transmite un flujo de bits a través del medio. El anclaje principal es **bits y medio**.

### Hechos examinables

- La capa física transmite un flujo de bits a través del medio. <!-- FACT:PN-T39-F033 -->
- Se ocupa de características eléctricas, ópticas, radioeléctricas, mecánicas y de señalización. <!-- FACT:PN-T39-F034 -->
- Conectores, modulación y velocidad física se asocian a esta capa. <!-- FACT:PN-T39-F035 -->
- La capa física no interpreta direcciones IP ni decide rutas. <!-- FACT:PN-T39-F036 -->

### Ejemplos razonados

- **Aplicación correcta:** Se ocupa de características eléctricas, ópticas, radioeléctricas, mecánicas y de señalización.
- **Contraste útil:** Conectores, modulación y velocidad física se asocian a esta capa.

### Trampas de examen

- **Incorrecto:** La capa física crea registros DNS.
- **Incorrecto:** La capa física selecciona el mejor prefijo IP.

<!-- VISUAL:t39-09-capa-1-fisica.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-09-capa-1-fisica.webp" alt="Capa 1: física" width="820">
</p>
<p align="center"><em>Infografía: Capa 1: física.</em></p>

:::hablemos-claro
La capa física transmite un flujo de bits a través del medio.
:::

:::en-la-calle
Al aislar un fallo mediante el modelo OSI, La capa física transmite un flujo de bits a través del medio.
:::

:::lo-que-cae
Prioriza **bits y medio** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: ISO-7498-1-OSI-T39 -->

## 10. Capa 2: enlace de datos

### Lógica del bloque

Para dominar **capa 2: enlace de datos**, aplica esta regla: La capa de enlace organiza la transmisión sobre un enlace en unidades como tramas. El anclaje principal es **tramas en el enlace**.

### Hechos examinables

- La capa de enlace organiza la transmisión sobre un enlace en unidades como tramas. <!-- FACT:PN-T39-F037 -->
- Puede proporcionar delimitación, detección de errores y control de acceso al medio. <!-- FACT:PN-T39-F038 -->
- Ethernet utiliza direcciones MAC para el reenvío dentro del dominio de enlace. <!-- FACT:PN-T39-F039 -->
- La entrega de capa 2 no sustituye el encaminamiento entre redes IP. <!-- FACT:PN-T39-F040 -->

### Ejemplos razonados

- **Aplicación correcta:** Puede proporcionar delimitación, detección de errores y control de acceso al medio.
- **Contraste útil:** Ethernet utiliza direcciones MAC para el reenvío dentro del dominio de enlace.

### Trampas de examen

- **Incorrecto:** Una trama Ethernet se encamina por Internet sin encapsulación IP.
- **Incorrecto:** Las direcciones MAC son nombres DNS.

<!-- VISUAL:t39-il-10-capa-2-enlace-de-datos.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-il-10-capa-2-enlace-de-datos.webp" alt="Capa 2: enlace de datos" width="820">
</p>
<p align="center"><em>Infografía: Capa 2: enlace de datos.</em></p>

:::hablemos-claro
La capa de enlace organiza la transmisión sobre un enlace en unidades como tramas.
:::

:::en-la-calle
Al aislar un fallo mediante el modelo OSI, La capa de enlace organiza la transmisión sobre un enlace en unidades como tramas.
:::

:::lo-que-cae
Prioriza **tramas en el enlace** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: ISO-7498-1-OSI-T39 -->

## 11. Sublayers LLC y MAC

### Lógica del bloque

Para dominar **sublayers llc y mac**, aplica esta regla: La subcapa MAC se relaciona con el acceso al medio y el direccionamiento físico. El anclaje principal es **control lógico y acceso**.

### Hechos examinables

- La subcapa MAC se relaciona con el acceso al medio y el direccionamiento físico. <!-- FACT:PN-T39-F041 -->
- La subcapa LLC proporciona una interfaz lógica hacia capas superiores en arquitecturas IEEE 802. <!-- FACT:PN-T39-F042 -->
- Un switch Ethernet aprende y reenvía usando información MAC. <!-- FACT:PN-T39-F043 -->
- No debe confundirse la dirección MAC con la dirección IP de capa de red. <!-- FACT:PN-T39-F044 -->

### Ejemplos razonados

- **Aplicación correcta:** La subcapa LLC proporciona una interfaz lógica hacia capas superiores en arquitecturas IEEE 802.
- **Contraste útil:** Un switch Ethernet aprende y reenvía usando información MAC.

### Trampas de examen

- **Incorrecto:** LLC asigna direcciones IPv6 globales.
- **Incorrecto:** Una MAC identifica siempre a una persona y nunca puede cambiar.

<!-- VISUAL:t39-11-sublayers-llc-y-mac.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-11-sublayers-llc-y-mac.webp" alt="Sublayers LLC y MAC" width="820">
</p>
<p align="center"><em>Infografía: Sublayers LLC y MAC.</em></p>

:::hablemos-claro
La subcapa MAC se relaciona con el acceso al medio y el direccionamiento físico.
:::

:::en-la-calle
Al aislar un fallo mediante el modelo OSI, La subcapa MAC se relaciona con el acceso al medio y el direccionamiento físico.
:::

:::lo-que-cae
Prioriza **control lógico y acceso** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: IEEE8021Q-BRIDGES-T39 -->

## 12. Capa 3: red

### Lógica del bloque

Para dominar **capa 3: red**, aplica esta regla: La capa de red permite transferir paquetes entre sistemas a través de redes intermedias. El anclaje principal es **paquetes y rutas**.

### Hechos examinables

- La capa de red permite transferir paquetes entre sistemas a través de redes intermedias. <!-- FACT:PN-T39-F045 -->
- IP aporta direccionamiento lógico y soporte para el encaminamiento. <!-- FACT:PN-T39-F046 -->
- Los routers operan principalmente tomando decisiones de capa 3. <!-- FACT:PN-T39-F047 -->
- La capa de red no garantiza por sí sola la entrega fiable de extremo a extremo. <!-- FACT:PN-T39-F048 -->

### Ejemplos razonados

- **Aplicación correcta:** IP aporta direccionamiento lógico y soporte para el encaminamiento.
- **Contraste útil:** Los routers operan principalmente tomando decisiones de capa 3.

### Trampas de examen

- **Incorrecto:** La capa de red es la capa de sesión.
- **Incorrecto:** IP confirma necesariamente cada paquete recibido.

<!-- VISUAL:t39-12-capa-3-red.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-12-capa-3-red.webp" alt="Capa 3: red" width="820">
</p>
<p align="center"><em>Infografía: Capa 3: red.</em></p>

:::hablemos-claro
La capa de red permite transferir paquetes entre sistemas a través de redes intermedias.
:::

:::en-la-calle
Al aislar un fallo mediante el modelo OSI, La capa de red permite transferir paquetes entre sistemas a través de redes intermedias.
:::

:::lo-que-cae
Prioriza **paquetes y rutas** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: ISO-7498-1-OSI-T39 -->

## 13. Capa 4: transporte

### Lógica del bloque

Para dominar **capa 4: transporte**, aplica esta regla: La capa de transporte ofrece comunicación lógica entre extremos o procesos. El anclaje principal es **extremo a extremo**.

### Hechos examinables

- La capa de transporte ofrece comunicación lógica entre extremos o procesos. <!-- FACT:PN-T39-F049 -->
- Puede segmentar, reensamblar, multiplexar y controlar la transmisión. <!-- FACT:PN-T39-F050 -->
- TCP proporciona un servicio fiable orientado a conexión. <!-- FACT:PN-T39-F051 -->
- UDP proporciona datagramas sin establecer una conexión fiable. <!-- FACT:PN-T39-F052 -->

### Ejemplos razonados

- **Aplicación correcta:** Puede segmentar, reensamblar, multiplexar y controlar la transmisión.
- **Contraste útil:** TCP proporciona un servicio fiable orientado a conexión.

### Trampas de examen

- **Incorrecto:** Todo protocolo de transporte confirma y retransmite.
- **Incorrecto:** La capa de transporte elige la dirección MAC del siguiente enlace.

<!-- VISUAL:t39-13-capa-4-transporte.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-13-capa-4-transporte.webp" alt="Capa 4: transporte" width="820">
</p>
<p align="center"><em>Infografía: Capa 4: transporte.</em></p>

:::hablemos-claro
La capa de transporte ofrece comunicación lógica entre extremos o procesos.
:::

:::en-la-calle
Al aislar un fallo mediante el modelo OSI, La capa de transporte ofrece comunicación lógica entre extremos o procesos.
:::

:::lo-que-cae
Prioriza **extremo a extremo** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: ISO-7498-1-OSI-T39 -->

## 14. Capa 5: sesión

### Lógica del bloque

Para dominar **capa 5: sesión**, aplica esta regla: La capa de sesión modela el establecimiento, mantenimiento y cierre de diálogos. El anclaje principal es **diálogo entre aplicaciones**.

### Hechos examinables

- La capa de sesión modela el establecimiento, mantenimiento y cierre de diálogos. <!-- FACT:PN-T39-F053 -->
- Puede coordinar puntos de sincronización y recuperación del diálogo. <!-- FACT:PN-T39-F054 -->
- En pilas actuales sus funciones suelen integrarse en protocolos o aplicaciones superiores. <!-- FACT:PN-T39-F055 -->
- Que una función no aparezca como capa separada en TCP/IP no significa que desaparezca. <!-- FACT:PN-T39-F056 -->

### Ejemplos razonados

- **Aplicación correcta:** Puede coordinar puntos de sincronización y recuperación del diálogo.
- **Contraste útil:** En pilas actuales sus funciones suelen integrarse en protocolos o aplicaciones superiores.

### Trampas de examen

- **Incorrecto:** La capa de sesión transmite voltajes.
- **Incorrecto:** TCP/IP exige un protocolo autónomo llamado siempre sesión.

<!-- VISUAL:t39-14-capa-5-sesion.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-14-capa-5-sesion.webp" alt="Capa 5: sesión" width="820">
</p>
<p align="center"><em>Infografía: Capa 5: sesión.</em></p>

:::hablemos-claro
La capa de sesión modela el establecimiento, mantenimiento y cierre de diálogos.
:::

:::en-la-calle
Al aislar un fallo mediante el modelo OSI, La capa de sesión modela el establecimiento, mantenimiento y cierre de diálogos.
:::

:::lo-que-cae
Prioriza **diálogo entre aplicaciones** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: ISO-7498-1-OSI-T39 -->

## 15. Capa 6: presentación

### Lógica del bloque

Para dominar **capa 6: presentación**, aplica esta regla: La capa de presentación trata la sintaxis y representación de la información. El anclaje principal es **representación de datos**.

### Hechos examinables

- La capa de presentación trata la sintaxis y representación de la información. <!-- FACT:PN-T39-F057 -->
- Codificación, transformación de formatos, compresión o cifrado pueden asociarse a esta función. <!-- FACT:PN-T39-F058 -->
- Su objetivo es que entidades con representaciones distintas intercambien datos comprensibles. <!-- FACT:PN-T39-F059 -->
- En Internet estas funciones suelen residir en bibliotecas y protocolos de aplicación. <!-- FACT:PN-T39-F060 -->

### Ejemplos razonados

- **Aplicación correcta:** Codificación, transformación de formatos, compresión o cifrado pueden asociarse a esta función.
- **Contraste útil:** Su objetivo es que entidades con representaciones distintas intercambien datos comprensibles.

### Trampas de examen

- **Incorrecto:** La capa de presentación diseña la interfaz gráfica de la pantalla.
- **Incorrecto:** Todo cifrado pertenece exclusivamente y sin excepción a la capa 6.

<!-- VISUAL:t39-il-15-capa-6-presentacion.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-il-15-capa-6-presentacion.webp" alt="Capa 6: presentación" width="820">
</p>
<p align="center"><em>Infografía: Capa 6: presentación.</em></p>

:::hablemos-claro
La capa de presentación trata la sintaxis y representación de la información.
:::

:::en-la-calle
Al aislar un fallo mediante el modelo OSI, La capa de presentación trata la sintaxis y representación de la información.
:::

:::lo-que-cae
Prioriza **representación de datos** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: ISO-7498-1-OSI-T39 -->

## 16. Capa 7: aplicación

### Lógica del bloque

Para dominar **capa 7: aplicación**, aplica esta regla: La capa de aplicación ofrece servicios de comunicación a procesos de aplicación. El anclaje principal es **servicios para aplicaciones**.

### Hechos examinables

- La capa de aplicación ofrece servicios de comunicación a procesos de aplicación. <!-- FACT:PN-T39-F061 -->
- HTTP, DNS y protocolos de correo son ejemplos habituales de protocolos de aplicación en TCP/IP. <!-- FACT:PN-T39-F062 -->
- Aplicación no significa que el usuario interactúe siempre directamente con el protocolo. <!-- FACT:PN-T39-F063 -->
- La capa de aplicación utiliza servicios de transporte para intercambiar mensajes. <!-- FACT:PN-T39-F064 -->

### Ejemplos razonados

- **Aplicación correcta:** HTTP, DNS y protocolos de correo son ejemplos habituales de protocolos de aplicación en TCP/IP.
- **Contraste útil:** Aplicación no significa que el usuario interactúe siempre directamente con el protocolo.

### Trampas de examen

- **Incorrecto:** La capa de aplicación es el programa completo y no contiene protocolos.
- **Incorrecto:** DNS opera como señal eléctrica de capa física.

<!-- VISUAL:t39-16-capa-7-aplicacion.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-16-capa-7-aplicacion.webp" alt="Capa 7: aplicación" width="820">
</p>
<p align="center"><em>Infografía: Capa 7: aplicación.</em></p>

:::hablemos-claro
La capa de aplicación ofrece servicios de comunicación a procesos de aplicación.
:::

:::en-la-calle
Al aislar un fallo mediante el modelo OSI, La capa de aplicación ofrece servicios de comunicación a procesos de aplicación.
:::

:::lo-que-cae
Prioriza **servicios para aplicaciones** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: ISO-7498-1-OSI-T39 -->

## 17. PDU: bits, tramas, paquetes y segmentos

### Lógica del bloque

Para dominar **pdu: bits, tramas, paquetes y segmentos**, aplica esta regla: Bits es la denominación elemental asociada a la transmisión física. El anclaje principal es **nombre según la capa**.

### Hechos examinables

- Bits es la denominación elemental asociada a la transmisión física. <!-- FACT:PN-T39-F065 -->
- Trama es la unidad habitual de enlace de datos. <!-- FACT:PN-T39-F066 -->
- Paquete o datagrama IP es la unidad habitual de capa de red. <!-- FACT:PN-T39-F067 -->
- Segmento TCP y datagrama UDP son denominaciones usuales de transporte. <!-- FACT:PN-T39-F068 -->

### Ejemplos razonados

- **Aplicación correcta:** Trama es la unidad habitual de enlace de datos.
- **Contraste útil:** Paquete o datagrama IP es la unidad habitual de capa de red.

### Trampas de examen

- **Incorrecto:** Todos los niveles llaman trama a su unidad.
- **Incorrecto:** Un segmento TCP es una señal eléctrica sin cabecera.

<!-- VISUAL:t39-17-pdu-bits-tramas-paquetes-y-segmentos.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-17-pdu-bits-tramas-paquetes-y-segmentos.webp" alt="PDU: bits, tramas, paquetes y segmentos" width="820">
</p>
<p align="center"><em>Infografía: PDU: bits, tramas, paquetes y segmentos.</em></p>

:::hablemos-claro
Bits es la denominación elemental asociada a la transmisión física.
:::

:::en-la-calle
Al aislar un fallo mediante el modelo OSI, Bits es la denominación elemental asociada a la transmisión física.
:::

:::lo-que-cae
Prioriza **nombre según la capa** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: ISO-7498-1-OSI-T39 -->

## 18. Encapsulación en el modelo OSI

### Lógica del bloque

Para dominar **encapsulación en el modelo osi**, aplica esta regla: Cada capa puede añadir su cabecera a la unidad recibida de la superior. El anclaje principal es **datos dentro de datos**.

### Hechos examinables

- Cada capa puede añadir su cabecera a la unidad recibida de la superior. <!-- FACT:PN-T39-F069 -->
- En Ethernet puede existir además un tráiler para detección de errores. <!-- FACT:PN-T39-F070 -->
- El receptor procesa las cabeceras en orden inverso al emisor. <!-- FACT:PN-T39-F071 -->
- La misma carga útil cambia de denominación funcional al atravesar capas. <!-- FACT:PN-T39-F072 -->

### Ejemplos razonados

- **Aplicación correcta:** En Ethernet puede existir además un tráiler para detección de errores.
- **Contraste útil:** El receptor procesa las cabeceras en orden inverso al emisor.

### Trampas de examen

- **Incorrecto:** El receptor añade todas las cabeceras antes de entregar datos.
- **Incorrecto:** El tráiler Ethernet contiene la ruta IP completa.

<!-- VISUAL:t39-18-encapsulacion-en-el-modelo-osi.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-18-encapsulacion-en-el-modelo-osi.webp" alt="Encapsulación en el modelo OSI" width="820">
</p>
<p align="center"><em>Infografía: Encapsulación en el modelo OSI.</em></p>

:::hablemos-claro
Cada capa puede añadir su cabecera a la unidad recibida de la superior.
:::

:::en-la-calle
Al aislar un fallo mediante el modelo OSI, Cada capa puede añadir su cabecera a la unidad recibida de la superior.
:::

:::lo-que-cae
Prioriza **datos dentro de datos** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: ISO-7498-1-OSI-T39 -->

## 19. Dispositivos y capas OSI

### Lógica del bloque

Para dominar **dispositivos y capas osi**, aplica esta regla: Hub y repetidor se asocian principalmente a la capa física. El anclaje principal es **función principal, no etiqueta absoluta**.

### Hechos examinables

- Hub y repetidor se asocian principalmente a la capa física. <!-- FACT:PN-T39-F073 -->
- Bridge y switch Ethernet se asocian principalmente a la capa de enlace. <!-- FACT:PN-T39-F074 -->
- Router se asocia principalmente a la capa de red. <!-- FACT:PN-T39-F075 -->
- Firewall y proxy pueden examinar varias capas según su tecnología. <!-- FACT:PN-T39-F076 -->

### Ejemplos razonados

- **Aplicación correcta:** Bridge y switch Ethernet se asocian principalmente a la capa de enlace.
- **Contraste útil:** Router se asocia principalmente a la capa de red.

### Trampas de examen

- **Incorrecto:** Todo firewall funciona únicamente en capa física.
- **Incorrecto:** Un switch nunca puede incorporar funciones de capa 3.

<!-- VISUAL:t39-19-dispositivos-y-capas-osi.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-19-dispositivos-y-capas-osi.webp" alt="Dispositivos y capas OSI" width="820">
</p>
<p align="center"><em>Infografía: Dispositivos y capas OSI.</em></p>

:::hablemos-claro
Hub y repetidor se asocian principalmente a la capa física.
:::

:::en-la-calle
Al aislar un fallo mediante el modelo OSI, Hub y repetidor se asocian principalmente a la capa física.
:::

:::lo-que-cae
Prioriza **función principal, no etiqueta absoluta** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: ISO-7498-1-OSI-T39 -->

## 20. Diagnóstico por capas

### Lógica del bloque

Para dominar **diagnóstico por capas**, aplica esta regla: La ausencia de enlace físico se investiga antes que la resolución DNS. El anclaje principal es **aislar antes de sustituir**.

### Hechos examinables

- La ausencia de enlace físico se investiga antes que la resolución DNS. <!-- FACT:PN-T39-F077 -->
- Una MAC aprendida no demuestra que exista ruta IP extremo a extremo. <!-- FACT:PN-T39-F078 -->
- Una IP alcanzable no demuestra que el servicio de aplicación responda. <!-- FACT:PN-T39-F079 -->
- El análisis por capas evita atribuir a DNS fallos de cableado o a TCP errores de direccionamiento. <!-- FACT:PN-T39-F080 -->

### Ejemplos razonados

- **Aplicación correcta:** Una MAC aprendida no demuestra que exista ruta IP extremo a extremo.
- **Contraste útil:** Una IP alcanzable no demuestra que el servicio de aplicación responda.

### Trampas de examen

- **Incorrecto:** Si ping responde, toda aplicación funciona necesariamente.
- **Incorrecto:** Un fallo DNS impide que una interfaz tenga enlace físico.

<!-- VISUAL:t39-il-20-diagnostico-por-capas.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-il-20-diagnostico-por-capas.webp" alt="Diagnóstico por capas" width="820">
</p>
<p align="center"><em>Infografía: Diagnóstico por capas.</em></p>

:::hablemos-claro
La ausencia de enlace físico se investiga antes que la resolución DNS.
:::

:::en-la-calle
Al aislar un fallo mediante el modelo OSI, La ausencia de enlace físico se investiga antes que la resolución DNS.
:::

:::lo-que-cae
Prioriza **aislar antes de sustituir** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: ISO-7498-1-OSI-T39 -->

## 21. Finalidad del modelo TCP/IP

### Lógica del bloque

Para dominar **finalidad del modelo tcp/ip**, aplica esta regla: TCP/IP agrupa protocolos usados para interconectar redes y prestar servicios de Internet. El anclaje principal es **pila práctica de Internet**.

### Hechos examinables

- TCP/IP agrupa protocolos usados para interconectar redes y prestar servicios de Internet. <!-- FACT:PN-T39-F081 -->
- El modelo se describe habitualmente mediante capas de aplicación, transporte, Internet y enlace. <!-- FACT:PN-T39-F082 -->
- Algunas obras separan la física y hablan de cinco capas sin cambiar los protocolos básicos. <!-- FACT:PN-T39-F083 -->
- El número de capas citado debe acompañarse del modelo concreto empleado. <!-- FACT:PN-T39-F084 -->

### Ejemplos razonados

- **Aplicación correcta:** El modelo se describe habitualmente mediante capas de aplicación, transporte, Internet y enlace.
- **Contraste útil:** Algunas obras separan la física y hablan de cinco capas sin cambiar los protocolos básicos.

### Trampas de examen

- **Incorrecto:** TCP/IP tiene siempre siete capas idénticas a OSI.
- **Incorrecto:** TCP/IP es únicamente el protocolo TCP.

<!-- VISUAL:t39-21-finalidad-del-modelo-tcp-ip.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-21-finalidad-del-modelo-tcp-ip.webp" alt="Finalidad del modelo TCP/IP" width="820">
</p>
<p align="center"><em>Infografía: Finalidad del modelo TCP/IP.</em></p>

:::hablemos-claro
TCP/IP agrupa protocolos usados para interconectar redes y prestar servicios de Internet.
:::

:::en-la-calle
Al seguir un flujo real de la pila TCP/IP, TCP/IP agrupa protocolos usados para interconectar redes y prestar servicios de Internet.
:::

:::lo-que-cae
Prioriza **pila práctica de Internet** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: RFC1122-HOSTS-T39 -->

## 22. Correspondencia OSI y TCP/IP

### Lógica del bloque

Para dominar **correspondencia osi y tcp/ip**, aplica esta regla: La aplicación TCP/IP agrupa funciones que OSI separa en aplicación, presentación y sesión. El anclaje principal es **aproximación, no identidad**.

### Hechos examinables

- La aplicación TCP/IP agrupa funciones que OSI separa en aplicación, presentación y sesión. <!-- FACT:PN-T39-F085 -->
- La capa de transporte se corresponde de forma aproximada en ambos modelos. <!-- FACT:PN-T39-F086 -->
- La capa Internet se relaciona con la capa de red OSI. <!-- FACT:PN-T39-F087 -->
- El acceso a red TCP/IP reúne funciones de enlace y del medio físico. <!-- FACT:PN-T39-F088 -->

### Ejemplos razonados

- **Aplicación correcta:** La capa de transporte se corresponde de forma aproximada en ambos modelos.
- **Contraste útil:** La capa Internet se relaciona con la capa de red OSI.

### Trampas de examen

- **Incorrecto:** La equivalencia entre ambos modelos es exacta protocolo por protocolo.
- **Incorrecto:** La capa Internet TCP/IP equivale a presentación OSI.

<!-- VISUAL:t39-22-correspondencia-osi-y-tcp-ip.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-22-correspondencia-osi-y-tcp-ip.webp" alt="Correspondencia OSI y TCP/IP" width="820">
</p>
<p align="center"><em>Infografía: Correspondencia OSI y TCP/IP.</em></p>

:::hablemos-claro
La aplicación TCP/IP agrupa funciones que OSI separa en aplicación, presentación y sesión.
:::

:::en-la-calle
Al seguir un flujo real de la pila TCP/IP, La aplicación TCP/IP agrupa funciones que OSI separa en aplicación, presentación y sesión.
:::

:::lo-que-cae
Prioriza **aproximación, no identidad** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: RFC1122-HOSTS-T39 -->

## 23. Capa de aplicación TCP/IP

### Lógica del bloque

Para dominar **capa de aplicación tcp/ip**, aplica esta regla: La capa de aplicación contiene protocolos que soportan servicios para programas y usuarios. El anclaje principal es **protocolos orientados a servicios**.

### Hechos examinables

- La capa de aplicación contiene protocolos que soportan servicios para programas y usuarios. <!-- FACT:PN-T39-F089 -->
- HTTP intercambia representaciones web, DNS resuelve nombres y DHCP configura nodos. <!-- FACT:PN-T39-F090 -->
- Los protocolos de aplicación se apoyan normalmente en TCP o UDP. <!-- FACT:PN-T39-F091 -->
- Un puerto identifica un punto lógico de transporte, no una aplicación de forma absoluta. <!-- FACT:PN-T39-F092 -->

### Ejemplos razonados

- **Aplicación correcta:** HTTP intercambia representaciones web, DNS resuelve nombres y DHCP configura nodos.
- **Contraste útil:** Los protocolos de aplicación se apoyan normalmente en TCP o UDP.

### Trampas de examen

- **Incorrecto:** Todo protocolo de aplicación usa exclusivamente TCP.
- **Incorrecto:** El número de puerto es una dirección IP.

<!-- VISUAL:t39-23-capa-de-aplicacion-tcp-ip.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-23-capa-de-aplicacion-tcp-ip.webp" alt="Capa de aplicación TCP/IP" width="820">
</p>
<p align="center"><em>Infografía: Capa de aplicación TCP/IP.</em></p>

:::hablemos-claro
La capa de aplicación contiene protocolos que soportan servicios para programas y usuarios.
:::

:::en-la-calle
Al seguir un flujo real de la pila TCP/IP, La capa de aplicación contiene protocolos que soportan servicios para programas y usuarios.
:::

:::lo-que-cae
Prioriza **protocolos orientados a servicios** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: RFC1122-HOSTS-T39 -->

## 24. TCP: conexión y fiabilidad

### Lógica del bloque

Para dominar **tcp: conexión y fiabilidad**, aplica esta regla: TCP ofrece a las aplicaciones un flujo fiable y ordenado de bytes. El anclaje principal es **flujo fiable de bytes**.

### Hechos examinables

- TCP ofrece a las aplicaciones un flujo fiable y ordenado de bytes. <!-- FACT:PN-T39-F093 -->
- TCP establece estado de conexión entre los extremos. <!-- FACT:PN-T39-F094 -->
- Números de secuencia, reconocimientos y retransmisión contribuyen a la fiabilidad. <!-- FACT:PN-T39-F095 -->
- TCP incorpora control de flujo y mecanismos de control de congestión en la pila de Internet. <!-- FACT:PN-T39-F096 -->

### Ejemplos razonados

- **Aplicación correcta:** TCP establece estado de conexión entre los extremos.
- **Contraste útil:** Números de secuencia, reconocimientos y retransmisión contribuyen a la fiabilidad.

### Trampas de examen

- **Incorrecto:** TCP preserva necesariamente los límites de cada mensaje de la aplicación.
- **Incorrecto:** TCP elimina toda posibilidad de congestión.

<!-- VISUAL:t39-24-tcp-conexion-y-fiabilidad.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-24-tcp-conexion-y-fiabilidad.webp" alt="TCP: conexión y fiabilidad" width="820">
</p>
<p align="center"><em>Infografía: TCP: conexión y fiabilidad.</em></p>

:::hablemos-claro
TCP ofrece a las aplicaciones un flujo fiable y ordenado de bytes.
:::

:::en-la-calle
Al seguir un flujo real de la pila TCP/IP, TCP ofrece a las aplicaciones un flujo fiable y ordenado de bytes.
:::

:::lo-que-cae
Prioriza **flujo fiable de bytes** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: RFC9293-TCP-T39 -->

## 25. Establecimiento y cierre TCP

### Lógica del bloque

Para dominar **establecimiento y cierre tcp**, aplica esta regla: El establecimiento normal de TCP usa el intercambio SYN, SYN-ACK y ACK. El anclaje principal es **sincronizar antes de transferir**.

### Hechos examinables

- El establecimiento normal de TCP usa el intercambio SYN, SYN-ACK y ACK. <!-- FACT:PN-T39-F097 -->
- El three-way handshake sincroniza números de secuencia y confirma capacidad de comunicación. <!-- FACT:PN-T39-F098 -->
- FIN participa en un cierre ordenado y RST aborta o rechaza una conexión. <!-- FACT:PN-T39-F099 -->
- El cierre de un sentido del flujo no implica siempre el cierre simultáneo del otro. <!-- FACT:PN-T39-F100 -->

### Ejemplos razonados

- **Aplicación correcta:** El three-way handshake sincroniza números de secuencia y confirma capacidad de comunicación.
- **Contraste útil:** FIN participa en un cierre ordenado y RST aborta o rechaza una conexión.

### Trampas de examen

- **Incorrecto:** SYN transmite siempre el archivo completo.
- **Incorrecto:** RST representa un cierre ordenado confirmado por ambas partes.

<!-- VISUAL:t39-il-25-establecimiento-y-cierre-tcp.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-il-25-establecimiento-y-cierre-tcp.webp" alt="Establecimiento y cierre TCP" width="820">
</p>
<p align="center"><em>Infografía: Establecimiento y cierre TCP.</em></p>

:::hablemos-claro
El establecimiento normal de TCP usa el intercambio SYN, SYN-ACK y ACK.
:::

:::en-la-calle
Al seguir un flujo real de la pila TCP/IP, El establecimiento normal de TCP usa el intercambio SYN, SYN-ACK y ACK.
:::

:::lo-que-cae
Prioriza **sincronizar antes de transferir** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: RFC9293-TCP-T39 -->

## 26. UDP: datagramas sin conexión

### Lógica del bloque

Para dominar **udp: datagramas sin conexión**, aplica esta regla: UDP transporta datagramas sin establecer una conexión fiable. El anclaje principal es **mínimo mecanismo de transporte**.

### Hechos examinables

- UDP transporta datagramas sin establecer una conexión fiable. <!-- FACT:PN-T39-F101 -->
- Su cabecera incluye puertos, longitud y suma de comprobación. <!-- FACT:PN-T39-F102 -->
- UDP no garantiza entrega, orden, eliminación de duplicados ni retransmisión. <!-- FACT:PN-T39-F103 -->
- Una aplicación puede añadir sobre UDP los controles que necesite. <!-- FACT:PN-T39-F104 -->

### Ejemplos razonados

- **Aplicación correcta:** Su cabecera incluye puertos, longitud y suma de comprobación.
- **Contraste útil:** UDP no garantiza entrega, orden, eliminación de duplicados ni retransmisión.

### Trampas de examen

- **Incorrecto:** UDP garantiza que los datagramas llegan en orden.
- **Incorrecto:** UDP carece de números de puerto.

<!-- VISUAL:t39-26-udp-datagramas-sin-conexion.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-26-udp-datagramas-sin-conexion.webp" alt="UDP: datagramas sin conexión" width="820">
</p>
<p align="center"><em>Infografía: UDP: datagramas sin conexión.</em></p>

:::hablemos-claro
UDP transporta datagramas sin establecer una conexión fiable.
:::

:::en-la-calle
Al seguir un flujo real de la pila TCP/IP, UDP transporta datagramas sin establecer una conexión fiable.
:::

:::lo-que-cae
Prioriza **mínimo mecanismo de transporte** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: RFC768-UDP-T39 -->

## 27. IP: servicio de datagramas

### Lógica del bloque

Para dominar **ip: servicio de datagramas**, aplica esta regla: IP transporta datagramas entre redes mediante direcciones lógicas. El anclaje principal es **mejor esfuerzo**.

### Hechos examinables

- IP transporta datagramas entre redes mediante direcciones lógicas. <!-- FACT:PN-T39-F105 -->
- El servicio IP básico es no orientado a conexión y de mejor esfuerzo. <!-- FACT:PN-T39-F106 -->
- Los routers reenvían cada paquete según destino y tabla de encaminamiento. <!-- FACT:PN-T39-F107 -->
- La fiabilidad extremo a extremo, cuando se exige, se aporta en otras capas. <!-- FACT:PN-T39-F108 -->

### Ejemplos razonados

- **Aplicación correcta:** El servicio IP básico es no orientado a conexión y de mejor esfuerzo.
- **Contraste útil:** Los routers reenvían cada paquete según destino y tabla de encaminamiento.

### Trampas de examen

- **Incorrecto:** IP establece por sí mismo una sesión fiable antes de cada paquete.
- **Incorrecto:** Un router confirma a la aplicación la entrega de todos los datagramas.

<!-- VISUAL:t39-27-ip-servicio-de-datagramas.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-27-ip-servicio-de-datagramas.webp" alt="IP: servicio de datagramas" width="820">
</p>
<p align="center"><em>Infografía: IP: servicio de datagramas.</em></p>

:::hablemos-claro
IP transporta datagramas entre redes mediante direcciones lógicas.
:::

:::en-la-calle
Al seguir un flujo real de la pila TCP/IP, IP transporta datagramas entre redes mediante direcciones lógicas.
:::

:::lo-que-cae
Prioriza **mejor esfuerzo** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: RFC791-IPV4-T39 -->

## 28. ICMP y el comando ping

### Lógica del bloque

Para dominar **icmp y el comando ping**, aplica esta regla: ICMP comunica determinados errores y condiciones de control asociados a IP. El anclaje principal es **control y diagnóstico**.

### Hechos examinables

- ICMP comunica determinados errores y condiciones de control asociados a IP. <!-- FACT:PN-T39-F109 -->
- Ping utiliza normalmente mensajes ICMP Echo Request y Echo Reply. <!-- FACT:PN-T39-F110 -->
- Una respuesta ICMP no demuestra que todos los puertos o aplicaciones estén disponibles. <!-- FACT:PN-T39-F111 -->
- Bloquear ICMP puede impedir diagnósticos sin significar que el destino esté apagado. <!-- FACT:PN-T39-F112 -->

### Ejemplos razonados

- **Aplicación correcta:** Ping utiliza normalmente mensajes ICMP Echo Request y Echo Reply.
- **Contraste útil:** Una respuesta ICMP no demuestra que todos los puertos o aplicaciones estén disponibles.

### Trampas de examen

- **Incorrecto:** Ping utiliza necesariamente RIP.
- **Incorrecto:** ICMP es un protocolo de transferencia de archivos.

<!-- VISUAL:t39-28-icmp-y-el-comando-ping.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-28-icmp-y-el-comando-ping.webp" alt="ICMP y el comando ping" width="820">
</p>
<p align="center"><em>Infografía: ICMP y el comando ping.</em></p>

:::hablemos-claro
ICMP comunica determinados errores y condiciones de control asociados a IP.
:::

:::en-la-calle
Al seguir un flujo real de la pila TCP/IP, ICMP comunica determinados errores y condiciones de control asociados a IP.
:::

:::lo-que-cae
Prioriza **control y diagnóstico** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: RFC792-ICMP-T39 -->

## 29. ARP en IPv4 y NDP en IPv6

### Lógica del bloque

Para dominar **arp en ipv4 y ndp en ipv6**, aplica esta regla: ARP permite asociar una dirección IPv4 con una dirección de enlace en la red local. El anclaje principal es **resolver vecino local**.

### Hechos examinables

- ARP permite asociar una dirección IPv4 con una dirección de enlace en la red local. <!-- FACT:PN-T39-F113 -->
- IPv6 utiliza Neighbor Discovery basado en ICMPv6, no ARP. <!-- FACT:PN-T39-F114 -->
- La resolución local del vecino es distinta de la resolución DNS de nombres. <!-- FACT:PN-T39-F115 -->
- Para un destino remoto se resuelve normalmente la dirección de enlace del siguiente salto, no la del destino final. <!-- FACT:PN-T39-F116 -->

### Ejemplos razonados

- **Aplicación correcta:** IPv6 utiliza Neighbor Discovery basado en ICMPv6, no ARP.
- **Contraste útil:** La resolución local del vecino es distinta de la resolución DNS de nombres.

### Trampas de examen

- **Incorrecto:** DNS sustituye a ARP dentro de Ethernet.
- **Incorrecto:** Un host busca por ARP la MAC del servidor remoto a través de todos los routers.

<!-- VISUAL:t39-29-arp-en-ipv4-y-ndp-en-ipv6.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-29-arp-en-ipv4-y-ndp-en-ipv6.webp" alt="ARP en IPv4 y NDP en IPv6" width="820">
</p>
<p align="center"><em>Infografía: ARP en IPv4 y NDP en IPv6.</em></p>

:::hablemos-claro
ARP permite asociar una dirección IPv4 con una dirección de enlace en la red local.
:::

:::en-la-calle
Al seguir un flujo real de la pila TCP/IP, ARP permite asociar una dirección IPv4 con una dirección de enlace en la red local.
:::

:::lo-que-cae
Prioriza **resolver vecino local** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: RFC4861-NDP-T39 -->

## 30. Puertos, sockets y multiplexación

### Lógica del bloque

Para dominar **puertos, sockets y multiplexación**, aplica esta regla: Los puertos permiten multiplexar conversaciones de transporte en un host. El anclaje principal es **dirección más transporte**.

### Hechos examinables

- Los puertos permiten multiplexar conversaciones de transporte en un host. <!-- FACT:PN-T39-F117 -->
- Un extremo TCP se identifica mediante una dirección IP y un puerto. <!-- FACT:PN-T39-F118 -->
- Una conexión TCP queda distinguida por direcciones y puertos de ambos extremos. <!-- FACT:PN-T39-F119 -->
- Un puerto conocido es una convención de servicio, no una garantía de la aplicación ejecutada. <!-- FACT:PN-T39-F120 -->

### Ejemplos razonados

- **Aplicación correcta:** Un extremo TCP se identifica mediante una dirección IP y un puerto.
- **Contraste útil:** Una conexión TCP queda distinguida por direcciones y puertos de ambos extremos.

### Trampas de examen

- **Incorrecto:** El puerto 443 convierte automáticamente cualquier tráfico en seguro.
- **Incorrecto:** Dos conexiones TCP son idénticas si comparten solo el puerto de destino.

<!-- VISUAL:t39-il-30-puertos-sockets-y-multiplexacion.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-il-30-puertos-sockets-y-multiplexacion.webp" alt="Puertos, sockets y multiplexación" width="820">
</p>
<p align="center"><em>Infografía: Puertos, sockets y multiplexación.</em></p>

:::hablemos-claro
Los puertos permiten multiplexar conversaciones de transporte en un host.
:::

:::en-la-calle
Al seguir un flujo real de la pila TCP/IP, Los puertos permiten multiplexar conversaciones de transporte en un host.
:::

:::lo-que-cae
Prioriza **dirección más transporte** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: RFC9293-TCP-T39 -->

## 31. Repetidor y concentrador hub

### Lógica del bloque

Para dominar **repetidor y concentrador hub**, aplica esta regla: Un repetidor regenera o repite señales para extender un segmento físico. El anclaje principal es **repetir bits**.

### Hechos examinables

- Un repetidor regenera o repite señales para extender un segmento físico. <!-- FACT:PN-T39-F121 -->
- Un hub multipuerto replica hacia otros puertos la señal recibida. <!-- FACT:PN-T39-F122 -->
- El hub no aprende direcciones MAC ni selecciona un único puerto por destino. <!-- FACT:PN-T39-F123 -->
- Hub y switch no son equivalentes aunque ambos tengan varios puertos. <!-- FACT:PN-T39-F124 -->

### Ejemplos razonados

- **Aplicación correcta:** Un hub multipuerto replica hacia otros puertos la señal recibida.
- **Contraste útil:** El hub no aprende direcciones MAC ni selecciona un único puerto por destino.

### Trampas de examen

- **Incorrecto:** Un hub construye una tabla de rutas IP.
- **Incorrecto:** Un hub envía la trama solo al puerto de la MAC destino aprendida.

<!-- VISUAL:t39-31-repetidor-y-concentrador-hub.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-31-repetidor-y-concentrador-hub.webp" alt="Repetidor y concentrador hub" width="820">
</p>
<p align="center"><em>Infografía: Repetidor y concentrador hub.</em></p>

:::hablemos-claro
Un repetidor regenera o repite señales para extender un segmento físico.
:::

:::en-la-calle
Al observar cómo un hub o un switch mueve tráfico, Un repetidor regenera o repite señales para extender un segmento físico.
:::

:::lo-que-cae
Prioriza **repetir bits** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: IEEE8023-ETHERNET-T39 -->

## 32. Dominio de colisión compartido

### Lógica del bloque

Para dominar **dominio de colisión compartido**, aplica esta regla: Los puertos de un hub comparten el mismo dominio de colisión. El anclaje principal es **un medio lógico común**.

### Hechos examinables

- Los puertos de un hub comparten el mismo dominio de colisión. <!-- FACT:PN-T39-F125 -->
- El ancho de banda del segmento se comparte entre los equipos conectados. <!-- FACT:PN-T39-F126 -->
- La operación clásica con hub es semidúplex y puede requerir CSMA/CD. <!-- FACT:PN-T39-F127 -->
- Un hub no separa el tráfico de broadcast del resto del segmento. <!-- FACT:PN-T39-F128 -->

### Ejemplos razonados

- **Aplicación correcta:** El ancho de banda del segmento se comparte entre los equipos conectados.
- **Contraste útil:** La operación clásica con hub es semidúplex y puede requerir CSMA/CD.

### Trampas de examen

- **Incorrecto:** Cada puerto de un hub crea un dominio de colisión independiente.
- **Incorrecto:** Un hub garantiza full-duplex simultáneo en todos sus puertos.

<!-- VISUAL:t39-32-dominio-de-colision-compartido.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-32-dominio-de-colision-compartido.webp" alt="Dominio de colisión compartido" width="820">
</p>
<p align="center"><em>Infografía: Dominio de colisión compartido.</em></p>

:::hablemos-claro
Los puertos de un hub comparten el mismo dominio de colisión.
:::

:::en-la-calle
Al observar cómo un hub o un switch mueve tráfico, Los puertos de un hub comparten el mismo dominio de colisión.
:::

:::lo-que-cae
Prioriza **un medio lógico común** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: IEEE8023-ETHERNET-T39 -->

## 33. Bridge y switch Ethernet

### Lógica del bloque

Para dominar **bridge y switch ethernet**, aplica esta regla: Un bridge conecta segmentos de capa 2 y filtra o reenvía tramas. El anclaje principal es **conmutar tramas**.

### Hechos examinables

- Un bridge conecta segmentos de capa 2 y filtra o reenvía tramas. <!-- FACT:PN-T39-F129 -->
- Un switch Ethernet es funcionalmente un bridge multipuerto. <!-- FACT:PN-T39-F130 -->
- El switch toma decisiones principalmente con la MAC de destino. <!-- FACT:PN-T39-F131 -->
- La conmutación reduce colisiones respecto de un medio compartido por hub. <!-- FACT:PN-T39-F132 -->

### Ejemplos razonados

- **Aplicación correcta:** Un switch Ethernet es funcionalmente un bridge multipuerto.
- **Contraste útil:** El switch toma decisiones principalmente con la MAC de destino.

### Trampas de examen

- **Incorrecto:** Un switch de capa 2 elige rutas globales por prefijos IP.
- **Incorrecto:** Bridge y hub repiten siempre todas las señales del mismo modo.

<!-- VISUAL:t39-33-bridge-y-switch-ethernet.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-33-bridge-y-switch-ethernet.webp" alt="Bridge y switch Ethernet" width="820">
</p>
<p align="center"><em>Infografía: Bridge y switch Ethernet.</em></p>

:::hablemos-claro
Un bridge conecta segmentos de capa 2 y filtra o reenvía tramas.
:::

:::en-la-calle
Al observar cómo un hub o un switch mueve tráfico, Un bridge conecta segmentos de capa 2 y filtra o reenvía tramas.
:::

:::lo-que-cae
Prioriza **conmutar tramas** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: IEEE8021Q-BRIDGES-T39 -->

## 34. Aprendizaje de la tabla MAC

### Lógica del bloque

Para dominar **aprendizaje de la tabla mac**, aplica esta regla: El switch aprende la asociación entre MAC de origen y puerto de entrada. El anclaje principal es **aprender por el origen**.

### Hechos examinables

- El switch aprende la asociación entre MAC de origen y puerto de entrada. <!-- FACT:PN-T39-F133 -->
- Las entradas dinámicas envejecen para adaptarse a cambios de ubicación. <!-- FACT:PN-T39-F134 -->
- La tabla MAC se denomina también tabla de reenvío o filtrado según el contexto. <!-- FACT:PN-T39-F135 -->
- Aprender una MAC no equivale a asignar una dirección IP mediante DHCP. <!-- FACT:PN-T39-F136 -->

### Ejemplos razonados

- **Aplicación correcta:** Las entradas dinámicas envejecen para adaptarse a cambios de ubicación.
- **Contraste útil:** La tabla MAC se denomina también tabla de reenvío o filtrado según el contexto.

### Trampas de examen

- **Incorrecto:** El switch aprende el puerto mirando solo la MAC de destino.
- **Incorrecto:** La tabla MAC es la zona DNS del conmutador.

<!-- VISUAL:t39-34-aprendizaje-de-la-tabla-mac.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-34-aprendizaje-de-la-tabla-mac.webp" alt="Aprendizaje de la tabla MAC" width="820">
</p>
<p align="center"><em>Infografía: Aprendizaje de la tabla MAC.</em></p>

:::hablemos-claro
El switch aprende la asociación entre MAC de origen y puerto de entrada.
:::

:::en-la-calle
Al observar cómo un hub o un switch mueve tráfico, El switch aprende la asociación entre MAC de origen y puerto de entrada.
:::

:::lo-que-cae
Prioriza **aprender por el origen** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: IEEE8021Q-BRIDGES-T39 -->

## 35. Filtrado, reenvío y flooding

### Lógica del bloque

Para dominar **filtrado, reenvío y flooding**, aplica esta regla: Si el destino conocido está en otro puerto, el switch reenvía hacia ese puerto. El anclaje principal es **tres decisiones**.

### Hechos examinables

- Si el destino conocido está en otro puerto, el switch reenvía hacia ese puerto. <!-- FACT:PN-T39-F137 -->
- Si origen y destino se localizan en el mismo puerto, puede filtrar la trama. <!-- FACT:PN-T39-F138 -->
- Un unicast desconocido se difunde por los puertos pertinentes salvo el de entrada. <!-- FACT:PN-T39-F139 -->
- Broadcast y ciertos multicast también se propagan dentro del dominio correspondiente. <!-- FACT:PN-T39-F140 -->

### Ejemplos razonados

- **Aplicación correcta:** Si origen y destino se localizan en el mismo puerto, puede filtrar la trama.
- **Contraste útil:** Un unicast desconocido se difunde por los puertos pertinentes salvo el de entrada.

### Trampas de examen

- **Incorrecto:** Un destino desconocido hace que el switch descarte siempre la trama.
- **Incorrecto:** Flooding significa enviar la trama de vuelta solo al puerto de entrada.

<!-- VISUAL:t39-il-35-filtrado-reenvio-y-flooding.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-il-35-filtrado-reenvio-y-flooding.webp" alt="Filtrado, reenvío y flooding" width="820">
</p>
<p align="center"><em>Infografía: Filtrado, reenvío y flooding.</em></p>

:::hablemos-claro
Si el destino conocido está en otro puerto, el switch reenvía hacia ese puerto.
:::

:::en-la-calle
Al observar cómo un hub o un switch mueve tráfico, Si el destino conocido está en otro puerto, el switch reenvía hacia ese puerto.
:::

:::lo-que-cae
Prioriza **tres decisiones** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: IEEE8021Q-BRIDGES-T39 -->

## 36. Dominios de colisión y broadcast

### Lógica del bloque

Para dominar **dominios de colisión y broadcast**, aplica esta regla: Cada puerto de switch constituye normalmente un dominio de colisión separado. El anclaje principal es **switch separa colisión; router separa broadcast**.

### Hechos examinables

- Cada puerto de switch constituye normalmente un dominio de colisión separado. <!-- FACT:PN-T39-F141 -->
- Un switch de capa 2 mantiene por defecto un dominio de broadcast por VLAN. <!-- FACT:PN-T39-F142 -->
- Un router separa dominios de broadcast de capa 2. <!-- FACT:PN-T39-F143 -->
- Full-duplex elimina las colisiones Ethernet del enlace punto a punto conmutado. <!-- FACT:PN-T39-F144 -->

### Ejemplos razonados

- **Aplicación correcta:** Un switch de capa 2 mantiene por defecto un dominio de broadcast por VLAN.
- **Contraste útil:** Un router separa dominios de broadcast de capa 2.

### Trampas de examen

- **Incorrecto:** Un switch sin VLAN separa automáticamente cada puerto en un dominio de broadcast.
- **Incorrecto:** Un router une todos los broadcasts Ethernet entre interfaces.

<!-- VISUAL:t39-36-dominios-de-colision-y-broadcast.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-36-dominios-de-colision-y-broadcast.webp" alt="Dominios de colisión y broadcast" width="820">
</p>
<p align="center"><em>Infografía: Dominios de colisión y broadcast.</em></p>

:::hablemos-claro
Cada puerto de switch constituye normalmente un dominio de colisión separado.
:::

:::en-la-calle
Al observar cómo un hub o un switch mueve tráfico, Cada puerto de switch constituye normalmente un dominio de colisión separado.
:::

:::lo-que-cae
Prioriza **switch separa colisión; router separa broadcast** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: IEEE8021Q-BRIDGES-T39 -->

## 37. VLAN y etiquetado

### Lógica del bloque

Para dominar **vlan y etiquetado**, aplica esta regla: Una VLAN crea un dominio lógico de broadcast dentro de una infraestructura conmutada. El anclaje principal es **segmentación lógica de capa 2**.

### Hechos examinables

- Una VLAN crea un dominio lógico de broadcast dentro de una infraestructura conmutada. <!-- FACT:PN-T39-F145 -->
- IEEE 802.1Q define etiquetado para transportar varias VLAN por determinados enlaces. <!-- FACT:PN-T39-F146 -->
- Puertos de acceso y enlaces troncales cumplen funciones diferentes. <!-- FACT:PN-T39-F147 -->
- La comunicación entre VLAN distintas requiere una función de capa 3. <!-- FACT:PN-T39-F148 -->

### Ejemplos razonados

- **Aplicación correcta:** IEEE 802.1Q define etiquetado para transportar varias VLAN por determinados enlaces.
- **Contraste útil:** Puertos de acceso y enlaces troncales cumplen funciones diferentes.

### Trampas de examen

- **Incorrecto:** Una VLAN cifra automáticamente todo el tráfico.
- **Incorrecto:** Dos VLAN distintas se comunican sin encaminamiento por ser del mismo switch.

<!-- VISUAL:t39-37-vlan-y-etiquetado.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-37-vlan-y-etiquetado.webp" alt="VLAN y etiquetado" width="820">
</p>
<p align="center"><em>Infografía: VLAN y etiquetado.</em></p>

:::hablemos-claro
Una VLAN crea un dominio lógico de broadcast dentro de una infraestructura conmutada.
:::

:::en-la-calle
Al observar cómo un hub o un switch mueve tráfico, Una VLAN crea un dominio lógico de broadcast dentro de una infraestructura conmutada.
:::

:::lo-que-cae
Prioriza **segmentación lógica de capa 2** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: IEEE8021Q-BRIDGES-T39 -->

## 38. Bucles y Spanning Tree

### Lógica del bloque

Para dominar **bucles y spanning tree**, aplica esta regla: Un bucle de capa 2 puede multiplicar tramas y causar tormentas de broadcast. El anclaje principal es **redundancia sin tormenta**.

### Hechos examinables

- Un bucle de capa 2 puede multiplicar tramas y causar tormentas de broadcast. <!-- FACT:PN-T39-F149 -->
- Ethernet no incorpora un campo TTL en la trama que extinga por sí solo el bucle. <!-- FACT:PN-T39-F150 -->
- Spanning Tree mantiene una topología lógica sin bucles bloqueando caminos redundantes. <!-- FACT:PN-T39-F151 -->
- La redundancia física puede conservarse aunque no todos los enlaces reenvíen simultáneamente. <!-- FACT:PN-T39-F152 -->

### Ejemplos razonados

- **Aplicación correcta:** Ethernet no incorpora un campo TTL en la trama que extinga por sí solo el bucle.
- **Contraste útil:** Spanning Tree mantiene una topología lógica sin bucles bloqueando caminos redundantes.

### Trampas de examen

- **Incorrecto:** Una trama Ethernet reduce su TTL en cada switch.
- **Incorrecto:** Spanning Tree obliga a eliminar físicamente todos los enlaces redundantes.

<!-- VISUAL:t39-38-bucles-y-spanning-tree.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-38-bucles-y-spanning-tree.webp" alt="Bucles y Spanning Tree" width="820">
</p>
<p align="center"><em>Infografía: Bucles y Spanning Tree.</em></p>

:::hablemos-claro
Un bucle de capa 2 puede multiplicar tramas y causar tormentas de broadcast.
:::

:::en-la-calle
Al observar cómo un hub o un switch mueve tráfico, Un bucle de capa 2 puede multiplicar tramas y causar tormentas de broadcast.
:::

:::lo-que-cae
Prioriza **redundancia sin tormenta** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: IEEE8021Q-BRIDGES-T39 -->

## 39. Función del router

### Lógica del bloque

Para dominar **función del router**, aplica esta regla: Un router conecta redes y reenvía datagramas IP entre interfaces. El anclaje principal es **conectar redes IP**.

### Hechos examinables

- Un router conecta redes y reenvía datagramas IP entre interfaces. <!-- FACT:PN-T39-F153 -->
- La decisión se basa en la dirección IP de destino y la tabla de encaminamiento. <!-- FACT:PN-T39-F154 -->
- El router vuelve a encapsular el paquete en una trama adecuada al siguiente enlace. <!-- FACT:PN-T39-F155 -->
- La MAC de la trama cambia por salto aunque la IP extremo a extremo normalmente se conserve. <!-- FACT:PN-T39-F156 -->

### Ejemplos razonados

- **Aplicación correcta:** La decisión se basa en la dirección IP de destino y la tabla de encaminamiento.
- **Contraste útil:** El router vuelve a encapsular el paquete en una trama adecuada al siguiente enlace.

### Trampas de examen

- **Incorrecto:** El router reenvía siempre la misma trama Ethernet intacta de origen a destino.
- **Incorrecto:** El router decide por el nombre DNS del archivo solicitado.

<!-- VISUAL:t39-39-funcion-del-router.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-39-funcion-del-router.webp" alt="Función del router" width="820">
</p>
<p align="center"><em>Infografía: Función del router.</em></p>

:::hablemos-claro
Un router conecta redes y reenvía datagramas IP entre interfaces.
:::

:::en-la-calle
Al decidir el siguiente salto o aplicar una política, Un router conecta redes y reenvía datagramas IP entre interfaces.
:::

:::lo-que-cae
Prioriza **conectar redes IP** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: RFC1812-ROUTERS-T39 -->

## 40. Tabla de encaminamiento y ruta por defecto

### Lógica del bloque

Para dominar **tabla de encaminamiento y ruta por defecto**, aplica esta regla: Una ruta asocia un prefijo de destino con un siguiente salto o una interfaz. El anclaje principal es **prefijo más específico**.

### Hechos examinables

- Una ruta asocia un prefijo de destino con un siguiente salto o una interfaz. <!-- FACT:PN-T39-F157 -->
- El reenvío selecciona normalmente la coincidencia de prefijo más larga. <!-- FACT:PN-T39-F158 -->
- La ruta por defecto se usa cuando no existe una ruta más específica aplicable. <!-- FACT:PN-T39-F159 -->
- En IPv4 la ruta por defecto se representa como 0.0.0.0/0. <!-- FACT:PN-T39-F160 -->

### Ejemplos razonados

- **Aplicación correcta:** El reenvío selecciona normalmente la coincidencia de prefijo más larga.
- **Contraste útil:** La ruta por defecto se usa cuando no existe una ruta más específica aplicable.

### Trampas de examen

- **Incorrecto:** La primera ruta escrita es siempre la elegida aunque sea menos específica.
- **Incorrecto:** 0.0.0.0/0 coincide solo con la dirección 0.0.0.0.

<!-- VISUAL:t39-il-40-tabla-de-encaminamiento-y-ruta-por-defecto.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-il-40-tabla-de-encaminamiento-y-ruta-por-defecto.webp" alt="Tabla de encaminamiento y ruta por defecto" width="820">
</p>
<p align="center"><em>Infografía: Tabla de encaminamiento y ruta por defecto.</em></p>

:::hablemos-claro
Una ruta asocia un prefijo de destino con un siguiente salto o una interfaz.
:::

:::en-la-calle
Al decidir el siguiente salto o aplicar una política, Una ruta asocia un prefijo de destino con un siguiente salto o una interfaz.
:::

:::lo-que-cae
Prioriza **prefijo más específico** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: RFC1812-ROUTERS-T39 -->

## 41. Siguiente salto, TTL y Hop Limit

### Lógica del bloque

Para dominar **siguiente salto, ttl y hop limit**, aplica esta regla: El siguiente salto es el router o destino vecino al que se entrega el paquete. El anclaje principal es **evitar circulación indefinida**.

### Hechos examinables

- El siguiente salto es el router o destino vecino al que se entrega el paquete. <!-- FACT:PN-T39-F161 -->
- Cada router reduce el TTL de IPv4 antes de reenviar. <!-- FACT:PN-T39-F162 -->
- IPv6 usa Hop Limit con finalidad equivalente. <!-- FACT:PN-T39-F163 -->
- Al agotarse el contador, el paquete se descarta y puede generarse un mensaje ICMP. <!-- FACT:PN-T39-F164 -->

### Ejemplos razonados

- **Aplicación correcta:** Cada router reduce el TTL de IPv4 antes de reenviar.
- **Contraste útil:** IPv6 usa Hop Limit con finalidad equivalente.

### Trampas de examen

- **Incorrecto:** TTL mide el tiempo exacto en segundos que un paquete permanece en Internet.
- **Incorrecto:** Los switches de capa 2 reducen siempre el Hop Limit.

<!-- VISUAL:t39-41-siguiente-salto-ttl-y-hop-limit.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-41-siguiente-salto-ttl-y-hop-limit.webp" alt="Siguiente salto, TTL y Hop Limit" width="820">
</p>
<p align="center"><em>Infografía: Siguiente salto, TTL y Hop Limit.</em></p>

:::hablemos-claro
El siguiente salto es el router o destino vecino al que se entrega el paquete.
:::

:::en-la-calle
Al decidir el siguiente salto o aplicar una política, El siguiente salto es el router o destino vecino al que se entrega el paquete.
:::

:::lo-que-cae
Prioriza **evitar circulación indefinida** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: RFC1812-ROUTERS-T39 -->

## 42. Rutas estáticas y protocolos dinámicos

### Lógica del bloque

Para dominar **rutas estáticas y protocolos dinámicos**, aplica esta regla: Una ruta estática se configura explícitamente y no se aprende por intercambio dinámico. El anclaje principal es **configurar o aprender**.

### Hechos examinables

- Una ruta estática se configura explícitamente y no se aprende por intercambio dinámico. <!-- FACT:PN-T39-F165 -->
- Los protocolos de encaminamiento intercambian información para calcular rutas. <!-- FACT:PN-T39-F166 -->
- RIP, OSPF y BGP responden a diseños y ámbitos distintos. <!-- FACT:PN-T39-F167 -->
- La existencia de una ruta no garantiza que la aplicación de destino esté disponible. <!-- FACT:PN-T39-F168 -->

### Ejemplos razonados

- **Aplicación correcta:** Los protocolos de encaminamiento intercambian información para calcular rutas.
- **Contraste útil:** RIP, OSPF y BGP responden a diseños y ámbitos distintos.

### Trampas de examen

- **Incorrecto:** BGP asigna direcciones MAC a los hosts de una LAN.
- **Incorrecto:** Toda ruta dinámica es necesariamente mejor y más segura que una estática.

<!-- VISUAL:t39-42-rutas-estaticas-y-protocolos-dinamicos.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-42-rutas-estaticas-y-protocolos-dinamicos.webp" alt="Rutas estáticas y protocolos dinámicos" width="820">
</p>
<p align="center"><em>Infografía: Rutas estáticas y protocolos dinámicos.</em></p>

:::hablemos-claro
Una ruta estática se configura explícitamente y no se aprende por intercambio dinámico.
:::

:::en-la-calle
Al decidir el siguiente salto o aplicar una política, Una ruta estática se configura explícitamente y no se aprende por intercambio dinámico.
:::

:::lo-que-cae
Prioriza **configurar o aprender** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: RFC1812-ROUTERS-T39 -->

## 43. NAT y PAT

### Lógica del bloque

Para dominar **nat y pat**, aplica esta regla: NAT modifica direcciones IP al atravesar el traductor. El anclaje principal es **traducir identificadores**.

### Hechos examinables

- NAT modifica direcciones IP al atravesar el traductor. <!-- FACT:PN-T39-F169 -->
- NAPT o PAT distingue múltiples flujos también mediante puertos de transporte. <!-- FACT:PN-T39-F170 -->
- La traducción permite reutilizar direcciones privadas, pero altera la transparencia extremo a extremo. <!-- FACT:PN-T39-F171 -->
- NAT no sustituye por sí solo una política completa de cortafuegos. <!-- FACT:PN-T39-F172 -->

### Ejemplos razonados

- **Aplicación correcta:** NAPT o PAT distingue múltiples flujos también mediante puertos de transporte.
- **Contraste útil:** La traducción permite reutilizar direcciones privadas, pero altera la transparencia extremo a extremo.

### Trampas de examen

- **Incorrecto:** NAT cifra el contenido de todos los paquetes.
- **Incorrecto:** Una dirección privada se vuelve pública sin que el traductor modifique nada.

<!-- VISUAL:t39-43-nat-y-pat.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-43-nat-y-pat.webp" alt="NAT y PAT" width="820">
</p>
<p align="center"><em>Infografía: NAT y PAT.</em></p>

:::hablemos-claro
NAT modifica direcciones IP al atravesar el traductor.
:::

:::en-la-calle
Al decidir el siguiente salto o aplicar una política, NAT modifica direcciones IP al atravesar el traductor.
:::

:::lo-que-cae
Prioriza **traducir identificadores** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: RFC3022-NAT-T39 -->

## 44. Concepto y política de firewall

### Lógica del bloque

Para dominar **concepto y política de firewall**, aplica esta regla: Un firewall es un dispositivo o programa que controla tráfico entre redes o hosts con posturas de seguridad diferentes. El anclaje principal es **controlar flujo por reglas**.

### Hechos examinables

- Un firewall es un dispositivo o programa que controla tráfico entre redes o hosts con posturas de seguridad diferentes. <!-- FACT:PN-T39-F173 -->
- La política define qué tráfico se permite o bloquea según criterios establecidos. <!-- FACT:PN-T39-F174 -->
- La regla de denegación por defecto permite solo lo expresamente autorizado. <!-- FACT:PN-T39-F175 -->
- Un firewall mal configurado no aporta protección efectiva por el mero hecho de existir. <!-- FACT:PN-T39-F176 -->

### Ejemplos razonados

- **Aplicación correcta:** La política define qué tráfico se permite o bloquea según criterios establecidos.
- **Contraste útil:** La regla de denegación por defecto permite solo lo expresamente autorizado.

### Trampas de examen

- **Incorrecto:** Firewall significa necesariamente antivirus.
- **Incorrecto:** Toda política segura debe permitir por defecto cualquier tráfico desconocido.

<!-- VISUAL:t39-44-concepto-y-politica-de-firewall.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-44-concepto-y-politica-de-firewall.webp" alt="Concepto y política de firewall" width="820">
</p>
<p align="center"><em>Infografía: Concepto y política de firewall.</em></p>

:::hablemos-claro
Un firewall es un dispositivo o programa que controla tráfico entre redes o hosts con posturas de seguridad diferentes.
:::

:::en-la-calle
Al decidir el siguiente salto o aplicar una política, Un firewall es un dispositivo o programa que controla tráfico entre redes o hosts con posturas de seguridad diferentes.
:::

:::lo-que-cae
Prioriza **controlar flujo por reglas** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: NIST-SP800-41R1-T39 -->

## 45. Filtrado de paquetes y estado

### Lógica del bloque

Para dominar **filtrado de paquetes y estado**, aplica esta regla: El filtrado de paquetes evalúa campos como direcciones, protocolos y puertos. El anclaje principal es **cabeceras frente a contexto**.

### Hechos examinables

- El filtrado de paquetes evalúa campos como direcciones, protocolos y puertos. <!-- FACT:PN-T39-F177 -->
- La inspección con estado mantiene contexto sobre conexiones o flujos. <!-- FACT:PN-T39-F178 -->
- El estado permite distinguir respuestas asociadas de tráfico nuevo no solicitado. <!-- FACT:PN-T39-F179 -->
- Ni el filtrado simple ni el estado comprenden necesariamente toda la semántica de la aplicación. <!-- FACT:PN-T39-F180 -->

### Ejemplos razonados

- **Aplicación correcta:** La inspección con estado mantiene contexto sobre conexiones o flujos.
- **Contraste útil:** El estado permite distinguir respuestas asociadas de tráfico nuevo no solicitado.

### Trampas de examen

- **Incorrecto:** Un firewall con estado solo mira la dirección MAC.
- **Incorrecto:** Mantener estado equivale a descifrar siempre el contenido cifrado.

<!-- VISUAL:t39-il-45-filtrado-de-paquetes-y-estado.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-il-45-filtrado-de-paquetes-y-estado.webp" alt="Filtrado de paquetes y estado" width="820">
</p>
<p align="center"><em>Infografía: Filtrado de paquetes y estado.</em></p>

:::hablemos-claro
El filtrado de paquetes evalúa campos como direcciones, protocolos y puertos.
:::

:::en-la-calle
Al decidir el siguiente salto o aplicar una política, El filtrado de paquetes evalúa campos como direcciones, protocolos y puertos.
:::

:::lo-que-cae
Prioriza **cabeceras frente a contexto** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: NIST-SP800-41R1-T39 -->

## 46. Proxy firewall, UTM y defensa en profundidad

### Lógica del bloque

Para dominar **proxy firewall, utm y defensa en profundidad**, aplica esta regla: Un proxy de aplicación termina una conversación y origina otra como intermediario. El anclaje principal es **intermediación y funciones combinadas**.

### Hechos examinables

- Un proxy de aplicación termina una conversación y origina otra como intermediario. <!-- FACT:PN-T39-F181 -->
- Un firewall proxy puede inspeccionar información específica del protocolo de aplicación. <!-- FACT:PN-T39-F182 -->
- UTM integra varias funciones de seguridad en una plataforma, sin convertirlas en una sola técnica. <!-- FACT:PN-T39-F183 -->
- La defensa en profundidad no debe depender exclusivamente de un único firewall perimetral. <!-- FACT:PN-T39-F184 -->

### Ejemplos razonados

- **Aplicación correcta:** Un firewall proxy puede inspeccionar información específica del protocolo de aplicación.
- **Contraste útil:** UTM integra varias funciones de seguridad en una plataforma, sin convertirlas en una sola técnica.

### Trampas de examen

- **Incorrecto:** Proxy y router trabajan necesariamente al mismo nivel de la pila.
- **Incorrecto:** UTM garantiza seguridad completa sin actualización ni política.

<!-- VISUAL:t39-46-proxy-firewall-utm-y-defensa-en-profundidad.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-46-proxy-firewall-utm-y-defensa-en-profundidad.webp" alt="Proxy firewall, UTM y defensa en profundidad" width="820">
</p>
<p align="center"><em>Infografía: Proxy firewall, UTM y defensa en profundidad.</em></p>

:::hablemos-claro
Un proxy de aplicación termina una conversación y origina otra como intermediario.
:::

:::en-la-calle
Al decidir el siguiente salto o aplicar una política, Un proxy de aplicación termina una conversación y origina otra como intermediario.
:::

:::lo-que-cae
Prioriza **intermediación y funciones combinadas** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: NIST-SP800-41R1-T39 -->

## 47. Finalidad y actores de DHCPv4

### Lógica del bloque

Para dominar **finalidad y actores de dhcpv4**, aplica esta regla: DHCPv4 permite entregar parámetros de configuración a clientes de forma automática. El anclaje principal es **cliente, servidor y relay**.

### Hechos examinables

- DHCPv4 permite entregar parámetros de configuración a clientes de forma automática. <!-- FACT:PN-T39-F185 -->
- El cliente solicita configuración y el servidor ofrece o asigna valores. <!-- FACT:PN-T39-F186 -->
- Un relay reenvía mensajes DHCP entre subredes cuando el servidor no está en el enlace local. <!-- FACT:PN-T39-F187 -->
- DHCP puede proporcionar dirección, máscara, router y servidores DNS, entre otras opciones. <!-- FACT:PN-T39-F188 -->

### Ejemplos razonados

- **Aplicación correcta:** El cliente solicita configuración y el servidor ofrece o asigna valores.
- **Contraste útil:** Un relay reenvía mensajes DHCP entre subredes cuando el servidor no está en el enlace local.

### Trampas de examen

- **Incorrecto:** DHCP traduce nombres de dominio a direcciones IP.
- **Incorrecto:** Un relay DHCP es el servidor que almacena necesariamente todas las concesiones.

<!-- VISUAL:t39-47-finalidad-y-actores-de-dhcpv4.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-47-finalidad-y-actores-de-dhcpv4.webp" alt="Finalidad y actores de DHCPv4" width="820">
</p>
<p align="center"><em>Infografía: Finalidad y actores de DHCPv4.</em></p>

:::hablemos-claro
DHCPv4 permite entregar parámetros de configuración a clientes de forma automática.
:::

:::en-la-calle
Al configurar o diagnosticar DHCP, DNS y proxy, DHCPv4 permite entregar parámetros de configuración a clientes de forma automática.
:::

:::lo-que-cae
Prioriza **cliente, servidor y relay** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: RFC2131-DHCP-T39 -->

## 48. DORA: descubrimiento y concesión

### Lógica del bloque

Para dominar **dora: descubrimiento y concesión**, aplica esta regla: DHCPDISCOVER permite al cliente localizar servidores disponibles. El anclaje principal es **Discover, Offer, Request, Ack**.

### Hechos examinables

- DHCPDISCOVER permite al cliente localizar servidores disponibles. <!-- FACT:PN-T39-F189 -->
- DHCPOFFER comunica una oferta de configuración. <!-- FACT:PN-T39-F190 -->
- DHCPREQUEST identifica la oferta solicitada o renueva una concesión. <!-- FACT:PN-T39-F191 -->
- DHCPACK confirma los parámetros concedidos; DHCPNAK puede rechazar una solicitud inválida. <!-- FACT:PN-T39-F192 -->

### Ejemplos razonados

- **Aplicación correcta:** DHCPOFFER comunica una oferta de configuración.
- **Contraste útil:** DHCPREQUEST identifica la oferta solicitada o renueva una concesión.

### Trampas de examen

- **Incorrecto:** DORA termina con una consulta DNS.
- **Incorrecto:** DHCPACK es el primer mensaje enviado por un cliente sin configuración.

<!-- VISUAL:t39-48-dora-descubrimiento-y-concesion.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-48-dora-descubrimiento-y-concesion.webp" alt="DORA: descubrimiento y concesión" width="820">
</p>
<p align="center"><em>Infografía: DORA: descubrimiento y concesión.</em></p>

:::hablemos-claro
DHCPDISCOVER permite al cliente localizar servidores disponibles.
:::

:::en-la-calle
Al configurar o diagnosticar DHCP, DNS y proxy, DHCPDISCOVER permite al cliente localizar servidores disponibles.
:::

:::lo-que-cae
Prioriza **Discover, Offer, Request, Ack** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: RFC2131-DHCP-T39 -->

## 49. Concesión, renovación y reserva DHCP

### Lógica del bloque

Para dominar **concesión, renovación y reserva dhcp**, aplica esta regla: Una concesión DHCP asigna parámetros durante un intervalo administrado. El anclaje principal es **configuración temporal o vinculada**.

### Hechos examinables

- Una concesión DHCP asigna parámetros durante un intervalo administrado. <!-- FACT:PN-T39-F193 -->
- El cliente intenta renovar antes de que expire la concesión. <!-- FACT:PN-T39-F194 -->
- Una reserva vincula administrativamente un cliente identificado con una dirección prevista. <!-- FACT:PN-T39-F195 -->
- Dirección dinámica y dirección aleatoria no son sinónimos. <!-- FACT:PN-T39-F196 -->

### Ejemplos razonados

- **Aplicación correcta:** El cliente intenta renovar antes de que expire la concesión.
- **Contraste útil:** Una reserva vincula administrativamente un cliente identificado con una dirección prevista.

### Trampas de examen

- **Incorrecto:** Una concesión DHCP nunca caduca.
- **Incorrecto:** Una reserva impide que el cliente use protocolo DHCP.

<!-- VISUAL:t39-49-concesion-renovacion-y-reserva-dhcp.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-49-concesion-renovacion-y-reserva-dhcp.webp" alt="Concesión, renovación y reserva DHCP" width="820">
</p>
<p align="center"><em>Infografía: Concesión, renovación y reserva DHCP.</em></p>

:::hablemos-claro
Una concesión DHCP asigna parámetros durante un intervalo administrado.
:::

:::en-la-calle
Al configurar o diagnosticar DHCP, DNS y proxy, Una concesión DHCP asigna parámetros durante un intervalo administrado.
:::

:::lo-que-cae
Prioriza **configuración temporal o vinculada** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: RFC2131-DHCP-T39 -->

## 50. Broadcast, relay y autoconfiguración IPv4

### Lógica del bloque

Para dominar **broadcast, relay y autoconfiguración ipv4**, aplica esta regla: Un cliente IPv4 sin dirección puede utilizar broadcast para iniciar DHCP. El anclaje principal es **arrancar sin conocer la red**.

### Hechos examinables

- Un cliente IPv4 sin dirección puede utilizar broadcast para iniciar DHCP. <!-- FACT:PN-T39-F197 -->
- Los routers no reenvían broadcasts locales de forma ordinaria; el relay resuelve ese límite. <!-- FACT:PN-T39-F198 -->
- 169.254.0.0/16 está reservado para direccionamiento link-local IPv4. <!-- FACT:PN-T39-F199 -->
- Una dirección link-local no sustituye una configuración enrutable completa. <!-- FACT:PN-T39-F200 -->

### Ejemplos razonados

- **Aplicación correcta:** Los routers no reenvían broadcasts locales de forma ordinaria; el relay resuelve ese límite.
- **Contraste útil:** 169.254.0.0/16 está reservado para direccionamiento link-local IPv4.

### Trampas de examen

- **Incorrecto:** Los broadcasts DHCP atraviesan todos los routers por defecto.
- **Incorrecto:** 169.254.0.0/16 es un rango público global.

<!-- VISUAL:t39-il-50-broadcast-relay-y-autoconfiguracion-ipv4.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-il-50-broadcast-relay-y-autoconfiguracion-ipv4.webp" alt="Broadcast, relay y autoconfiguración IPv4" width="820">
</p>
<p align="center"><em>Infografía: Broadcast, relay y autoconfiguración IPv4.</em></p>

:::hablemos-claro
Un cliente IPv4 sin dirección puede utilizar broadcast para iniciar DHCP.
:::

:::en-la-calle
Al configurar o diagnosticar DHCP, DNS y proxy, Un cliente IPv4 sin dirección puede utilizar broadcast para iniciar DHCP.
:::

:::lo-que-cae
Prioriza **arrancar sin conocer la red** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: RFC2131-DHCP-T39 -->

## 51. DHCPv6 y SLAAC

### Lógica del bloque

Para dominar **dhcpv6 y slaac**, aplica esta regla: DHCPv6 puede proporcionar direcciones, prefijos y parámetros de configuración. El anclaje principal es **mecanismos compatibles, no idénticos**.

### Hechos examinables

- DHCPv6 puede proporcionar direcciones, prefijos y parámetros de configuración. <!-- FACT:PN-T39-F201 -->
- SLAAC permite formar direcciones a partir de anuncios de router sin asignación DHCPv6 con estado. <!-- FACT:PN-T39-F202 -->
- DHCPv6 puede operar con estado o sin estado y coexistir con SLAAC. <!-- FACT:PN-T39-F203 -->
- En 2026 la especificación vigente de DHCPv6 es RFC 9915, que reemplaza RFC 8415. <!-- FACT:PN-T39-F204 -->

### Ejemplos razonados

- **Aplicación correcta:** SLAAC permite formar direcciones a partir de anuncios de router sin asignación DHCPv6 con estado.
- **Contraste útil:** DHCPv6 puede operar con estado o sin estado y coexistir con SLAAC.

### Trampas de examen

- **Incorrecto:** IPv6 solo puede configurarse mediante DHCPv6.
- **Incorrecto:** DHCPv6 utiliza exactamente los mensajes DORA de DHCPv4.

<!-- VISUAL:t39-51-dhcpv6-y-slaac.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-51-dhcpv6-y-slaac.webp" alt="DHCPv6 y SLAAC" width="820">
</p>
<p align="center"><em>Infografía: DHCPv6 y SLAAC.</em></p>

:::hablemos-claro
DHCPv6 puede proporcionar direcciones, prefijos y parámetros de configuración.
:::

:::en-la-calle
Al configurar o diagnosticar DHCP, DNS y proxy, DHCPv6 puede proporcionar direcciones, prefijos y parámetros de configuración.
:::

:::lo-que-cae
Prioriza **mecanismos compatibles, no idénticos** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: RFC9915-DHCPV6-T39 -->

## 52. Espacio de nombres DNS

### Lógica del bloque

Para dominar **espacio de nombres dns**, aplica esta regla: DNS organiza nombres en un espacio jerárquico distribuido. El anclaje principal es **jerarquía distribuida**.

### Hechos examinables

- DNS organiza nombres en un espacio jerárquico distribuido. <!-- FACT:PN-T39-F205 -->
- La raíz se sitúa sobre dominios de nivel superior y dominios delegados. <!-- FACT:PN-T39-F206 -->
- Una zona es una porción administrada del espacio de nombres. <!-- FACT:PN-T39-F207 -->
- Dominio y zona se relacionan, pero no son necesariamente idénticos. <!-- FACT:PN-T39-F208 -->

### Ejemplos razonados

- **Aplicación correcta:** La raíz se sitúa sobre dominios de nivel superior y dominios delegados.
- **Contraste útil:** Una zona es una porción administrada del espacio de nombres.

### Trampas de examen

- **Incorrecto:** DNS es una única tabla mundial almacenada en un servidor.
- **Incorrecto:** Toda zona contiene siempre todos los subdominios descendientes.

<!-- VISUAL:t39-52-espacio-de-nombres-dns.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-52-espacio-de-nombres-dns.webp" alt="Espacio de nombres DNS" width="820">
</p>
<p align="center"><em>Infografía: Espacio de nombres DNS.</em></p>

:::hablemos-claro
DNS organiza nombres en un espacio jerárquico distribuido.
:::

:::en-la-calle
Al configurar o diagnosticar DHCP, DNS y proxy, DNS organiza nombres en un espacio jerárquico distribuido.
:::

:::lo-que-cae
Prioriza **jerarquía distribuida** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: RFC1034-DNS-T39 -->

## 53. Registros DNS principales

### Lógica del bloque

Para dominar **registros dns principales**, aplica esta regla: A asocia un nombre con una dirección IPv4 y AAAA con una dirección IPv6. El anclaje principal es **nombre, tipo y datos**.

### Hechos examinables

- A asocia un nombre con una dirección IPv4 y AAAA con una dirección IPv6. <!-- FACT:PN-T39-F209 -->
- NS identifica servidores autorizados para una zona. <!-- FACT:PN-T39-F210 -->
- MX indica intercambiadores de correo y CNAME crea un alias canónico. <!-- FACT:PN-T39-F211 -->
- PTR se usa habitualmente en resolución inversa y TXT transporta texto asociado a un nombre. <!-- FACT:PN-T39-F212 -->

### Ejemplos razonados

- **Aplicación correcta:** NS identifica servidores autorizados para una zona.
- **Contraste útil:** MX indica intercambiadores de correo y CNAME crea un alias canónico.

### Trampas de examen

- **Incorrecto:** Un registro A contiene una dirección IPv6.
- **Incorrecto:** CNAME es un registro de ruta por defecto.

<!-- VISUAL:t39-53-registros-dns-principales.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-53-registros-dns-principales.webp" alt="Registros DNS principales" width="820">
</p>
<p align="center"><em>Infografía: Registros DNS principales.</em></p>

:::hablemos-claro
A asocia un nombre con una dirección IPv4 y AAAA con una dirección IPv6.
:::

:::en-la-calle
Al configurar o diagnosticar DHCP, DNS y proxy, A asocia un nombre con una dirección IPv4 y AAAA con una dirección IPv6.
:::

:::lo-que-cae
Prioriza **nombre, tipo y datos** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: RFC1035-DNS-T39 -->

## 54. Consulta recursiva e iterativa

### Lógica del bloque

Para dominar **consulta recursiva e iterativa**, aplica esta regla: En una consulta recursiva el servidor consultado debe devolver una respuesta final o un error. El anclaje principal es **quién continúa la búsqueda**.

### Hechos examinables

- En una consulta recursiva el servidor consultado debe devolver una respuesta final o un error. <!-- FACT:PN-T39-F213 -->
- En una consulta iterativa el servidor puede remitir al consultante hacia otra autoridad. <!-- FACT:PN-T39-F214 -->
- Los resolvers recursivos consultan la jerarquía en nombre de clientes stub. <!-- FACT:PN-T39-F215 -->
- Recursión y autoridad son funciones diferentes que pueden coexistir o separarse. <!-- FACT:PN-T39-F216 -->

### Ejemplos razonados

- **Aplicación correcta:** En una consulta iterativa el servidor puede remitir al consultante hacia otra autoridad.
- **Contraste útil:** Los resolvers recursivos consultan la jerarquía en nombre de clientes stub.

### Trampas de examen

- **Incorrecto:** Una respuesta iterativa obliga al servidor a consultar toda la jerarquía por el cliente.
- **Incorrecto:** Todo servidor autoritativo debe ofrecer recursión pública.

<!-- VISUAL:t39-54-consulta-recursiva-e-iterativa.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-54-consulta-recursiva-e-iterativa.webp" alt="Consulta recursiva e iterativa" width="820">
</p>
<p align="center"><em>Infografía: Consulta recursiva e iterativa.</em></p>

:::hablemos-claro
En una consulta recursiva el servidor consultado debe devolver una respuesta final o un error.
:::

:::en-la-calle
Al configurar o diagnosticar DHCP, DNS y proxy, En una consulta recursiva el servidor consultado debe devolver una respuesta final o un error.
:::

:::lo-que-cae
Prioriza **quién continúa la búsqueda** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: RFC1034-DNS-T39 -->

## 55. Servidores autoritativos, primario y secundario

### Lógica del bloque

Para dominar **servidores autoritativos, primario y secundario**, aplica esta regla: Un servidor autoritativo responde con datos de las zonas para las que tiene autoridad. El anclaje principal es **autoridad y transferencia de zona**.

### Hechos examinables

- Un servidor autoritativo responde con datos de las zonas para las que tiene autoridad. <!-- FACT:PN-T39-F217 -->
- Primario y secundario describen cómo obtiene el servidor los datos de zona, no distinta autoridad del nombre. <!-- FACT:PN-T39-F218 -->
- El secundario puede obtener la zona mediante transferencia desde otro servidor autorizado. <!-- FACT:PN-T39-F219 -->
- Un resolver de caché no se convierte en autoritativo por almacenar temporalmente una respuesta. <!-- FACT:PN-T39-F220 -->

### Ejemplos razonados

- **Aplicación correcta:** Primario y secundario describen cómo obtiene el servidor los datos de zona, no distinta autoridad del nombre.
- **Contraste útil:** El secundario puede obtener la zona mediante transferencia desde otro servidor autorizado.

### Trampas de examen

- **Incorrecto:** El servidor secundario ofrece respuestas menos oficiales que el primario.
- **Incorrecto:** Toda respuesta en caché implica autoridad sobre la zona.

<!-- VISUAL:t39-il-55-servidores-autoritativos-primario-y-secundario.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-il-55-servidores-autoritativos-primario-y-secundario.webp" alt="Servidores autoritativos, primario y secundario" width="820">
</p>
<p align="center"><em>Infografía: Servidores autoritativos, primario y secundario.</em></p>

:::hablemos-claro
Un servidor autoritativo responde con datos de las zonas para las que tiene autoridad.
:::

:::en-la-calle
Al configurar o diagnosticar DHCP, DNS y proxy, Un servidor autoritativo responde con datos de las zonas para las que tiene autoridad.
:::

:::lo-que-cae
Prioriza **autoridad y transferencia de zona** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: RFC8499-DNS-TERMS-T39 -->

## 56. Caché, TTL y transporte DNS

### Lógica del bloque

Para dominar **caché, ttl y transporte dns**, aplica esta regla: El TTL de un registro limita cuánto tiempo puede conservarse en caché. El anclaje principal es **reutilizar sin eternizar**.

### Hechos examinables

- El TTL de un registro limita cuánto tiempo puede conservarse en caché. <!-- FACT:PN-T39-F221 -->
- La caché reduce latencia y carga de consultas repetidas. <!-- FACT:PN-T39-F222 -->
- DNS usa tradicionalmente el puerto 53 y puede operar sobre UDP o TCP. <!-- FACT:PN-T39-F223 -->
- TCP no se limita hoy únicamente a transferencias de zona; el tamaño y otras condiciones también influyen. <!-- FACT:PN-T39-F224 -->

### Ejemplos razonados

- **Aplicación correcta:** La caché reduce latencia y carga de consultas repetidas.
- **Contraste útil:** DNS usa tradicionalmente el puerto 53 y puede operar sobre UDP o TCP.

### Trampas de examen

- **Incorrecto:** El TTL indica la distancia en saltos hasta el servidor.
- **Incorrecto:** DNS funciona exclusivamente mediante UDP.

<!-- VISUAL:t39-56-cache-ttl-y-transporte-dns.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-56-cache-ttl-y-transporte-dns.webp" alt="Caché, TTL y transporte DNS" width="820">
</p>
<p align="center"><em>Infografía: Caché, TTL y transporte DNS.</em></p>

:::hablemos-claro
El TTL de un registro limita cuánto tiempo puede conservarse en caché.
:::

:::en-la-calle
Al configurar o diagnosticar DHCP, DNS y proxy, El TTL de un registro limita cuánto tiempo puede conservarse en caché.
:::

:::lo-que-cae
Prioriza **reutilizar sin eternizar** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: RFC1035-DNS-T39 -->

## 57. Proxy directo o forward proxy

### Lógica del bloque

Para dominar **proxy directo o forward proxy**, aplica esta regla: Un forward proxy actúa en nombre del cliente frente a servidores de destino. El anclaje principal es **intermediario del cliente**.

### Hechos examinables

- Un forward proxy actúa en nombre del cliente frente a servidores de destino. <!-- FACT:PN-T39-F225 -->
- Puede aplicar control de acceso, registro, filtrado o caché según su diseño. <!-- FACT:PN-T39-F226 -->
- El cliente puede estar configurado explícitamente para utilizarlo. <!-- FACT:PN-T39-F227 -->
- Un proxy de aplicación no es simplemente la parte software de cualquier router. <!-- FACT:PN-T39-F228 -->

### Ejemplos razonados

- **Aplicación correcta:** Puede aplicar control de acceso, registro, filtrado o caché según su diseño.
- **Contraste útil:** El cliente puede estar configurado explícitamente para utilizarlo.

### Trampas de examen

- **Incorrecto:** Todo proxy es un dispositivo físico independiente.
- **Incorrecto:** Un forward proxy representa al servidor de origen ante Internet.

<!-- VISUAL:t39-57-proxy-directo-o-forward-proxy.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-57-proxy-directo-o-forward-proxy.webp" alt="Proxy directo o forward proxy" width="820">
</p>
<p align="center"><em>Infografía: Proxy directo o forward proxy.</em></p>

:::hablemos-claro
Un forward proxy actúa en nombre del cliente frente a servidores de destino.
:::

:::en-la-calle
Al configurar o diagnosticar DHCP, DNS y proxy, Un forward proxy actúa en nombre del cliente frente a servidores de destino.
:::

:::lo-que-cae
Prioriza **intermediario del cliente** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: RFC9110-HTTP-T39 -->

## 58. Reverse proxy, caché y túnel

### Lógica del bloque

Para dominar **reverse proxy, caché y túnel**, aplica esta regla: Un reverse proxy recibe solicitudes en nombre de uno o varios servidores de origen. El anclaje principal es **intermediario delante del servidor**.

### Hechos examinables

- Un reverse proxy recibe solicitudes en nombre de uno o varios servidores de origen. <!-- FACT:PN-T39-F229 -->
- Puede distribuir carga, terminar TLS, ocultar orígenes o aplicar controles. <!-- FACT:PN-T39-F230 -->
- Una caché reutiliza respuestas solo bajo reglas de validez aplicables. <!-- FACT:PN-T39-F231 -->
- El método CONNECT permite establecer un túnel a través de un intermediario HTTP cuando está autorizado. <!-- FACT:PN-T39-F232 -->

### Ejemplos razonados

- **Aplicación correcta:** Puede distribuir carga, terminar TLS, ocultar orígenes o aplicar controles.
- **Contraste útil:** Una caché reutiliza respuestas solo bajo reglas de validez aplicables.

### Trampas de examen

- **Incorrecto:** Un reverse proxy representa al cliente dentro de su red local.
- **Incorrecto:** Toda respuesta HTTP puede almacenarse indefinidamente en caché.

<!-- VISUAL:t39-58-reverse-proxy-cache-y-tunel.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-58-reverse-proxy-cache-y-tunel.webp" alt="Reverse proxy, caché y túnel" width="820">
</p>
<p align="center"><em>Infografía: Reverse proxy, caché y túnel.</em></p>

:::hablemos-claro
Un reverse proxy recibe solicitudes en nombre de uno o varios servidores de origen.
:::

:::en-la-calle
Al configurar o diagnosticar DHCP, DNS y proxy, Un reverse proxy recibe solicitudes en nombre de uno o varios servidores de origen.
:::

:::lo-que-cae
Prioriza **intermediario delante del servidor** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: RFC9110-HTTP-T39 -->

## 59. Formato y longitud de IPv4

### Lógica del bloque

Para dominar **formato y longitud de ipv4**, aplica esta regla: Una dirección IPv4 tiene 32 bits. El anclaje principal es **32 bits en cuatro octetos**.

### Hechos examinables

- Una dirección IPv4 tiene 32 bits. <!-- FACT:PN-T39-F233 -->
- La notación habitual usa cuatro octetos decimales separados por puntos. <!-- FACT:PN-T39-F234 -->
- Cada octeto representa un valor entre 0 y 255. <!-- FACT:PN-T39-F235 -->
- La validez sintáctica de una dirección no demuestra que sea asignable o enrutable globalmente. <!-- FACT:PN-T39-F236 -->

### Ejemplos razonados

- **Aplicación correcta:** La notación habitual usa cuatro octetos decimales separados por puntos.
- **Contraste útil:** Cada octeto representa un valor entre 0 y 255.

### Trampas de examen

- **Incorrecto:** IPv4 tiene 128 bits.
- **Incorrecto:** Cualquier combinación 0-255 identifica una conexión pública válida.

<!-- VISUAL:t39-59-formato-y-longitud-de-ipv4.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-59-formato-y-longitud-de-ipv4.webp" alt="Formato y longitud de IPv4" width="820">
</p>
<p align="center"><em>Infografía: Formato y longitud de IPv4.</em></p>

:::hablemos-claro
Una dirección IPv4 tiene 32 bits.
:::

:::en-la-calle
Al calcular una red IPv4 o interpretar una clase histórica, Una dirección IPv4 tiene 32 bits.
:::

:::lo-que-cae
Prioriza **32 bits en cuatro octetos** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: RFC791-IPV4-T39 -->

## 60. Prefijo, host y máscara de subred

### Lógica del bloque

Para dominar **prefijo, host y máscara de subred**, aplica esta regla: El prefijo identifica la parte de red usada para el encaminamiento. El anclaje principal es **unos de red y ceros de host**.

### Hechos examinables

- El prefijo identifica la parte de red usada para el encaminamiento. <!-- FACT:PN-T39-F237 -->
- La longitud /n indica cuántos bits iniciales pertenecen al prefijo. <!-- FACT:PN-T39-F238 -->
- Una máscara IPv4 representa el prefijo con unos contiguos seguidos de ceros. <!-- FACT:PN-T39-F239 -->
- Dos hosts están en la misma subred lógica cuando sus prefijos calculados coinciden. <!-- FACT:PN-T39-F240 -->

### Ejemplos razonados

- **Aplicación correcta:** La longitud /n indica cuántos bits iniciales pertenecen al prefijo.
- **Contraste útil:** Una máscara IPv4 representa el prefijo con unos contiguos seguidos de ceros.

### Trampas de examen

- **Incorrecto:** La máscara 255.0.255.0 es una máscara CIDR contigua ordinaria.
- **Incorrecto:** /24 significa que quedan 24 bits de host.

<!-- VISUAL:t39-il-60-prefijo-host-y-mascara-de-subred.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-il-60-prefijo-host-y-mascara-de-subred.webp" alt="Prefijo, host y máscara de subred" width="820">
</p>
<p align="center"><em>Infografía: Prefijo, host y máscara de subred.</em></p>

:::hablemos-claro
El prefijo identifica la parte de red usada para el encaminamiento.
:::

:::en-la-calle
Al calcular una red IPv4 o interpretar una clase histórica, El prefijo identifica la parte de red usada para el encaminamiento.
:::

:::lo-que-cae
Prioriza **unos de red y ceros de host** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: RFC4632-CIDR-T39 -->

## 61. Clase A histórica

### Lógica del bloque

Para dominar **clase a histórica**, aplica esta regla: En el esquema histórico, una dirección de clase A comienza con bit 0. El anclaje principal es **primer bit 0**.

### Hechos examinables

- En el esquema histórico, una dirección de clase A comienza con bit 0. <!-- FACT:PN-T39-F241 -->
- Su primer octeto se sitúa convencionalmente entre 1 y 126 para redes unicast ordinarias. <!-- FACT:PN-T39-F242 -->
- La máscara por defecto histórica de clase A es 255.0.0.0 o /8. <!-- FACT:PN-T39-F243 -->
- El rango 127.0.0.0/8 se reserva para loopback y no es una red clase A ordinaria asignable. <!-- FACT:PN-T39-F244 -->

### Ejemplos razonados

- **Aplicación correcta:** Su primer octeto se sitúa convencionalmente entre 1 y 126 para redes unicast ordinarias.
- **Contraste útil:** La máscara por defecto histórica de clase A es 255.0.0.0 o /8.

### Trampas de examen

- **Incorrecto:** Clase A usa por defecto /24.
- **Incorrecto:** 127.0.0.0/8 se asigna como red pública ordinaria.

<!-- VISUAL:t39-61-clase-a-historica.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-61-clase-a-historica.webp" alt="Clase A histórica" width="820">
</p>
<p align="center"><em>Infografía: Clase A histórica.</em></p>

:::hablemos-claro
En el esquema histórico, una dirección de clase A comienza con bit 0.
:::

:::en-la-calle
Al calcular una red IPv4 o interpretar una clase histórica, En el esquema histórico, una dirección de clase A comienza con bit 0.
:::

:::lo-que-cae
Prioriza **primer bit 0** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: RFC791-IPV4-T39 -->

## 62. Clase B histórica

### Lógica del bloque

Para dominar **clase b histórica**, aplica esta regla: En el esquema histórico, una dirección de clase B comienza con bits 10. El anclaje principal es **bits iniciales 10**.

### Hechos examinables

- En el esquema histórico, una dirección de clase B comienza con bits 10. <!-- FACT:PN-T39-F245 -->
- El primer octeto se sitúa entre 128 y 191. <!-- FACT:PN-T39-F246 -->
- La máscara por defecto histórica es 255.255.0.0 o /16. <!-- FACT:PN-T39-F247 -->
- La clase no determina hoy el prefijo real de una red configurada mediante CIDR. <!-- FACT:PN-T39-F248 -->

### Ejemplos razonados

- **Aplicación correcta:** El primer octeto se sitúa entre 128 y 191.
- **Contraste útil:** La máscara por defecto histórica es 255.255.0.0 o /16.

### Trampas de examen

- **Incorrecto:** Clase B comienza en 192.
- **Incorrecto:** Toda dirección cuyo primer octeto es 172 usa obligatoriamente /16.

<!-- VISUAL:t39-62-clase-b-historica.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-62-clase-b-historica.webp" alt="Clase B histórica" width="820">
</p>
<p align="center"><em>Infografía: Clase B histórica.</em></p>

:::hablemos-claro
En el esquema histórico, una dirección de clase B comienza con bits 10.
:::

:::en-la-calle
Al calcular una red IPv4 o interpretar una clase histórica, En el esquema histórico, una dirección de clase B comienza con bits 10.
:::

:::lo-que-cae
Prioriza **bits iniciales 10** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: RFC791-IPV4-T39 -->

## 63. Clase C histórica

### Lógica del bloque

Para dominar **clase c histórica**, aplica esta regla: En el esquema histórico, una dirección de clase C comienza con bits 110. El anclaje principal es **bits iniciales 110**.

### Hechos examinables

- En el esquema histórico, una dirección de clase C comienza con bits 110. <!-- FACT:PN-T39-F249 -->
- El primer octeto se sitúa entre 192 y 223. <!-- FACT:PN-T39-F250 -->
- La máscara por defecto histórica es 255.255.255.0 o /24. <!-- FACT:PN-T39-F251 -->
- Una red /24 dispone de 256 combinaciones, aunque no todas son hosts unicast ordinarios. <!-- FACT:PN-T39-F252 -->

### Ejemplos razonados

- **Aplicación correcta:** El primer octeto se sitúa entre 192 y 223.
- **Contraste útil:** La máscara por defecto histórica es 255.255.255.0 o /24.

### Trampas de examen

- **Incorrecto:** Clase C usa por defecto /8.
- **Incorrecto:** Una /24 ofrece siempre 256 direcciones utilizables por hosts.

<!-- VISUAL:t39-63-clase-c-historica.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-63-clase-c-historica.webp" alt="Clase C histórica" width="820">
</p>
<p align="center"><em>Infografía: Clase C histórica.</em></p>

:::hablemos-claro
En el esquema histórico, una dirección de clase C comienza con bits 110.
:::

:::en-la-calle
Al calcular una red IPv4 o interpretar una clase histórica, En el esquema histórico, una dirección de clase C comienza con bits 110.
:::

:::lo-que-cae
Prioriza **bits iniciales 110** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: RFC791-IPV4-T39 -->

## 64. Clases D y E históricas

### Lógica del bloque

Para dominar **clases d y e históricas**, aplica esta regla: El rango histórico de clase D comprende primeros octetos 224 a 239 y se asocia a multicast. El anclaje principal es **multicast y reserva**.

### Hechos examinables

- El rango histórico de clase D comprende primeros octetos 224 a 239 y se asocia a multicast. <!-- FACT:PN-T39-F253 -->
- El rango histórico de clase E comprende 240 a 255 y se reservó para usos especiales o experimentales. <!-- FACT:PN-T39-F254 -->
- Clases D y E no usan la división red/host de A, B y C. <!-- FACT:PN-T39-F255 -->
- Las propiedades actuales de cada bloque deben consultarse en los registros de propósito especial. <!-- FACT:PN-T39-F256 -->

### Ejemplos razonados

- **Aplicación correcta:** El rango histórico de clase E comprende 240 a 255 y se reservó para usos especiales o experimentales.
- **Contraste útil:** Clases D y E no usan la división red/host de A, B y C.

### Trampas de examen

- **Incorrecto:** Clase D es el rango privado doméstico.
- **Incorrecto:** Clase E usa máscara por defecto /32 para redes de host ordinarias.

<!-- VISUAL:t39-64-clases-d-y-e-historicas.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-64-clases-d-y-e-historicas.webp" alt="Clases D y E históricas" width="820">
</p>
<p align="center"><em>Infografía: Clases D y E históricas.</em></p>

:::hablemos-claro
El rango histórico de clase D comprende primeros octetos 224 a 239 y se asocia a multicast.
:::

:::en-la-calle
Al calcular una red IPv4 o interpretar una clase histórica, El rango histórico de clase D comprende primeros octetos 224 a 239 y se asocia a multicast.
:::

:::lo-que-cae
Prioriza **multicast y reserva** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: RFC6890-SPECIAL-T39 -->

## 65. CIDR frente a direccionamiento por clases

### Lógica del bloque

Para dominar **cidr frente a direccionamiento por clases**, aplica esta regla: CIDR sustituyó operacionalmente las fronteras rígidas de clases por longitudes de prefijo. El anclaje principal es **prefijos sin clase**.

### Hechos examinables

- CIDR sustituyó operacionalmente las fronteras rígidas de clases por longitudes de prefijo. <!-- FACT:PN-T39-F257 -->
- Un prefijo CIDR puede agregarse para reducir entradas de encaminamiento. <!-- FACT:PN-T39-F258 -->
- La notación /n expresa el tamaño del prefijo sin depender de A, B o C. <!-- FACT:PN-T39-F259 -->
- Las clases se estudian por exigencia histórica y de examen, no como regla actual universal. <!-- FACT:PN-T39-F260 -->

### Ejemplos razonados

- **Aplicación correcta:** Un prefijo CIDR puede agregarse para reducir entradas de encaminamiento.
- **Contraste útil:** La notación /n expresa el tamaño del prefijo sin depender de A, B o C.

### Trampas de examen

- **Incorrecto:** CIDR obliga a usar solo /8, /16 o /24.
- **Incorrecto:** Con CIDR el primer octeto fija automáticamente la máscara.

<!-- VISUAL:t39-il-65-cidr-frente-a-direccionamiento-por-clases.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-il-65-cidr-frente-a-direccionamiento-por-clases.webp" alt="CIDR frente a direccionamiento por clases" width="820">
</p>
<p align="center"><em>Infografía: CIDR frente a direccionamiento por clases.</em></p>

:::hablemos-claro
CIDR sustituyó operacionalmente las fronteras rígidas de clases por longitudes de prefijo.
:::

:::en-la-calle
Al calcular una red IPv4 o interpretar una clase histórica, CIDR sustituyó operacionalmente las fronteras rígidas de clases por longitudes de prefijo.
:::

:::lo-que-cae
Prioriza **prefijos sin clase** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: RFC4632-CIDR-T39 -->

## 66. Cálculo de subred, red y broadcast

### Lógica del bloque

Para dominar **cálculo de subred, red y broadcast**, aplica esta regla: La dirección de red IPv4 se obtiene aplicando la máscara a la dirección. El anclaje principal es **operar con el prefijo**.

### Hechos examinables

- La dirección de red IPv4 se obtiene aplicando la máscara a la dirección. <!-- FACT:PN-T39-F261 -->
- En una subred convencional, la combinación con todos los bits de host a uno identifica el broadcast dirigido. <!-- FACT:PN-T39-F262 -->
- Una /30 tiene cuatro direcciones totales y normalmente dos hosts unicast ordinarios. <!-- FACT:PN-T39-F263 -->
- Una /31 puede emplearse en enlaces punto a punto conforme a reglas específicas y rompe la regla escolar de dos direcciones no utilizables. <!-- FACT:PN-T39-F264 -->

### Ejemplos razonados

- **Aplicación correcta:** En una subred convencional, la combinación con todos los bits de host a uno identifica el broadcast dirigido.
- **Contraste útil:** Una /30 tiene cuatro direcciones totales y normalmente dos hosts unicast ordinarios.

### Trampas de examen

- **Incorrecto:** El broadcast se obtiene poniendo a cero todos los bits de host.
- **Incorrecto:** Toda subred sin excepción pierde siempre dos direcciones de host.

<!-- VISUAL:t39-66-calculo-de-subred-red-y-broadcast.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-66-calculo-de-subred-red-y-broadcast.webp" alt="Cálculo de subred, red y broadcast" width="820">
</p>
<p align="center"><em>Infografía: Cálculo de subred, red y broadcast.</em></p>

:::hablemos-claro
La dirección de red IPv4 se obtiene aplicando la máscara a la dirección.
:::

:::en-la-calle
Al calcular una red IPv4 o interpretar una clase histórica, La dirección de red IPv4 se obtiene aplicando la máscara a la dirección.
:::

:::lo-que-cae
Prioriza **operar con el prefijo** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: RFC4632-CIDR-T39 -->

## 67. Direcciones IPv4 privadas

### Lógica del bloque

Para dominar **direcciones ipv4 privadas**, aplica esta regla: Los bloques privados son 10.0.0.0/8, 172.16.0.0/12 y 192.168.0.0/16. El anclaje principal es **tres bloques RFC 1918**.

### Hechos examinables

- Los bloques privados son 10.0.0.0/8, 172.16.0.0/12 y 192.168.0.0/16. <!-- FACT:PN-T39-F265 -->
- Las direcciones privadas no deben anunciarse como rutas globales públicas. <!-- FACT:PN-T39-F266 -->
- El bloque 172.16.0.0/12 abarca de 172.16.0.0 a 172.31.255.255. <!-- FACT:PN-T39-F267 -->
- 172.0.0.0/8 completo no es privado, y 192.0.0.0/8 completo tampoco lo es. <!-- FACT:PN-T39-F268 -->

### Ejemplos razonados

- **Aplicación correcta:** Las direcciones privadas no deben anunciarse como rutas globales públicas.
- **Contraste útil:** El bloque 172.16.0.0/12 abarca de 172.16.0.0 a 172.31.255.255.

### Trampas de examen

- **Incorrecto:** Cualquier dirección 172.x.x.x es privada.
- **Incorrecto:** 192.0.0.0/8 completo está reservado para redes privadas.

<!-- VISUAL:t39-67-direcciones-ipv4-privadas.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-67-direcciones-ipv4-privadas.webp" alt="Direcciones IPv4 privadas" width="820">
</p>
<p align="center"><em>Infografía: Direcciones IPv4 privadas.</em></p>

:::hablemos-claro
Los bloques privados son 10.0.0.0/8, 172.16.0.0/12 y 192.168.0.0/16.
:::

:::en-la-calle
Al calcular una red IPv4 o interpretar una clase histórica, Los bloques privados son 10.0.0.0/8, 172.16.0.0/12 y 192.168.0.0/16.
:::

:::lo-que-cae
Prioriza **tres bloques RFC 1918** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: RFC1918-PRIVATE-T39 -->

## 68. Direcciones IPv4 especiales y puerta de enlace

### Lógica del bloque

Para dominar **direcciones ipv4 especiales y puerta de enlace**, aplica esta regla: 0.0.0.0 puede expresar dirección no especificada y 0.0.0.0/0 la ruta por defecto según contexto. El anclaje principal es **el contexto cambia el significado**.

### Hechos examinables

- 0.0.0.0 puede expresar dirección no especificada y 0.0.0.0/0 la ruta por defecto según contexto. <!-- FACT:PN-T39-F269 -->
- 127.0.0.0/8 está reservado para loopback. <!-- FACT:PN-T39-F270 -->
- 255.255.255.255 es el broadcast limitado y no se reenvía como tráfico global ordinario. <!-- FACT:PN-T39-F271 -->
- La puerta de enlace predeterminada es el siguiente salto usado para destinos sin ruta más específica. <!-- FACT:PN-T39-F272 -->

### Ejemplos razonados

- **Aplicación correcta:** 127.0.0.0/8 está reservado para loopback.
- **Contraste útil:** 255.255.255.255 es el broadcast limitado y no se reenvía como tráfico global ordinario.

### Trampas de examen

- **Incorrecto:** 0.0.0.0 y 0.0.0.0/0 significan siempre exactamente lo mismo.
- **Incorrecto:** 127.0.0.1 identifica el router predeterminado de cualquier red.

<!-- VISUAL:t39-68-direcciones-ipv4-especiales-y-puerta-de-enlace.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-68-direcciones-ipv4-especiales-y-puerta-de-enlace.webp" alt="Direcciones IPv4 especiales y puerta de enlace" width="820">
</p>
<p align="center"><em>Infografía: Direcciones IPv4 especiales y puerta de enlace.</em></p>

:::hablemos-claro
0.0.0.0 puede expresar dirección no especificada y 0.0.0.0/0 la ruta por defecto según contexto.
:::

:::en-la-calle
Al calcular una red IPv4 o interpretar una clase histórica, 0.0.0.0 puede expresar dirección no especificada y 0.0.0.0/0 la ruta por defecto según contexto.
:::

:::lo-que-cae
Prioriza **el contexto cambia el significado** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: RFC6890-SPECIAL-T39 -->

## 69. Longitud y notación IPv6

### Lógica del bloque

Para dominar **longitud y notación ipv6**, aplica esta regla: Una dirección IPv6 tiene 128 bits. El anclaje principal es **128 bits hexadecimales**.

### Hechos examinables

- Una dirección IPv6 tiene 128 bits. <!-- FACT:PN-T39-F273 -->
- Se representa normalmente en ocho grupos hexadecimales de 16 bits separados por dos puntos. <!-- FACT:PN-T39-F274 -->
- Los ceros iniciales de cada grupo pueden omitirse. <!-- FACT:PN-T39-F275 -->
- Una única secuencia continua de grupos cero puede comprimirse con doble dos puntos. <!-- FACT:PN-T39-F276 -->

### Ejemplos razonados

- **Aplicación correcta:** Se representa normalmente en ocho grupos hexadecimales de 16 bits separados por dos puntos.
- **Contraste útil:** Los ceros iniciales de cada grupo pueden omitirse.

### Trampas de examen

- **Incorrecto:** IPv6 usa cuatro octetos decimales.
- **Incorrecto:** El doble dos puntos puede aparecer varias veces en la misma dirección sin ambigüedad.

<!-- VISUAL:t39-69-longitud-y-notacion-ipv6.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-69-longitud-y-notacion-ipv6.webp" alt="Longitud y notación IPv6" width="820">
</p>
<p align="center"><em>Infografía: Longitud y notación IPv6.</em></p>

:::hablemos-claro
Una dirección IPv6 tiene 128 bits.
:::

:::en-la-calle
Al leer y configurar una dirección IPv6, Una dirección IPv6 tiene 128 bits.
:::

:::lo-que-cae
Prioriza **128 bits hexadecimales** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: RFC4291-IPV6-ADDR-T39 -->

## 70. Unicast, anycast y multicast

### Lógica del bloque

Para dominar **unicast, anycast y multicast**, aplica esta regla: Una dirección unicast identifica una interfaz individual. El anclaje principal es **uno, uno de varios o grupo**.

### Hechos examinables

- Una dirección unicast identifica una interfaz individual. <!-- FACT:PN-T39-F277 -->
- Una dirección anycast se asigna a varias interfaces y entrega al miembro apropiado según el encaminamiento. <!-- FACT:PN-T39-F278 -->
- Una dirección multicast identifica un grupo de interfaces. <!-- FACT:PN-T39-F279 -->
- IPv6 no utiliza broadcast; sus funciones se resuelven mediante multicast u otros mecanismos. <!-- FACT:PN-T39-F280 -->

### Ejemplos razonados

- **Aplicación correcta:** Una dirección anycast se asigna a varias interfaces y entrega al miembro apropiado según el encaminamiento.
- **Contraste útil:** Una dirección multicast identifica un grupo de interfaces.

### Trampas de examen

- **Incorrecto:** Anycast entrega necesariamente a todos los miembros.
- **Incorrecto:** IPv6 conserva 255.255.255.255 como broadcast nativo.

<!-- VISUAL:t39-il-70-unicast-anycast-y-multicast.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-il-70-unicast-anycast-y-multicast.webp" alt="Unicast, anycast y multicast" width="820">
</p>
<p align="center"><em>Infografía: Unicast, anycast y multicast.</em></p>

:::hablemos-claro
Una dirección unicast identifica una interfaz individual.
:::

:::en-la-calle
Al leer y configurar una dirección IPv6, Una dirección unicast identifica una interfaz individual.
:::

:::lo-que-cae
Prioriza **uno, uno de varios o grupo** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: RFC4291-IPV6-ADDR-T39 -->

## 71. Prefijos IPv6 principales

### Lógica del bloque

Para dominar **prefijos ipv6 principales**, aplica esta regla: 2000::/3 cubre el espacio general de unicast global actualmente asignable. El anclaje principal es **global, enlace y casos especiales**.

### Hechos examinables

- 2000::/3 cubre el espacio general de unicast global actualmente asignable. <!-- FACT:PN-T39-F281 -->
- fe80::/10 identifica direcciones unicast link-local. <!-- FACT:PN-T39-F282 -->
- ::1 es la dirección loopback y :: la dirección no especificada. <!-- FACT:PN-T39-F283 -->
- ff00::/8 identifica direcciones multicast IPv6. <!-- FACT:PN-T39-F284 -->

### Ejemplos razonados

- **Aplicación correcta:** fe80::/10 identifica direcciones unicast link-local.
- **Contraste útil:** ::1 es la dirección loopback y :: la dirección no especificada.

### Trampas de examen

- **Incorrecto:** fe80::/10 se enruta globalmente por Internet.
- **Incorrecto:** ::1 es la ruta por defecto IPv6.

<!-- VISUAL:t39-71-prefijos-ipv6-principales.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-71-prefijos-ipv6-principales.webp" alt="Prefijos IPv6 principales" width="820">
</p>
<p align="center"><em>Infografía: Prefijos IPv6 principales.</em></p>

:::hablemos-claro
2000::/3 cubre el espacio general de unicast global actualmente asignable.
:::

:::en-la-calle
Al leer y configurar una dirección IPv6, 2000::/3 cubre el espacio general de unicast global actualmente asignable.
:::

:::lo-que-cae
Prioriza **global, enlace y casos especiales** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: RFC4291-IPV6-ADDR-T39 -->

## 72. Cabecera básica y extensiones IPv6

### Lógica del bloque

Para dominar **cabecera básica y extensiones ipv6**, aplica esta regla: La cabecera básica IPv6 tiene longitud fija de 40 bytes. El anclaje principal es **cabecera fija de 40 bytes**.

### Hechos examinables

- La cabecera básica IPv6 tiene longitud fija de 40 bytes. <!-- FACT:PN-T39-F285 -->
- IPv6 usa direcciones origen y destino de 128 bits. <!-- FACT:PN-T39-F286 -->
- Next Header encadena una cabecera de extensión o un protocolo superior. <!-- FACT:PN-T39-F287 -->
- Los routers no fragmentan paquetes IPv6; la fragmentación corresponde al nodo origen mediante cabecera de fragmento. <!-- FACT:PN-T39-F288 -->

### Ejemplos razonados

- **Aplicación correcta:** IPv6 usa direcciones origen y destino de 128 bits.
- **Contraste útil:** Next Header encadena una cabecera de extensión o un protocolo superior.

### Trampas de examen

- **Incorrecto:** La cabecera básica IPv6 contiene una suma de comprobación propia.
- **Incorrecto:** Cada router IPv6 fragmenta libremente los paquetes demasiado grandes.

<!-- VISUAL:t39-72-cabecera-basica-y-extensiones-ipv6.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-72-cabecera-basica-y-extensiones-ipv6.webp" alt="Cabecera básica y extensiones IPv6" width="820">
</p>
<p align="center"><em>Infografía: Cabecera básica y extensiones IPv6.</em></p>

:::hablemos-claro
La cabecera básica IPv6 tiene longitud fija de 40 bytes.
:::

:::en-la-calle
Al leer y configurar una dirección IPv6, La cabecera básica IPv6 tiene longitud fija de 40 bytes.
:::

:::lo-que-cae
Prioriza **cabecera fija de 40 bytes** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: RFC8200-IPV6-T39 -->

## 73. Neighbor Discovery y SLAAC

### Lógica del bloque

Para dominar **neighbor discovery y slaac**, aplica esta regla: Neighbor Discovery usa ICMPv6 para descubrir vecinos, routers y parámetros del enlace. El anclaje principal es **ICMPv6 para vecinos y routers**.

### Hechos examinables

- Neighbor Discovery usa ICMPv6 para descubrir vecinos, routers y parámetros del enlace. <!-- FACT:PN-T39-F289 -->
- Los anuncios de router comunican prefijos y otra información de configuración. <!-- FACT:PN-T39-F290 -->
- SLAAC permite autoconfigurar direcciones sin un servidor DHCPv6 con estado. <!-- FACT:PN-T39-F291 -->
- La detección de direcciones duplicadas comprueba si una dirección prevista ya está en uso. <!-- FACT:PN-T39-F292 -->

### Ejemplos razonados

- **Aplicación correcta:** Los anuncios de router comunican prefijos y otra información de configuración.
- **Contraste útil:** SLAAC permite autoconfigurar direcciones sin un servidor DHCPv6 con estado.

### Trampas de examen

- **Incorrecto:** IPv6 utiliza ARP sin cambios.
- **Incorrecto:** SLAAC exige que un servidor DHCPv6 asigne siempre la dirección.

<!-- VISUAL:t39-73-neighbor-discovery-y-slaac.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-73-neighbor-discovery-y-slaac.webp" alt="Neighbor Discovery y SLAAC" width="820">
</p>
<p align="center"><em>Infografía: Neighbor Discovery y SLAAC.</em></p>

:::hablemos-claro
Neighbor Discovery usa ICMPv6 para descubrir vecinos, routers y parámetros del enlace.
:::

:::en-la-calle
Al leer y configurar una dirección IPv6, Neighbor Discovery usa ICMPv6 para descubrir vecinos, routers y parámetros del enlace.
:::

:::lo-que-cae
Prioriza **ICMPv6 para vecinos y routers** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: RFC4861-NDP-T39 -->

## 74. Transición y límites de IPv6

### Lógica del bloque

Para dominar **transición y límites de ipv6**, aplica esta regla: Dual stack permite ejecutar IPv4 e IPv6 simultáneamente. El anclaje principal es **coexistir sin mitos**.

### Hechos examinables

- Dual stack permite ejecutar IPv4 e IPv6 simultáneamente. <!-- FACT:PN-T39-F293 -->
- Túneles encapsulan un protocolo dentro de otro y la traducción conecta dominios incompatibles. <!-- FACT:PN-T39-F294 -->
- IPv6 amplía el espacio de direcciones, pero no elimina por sí solo vulnerabilidades ni errores de configuración. <!-- FACT:PN-T39-F295 -->
- IPsec está definido para IPv6, pero su mera presencia no cifra automáticamente todo el tráfico. <!-- FACT:PN-T39-F296 -->

### Ejemplos razonados

- **Aplicación correcta:** Túneles encapsulan un protocolo dentro de otro y la traducción conecta dominios incompatibles.
- **Contraste útil:** IPv6 amplía el espacio de direcciones, pero no elimina por sí solo vulnerabilidades ni errores de configuración.

### Trampas de examen

- **Incorrecto:** Migrar a IPv6 hace innecesarios firewall y actualización.
- **Incorrecto:** Todo paquete IPv6 viaja cifrado obligatoriamente por IPsec.

<!-- VISUAL:t39-74-transicion-y-limites-de-ipv6.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-39/t39-74-transicion-y-limites-de-ipv6.webp" alt="Transición y límites de IPv6" width="820">
</p>
<p align="center"><em>Infografía: Transición y límites de IPv6.</em></p>

:::hablemos-claro
Dual stack permite ejecutar IPv4 e IPv6 simultáneamente.
:::

:::en-la-calle
Al leer y configurar una dirección IPv6, Dual stack permite ejecutar IPv4 e IPv6 simultáneamente.
:::

:::lo-que-cae
Prioriza **coexistir sin mitos** y descarta respuestas que confundan capa, dirección, dispositivo, servicio o alcance.
:::

<!-- FUENTE: RFC8200-IPV6-T39 -->

# Hablemos claro

:::hablemos-claro
Este tema tiene cuatro trampas maestras: tomar OSI como implementación literal; confundir hub, switch y router; mezclar DNS, DHCP y proxy; y tratar las clases A, B y C como direccionamiento vigente. Antes de responder identifica capa, función, alcance y versión del protocolo.
:::

# En la calle

:::en-la-calle
En una intervención, separar enlace físico, conmutación local, ruta IP, resolución DNS y servicio de aplicación permite localizar el fallo sin alterar más sistemas de los necesarios y documentar la conectividad observada.
:::

# Lo que cae

:::lo-que-cae
Prioriza las siete capas OSI y su correspondencia aproximada con TCP/IP; diferencias entre hub, switch, router, firewall y proxy; DORA, DNS autoritativo y recursivo; clases históricas frente a CIDR; rangos IPv4 especiales; y notación, tipos y autoconfiguración IPv6.
:::

# Ha caído

:::ha-caido
Se han localizado 8 referencias históricas del Tema 39. Permanecen ocultas y en cuarentena porque no existe plantilla oficial final verificable en el repositorio.
:::

## Fuentes legales, institucionales y primarias

- `CONVOCATORIA-PN-2026-T39`
- `ISO-7498-1-OSI-T39`
- `RFC1122-HOSTS-T39`
- `RFC9293-TCP-T39`
- `RFC768-UDP-T39`
- `RFC792-ICMP-T39`
- `IEEE8023-ETHERNET-T39`
- `IEEE8021Q-BRIDGES-T39`
- `RFC1812-ROUTERS-T39`
- `NIST-SP800-41R1-T39`
- `RFC3022-NAT-T39`
- `RFC2131-DHCP-T39`
- `RFC9915-DHCPV6-T39`
- `RFC1034-DNS-T39`
- `RFC1035-DNS-T39`
- `RFC8499-DNS-TERMS-T39`
- `RFC9110-HTTP-T39`
- `RFC791-IPV4-T39`
- `RFC4632-CIDR-T39`
- `RFC1918-PRIVATE-T39`
- `RFC6890-SPECIAL-T39`
- `RFC8200-IPV6-T39`
- `RFC4291-IPV6-ADDR-T39`
- `RFC4861-NDP-T39`
- `RFC4862-SLAAC-T39`

---

*Academia En Vigor · El temario que nunca duerme · Tema 39 · v1.0.0 · Documento interno no publicado.*
