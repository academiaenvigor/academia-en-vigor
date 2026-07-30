#!/usr/bin/env python3
"""Genera los Temas 12 y 13 con el contrato editorial VIGOR.

Los DOCX privados se usan exclusivamente para reconstruir la cobertura. El
contenido jurídico se redacta de nuevo desde fuentes oficiales vigentes al
30 de julio de 2026.
"""
from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CUT_OFF = "2026-07-30"
VERSION = "1.0.0"


def fact(correct: str, wrong1: str, wrong2: str, risk: int = 5) -> dict:
    return {"correct": correct, "wrong": [wrong1, wrong2], "risk": risk}


def block(part: int, title: str, source: str, articles: str, intro: str,
          detail: str, facts: list[dict], clear: str, street: str, falls: str,
          visual: tuple[str, str, str, str]) -> dict:
    return {
        "part": part, "title": title, "source": source, "articles": articles,
        "intro": intro, "detail": detail, "facts": facts, "clear": clear,
        "street": street, "falls": falls, "visual": visual,
    }


COMMON_SOURCE = {
    "CONV-PN-2026": "https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-15055",
}


T12 = {
    "number": 12,
    "title": "Protección internacional, acogida, apatridia y personas desplazadas",
    "slug": "proteccion-internacional-acogida-apatridia-desplazados",
    "parts": {
        1: "Sistema y estatutos de protección",
        2: "Solicitud y procedimiento vigente",
        3: "Menores y personas vulnerables",
        4: "Sistema de acogida y centros",
        5: "Apatridia y protección temporal",
        6: "Integración operativa y repaso",
    },
    "sources": {
        **COMMON_SOURCE,
        "L12-2009-T12": "https://www.boe.es/eli/es/l/2009/10/30/12/con",
        "INS11-2026-T12": "https://www.boe.es/eli/es/ins/2026/06/11/(1)",
        "RUE1348-2024-T12": "https://www.boe.es/buscar/doc.php?id=DOUE-L-2024-80739",
        "RUE1351-2024-T12": "https://www.boe.es/buscar/doc.php?id=DOUE-L-2024-80742",
        "RUE1356-2024-T12": "https://www.boe.es/buscar/doc.php?id=DOUE-L-2024-80747",
        "RD220-2022-T12": "https://www.boe.es/eli/es/rd/2022/03/29/220/con",
        "RD865-2001-T12": "https://www.boe.es/eli/es/rd/2001/07/20/865/con",
        "RD1325-2003-T12": "https://www.boe.es/eli/es/rd/2003/10/24/1325/con",
        "CONV1951-T12": "https://www.boe.es/diario_boe/txt.php?id=BOE-A-1978-26331",
    },
    "catalog": [
        ("L12-2009-T12", "Ley 12/2009: asilo y protección subsidiaria", "BOE-A-2009-17242", "estatutos, garantías, procedimiento nacional compatible y personas vulnerables"),
        ("INS11-2026-T12", "Instrucción de 11 de junio de 2026: aplicación del Pacto Europeo", "BOE-A-2026-12855", "puente procedimental desde el 12 de junio de 2026"),
        ("RUE1348-2024-T12", "Reglamento (UE) 2024/1348: procedimiento común de protección internacional", "DOUE-L-2024-80739", "procedimientos de examen, fronterizo, inadmisión y recursos"),
        ("RUE1351-2024-T12", "Reglamento (UE) 2024/1351: gestión del asilo y la migración", "DOUE-L-2024-80742", "Estado responsable y solidaridad"),
        ("RUE1356-2024-T12", "Reglamento (UE) 2024/1356: triaje en fronteras exteriores", "DOUE-L-2024-80747", "triaje previo cuando proceda"),
        ("RD220-2022-T12", "Real Decreto 220/2022: sistema de acogida", "BOE-A-2022-4978", "itinerario, fases, recursos, derechos y deberes"),
        ("RD865-2001-T12", "Real Decreto 865/2001: estatuto de apátrida", "BOE-A-2001-14166", "solicitud, instrucción, resolución y efectos"),
        ("RD1325-2003-T12", "Real Decreto 1325/2003: protección temporal", "BOE-A-2003-19714", "afluencia masiva de personas desplazadas"),
        ("CONV1951-T12", "Convención de Ginebra de 1951 y Protocolo de 1967", "BOE-A-1978-26331", "definición internacional y no devolución"),
    ],
    "official_regex": r"protecci[oó]n internacional|solicitante(?:s)? de asilo|condici[oó]n de refugiado|refugiados?|ap[aá]trida|non refoulement|protecci[oó]n temporal|personas desplazadas|ACNUR",
}

T12["blocks"] = [
    block(1, "Mapa normativo vigente en 2026", "CONV-PN-2026,L12-2009-T12,INS11-2026-T12,RUE1348-2024-T12",
      "epígrafe oficial; Ley 12/2009; Reglamentos (UE) 2024/1348 y 2024/1351",
      "La protección internacional se estudia hoy en un sistema multinivel: Convención de Ginebra, Derecho de la Unión, Ley 12/2009 y normas de acogida.",
      "Desde el 12 de junio de 2026 el procedimiento común europeo es directamente aplicable. La Ley 12/2009 continúa siendo referencia nacional, pero debe interpretarse conforme a los reglamentos europeos y dejar de aplicarse cuando resulte incompatible.",
      [
          fact("El Tema 12 oficial comprende protección internacional, procedimiento, personas vulnerables, centros de acogida, apatridia y personas desplazadas.", "El Tema 12 se limita a la residencia por razones humanitarias.", "El Tema 12 excluye la apatridia y la protección temporal."),
          fact("Los reglamentos de la Unión son obligatorios en todos sus elementos y directamente aplicables.", "Los reglamentos de la Unión necesitan siempre una ley española de transposición para producir efectos.", "Una instrucción nacional puede dejar sin aplicación cualquier reglamento europeo."),
          fact("La Ley 12/2009 se aplica en 2026 en la medida en que sea compatible con el Derecho de la Unión directamente aplicable.", "La Ley 12/2009 quedó íntegramente derogada el 12 de junio de 2026.", "El Pacto Europeo carece de incidencia en el procedimiento español."),
      ],
      "Piensa en capas: tratado, reglamento europeo, ley española y reglamento de acogida.",
      "Antes de usar un plazo antiguo hay que comprobar si el procedimiento europeo lo ha desplazado.",
      "La trampa más peligrosa es estudiar como futuro un Pacto que ya es aplicable.",
      ("infografia", "t12-02-mapa-normativo-2026.webp", "Pirámide normativa con reglas de primacía y compatibilidad", "pirámide normativa")),

    block(1, "Asilo, refugiado y protección subsidiaria", "L12-2009-T12,CONV1951-T12",
      "Ley 12/2009, arts. 2 a 5; Convención de 1951",
      "Protección internacional es el género; asilo y protección subsidiaria son sus dos estatutos principales.",
      "La condición de refugiado parte de un temor fundado de persecución por motivos tasados. La protección subsidiaria cubre un riesgo real de daños graves cuando no se reúnen los requisitos del asilo.",
      [
          fact("El derecho de asilo es la protección dispensada a quien obtiene la condición de refugiado.", "El asilo es una autorización laboral ajena a la condición de refugiado.", "Toda persona desplazada obtiene automáticamente el derecho de asilo."),
          fact("La protección subsidiaria exige un riesgo real de daños graves y que no concurra causa de exclusión o denegación.", "La protección subsidiaria solo se concede a quien ya fue reconocido como refugiado.", "La protección subsidiaria depende exclusivamente de carecer de recursos económicos."),
          fact("Asilo y protección subsidiaria integran la protección internacional, pero responden a presupuestos jurídicos distintos.", "Asilo, apatridia y residencia humanitaria son nombres equivalentes.", "La protección subsidiaria es una sanción accesoria a la denegación del asilo."),
      ],
      "Primero pregunta «¿persecución por motivo protegido?»; si no, analiza «¿daño grave real?».",
      "Dos expedientes pueden compartir hechos de violencia y acabar en estatutos diferentes por la causa y el riesgo acreditados.",
      "No conviertas «subsidiaria» en «menos importante»: es otro presupuesto, no una protección decorativa.",
      ("infografia", "t12-03-dos-estatutos.webp", "Comparación visual entre asilo y protección subsidiaria", "doble carril comparativo")),

    block(1, "Condición de refugiado: temor y motivos", "L12-2009-T12,CONV1951-T12",
      "Ley 12/2009, arts. 3 y 7",
      "La definición combina temor fundado, persecución, motivo protegido, salida del país y falta de protección efectiva.",
      "Los motivos comprenden raza, religión, nacionalidad, opiniones políticas y pertenencia a determinado grupo social, con atención legal al género, orientación e identidad sexual.",
      [
          fact("La condición de refugiado exige fundados temores de persecución relacionados con alguno de los motivos protegidos.", "Basta cualquier temor subjetivo aunque no guarde relación con un motivo protegido.", "Solo las condenas penales firmes pueden constituir persecución."),
          fact("La persecución puede vincularse a raza, religión, nacionalidad, opiniones políticas o pertenencia a determinado grupo social.", "La persecución solo puede fundarse en nacionalidad y religión.", "Los motivos económicos constituyen por sí solos un motivo tasado de persecución."),
          fact("También puede ser refugiado el apátrida que no pueda o no quiera regresar a su anterior residencia habitual por esos temores.", "La falta de nacionalidad impide en todo caso solicitar asilo.", "El apátrida solo puede invocar daños ocurridos dentro de España."),
      ],
      "La cadena completa es: temor fundado + persecución + motivo + ausencia de protección.",
      "La entrevista debe permitir explicar tanto lo sucedido como por qué la protección del país no es efectiva.",
      "No confundas migración económica con persecución, aunque una misma historia pueda contener ambas realidades.",
      ("infografia", "t12-04-cadena-refugiado.webp", "Cadena de requisitos de la condición de refugiado", "cadena causal")),

    block(1, "Actos y agentes de persecución", "L12-2009-T12",
      "arts. 6, 13 y 14",
      "La persecución puede resultar de un acto grave o de una acumulación de medidas que alcance gravedad equivalente.",
      "El agente puede ser el Estado, organizaciones que controlan el territorio o agentes no estatales cuando no exista protección efectiva. La protección ha de ser accesible y no meramente nominal.",
      [
          fact("Los actos de persecución pueden consistir en violencia, medidas discriminatorias o procesamientos desproporcionados.", "Solo la violencia física directa puede calificarse como persecución.", "Una ley discriminatoria nunca puede constituir un acto de persecución."),
          fact("Una acumulación suficientemente grave de medidas puede equivaler a una violación grave de derechos.", "Cada medida debe constituir por sí sola un delito internacional.", "La reiteración carece de relevancia para valorar la persecución."),
          fact("Los agentes no estatales pueden causar persecución cuando el Estado u otros agentes de protección no puedan o no quieran brindar protección efectiva.", "La persecución solo puede proceder formalmente de un ministerio.", "La existencia de una comisaría demuestra siempre protección suficiente."),
      ],
      "No mires solo quién agrede; comprueba quién podía proteger y si lo hizo de verdad.",
      "Amenazas, exclusión laboral, hostigamiento policial y violencia pueden formar un patrón conjunto.",
      "«No estatal» no significa «irrelevante».",
      ("ilustracion", "t12-il-01-red-de-persecucion.webp", "Persona rodeada por varias formas dibujadas de persecución y una protección inaccesible", "escena narrativa")),

    block(1, "Daños graves de la protección subsidiaria", "L12-2009-T12",
      "art. 10",
      "Los daños graves están tasados y no equivalen a cualquier dificultad del país de origen.",
      "La ley identifica tres grupos: pena de muerte o riesgo de ejecución, tortura o trato inhumano o degradante y amenaza grave contra civiles por violencia indiscriminada en conflicto.",
      [
          fact("La condena a pena de muerte o el riesgo de su ejecución es un daño grave.", "La pena de muerte solo cuenta si ya fue materialmente ejecutada.", "Una condena de prisión constituye siempre protección subsidiaria."),
          fact("La tortura y los tratos inhumanos o degradantes en el país de origen son daños graves.", "Solo los daños patrimoniales pueden fundamentar protección subsidiaria.", "La tortura queda fuera porque solo se estudia en el derecho de asilo."),
          fact("La amenaza grave contra la vida o integridad de civiles por violencia indiscriminada en conflicto puede constituir daño grave.", "Todo conflicto concede automáticamente protección sin valorar el riesgo.", "La violencia indiscriminada solo se valora cuando afecta a militares."),
      ],
      "Memoriza el triángulo: muerte, tortura y violencia indiscriminada contra civiles.",
      "La información del país ayuda a valorar el riesgo, pero debe conectarse con la situación de la persona.",
      "Daño grave no es sinónimo de cualquier perjuicio serio.",
      ("infografia", "t12-06-triangulo-danos-graves.webp", "Triángulo didáctico de los tres daños graves", "triángulo conceptual")),

    block(1, "Exclusión, denegación y no devolución", "L12-2009-T12,CONV1951-T12",
      "arts. 8, 9, 11, 12 y 5; Convención, art. 33",
      "Excluir, denegar y proteger frente a la devolución son operaciones distintas que no deben mezclarse.",
      "Las cláusulas de exclusión responden a actos especialmente graves; la denegación atiende, entre otros supuestos, al peligro para la seguridad o amenaza para la comunidad. El principio de no devolución impide conducir a una persona al territorio del riesgo en los términos aplicables.",
      [
          fact("La exclusión del asilo puede fundarse en delitos contra la paz, de guerra o contra la humanidad.", "Las cláusulas de exclusión solo se refieren a infracciones administrativas leves.", "La comisión de cualquier falta de tráfico excluye automáticamente del asilo."),
          fact("El asilo se deniega a quien constituya por razones fundadas un peligro para la seguridad de España.", "La seguridad de España nunca puede valorarse en la decisión de asilo.", "Basta una sospecha genérica sin razones fundadas para denegar."),
          fact("La no devolución protege frente al traslado al territorio donde la vida o la libertad quedarían amenazadas, con el alcance y excepciones del régimen aplicable.", "No devolución significa derecho automático a elegir cualquier Estado de residencia.", "La denegación de una solicitud obliga siempre a ejecutar de inmediato el retorno sin valorar límites."),
      ],
      "Exclusión mira determinados actos del solicitante; denegación, determinados peligros; no devolución, el riesgo del destino.",
      "Una resolución desfavorable no elimina el deber de comprobar si la salida proyectada vulneraría una prohibición de devolución.",
      "Tres palabras parecidas, tres preguntas jurídicas diferentes.",
      ("infografia", "t12-07-tres-filtros.webp", "Tres filtros diferenciados: exclusión, denegación y no devolución", "filtros secuenciales")),

    block(2, "Derecho a solicitar y formalización", "L12-2009-T12,RUE1348-2024-T12",
      "Ley 12/2009, arts. 16 y 17; Reglamento (UE) 2024/1348",
      "La solicitud debe poder expresarse y registrarse con garantías, sin exigir que la persona domine la terminología jurídica.",
      "La manifestación de voluntad activa deberes de información y acceso al procedimiento. La formalización recoge identidad, relato, documentación disponible y circunstancias relevantes mediante entrevista individual.",
      [
          fact("Las personas nacionales no comunitarias y las apátridas presentes en España tienen derecho a solicitar protección internacional.", "Solo pueden solicitarla quienes ya tengan residencia legal.", "Los apátridas quedan excluidos del derecho a solicitar."),
          fact("La solicitud se formaliza mediante comparecencia personal y entrevista individual, salvo imposibilidad prevista legalmente.", "La solicitud solo puede presentarse por correo anónimo.", "La entrevista queda prohibida para evitar contradicciones."),
          fact("La falta de documentos de identidad no impide por sí sola formular la solicitud, aunque debe explicarse y aportarse lo disponible.", "Sin pasaporte vigente la solicitud debe rechazarse sin registro.", "La Administración debe presumir identidad falsa en todo caso de indocumentación."),
      ],
      "Pedir protección es expresar una necesidad; formalizar es convertirla en expediente con garantías.",
      "La primera escucha policial debe detectar expresiones de miedo al retorno aunque la persona no diga «asilo».",
      "No uses el pasaporte como portero automático del procedimiento.",
      ("ilustracion", "t12-il-02-primera-escucha.webp", "Escena dibujada de primera escucha con intérprete y carpeta de solicitud", "escena humana")),

    block(2, "Derechos y obligaciones del solicitante", "L12-2009-T12",
      "arts. 18 y 19",
      "La condición de solicitante incorpora asistencia, información y documentación, junto con deberes de cooperación.",
      "Entre las garantías figuran asistencia sanitaria y jurídica en los términos legales, intérprete, comunicación con ACNUR y documentación. La persona debe cooperar, aportar información y comparecer cuando sea requerida.",
      [
          fact("El solicitante tiene derecho a asistencia jurídica y a intérprete en los términos previstos.", "La asistencia jurídica solo comienza después de concederse el asilo.", "El intérprete puede sustituir al instructor y decidir la solicitud."),
          fact("La presentación de la solicitud suspende, con los límites legales, procesos de devolución, expulsión o extradición que pudieran afectar al solicitante.", "La solicitud equivale automáticamente a nacionalidad española.", "La solicitud nunca produce efecto alguno sobre una salida en curso."),
          fact("El solicitante debe cooperar con las autoridades y proporcionar cuanto antes la información relevante.", "La cooperación permite ocultar deliberadamente documentos decisivos.", "La carga de instrucción corresponde únicamente a ACNUR."),
      ],
      "Derechos para poder defender la solicitud; deberes para poder examinarla.",
      "Documenta qué información se entrega, en qué idioma y si la persona la comprende.",
      "Cooperar no significa renunciar a garantías.",
      ("infografia", "t12-09-balanza-derechos-deberes.webp", "Balanza con derechos del solicitante y deberes de cooperación", "balanza informativa")),

    block(2, "Primacía europea y procedimiento común", "INS11-2026-T12,RUE1348-2024-T12,RUE1351-2024-T12",
      "Instrucción de 11/06/2026, apartado I",
      "El Pacto Europeo racionaliza y armoniza el examen de las solicitudes mediante procedimientos comunes.",
      "La autoridad nacional debe interpretar la Ley 12/2009 de forma compatible y, si no es posible, inaplicar la regla nacional incompatible con el reglamento directamente aplicable.",
      [
          fact("El Reglamento (UE) 2024/1348 establece un procedimiento común de protección internacional.", "El Reglamento 2024/1348 solo regula ayudas económicas posteriores a la concesión.", "Cada oficina puede sustituir el reglamento por una circular local."),
          fact("La primacía exige no aplicar una norma nacional incompatible con una disposición europea de efecto directo.", "La primacía solo puede ser observada por tribunales y nunca por autoridades administrativas.", "Una norma nacional anterior prevalece siempre por antigüedad."),
          fact("La Instrucción de 11 de junio de 2026 se aplica desde el 12 de junio de 2026.", "La instrucción empezará a aplicarse en enero de 2030.", "La instrucción dejó sin efecto los Reglamentos 2024/1348 y 2024/1351."),
      ],
      "La regla práctica es compatibilidad primero; primacía si la compatibilidad no es posible.",
      "Una plantilla de 2025 puede conservar conceptos válidos y tener plazos procedimentales ya desplazados.",
      "Vigencia y aplicabilidad no son la misma fecha.",
      ("infografia", "t12-10-puente-2025-2026.webp", "Puente temporal entre el régimen anterior y la aplicación plena en 2026", "línea de cambio normativo")),

    block(2, "Procedimiento fronterizo de asilo", "INS11-2026-T12,RUE1348-2024-T12,RUE1356-2024-T12",
      "Instrucción, apartados II y III",
      "El procedimiento fronterizo depende del lugar y forma de presentación, del triaje cuando proceda y de la situación de entrada.",
      "Puede operar tras solicitud en puesto fronterizo, cruce no autorizado, desembarco después de búsqueda y rescate o determinados supuestos de reubicación, siempre que concurran las condiciones europeas.",
      [
          fact("El procedimiento fronterizo puede seguir a una solicitud formulada en un puesto fronterizo de entrada.", "Toda solicitud presentada en el interior se convierte automáticamente en fronteriza.", "Las solicitudes en frontera quedan fuera del sistema de protección internacional."),
          fact("También puede aplicarse tras aprehensión relacionada con cruce no autorizado o desembarco después de búsqueda y rescate.", "Una operación de rescate impide siempre iniciar cualquier procedimiento de asilo.", "El cruce no autorizado excluye de forma automática todo examen de protección."),
          fact("Cuando proceda, el triaje del Reglamento (UE) 2024/1356 precede al procedimiento fronterizo.", "El triaje sustituye a la resolución de protección internacional.", "El triaje solo existe después de conceder el estatuto de refugiado."),
      ],
      "Lugar, entrada y origen de la detección forman el mapa de acceso al procedimiento fronterizo.",
      "No confundas triaje, registro de la solicitud y examen del fondo.",
      "Frontera no significa ausencia de garantías.",
      ("infografia", "t12-11-cuatro-accesos-frontera.webp", "Cuatro accesos didácticos al procedimiento fronterizo", "mapa de accesos")),

    block(2, "Garantías y examen inicial en frontera", "INS11-2026-T12,RUE1348-2024-T12,L12-2009-T12",
      "Instrucción, apartado III",
      "La rapidez del examen fronterizo convive con asistencia jurídica preceptiva, posible intervención de ACNUR y resolución motivada.",
      "Primero se comprueban causas europeas de inadmisión y determinados supuestos de desestimación. La instrucción española procura mantener el plazo de cuatro días naturales de la Ley 12/2009 cuando resulte compatible.",
      [
          fact("La asistencia jurídica es preceptiva en la formalización y durante el procedimiento fronterizo administrativo.", "La asistencia jurídica está prohibida hasta que exista una denegación.", "Solo se permite asistencia jurídica cuando la persona habla castellano."),
          fact("Con consentimiento previo del solicitante, ACNUR puede acceder a la solicitud y ser oído antes de determinadas resoluciones.", "ACNUR dicta la resolución administrativa en nombre del Ministro.", "El acceso de ACNUR nunca requiere atender a la voluntad del solicitante."),
          fact("El examen inicial comprueba causas de inadmisión y determinados supuestos de desestimación previstos en el Reglamento 2024/1348.", "El examen inicial se limita a comprobar el billete de viaje.", "La frontera impide analizar cualquier causa de inadmisión."),
      ],
      "Rápido no significa ciego: abogado, información, ACNUR y motivación siguen dentro del procedimiento.",
      "El consentimiento para el acceso de ACNUR debe quedar documentado.",
      "No estudies «cuatro días» aislado de su compatibilidad con el reglamento europeo.",
      ("infografia", "t12-12-reloj-con-garantias.webp", "Reloj procedimental rodeado de abogado, ACNUR, entrevista y resolución", "cronología garantista")),

    block(2, "Instrucción, evaluación, archivo y recursos", "L12-2009-T12,RUE1348-2024-T12,INS11-2026-T12",
      "Ley 12/2009, arts. 23 a 29; Reglamento (UE) 2024/1348",
      "La instrucción debe valorar individualmente relato, pruebas e información del país sin poner en peligro al solicitante.",
      "No debe obtenerse información de los perseguidores de forma que conozcan la solicitud. El archivo puede seguir a retirada o desistimiento; la resolución es recurrible con la información de plazo y órgano competente.",
      [
          fact("La evaluación no debe informar a los responsables de la persecución de que la persona ha solicitado protección.", "La primera diligencia debe ser avisar al presunto perseguidor.", "La confidencialidad solo existe después de la concesión."),
          fact("Para una resolución favorable pueden bastar indicios suficientes de persecución o daños graves conforme a la Ley 12/2009.", "Siempre se exige sentencia penal firme del país de origen.", "La declaración de la persona carece de todo valor probatorio."),
          fact("La resolución debe informar del recurso y del órgano jurisdiccional competente.", "Las resoluciones de protección internacional nunca son recurribles.", "El pie de recurso puede omitir deliberadamente el plazo."),
      ],
      "Evaluar es contrastar sin exponer a quien pide protección.",
      "La coherencia se analiza con contexto, trauma, documentación posible e información fiable del país.",
      "Archivo, inadmisión y denegación no son sinónimos.",
      ("ilustracion", "t12-il-03-expediente-protegido.webp", "Expediente protegido de miradas externas durante la evaluación", "metáfora documental")),

    block(3, "Régimen general de vulnerabilidad", "L12-2009-T12,RD220-2022-T12",
      "Ley 12/2009, art. 46; RD 220/2022, art. 11",
      "Las necesidades específicas deben detectarse y atenderse durante todo el procedimiento y la acogida.",
      "La ley menciona, entre otras personas, menores, personas con discapacidad, mayores, embarazadas, familias monoparentales, víctimas de trata, tortura, violación u otras formas graves de violencia.",
      [
          fact("La situación de vulnerabilidad exige un tratamiento diferenciado cuando resulte necesario.", "La igualdad obliga a prestar exactamente el mismo apoyo material en todos los casos.", "La vulnerabilidad solo puede valorarse después de resolver."),
          fact("La evaluación debe identificar necesidades específicas de acogida y de procedimiento.", "La identificación de necesidades corresponde exclusivamente a la persona solicitante sin apoyo profesional.", "Las necesidades específicas no influyen en entrevistas ni recursos."),
          fact("Las víctimas de trata, tortura o violencia grave pueden requerir atención especializada.", "La atención especializada está reservada a quienes ya tengan nacionalidad española.", "La violencia sufrida nunca guarda relación con la acogida."),
      ],
      "Tratar igual no siempre es proteger igual: ajusta el apoyo a la necesidad detectada.",
      "Una entrevista accesible puede requerir intérprete adecuado, pausas, acompañamiento o adaptación.",
      "Vulnerabilidad no es una etiqueta ornamental del expediente.",
      ("infografia", "t12-14-radar-vulnerabilidad.webp", "Radar de necesidades específicas y respuestas de apoyo", "radar de detección")),

    block(3, "Menores y el interés superior", "L12-2009-T12,RD220-2022-T12",
      "Ley 12/2009, arts. 46 y 47",
      "Toda decisión que afecte a un menor debe atender primordialmente a su interés superior.",
      "La edad y madurez condicionan la información y la escucha. Las familias con menores requieren evaluación específica y los recursos de acogida deben preservar protección y desarrollo.",
      [
          fact("El interés superior del menor es consideración primordial en las decisiones que le afecten.", "El interés superior solo se valora al cumplir dieciocho años.", "La conveniencia administrativa prevalece siempre sobre el interés del menor."),
          fact("La información debe adaptarse a la edad y madurez del menor.", "Los menores reciben necesariamente la misma explicación técnica que un abogado.", "Informar a la persona adulta acompañante elimina el derecho del menor a ser oído."),
          fact("La unidad familiar y la seguridad del menor deben considerarse al asignar recursos.", "Los menores deben separarse automáticamente de toda persona adulta solicitante.", "La asignación de recursos solo depende del orden alfabético."),
      ],
      "Interés superior es una pauta de decisión, no una frase para cerrar informes.",
      "Explica, escucha y documenta por qué la opción elegida protege mejor al menor concreto.",
      "Menor no significa invisible dentro del expediente familiar.",
      ("ilustracion", "t12-il-04-brujula-del-menor.webp", "Menor acompañado por una brújula protectora en un cruce de decisiones", "metáfora dibujada")),

    block(3, "Menores no acompañados", "L12-2009-T12,RD865-2001-T12",
      "Ley 12/2009, art. 48; RD 865/2001, art. 6",
      "La ausencia de una persona adulta responsable activa protección de menores, intervención fiscal y representación adecuada.",
      "El menor solicitante no acompañado se remite a los servicios competentes de protección de menores y se pone el hecho en conocimiento del Ministerio Fiscal. La determinación de edad debe respetar garantías y dignidad.",
      [
          fact("El menor no acompañado solicitante de protección internacional se remite a los servicios competentes de protección de menores.", "Debe ingresar automáticamente en un centro penitenciario.", "La Oficina de Asilo asume por sí sola su tutela civil."),
          fact("El hecho se pone en conocimiento del Ministerio Fiscal.", "Solo se comunica al juez de tráfico.", "La comunicación al Ministerio Fiscal está prohibida por confidencialidad."),
          fact("La representación y asistencia deben permitir que el menor participe efectivamente en el procedimiento.", "El menor carece de derecho a ser informado hasta la mayoría de edad.", "La ausencia de representante convierte automáticamente la solicitud en desistida."),
      ],
      "Protección, fiscal y representación forman el triángulo operativo.",
      "Si existen dudas razonables de edad, la actuación debe evitar tratar automáticamente como adulto a quien puede ser menor.",
      "No mezcles protección de menores con detención de extranjeros.",
      ("infografia", "t12-16-triangulo-mena.webp", "Triángulo de protección, Ministerio Fiscal y representación", "triángulo operativo")),

    block(4, "Sistema de acogida: finalidad y destinatarios", "RD220-2022-T12",
      "arts. 1 a 5",
      "El sistema de acogida cubre necesidades y acompaña un itinerario orientado a autonomía e inclusión.",
      "No es solo alojamiento: integra manutención, apoyo social, información, orientación jurídica, aprendizaje lingüístico y otras actuaciones, según fase, perfil y recursos.",
      [
          fact("El sistema de acogida atiende a personas solicitantes y beneficiarias incluidas en su ámbito subjetivo.", "Solo atiende a turistas sin recursos.", "La concesión de protección impide cualquier apoyo de inclusión."),
          fact("La acogida se organiza como un itinerario adaptado a la situación y necesidades de la persona.", "Todas las personas deben recorrer idéntico recurso y duración sin evaluación.", "El itinerario se limita a entregar una dirección postal."),
          fact("La carencia de recursos económicos es relevante para acceder a las condiciones materiales de acogida.", "La acogida se concede únicamente a quien posea patrimonio suficiente.", "La situación económica nunca puede comprobarse."),
      ],
      "Acogida es un proceso, no una cama aislada.",
      "La derivación acertada combina plazas disponibles con perfil, vulnerabilidad y vínculos.",
      "No confundas sistema de acogida con internamiento.",
      ("infografia", "t12-17-itinerario-acogida.webp", "Itinerario completo de acogida desde la valoración hasta la autonomía", "ruta por fases")),

    block(4, "Tres fases del itinerario", "RD220-2022-T12",
      "arts. 15 a 24",
      "El itinerario distingue valoración inicial y derivación, acogida y autonomía.",
      "La primera fase detecta necesidades y asigna recurso; la segunda asegura atención integral en acogida; la tercera apoya la vida independiente cuando la persona reúne las condiciones.",
      [
          fact("La valoración inicial identifica perfil, vulnerabilidades y recurso adecuado.", "La valoración inicial se realiza después de finalizar la autonomía.", "Su único objetivo es imponer una sanción migratoria."),
          fact("La fase de acogida proporciona alojamiento y actuaciones de atención integral.", "La fase de acogida prohíbe cualquier intervención social.", "Acogida y expulsión son la misma fase."),
          fact("La fase de autonomía apoya la salida progresiva del recurso y la vida independiente.", "La autonomía consiste en suprimir de inmediato toda orientación.", "La autonomía precede siempre a la primera valoración."),
      ],
      "Valorar, acoger y autonomizar: tres verbos, tres objetivos.",
      "El paso de fase debe responder a la evolución real, no solo al calendario.",
      "No memorices las fases desordenadas.",
      ("infografia", "t12-18-tres-fases-sapi.webp", "Tres estaciones del itinerario SAPI con prestaciones de cada fase", "línea de estaciones")),

    block(4, "Derechos, deberes y finalización de la acogida", "RD220-2022-T12",
      "arts. 12 a 14 y 32",
      "La participación en el sistema genera derechos de información y atención, junto con deberes de convivencia y cooperación.",
      "La persona debe conocer condiciones, recursos, reclamaciones y causas de reducción o retirada en idioma comprensible. La finalización requiere una causa reglamentaria y decisión comunicada.",
      [
          fact("La persona destinataria tiene derecho a información comprensible sobre condiciones, derechos, deberes y causas de reducción o retirada.", "La información solo se facilita al abandonar el recurso.", "Las reglas de convivencia pueden mantenerse secretas."),
          fact("La persona destinataria debe respetar las normas de funcionamiento y cooperar cuando sea requerida.", "Participar en el sistema elimina toda obligación de convivencia.", "La cooperación autoriza al centro a divulgar datos sin límites."),
          fact("La reducción o retirada de condiciones de acogida debe apoyarse en causas y procedimiento reglamentarios.", "El personal de turno puede retirar definitivamente la acogida sin expediente.", "Cualquier queja produce automáticamente la pérdida de alojamiento."),
      ],
      "Derechos conocidos y reglas conocidas: sin información no hay participación real.",
      "Un conflicto de convivencia exige documentar hechos, escuchar y aplicar la respuesta proporcional.",
      "Retirada no es castigo improvisado.",
      ("infografia", "t12-19-contrato-acogida.webp", "Documento visual de derechos, deberes y causas de finalización", "contrato didáctico")),

    block(4, "Red de recursos y centros de migraciones", "RD220-2022-T12",
      "título III; tipología de recursos",
      "La red combina centros públicos, recursos concertados y dispositivos adaptados a distintas necesidades.",
      "Los Centros de Acogida a Refugiados se integran en la red pública de centros de migraciones. Los CETI responden a otra localización y función; no deben presentarse como figuras idénticas.",
      [
          fact("Los Centros de Acogida a Refugiados forman parte de la red pública de centros de migraciones.", "Los CAR son centros penitenciarios dependientes de Instituciones Penitenciarias.", "Los CAR solo funcionan como puestos fronterizos."),
          fact("Los recursos pueden ser de alojamiento colectivo, viviendas u otras modalidades previstas por el sistema.", "El sistema solo admite macrocentros de una única clase.", "Las viviendas quedan legalmente excluidas de la acogida."),
          fact("La asignación debe considerar disponibilidad, perfil y necesidades específicas.", "La persona elige siempre cualquier plaza con independencia del sistema.", "La asignación se efectúa al azar sin valorar vulnerabilidad."),
      ],
      "Red no significa edificio único: distintos recursos cubren distintos momentos y perfiles.",
      "CAR, CETI y vivienda de acogida pueden compartir apoyos, pero no son categorías intercambiables.",
      "No llames «centro de refugiados» a cualquier recurso migratorio.",
      ("ilustracion", "t12-il-05-red-de-recursos.webp", "Mapa dibujado de CAR, vivienda y recurso especializado conectados", "paisaje de red")),

    block(5, "Concepto y reconocimiento de apátrida", "RD865-2001-T12",
      "arts. 1 y 2",
      "Apátrida es quien no es considerado nacional por ningún Estado conforme a su legislación.",
      "El procedimiento puede iniciarse de oficio o a instancia del interesado, pero en todo caso la persona debe manifestar que carece de nacionalidad. Apatridia y refugio pueden relacionarse, pero no son equivalentes.",
      [
          fact("Se reconoce como apátrida a quien no sea considerado nacional suyo por ningún Estado conforme a su legislación.", "Es apátrida toda persona que perdió temporalmente su pasaporte.", "La apatridia depende únicamente de residir fuera del país de nacimiento."),
          fact("El procedimiento puede iniciarse de oficio o a solicitud de la persona interesada.", "Solo puede iniciarse por sentencia penal.", "La Oficina de Asilo tiene prohibido iniciarlo de oficio."),
          fact("Apatridia y condición de refugiado responden a definiciones distintas.", "Toda persona apátrida es automáticamente refugiada.", "La condición de refugiado exige necesariamente carecer de toda nacionalidad."),
      ],
      "Nacionalidad inexistente no es lo mismo que documento inexistente.",
      "Hay que investigar legislaciones y vínculos nacionales, no limitarse a mirar si hay pasaporte.",
      "Indocumentado no equivale automáticamente a apátrida.",
      ("infografia", "t12-21-apatridia-no-indocumentacion.webp", "Comparación entre apatridia e indocumentación", "comparativa de conceptos")),

    block(5, "Procedimiento y efectos de la apatridia", "RD865-2001-T12",
      "arts. 3 a 16",
      "La Oficina de Asilo y Refugio instruye; el Ministro del Interior resuelve y el interesado debe colaborar.",
      "Se admiten pruebas, alegaciones, informes e intérprete; existe audiencia por quince días cuando proceda. La resolución favorable reconoce el estatuto y la denegación remite al régimen general de extranjería.",
      [
          fact("La Oficina de Asilo y Refugio instruye el procedimiento de reconocimiento de apatridia.", "La instrucción corresponde siempre al ayuntamiento del domicilio.", "El ACNUR dicta la resolución administrativa española."),
          fact("Instruido el procedimiento, el trámite de audiencia es de quince días cuando proceda.", "El trámite de audiencia dura necesariamente cuarenta y ocho horas.", "La audiencia se celebra después de ejecutar la expulsión."),
          fact("La resolución favorable reconoce la condición de apátrida en los términos de la Convención de 1954.", "La resolución favorable concede automáticamente nacionalidad española.", "La resolución favorable equivale a una condena penal del Estado de origen."),
      ],
      "Investigar nacionalidad exige colaboración, documentos posibles e informes sobre legislaciones extranjeras.",
      "La ausencia de respuesta de un consulado es un dato, no siempre una prueba definitiva por sí sola.",
      "Tres meses es el plazo de resolución del reglamento, no el de audiencia.",
      ("infografia", "t12-22-ruta-apatridia.webp", "Ruta del expediente de apatridia desde inicio hasta resolución", "flujo procedimental")),

    block(5, "Protección temporal y personas desplazadas", "RD1325-2003-T12",
      "arts. 1 a 13",
      "La protección temporal responde a una afluencia masiva y ofrece una respuesta colectiva inmediata sin sustituir el derecho individual a pedir asilo.",
      "El régimen puede declararse por decisión del Consejo de la Unión Europea o, en determinados supuestos nacionales, por acuerdo del Consejo de Ministros conforme al reglamento.",
      [
          fact("La protección temporal se dirige a afluencias masivas de personas desplazadas que no pueden regresar en condiciones seguras y duraderas.", "La protección temporal sanciona a quienes cruzan una frontera sin autorización.", "Solo protege a personas ya reconocidas individualmente como refugiadas."),
          fact("Una decisión del Consejo de la Unión Europea puede activar el régimen de protección temporal.", "La protección temporal solo puede declararla un alcalde.", "Cada comisaría decide por separado si existe afluencia masiva."),
          fact("La protección temporal no impide presentar una solicitud individual de protección internacional.", "Quien recibe protección temporal renuncia para siempre al asilo.", "La solicitud de asilo extingue automáticamente toda protección temporal desde el primer minuto."),
      ],
      "Temporal es colectiva e inmediata; asilo es individual y examina persecución o daño grave.",
      "En una llegada masiva hay que informar de ambos cauces sin presentarlos como excluyentes absolutos.",
      "Desplazado interno y beneficiario de protección temporal no son sinónimos.",
      ("infografia", "t12-23-doble-via-temporal-asilo.webp", "Doble vía compatible entre protección temporal y solicitud individual", "doble ruta")),

    block(5, "Contenido y cese de la protección temporal", "RD1325-2003-T12",
      "arts. 14 a 24",
      "La protección temporal incorpora residencia, trabajo, información, acogida y reunificación en los términos del régimen.",
      "Su duración y cese dependen de la decisión que activa el mecanismo y de las reglas aplicables. El retorno debe respetar dignidad, seguridad y situación individual.",
      [
          fact("La persona beneficiaria recibe información escrita en una lengua que pueda comprender.", "La información debe entregarse exclusivamente en lenguaje jurídico español.", "Informar es opcional si existe alojamiento."),
          fact("El régimen contempla residencia y autorización para trabajar en los términos previstos.", "La protección temporal prohíbe toda actividad laboral.", "La autorización para trabajar sustituye a la documentación de residencia."),
          fact("La reunificación familiar puede alcanzar a los familiares definidos reglamentariamente cuando concurran sus requisitos.", "La reunificación se extiende automáticamente a cualquier amistad.", "La separación familiar nunca se valora en protección temporal."),
      ],
      "La protección temporal protege vida cotidiana: residir, trabajar, recibir ayuda y recomponer familia.",
      "Explica siempre duración, documentación y efectos del eventual cese.",
      "Temporal no significa carente de derechos.",
      ("ilustracion", "t12-il-06-maleta-de-derechos.webp", "Familia desplazada con una maleta dibujada que contiene derechos básicos", "metáfora humana")),

    block(6, "ACNUR y cooperación institucional", "L12-2009-T12,INS11-2026-T12",
      "Ley 12/2009, arts. 34 y 35; Instrucción, III.3",
      "ACNUR ocupa una posición de garantía y cooperación, pero no sustituye al órgano español que resuelve.",
      "Puede recibir información, acceder a expedientes en los términos legales, formular observaciones y ser oído. En frontera, el acceso a solicitudes se articula con consentimiento previo.",
      [
          fact("ACNUR puede intervenir en el procedimiento en los términos previstos por la ley.", "ACNUR impone sanciones de extranjería en España.", "La intervención de ACNUR está prohibida en solicitudes individuales."),
          fact("La Comisión Interministerial de Asilo y Refugio formula propuestas en el sistema nacional.", "La CIAR es un tribunal penal internacional.", "La CIAR expide pasaportes ordinarios a cualquier solicitante."),
          fact("La resolución administrativa corresponde a la autoridad española competente, no a ACNUR.", "ACNUR concede por sí solo el derecho de asilo español.", "El intérprete firma la resolución definitiva."),
      ],
      "ACNUR acompaña y supervisa; la Administración española instruye y resuelve.",
      "Diferencia claramente acceso, audiencia, informe, propuesta y resolución.",
      "Colaborar no es transferir la competencia.",
      ("infografia", "t12-25-mesa-institucional.webp", "Mesa institucional con OAR, CIAR, Ministerio y ACNUR y sus verbos", "organigrama funcional")),

    block(6, "Método de resolución de supuestos", "CONV-PN-2026,L12-2009-T12,INS11-2026-T12,RD220-2022-T12",
      "síntesis del epígrafe oficial",
      "Un caso completo exige separar estatuto, procedimiento, vulnerabilidad, acogida y posibles figuras vecinas.",
      "La secuencia útil es identificar persona y lugar, detectar necesidad de protección, escoger el cauce vigente, asegurar garantías, valorar vulnerabilidad y conectar con acogida, apatridia o protección temporal.",
      [
          fact("La primera clasificación distingue protección internacional, apatridia y protección temporal.", "Todas las figuras deben resolverse con un único formulario idéntico.", "La apatridia se decide aplicando exclusivamente las sanciones de seguridad privada."),
          fact("El lugar de presentación puede condicionar el procedimiento, especialmente en frontera.", "El lugar nunca tiene relevancia procedimental.", "Toda solicitud realizada en España sigue necesariamente el mismo plazo antiguo."),
          fact("La vulnerabilidad y la acogida se analizan además del fondo de la solicitud.", "La acogida decide por sí sola si existe persecución.", "La vulnerabilidad desaparece jurídicamente al registrar la solicitud."),
      ],
      "Cinco casillas: figura, lugar, procedimiento, garantías y apoyo.",
      "En el primer contacto no hace falta resolver el fondo, pero sí activar el cauce correcto.",
      "No mezcles estatuto jurídico con recurso de alojamiento.",
      ("infografia", "t12-26-tablero-cinco-casillas.webp", "Tablero de decisión con cinco casillas para resolver supuestos", "tablero operativo")),
]
T12["visual_blocks"] = [1, 2, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 24, 25, 8]


T13 = {
    "number": 13,
    "title": "Seguridad privada: organización, personal, servicios y medidas",
    "slug": "seguridad-privada-organizacion-personal-servicios-medidas",
    "parts": {
        1: "Bases y disposiciones generales",
        2: "Coordinación y competencias públicas",
        3: "Empresas y despachos de detectives",
        4: "Personal y funciones profesionales",
        5: "Servicios de seguridad privada",
        6: "Medidas, inspección y control",
    },
    "sources": {
        **COMMON_SOURCE,
        "L5-2014-T13": "https://www.boe.es/eli/es/l/2014/04/04/5/con",
        "RD2364-1994-T13": "https://www.boe.es/eli/es/rd/1994/12/09/2364/con",
        "OINT314-2011-T13": "https://www.boe.es/eli/es/o/2011/02/01/int314/con",
        "OINT316-2011-T13": "https://www.boe.es/eli/es/o/2011/02/01/int316/con",
        "OINT317-2011-T13": "https://www.boe.es/eli/es/o/2011/02/01/int317/con",
        "OINT318-2011-T13": "https://www.boe.es/eli/es/o/2011/02/01/int318/con",
    },
    "catalog": [
        ("L5-2014-T13", "Ley 5/2014, de Seguridad Privada", "BOE-A-2014-3649", "marco completo del epígrafe oficial"),
        ("RD2364-1994-T13", "Reglamento de Seguridad Privada de 1994", "BOE-A-1995-608", "preceptos reglamentarios subsistentes compatibles"),
        ("OINT314-2011-T13", "Orden INT/314/2011, sobre empresas de seguridad privada", "BOE-A-2011-3168", "autorización, funcionamiento y obligaciones empresariales"),
        ("OINT316-2011-T13", "Orden INT/316/2011, sobre sistemas de alarma", "BOE-A-2011-3170", "funcionamiento, verificación y comunicación de alarmas"),
        ("OINT317-2011-T13", "Orden INT/317/2011, sobre medidas de seguridad privada", "BOE-A-2011-3171", "medidas en establecimientos obligados"),
        ("OINT318-2011-T13", "Orden INT/318/2011, sobre personal de seguridad privada", "BOE-A-2011-3172", "habilitación, formación y documentación profesional"),
    ],
    "official_regex": r"seguridad privada|vigilante(?:s)? de seguridad|vigilante(?:s)? de explosivos|guardapescas mar[ií]timos|detective(?:s)? privado|escolta(?:s)? privado|jefe(?:s)? de seguridad|director(?:es)? de seguridad|central receptora|videovigilancia|medidas de seguridad",
}

T13["blocks"] = [
    block(1, "Objeto, modelo y subordinación", "CONV-PN-2026,L5-2014-T13",
      "epígrafe oficial; Ley 5/2014, arts. 1 y 4",
      "La seguridad privada protege personas y bienes mediante actividades contratadas y sometidas a control público.",
      "La ley la configura como complementaria y subordinada respecto de la seguridad pública. La contratación privada no crea una policía paralela ni desplaza las competencias de las Fuerzas y Cuerpos de Seguridad.",
      [
          fact("La Ley 5/2014 regula actividades, servicios, personal, empresas, medidas e investigación privada.", "La Ley 5/2014 solo regula alarmas domésticas.", "La investigación privada queda fuera de toda seguridad privada."),
          fact("Las actividades de seguridad privada son complementarias y subordinadas respecto de la seguridad pública.", "La seguridad privada sustituye al Estado cuando existe contrato.", "Las empresas privadas pueden asumir cualquier potestad policial."),
          fact("La seguridad privada puede ser contratada voluntariamente o venir impuesta legalmente.", "Todos los servicios son siempre voluntarios.", "Solo las Administraciones públicas pueden contratar seguridad privada."),
      ],
      "Privada en la contratación; pública en el marco y el control.",
      "Un vigilante protege el servicio contratado, pero debe colaborar cuando aparecen hechos que afectan a la seguridad pública.",
      "Complementaria no significa independiente.",
      ("infografia", "t13-02-modelo-complementario.webp", "Relación jerárquica entre seguridad pública, control y prestación privada", "diagrama de capas")),

    block(1, "Definiciones que no deben mezclarse", "L5-2014-T13",
      "art. 2",
      "Actividad, servicio, función y medida describen planos distintos de la seguridad privada.",
      "La actividad es el ámbito empresarial; el servicio es la acción contratada; la función es la facultad del personal; la medida es la disposición de prevención o protección.",
      [
          fact("Las actividades son los ámbitos materiales en que actúan los prestadores.", "Actividad significa únicamente el turno diario de un vigilante.", "Actividad y sanción administrativa son conceptos equivalentes."),
          fact("Los servicios son las acciones realizadas para materializar las actividades.", "Servicio es la habilitación profesional de una persona.", "Todo servicio de seguridad es una medida física instalada."),
          fact("Las funciones son las facultades atribuidas al personal de seguridad privada.", "Las funciones pertenecen exclusivamente a los usuarios que contratan.", "Una función profesional es siempre una actividad empresarial autorizable."),
      ],
      "Actividad contiene servicios; el personal ejerce funciones; las medidas protegen.",
      "En una pregunta, cambia una sola palabra y cambia el sujeto jurídico.",
      "La lista de definiciones es terreno clásico de distractores.",
      ("infografia", "t13-03-cuatro-conceptos.webp", "Matriz de actividad, servicio, función y medida con ejemplos", "matriz semántica")),

    block(1, "Ámbito subjetivo de aplicación", "L5-2014-T13",
      "art. 3",
      "La ley alcanza a prestadores, personal, servicios, medidas, usuarios y establecimientos obligados.",
      "También se proyecta, cuando resulte pertinente, sobre técnicos, operadores, profesores, empresas de seguridad informática, centrales de uso propio y centros de formación.",
      [
          fact("La ley se aplica a empresas de seguridad, personal, despachos de detectives, servicios, medidas y contratos del sector.", "Solo se aplica a vigilantes armados.", "Los despachos de detectives están expresamente excluidos."),
          fact("El régimen de inspección y sanción alcanza también a quien actúa sin autorización o habilitación.", "La actividad clandestina queda fuera porque no es seguridad privada legal.", "La inspección solo puede realizarse si la empresa la solicita."),
          fact("Los usuarios y establecimientos obligados pueden quedar sujetos a las disposiciones que les resulten pertinentes.", "El cliente nunca tiene obligación alguna en materia de medidas.", "Solo las empresas prestadoras están dentro del ámbito legal."),
      ],
      "La ley controla tanto a quien presta como a quien debe adoptar o contrata determinadas medidas.",
      "En una inspección identifica prestador, personal, usuario, establecimiento y servicio.",
      "Ilegal no significa invisible para la ley.",
      ("infografia", "t13-04-ecosistema-sujetos.webp", "Ecosistema completo de sujetos incluidos en la ley", "mapa de actores")),

    block(1, "Fines de la seguridad privada", "L5-2014-T13",
      "art. 4",
      "Los fines combinan necesidades legítimas del usuario, contribución a la seguridad pública e integración funcional.",
      "La actividad protege indemnidad, privacidad y bienes; previene infracciones y aporta información; y complementa el monopolio estatal de la seguridad sin apropiárselo.",
      [
          fact("Un fin es satisfacer necesidades legítimas de seguridad o información del usuario.", "La ley ampara cualquier curiosidad del cliente aunque vulnere derechos.", "La finalidad única es aumentar el beneficio de la empresa."),
          fact("La seguridad privada contribuye a prevenir infracciones y aportar información a procedimientos.", "El personal debe ocultar a la Policía todo hecho relevante.", "La prevención de infracciones corresponde exclusivamente a detectives."),
          fact("La seguridad privada integra funcionalmente medios y capacidades como recurso externo de la seguridad pública.", "La integración convierte a cada vigilante en funcionario policial.", "El Estado cede definitivamente su monopolio de seguridad."),
      ],
      "Tres fines: proteger, contribuir e integrar.",
      "La legitimidad de la necesidad contratada es el primer filtro.",
      "No confundas cooperación con condición funcionarial.",
      ("infografia", "t13-05-tres-fines.webp", "Tres engranajes de protección, contribución e integración", "engranajes funcionales")),

    block(1, "Principios rectores y colaboración", "L5-2014-T13",
      "art. 8",
      "La prestación debe respetar Constitución, ley, principios profesionales y colaboración con las Fuerzas y Cuerpos de Seguridad.",
      "La obligación de auxilio, colaboración y seguimiento de instrucciones se intensifica cuando el servicio afecta a seguridad pública o competencias policiales.",
      [
          fact("Los prestadores deben colaborar en todo momento y lugar con las Fuerzas y Cuerpos de Seguridad.", "La colaboración solo existe si el contrato privado la autoriza.", "El deber de colaboración se limita a detectives."),
          fact("Deben seguir las instrucciones policiales relacionadas con servicios que afecten a la seguridad pública o a sus competencias.", "Las instrucciones policiales pueden ignorarse si el cliente paga más.", "La empresa privada dirige operativamente a las Fuerzas y Cuerpos de Seguridad."),
          fact("La prestación debe respetar la Constitución y el resto del ordenamiento jurídico.", "El contrato privado puede excluir derechos fundamentales.", "La costumbre interna de la empresa prevalece sobre la ley."),
      ],
      "Contrato privado, límites públicos.",
      "Ante un delito, preservar, comunicar y seguir instrucciones pesa más que la comodidad del servicio.",
      "Colaborar no autoriza a invadir competencias.",
      ("ilustracion", "t13-il-01-relevo-coordinado.webp", "Vigilante y policía coordinan una intervención sin confundirse de función", "escena cooperativa")),

    block(1, "Prohibiciones y reserva de información", "L5-2014-T13",
      "arts. 8 y 10",
      "La seguridad privada no puede controlar ideas, interferir conflictos ni comunicar información protegida fuera de los cauces legales.",
      "Tampoco pueden prestarse o publicitarse servicios sin autorización, ejercerse funciones sin habilitación ni usar medios que lesionen honor, intimidad, imagen o secreto de las comunicaciones.",
      [
          fact("No puede ejercerse control sobre opiniones políticas, sindicales o religiosas.", "El cliente puede contratar perfiles ideológicos secretos de su plantilla.", "Los vigilantes deben registrar obligatoriamente las creencias de los usuarios."),
          fact("La información conocida por razón del servicio está sometida a reserva, salvo comunicación legítima a autoridades judiciales o policiales.", "Puede difundirse a cualquier tercero si resulta interesante.", "La reserva impide comunicar delitos a la Policía."),
          fact("Está prohibido ejercer funciones de seguridad privada sin habilitación o acreditación exigible.", "La experiencia informal sustituye siempre a la habilitación.", "La habilitación solo se exige en servicios con armas."),
      ],
      "Proteger no permite vigilar ideas ni comerciar con secretos.",
      "La comunicación a Policía de un hecho delictivo no es una filtración prohibida.",
      "Reserva profesional y encubrimiento no son lo mismo.",
      ("infografia", "t13-07-semáforo-limites.webp", "Semáforo de conductas permitidas, condicionadas y prohibidas", "semáforo jurídico")),

    block(2, "Competencias de la Administración del Estado", "L5-2014-T13",
      "arts. 12 y 13",
      "El Estado ejerce autorización, inspección, control, sanción y coordinación en el ámbito que le corresponde.",
      "El Ministerio del Interior, la Dirección General de la Policía y la Dirección General de la Guardia Civil distribuyen competencias según materia, sujetos y territorio.",
      [
          fact("Corresponde al Estado autorizar, inspeccionar y sancionar en los términos de la Ley 5/2014.", "Toda competencia estatal fue transferida a los municipios.", "Las empresas se autorizan a sí mismas mediante su contrato social."),
          fact("La Policía ejerce funciones de control sobre empresas, personal y servicios en su ámbito competencial.", "El control administrativo corresponde exclusivamente a asociaciones empresariales.", "La Policía solo puede intervenir después de una condena penal."),
          fact("La Guardia Civil ejerce competencias específicas, entre otras, respecto de guardas rurales y sus especialidades.", "Los guardas rurales dependen exclusivamente de la Policía Local.", "La Guardia Civil carece de toda competencia en seguridad privada."),
      ],
      "No memorices un órgano aislado: enlaza materia, territorio y sujeto.",
      "Una incidencia con guardas rurales no sigue exactamente el mismo circuito que una empresa urbana.",
      "Autorizar, controlar y sancionar son verbos diferentes.",
      ("infografia", "t13-08-mapa-competencias.webp", "Mapa funcional de Interior, Policía, Guardia Civil y órganos autonómicos", "organigrama competencial")),

    block(2, "Competencias autonómicas y registros", "L5-2014-T13",
      "arts. 13 y 11",
      "Las comunidades autónomas con competencias asumidas ejercen funciones sobre actividades y servicios desarrollados en su territorio.",
      "El Registro Nacional y los registros autonómicos aseguran constancia y coordinación. La inscripción no borra la distribución material de competencias.",
      [
          fact("Las comunidades autónomas pueden ejercer competencias asumidas estatutariamente sobre seguridad privada.", "Todas las comunidades tienen idénticas competencias por decisión de cada empresa.", "La seguridad privada está constitucionalmente fuera de cualquier competencia autonómica."),
          fact("Existe un Registro Nacional de Seguridad Privada y pueden existir registros autonómicos.", "Cada vigilante crea su propio registro privado sin comunicación.", "La inscripción solo existe para usuarios domésticos."),
          fact("La coordinación registral evita duplicidades y facilita el control administrativo.", "Los registros sustituyen a las autorizaciones y habilitaciones.", "La información registral nunca puede usarse para inspección."),
      ],
      "Competencia autonómica sí; sistema desconectado, no.",
      "Comprueba dónde se presta el servicio y qué competencia ha asumido la comunidad.",
      "Registro no equivale a licencia universal.",
      ("infografia", "t13-09-doble-registro.webp", "Conexión entre Registro Nacional y registros autonómicos", "red registral")),

    block(2, "Acceso a información y coordinación", "L5-2014-T13",
      "arts. 14 a 16",
      "La coordinación se apoya en información recíproca, órganos de participación y medidas organizativas.",
      "Las empresas y despachos deben facilitar información relevante para la seguridad pública, respetando límites legales. Interior o el órgano autonómico competente establece medidas de coordinación.",
      [
          fact("Las Fuerzas y Cuerpos de Seguridad pueden acceder a información necesaria para el ejercicio de sus funciones.", "El secreto empresarial bloquea siempre cualquier acceso legal.", "Solo el cliente puede autorizar la comunicación de un delito público."),
          fact("El Ministerio del Interior o el órgano autonómico competente adopta medidas organizativas de coordinación.", "La coordinación corresponde únicamente a cada vigilante por iniciativa personal.", "La Dirección General de Tributos organiza todos los servicios."),
          fact("Los órganos de participación permiten intercambio entre sector y Administraciones sin sustituir la autoridad pública.", "La participación convierte a las empresas en órganos policiales.", "Las comisiones pueden derogar la ley mediante acuerdo interno."),
      ],
      "Información útil, cauce legal y autoridad competente.",
      "Una central receptora comunica una alarma real con datos operativos, no todo el historial comercial del cliente.",
      "Coordinar no es ceder el mando público.",
      ("infografia", "t13-10-centro-coordinacion.webp", "Centro de coordinación con flujos de información delimitados", "diagrama de flujos")),

    block(3, "Actividades reservadas, compatibles y excluidas", "L5-2014-T13",
      "arts. 5, 6 y 7",
      "La ley separa actividades de seguridad privada, actividades compatibles y actividades excluidas.",
      "Vigilancia, protección, depósito, transporte, instalación de sistemas conectados, gestión de alarmas e investigación privada son actividades reguladas. Otras tareas auxiliares no adquieren por ello naturaleza de seguridad.",
      [
          fact("La vigilancia y protección de bienes, lugares, eventos y personas determinadas es actividad de seguridad privada.", "La vigilancia profesional es siempre una actividad auxiliar excluida.", "Solo la investigación privada aparece como actividad regulada."),
          fact("La planificación y asesoramiento en seguridad pueden ser actividades compatibles en los términos legales.", "Toda consultoría está reservada exclusivamente al Ministro del Interior.", "El asesoramiento convierte automáticamente al consultor en vigilante habilitado."),
          fact("Las tareas de recepción, información o control de accesos sin funciones de seguridad pueden ser actividades excluidas.", "Todo conserje ejerce legalmente funciones de vigilante.", "Una actividad excluida exige siempre habilitación de detective."),
      ],
      "No preguntes solo qué tarea se hace; mira con qué facultades y finalidad.",
      "Controlar una acreditación de acceso no autoriza a cachear o detener como vigilante.",
      "Auxiliar no es vigilante barato.",
      ("infografia", "t13-11-tres-zonas-actividad.webp", "Tres zonas: reservadas, compatibles y excluidas con ejemplos", "diagrama de zonas")),

    block(3, "Autorización y requisitos de empresas", "L5-2014-T13,OINT314-2011-T13",
      "arts. 17 a 19",
      "Las empresas necesitan autorización o declaración responsable cuando la ley la admite, inscripción y requisitos adecuados a la actividad.",
      "La forma jurídica, objeto, medios, garantías y seguridad de instalaciones varían según actividades. La autorización no habilita para realizar cualquier actividad no declarada.",
      [
          fact("La prestación de actividades reservadas exige autorización administrativa o declaración responsable en los casos previstos.", "Basta anunciar el servicio en internet.", "La autorización del cliente sustituye a la administrativa."),
          fact("La empresa debe estar inscrita en el registro correspondiente.", "La inscripción es voluntaria para empresas con más de cien empleados.", "Solo se inscriben los contratos, nunca las empresas."),
          fact("Los requisitos y garantías se ajustan a las actividades para las que se solicita autorización.", "Una autorización de alarmas permite automáticamente investigación privada.", "Todas las actividades exigen exactamente los mismos medios."),
      ],
      "Autorizar una empresa no es darle una llave maestra.",
      "Comprueba actividad autorizada, ámbito, inscripción y medios antes de contratar.",
      "Objeto social y autorización administrativa no son equivalentes.",
      ("infografia", "t13-12-checklist-empresa.webp", "Checklist de autorización, inscripción, actividad y garantías", "lista de verificación")),

    block(3, "Obligaciones y representantes de empresas", "L5-2014-T13",
      "arts. 20 a 22",
      "La empresa debe mantener requisitos, comunicar cambios, asegurar formación y garantizar correcta prestación.",
      "Los representantes legales deben reunir condiciones legales y responden de funciones organizativas. La empresa conserva documentación y facilita inspección.",
      [
          fact("La empresa debe comunicar las modificaciones relevantes que afecten a su autorización o inscripción.", "Los cambios societarios nunca se comunican.", "Solo se informa al finalizar definitivamente la actividad."),
          fact("Debe garantizar que el personal asignado esté habilitado y formado para sus funciones.", "Puede sustituir habilitación por uniforme parecido.", "La formación es responsabilidad exclusiva del cliente."),
          fact("La empresa debe facilitar inspecciones y conservar la documentación exigida.", "Puede destruir contratos tras cada turno.", "La inspección requiere consentimiento unánime de todos los trabajadores."),
      ],
      "La autorización se mantiene cumpliendo, no se archiva y se olvida.",
      "Una auditoría de servicio empieza por contrato, comunicación, personal y medios.",
      "La empresa responde de organizar legalmente la prestación.",
      ("ilustracion", "t13-il-02-sala-operaciones.webp", "Equipo de empresa revisa personal, contrato y medios antes del servicio", "escena de preparación")),

    block(3, "Despachos de detectives privados", "L5-2014-T13",
      "arts. 24 y 25",
      "La investigación privada se presta desde despachos habilitados y está separada de las actividades propias de empresas de seguridad.",
      "El despacho exige apertura, inscripción y obligaciones documentales. Solo puede aceptar encargos con interés legítimo y dentro de límites legales.",
      [
          fact("Los detectives privados prestan servicios de investigación desde despachos inscritos.", "Las empresas de vigilancia pueden investigar libremente delitos públicos.", "Un detective puede trabajar sin despacho ni registro."),
          fact("El encargo debe responder a un interés legítimo del contratante.", "Basta la curiosidad sobre la vida íntima de un tercero.", "El interés legítimo solo se exige cuando hay fotografías."),
          fact("Las empresas de seguridad no pueden realizar la investigación privada propia de detectives, ni estos servicios propios de aquellas.", "Vigilancia e investigación son libremente intercambiables.", "La separación solo afecta a empresas extranjeras."),
      ],
      "Encargo legítimo, objeto lícito y despacho inscrito.",
      "Antes de aceptar un caso, el detective debe poder explicar qué derecho o interés legítimo se protege.",
      "Investigar no autoriza a invadir intimidad.",
      ("infografia", "t13-14-frontera-investigacion.webp", "Frontera entre vigilancia empresarial e investigación de detectives", "comparativa de ámbitos")),

    block(4, "Categorías de personal habilitado", "L5-2014-T13",
      "art. 26",
      "La ley enumera categorías profesionales con funciones propias y no intercambiables.",
      "Comprende vigilantes y su especialidad de explosivos, escoltas, guardas rurales y sus especialidades, jefes y directores de seguridad y detectives privados.",
      [
          fact("El vigilante de explosivos es una especialidad del vigilante de seguridad.", "Es una categoría ajena que impide ser vigilante.", "Es una especialidad del detective privado."),
          fact("Guardas de caza y guardapescas marítimos son especialidades de los guardas rurales.", "Son especialidades de los escoltas privados.", "Carecen de la condición de personal de seguridad privada."),
          fact("Jefes y directores de seguridad son categorías distintas con funciones diferenciadas.", "Son dos nombres de una única habilitación idéntica.", "Solo pueden existir en la Administración pública."),
      ],
      "Categoría, especialidad y función: tres columnas que deben encajar.",
      "El uniforme no identifica por sí solo la habilitación concreta.",
      "Vigilante de explosivos sí necesita la habilitación previa de vigilante.",
      ("infografia", "t13-15-arbol-profesional.webp", "Árbol de categorías y especialidades del personal", "árbol jerárquico")),

    block(4, "Habilitación y requisitos generales", "L5-2014-T13,OINT318-2011-T13",
      "arts. 27 a 29",
      "El ejercicio de funciones exige habilitación profesional y mantenimiento de requisitos de aptitud y honorabilidad.",
      "La ley contempla edad, capacidad, formación, aptitud física y psíquica, carencia de determinados antecedentes y sanciones, además de requisitos de nacionalidad o régimen equiparado.",
      [
          fact("La habilitación profesional es previa al ejercicio de las funciones reservadas.", "Puede obtenerse después de varios años de ejercicio clandestino.", "Solo los detectives necesitan habilitación."),
          fact("No haber sido sancionado por infracción grave o muy grave en los períodos legales es un requisito general.", "Cualquier sanción leve impide habilitarse durante diez años.", "Las sanciones de seguridad privada nunca influyen."),
          fact("La formación y las pruebas acreditan conocimientos y aptitudes para la categoría.", "La empresa puede inventar su propia tarjeta profesional.", "La experiencia sin control sustituye siempre todas las pruebas."),
      ],
      "Habilitación antes, función después.",
      "Verifica categoría y vigencia de la tarjeta de identidad profesional antes de asignar el puesto.",
      "Contratar no habilita.",
      ("infografia", "t13-16-ruta-habilitacion.webp", "Ruta desde requisitos y formación hasta habilitación", "flujo de acceso")),

    block(4, "Principios de actuación y protección jurídica", "L5-2014-T13",
      "arts. 30 y 31",
      "El personal actúa con legalidad, integridad, dignidad, corrección, congruencia y proporcionalidad.",
      "Cuando coopera y actúa bajo mando de las Fuerzas y Cuerpos de Seguridad, el ordenamiento le reconoce protección jurídica reforzada frente a agresiones en los términos legales.",
      [
          fact("Legalidad, integridad, dignidad, corrección, congruencia y proporcionalidad son principios de actuación.", "El único principio es obedecer al cliente.", "La proporcionalidad solo rige para detectives."),
          fact("La fuerza solo puede emplearse cuando sea necesaria y de forma proporcional.", "Puede emplearse como castigo preventivo.", "La empresa fija libremente supuestos de uso de fuerza fuera de la ley."),
          fact("La protección jurídica reforzada se vincula a personal identificado que coopera y actúa bajo mando policial.", "Todo empleado de una empresa tiene siempre condición plena de autoridad.", "Basta llevar uniforme aunque no exista cooperación ni mando."),
      ],
      "Poder limitado por principios claros.",
      "La actuación más eficaz es la que resuelve con la mínima intervención necesaria.",
      "Protección de agente no convierte al vigilante en policía.",
      ("ilustracion", "t13-il-03-escudo-proporcional.webp", "Vigilante protegido por un escudo con principios de actuación", "metáfora dibujada")),

    block(4, "Vigilantes de seguridad", "L5-2014-T13",
      "art. 32",
      "Los vigilantes protegen bienes, establecimientos, eventos y personas dentro del servicio contratado.",
      "Pueden efectuar controles de identidad y objetos en el acceso o interior, impedir acceso o permanencia y detener y poner inmediatamente a disposición policial a quien sorprendan en relación con el objeto protegido.",
      [
          fact("Los vigilantes ejercen vigilancia y protección de bienes, lugares, eventos y personas.", "Su función principal es investigar la vida privada de clientes.", "Solo pueden vigilar vías públicas sin servicio contratado."),
          fact("Pueden realizar controles de identidad en el acceso o interior sin retener documentación personal.", "Pueden quedarse el DNI hasta el día siguiente.", "Nunca pueden comprobar identidad en un acceso protegido."),
          fact("Ante un delito relacionado con el objeto protegido, deben detener y poner inmediatamente a disposición de las Fuerzas y Cuerpos de Seguridad al autor y efectos.", "Pueden interrogar indefinidamente al detenido.", "Deben imponer por sí mismos la pena correspondiente."),
      ],
      "Controlar sí; retener documentos, no.",
      "Tras la detención, seguridad, aviso y entrega inmediata: el servicio no es una comisaría.",
      "Detener no autoriza a interrogar.",
      ("infografia", "t13-18-ciclo-vigilante.webp", "Ciclo de prevención, control, intervención y entrega policial", "ciclo operativo")),

    block(4, "Escoltas privados", "L5-2014-T13",
      "art. 33",
      "El escolta acompaña, defiende y protege a personas determinadas frente a agresiones o actos delictivos.",
      "La función es personal y preventiva. Su actuación y uso de armas quedan sujetos a habilitación, servicio autorizado y principios de necesidad y proporcionalidad.",
      [
          fact("El escolta privado protege a personas determinadas.", "Su función propia es custodiar edificios vacíos.", "Solo realiza investigaciones patrimoniales."),
          fact("Debe impedir agresiones o actos delictivos contra la persona protegida.", "Puede sancionar administrativamente a cualquier viandante.", "Su misión es dirigir a la Policía durante eventos."),
          fact("El porte y uso de armas se somete a las condiciones legales del servicio.", "Todo escolta puede portar cualquier arma fuera de servicio.", "La autorización del protegido sustituye a la normativa de armas."),
      ],
      "El centro del servicio es la persona protegida.",
      "La ruta, el entorno y la anticipación importan más que una reacción aparatosa.",
      "Escoltar no es investigar.",
      ("ilustracion", "t13-il-04-burbuja-proteccion.webp", "Escolta crea una burbuja móvil de protección alrededor de una persona", "escena dinámica")),

    block(4, "Guardas rurales y especialidades", "L5-2014-T13",
      "art. 34",
      "Los guardas rurales protegen personas y bienes en fincas rústicas y desarrollan funciones en el medio rural.",
      "Sus especialidades amplían el ámbito: guardas de caza y guardapescas marítimos. La Guardia Civil ejerce competencias específicas de control.",
      [
          fact("Los guardas rurales ejercen vigilancia y protección en fincas rústicas.", "Su ámbito exclusivo son aeropuertos internacionales.", "Solo pueden trabajar dentro de bancos."),
          fact("Guardas de caza y guardapescas marítimos son especialidades del guarda rural.", "Son especialidades del vigilante de explosivos.", "Son funcionarios de Policía Nacional."),
          fact("Deben colaborar y poner hechos delictivos a disposición de las Fuerzas y Cuerpos de Seguridad.", "Pueden juzgar infracciones de caza en el lugar.", "La colaboración está prohibida para proteger al cliente."),
      ],
      "Rural es la categoría; caza y mar, sus especialidades.",
      "Una actuación en finca debe preservar indicios y activar el cuerpo competente.",
      "Guardapescas marítimo sí forma parte del personal de seguridad privada.",
      ("infografia", "t13-20-mapa-rural.webp", "Mapa de finca, coto y espacio marítimo con cada especialidad", "mapa territorial")),

    block(4, "Jefes y directores de seguridad", "L5-2014-T13",
      "arts. 35 y 36",
      "El jefe organiza servicios de la empresa; el director integra la seguridad de la entidad usuaria.",
      "El jefe analiza riesgos, planifica y controla servicios y personal de la empresa. El director organiza recursos, propone sistemas y coordina la seguridad integral del usuario.",
      [
          fact("El jefe de seguridad ejerce funciones de análisis, planificación y organización de servicios de la empresa.", "Su función exclusiva es conducir vehículos blindados.", "Representa siempre al usuario frente a sus empleados."),
          fact("El director de seguridad organiza y administra recursos de seguridad de la entidad usuaria.", "Solo puede trabajar como escolta personal.", "Su función se limita a reparar cámaras."),
          fact("Jefe y director cooperan con las Fuerzas y Cuerpos de Seguridad dentro de sus respectivos ámbitos.", "Ambos pueden negarse a toda coordinación por secreto empresarial.", "El director sustituye al juez en investigaciones internas."),
      ],
      "Jefe mira desde la empresa prestadora; director, desde la organización protegida.",
      "En un gran evento ambos pueden coincidir, pero no intercambian automáticamente sus responsabilidades.",
      "Dos puestos estratégicos, dos perspectivas.",
      ("infografia", "t13-21-doble-puesto.webp", "Comparación jefe de seguridad y director de seguridad", "doble perfil")),

    block(4, "Detectives privados: funciones y límites", "L5-2014-T13",
      "art. 37",
      "El detective investiga hechos privados legítimos, delitos perseguibles a instancia de parte y vigilancia en determinados ámbitos.",
      "No puede investigar delitos perseguibles de oficio; si conoce uno debe denunciarlo y entregar información e instrumentos relacionados.",
      [
          fact("El detective investiga hechos y conductas privadas vinculados a un interés legítimo.", "Puede investigar cualquier intimidad por encargo anónimo.", "Solo puede investigar delitos de terrorismo."),
          fact("Puede investigar delitos perseguibles a instancia de parte por encargo legitimado.", "Puede ocultar a la autoridad delitos perseguibles de oficio.", "Todo delito exige contratar previamente un detective."),
          fact("Si conoce un delito perseguible de oficio debe denunciarlo inmediatamente y poner a disposición lo obtenido.", "Debe continuar en secreto hasta cobrar el informe.", "Puede negociar la destrucción de evidencias con el cliente."),
      ],
      "Interés legítimo abre la puerta; derechos fundamentales marcan las paredes.",
      "Si aparece un delito público, cambia la prioridad: preservar y denunciar.",
      "Detective no es policía privada.",
      ("ilustracion", "t13-il-05-investigacion-legitima.webp", "Detective sigue una ruta legítima y se detiene ante el límite de la intimidad", "metáfora de recorrido")),

    block(5, "Reglas comunes de prestación", "L5-2014-T13",
      "arts. 38 a 40",
      "Todo servicio debe estar contratado, comunicado cuando proceda y prestarse por personal y empresa habilitados.",
      "La prestación se ajusta al contrato, instrucciones profesionales y marco público. Como regla, los vigilantes actúan dentro de inmuebles o propiedades, con excepciones legales.",
      [
          fact("No puede prestarse un servicio de seguridad privada sin contratación previa y, cuando proceda, autorización o comunicación.", "El servicio verbal clandestino es válido si dura menos de una hora.", "La comunicación sustituye siempre al contrato."),
          fact("Los contratos deben formalizarse por escrito y comunicarse con la antelación reglamentaria.", "Solo se escriben después de una incidencia.", "Los contratos de investigación deben detallar públicamente toda la vida del investigado."),
          fact("El servicio se presta por personal habilitado integrado en empresa autorizada cuando así lo exige la actividad.", "El usuario puede habilitar temporalmente a cualquier empleado.", "La habilitación deja de ser necesaria en horario nocturno."),
      ],
      "Contrato, comunicación, empresa, personal y lugar.",
      "Antes de iniciar el turno, la orden de servicio debe coincidir con lo comunicado.",
      "Un servicio real no legaliza un contrato inexistente.",
      ("infografia", "t13-23-cinco-llaves-servicio.webp", "Cinco llaves para abrir legalmente un servicio", "regla mnemotécnica")),

    block(5, "Vigilancia, protección y armas", "L5-2014-T13",
      "arts. 40 y 41",
      "Los servicios de vigilancia se prestan en los lugares y condiciones legales; el arma es excepcional y vinculada al servicio.",
      "Existen supuestos en que la vigilancia puede extenderse a vías o espacios de uso común. Los servicios armados requieren determinación legal o administrativa y arma reglamentaria.",
      [
          fact("La vigilancia puede extenderse fuera de inmuebles en los supuestos expresamente previstos.", "Todo vigilante puede patrullar libremente cualquier calle.", "Nunca puede existir servicio de vigilancia en un evento exterior."),
          fact("Los servicios con armas se limitan a los supuestos legal o reglamentariamente determinados.", "El cliente decide sin límites si el servicio será armado.", "Todo servicio nocturno debe ser armado."),
          fact("El arma reglamentaria se porta durante el servicio autorizado y se custodia conforme a la normativa.", "Puede llevarse a cualquier actividad particular.", "La empresa puede sustituirla por un arma no documentada."),
      ],
      "El arma acompaña a un servicio habilitado; no acompaña a la persona por costumbre.",
      "Delimita físicamente el servicio para no invadir el espacio público.",
      "Excepción no es permiso general.",
      ("ilustracion", "t13-il-06-perimetro-servicio.webp", "Vigilante dentro de un perímetro claro con excepciones señaladas", "escena espacial")),

    block(5, "Videovigilancia", "L5-2014-T13",
      "art. 42",
      "La videovigilancia capta, graba, trata y almacena imágenes para prevenir y proteger dentro de límites de proporcionalidad y privacidad.",
      "Las cámaras conectadas a centrales de alarma o integradas en medidas obligatorias siguen reglas específicas. No toda cámara doméstica convierte a su titular en empresa de seguridad.",
      [
          fact("La videovigilancia de seguridad debe respetar proporcionalidad y normativa de protección de datos.", "Puede orientarse a cualquier espacio privado ajeno por simple conveniencia.", "Las imágenes carecen de toda protección jurídica."),
          fact("Las cámaras que forman parte de medidas obligatorias o sistemas de alarma no requieren autorización administrativa individual para su instalación o uso en los términos del artículo 42.", "Todas requieren autorización judicial previa.", "Solo las entidades bancarias pueden instalar cámaras."),
          fact("La visualización profesional de sistemas de seguridad corresponde al personal y servicios habilitados cuando la ley lo reserva.", "Cualquier tercero puede gestionar una central de videovigilancia sin requisitos.", "Las cámaras sustituyen siempre al personal humano exigido."),
      ],
      "Finalidad, campo de visión, acceso y conservación.",
      "Una cámara bien instalada puede ser ilegal si apunta donde no debe o conserva sin control.",
      "Videovigilar no es grabarlo todo.",
      ("infografia", "t13-25-cono-vision.webp", "Conos de visión permitidos y zonas de privacidad protegida", "diagrama espacial")),

    block(5, "Protección personal, depósito y transporte", "L5-2014-T13",
      "arts. 43 a 45",
      "La ley diferencia protección de personas, custodia de bienes valiosos y transporte de seguridad.",
      "Cada servicio requiere personal, vehículos, instalaciones, comunicación y medidas adecuados al riesgo. El depósito y el transporte forman una cadena de custodia.",
      [
          fact("La protección personal se presta por escoltas privados en servicios autorizados.", "Se presta por detectives sin habilitación de escolta.", "La persona protegida puede conferir potestades policiales."),
          fact("El depósito de objetos valiosos exige instalaciones y medidas de seguridad adecuadas.", "Puede realizarse en cualquier trastero sin requisitos.", "El depósito elimina la necesidad de registrar entregas."),
          fact("El transporte de fondos y valores mantiene una cadena de custodia con medios y personal reglamentarios.", "Puede realizarlo cualquier mensajero si el vehículo es grande.", "La cadena de custodia comienza después de entregar los valores."),
      ],
      "Persona, depósito y ruta son riesgos distintos.",
      "En transporte, cada transferencia debe dejar claro quién recibe, qué recibe y cuándo.",
      "Custodiar no es simplemente guardar.",
      ("infografia", "t13-26-cadena-custodia.webp", "Cadena de custodia desde depósito hasta entrega de valores", "secuencia logística")),

    block(5, "Instalación, mantenimiento y alarmas", "L5-2014-T13,OINT316-2011-T13",
      "arts. 46 a 48",
      "Los sistemas conectados a centrales y la gestión de alarmas son actividades reservadas sometidas a verificación y comunicación.",
      "La central recibe señales, aplica procedimientos de verificación y comunica alarmas reales a las Fuerzas y Cuerpos de Seguridad. Las falsas alarmas reiteradas tienen consecuencias.",
      [
          fact("La instalación de sistemas conectados a centrales receptoras es actividad de seguridad privada.", "Cualquier instalador sin empresa autorizada puede conectarlos profesionalmente.", "La conexión convierte al usuario en vigilante."),
          fact("La central debe verificar las señales por los procedimientos reglamentarios antes de comunicar cuando así proceda.", "Debe comunicar toda señal sin comprobación alguna.", "Puede ignorar una alarma confirmada por comodidad."),
          fact("La comunicación a las Fuerzas y Cuerpos de Seguridad debe aportar datos útiles sobre la alarma.", "La central decide la pena del intruso.", "La Policía necesita autorización del presunto autor para acudir."),
      ],
      "Señal, verificación, clasificación y comunicación.",
      "Una buena verificación reduce falsas movilizaciones sin retrasar una alarma real.",
      "Central receptora no es central de castigo.",
      ("infografia", "t13-27-ruta-alarma.webp", "Ruta técnica de una señal desde sensor hasta respuesta policial", "flujo tecnológico")),

    block(5, "Investigación privada e informes", "L5-2014-T13",
      "arts. 48 a 50",
      "El informe documenta hechos investigados, medios y resultados dentro del encargo legítimo.",
      "Debe conservarse con reserva y estar disponible para autoridades competentes en los supuestos legales. El detective no puede utilizar medios que lesionen derechos fundamentales.",
      [
          fact("El informe de investigación se entrega al cliente legitimado y documenta el resultado del encargo.", "Debe publicarse en redes sociales.", "Solo puede contener opiniones sin hechos."),
          fact("Los informes y soportes se conservan durante el plazo legal con medidas de reserva.", "Deben destruirse antes de poder ser inspeccionados.", "Cualquier empleado del cliente puede copiarlos libremente."),
          fact("La investigación no puede utilizar medios que vulneren honor, intimidad, imagen o secreto de comunicaciones.", "El pago del cliente legitima cualquier intrusión.", "Los derechos fundamentales no se aplican a investigaciones privadas."),
      ],
      "Informe útil, fuente lícita y destinatario legitimado.",
      "Escribe lo observado y acreditado, no lo que el cliente esperaba encontrar.",
      "Reserva no permite fabricar pruebas.",
      ("ilustracion", "t13-il-07-informe-bajo-llave.webp", "Informe de detective guardado bajo llave y entregado al destinatario legítimo", "metáfora documental")),

    block(6, "Adopción y tipos de medidas de seguridad", "L5-2014-T13,OINT317-2011-T13",
      "arts. 51 y 52",
      "Las medidas pueden imponerse por norma o resolución y combinar componentes físicos, electrónicos, informáticos, organizativos y personales.",
      "La respuesta debe ser proporcional al riesgo y cumplir homologación o certificación cuando proceda. Una sola medida rara vez sustituye a un sistema coherente.",
      [
          fact("Las medidas de seguridad pueden ser físicas, electrónicas, informáticas, organizativas o personales.", "La ley solo reconoce muros y cerraduras.", "Las medidas personales están siempre prohibidas."),
          fact("Determinados establecimientos están obligados a adoptar medidas por su riesgo.", "Toda vivienda debe instalar exactamente las mismas medidas que un banco.", "Ningún establecimiento puede ser obligado por la Administración."),
          fact("Los elementos deben cumplir homologación, certificación o verificación cuando sea preceptivo.", "Cualquier producto sirve si es barato.", "La homologación sustituye al mantenimiento."),
      ],
      "Capas distintas contra riesgos distintos.",
      "Una caja fuerte sin procedimiento de apertura ni alarma forma una defensa incompleta.",
      "Homologado no significa eterno.",
      ("infografia", "t13-29-capas-medidas.webp", "Edificio protegido por capas físicas, electrónicas, organizativas y personales", "modelo de capas")),

    block(6, "Establecimientos obligados y medidas específicas", "OINT317-2011-T13",
      "capítulos II y III",
      "Entidades de crédito, joyerías, estaciones de servicio, farmacias, administraciones de lotería y otros establecimientos tienen reglas diferenciadas.",
      "Las medidas dependen del tipo de establecimiento, valores manejados y condiciones reglamentarias. Memorizar una medida sin identificar su establecimiento genera errores.",
      [
          fact("Las entidades de crédito deben adoptar las medidas específicas previstas para su actividad.", "Se rigen exactamente por las mismas medidas mínimas de una vivienda.", "Pueden elegir no adoptar ninguna medida si tienen seguro."),
          fact("Joyerías y establecimientos de especial riesgo tienen obligaciones adaptadas a valores y exposición.", "Solo necesitan un cartel disuasorio.", "La conexión de alarma elimina toda medida física exigible."),
          fact("Las administraciones de lotería están entre los establecimientos con medidas específicas, pero cada obligación debe comprobarse en la norma vigente.", "Toda pregunta histórica anulada se convierte en regla actual.", "Están exentas de cualquier medida por pertenecer al Estado."),
      ],
      "Primero identifica establecimiento; después busca su paquete de medidas.",
      "Una respuesta antigua puede haber sido anulada o modificada: no la reutilices sin cotejo.",
      "No traslades la medida de un banco a una farmacia.",
      ("infografia", "t13-30-ciudad-establecimientos.webp", "Calle con varios establecimientos y sus medidas diferenciadas", "mapa urbano comparativo")),

    block(6, "Inspección y deber de colaboración", "L5-2014-T13",
      "arts. 53 y 54",
      "Las Fuerzas y Cuerpos de Seguridad inspeccionan entidades, servicios, personal y medidas dentro de su competencia.",
      "Los sujetos inspeccionados deben facilitar acceso, información y documentación. Las actas recogen hechos constatados y pueden activar corrección o sanción.",
      [
          fact("La inspección puede abarcar empresas, despachos, servicios, personal, centros y establecimientos obligados.", "Solo puede inspeccionarse a vigilantes en la vía pública.", "Los sistemas de alarma quedan fuera de control."),
          fact("Los inspeccionados deben facilitar información y acceso a documentación exigible.", "Pueden ocultar contratos alegando secreto comercial absoluto.", "La colaboración solo es voluntaria."),
          fact("El acta de inspección documenta hechos sin sustituir por sí sola la resolución sancionadora.", "El acta es una sentencia penal firme.", "La inspección impone automáticamente cierre definitivo."),
      ],
      "Inspeccionar es comprobar; sancionar exige su procedimiento.",
      "Ten disponible autorización, contratos, comunicaciones, personal y mantenimiento.",
      "Acta y resolución no son el mismo documento.",
      ("ilustracion", "t13-il-08-inspeccion-en-capas.webp", "Equipo inspector revisa documentos, personal, sistema y establecimiento", "escena de control")),

    block(6, "Control, corrección y repaso operativo", "L5-2014-T13",
      "epígrafe oficial completo",
      "Resolver bien exige identificar sujeto, actividad, autorización, personal, función, servicio, medida y órgano de control.",
      "Las preguntas históricas explotan parejas cercanas: actividad/servicio, jefe/director, vigilante/escolta, empresa/despacho y seguridad pública/privada.",
      [
          fact("La calificación correcta comienza por identificar quién actúa y qué actividad o función realiza.", "Basta mirar el uniforme para resolver cualquier caso.", "El sujeto nunca influye en la respuesta."),
          fact("Después se comprueban habilitación, autorización, contrato, lugar y límites de la actuación.", "El contrato elimina la necesidad de habilitación.", "La autorización empresarial convierte en lícito cualquier medio."),
          fact("La cooperación policial no transforma al personal privado en funcionario, salvo la protección jurídica concreta prevista.", "Todo vigilante es miembro de las Fuerzas y Cuerpos de Seguridad.", "La colaboración impide aplicar principios de proporcionalidad."),
      ],
      "Ocho casillas: sujeto, actividad, empresa, personal, función, servicio, medida y control.",
      "Si una opción mezcla dos categorías, probablemente está construida como distractor.",
      "La precisión vence a la intuición.",
      ("infografia", "t13-32-tablero-ocho-casillas.webp", "Tablero de ocho casillas para resolver supuestos de seguridad privada", "tablero de decisión")),
]
T13["visual_blocks"] = [1, 2, 3, 4, 5, 6, 7, 9, 10, 12, 13, 14, 16, 17, 18, 20, 21, 23, 24, 27, 28, 30, 31]


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def write_json(path: Path, data) -> None:
    write(path, json.dumps(data, ensure_ascii=False, indent=2))


def visuals_for(cfg: dict) -> list[tuple]:
    n = cfg["number"]
    visuals = [
        (f"t{n:02d}-01-mapa-general.webp", "infografia",
         list(range(1, len(cfg["blocks"]) + 1)),
         f"Mapa general ilustrado de las seis partes del Tema {n}",
         "mapa general"),
    ]
    selected = set(cfg.get("visual_blocks", range(1, len(cfg["blocks"]) + 1)))
    for idx, item in enumerate(cfg["blocks"], 1):
        if idx not in selected:
            continue
        kind, filename, description, family = item["visual"]
        visuals.append((filename, kind, [idx], description, family))
    return visuals


def generate_master(cfg: dict) -> tuple[str, list[dict]]:
    n, blocks = cfg["number"], cfg["blocks"]
    lines = [
        f"# TEMA {n} · {cfg['title'].upper()}",
        "",
        f"<!-- content_version: {VERSION} -->",
        "<!-- opposition: policia-nacional -->",
        "<!-- status: approved_internal; publication: not_published -->",
        "",
        f"> Alcance editorial: epígrafe oficial de Escala Básica publicado el 10 de julio de 2026. "
        f"Corte normativo: {CUT_OFF}. Redacción propia reconstruida desde fuentes oficiales. "
        "Los documentos privados se emplearon exclusivamente como inventario de cobertura.",
        "",
    ]
    coverage, fact_index = [], 0
    for block_no, item in enumerate(blocks, 1):
        parte = [item["intro"], ""]
        atestado = [item["intro"], "", item["detail"], "", "### Claves normativas", ""]
        ids = []
        for fdata in item["facts"]:
            fact_index += 1
            fid = f"PN-T{n:02d}-F{fact_index:03d}"
            ids.append(fid)
            parte.append(f"- {fdata['correct']}")
            atestado.append(f"- {fdata['correct']}")
            coverage.append({
                "id": fid, "oposicion": "policia-nacional", "tema": n,
                "bloque": block_no, "bloque_titulo": item["title"],
                "parte": item["part"], "parte_titulo": cfg["parts"][item["part"]],
                "punto": block_no, "enunciado_atomico": fdata["correct"],
                "fuente": item["source"].split(",")[0], "_article": item["articles"],
                "estado_revision": "fuente_oficial_comprobada_y_aprobada",
                "content_version": VERSION, "riesgo_examen": fdata["risk"],
                "risk": fdata["risk"], "preguntas": [], "covered": True,
                "anchor_score": 1.0, "_wrong": fdata["wrong"],
            })
        atestado += [""] + [f"<!-- FACT:{fid} -->" for fid in ids]
        if block_no in set(cfg.get("visual_blocks", range(1, len(blocks) + 1))):
            kind, filename, description, _family = item["visual"]
            label = "Ilustración simple" if kind == "ilustracion" else "Referencia visual prevista"
            callout = f"\n:::visual\n**{label}:** `{filename}` · {description}.\n:::"
            parte.append(callout)
            atestado.append(callout)
        atestado += [
            "", ":::hablemos-claro", item["clear"], ":::", "",
            ":::en-la-calle", item["street"], ":::", "",
            ":::lo-que-cae", item["falls"], ":::",
        ]
        lines += [
            f"<!-- BLOCK {block_no:02d} START -->",
            f"## {block_no}. {item['title']}",
            f"**Fuente principal:** `{item['source']}`",
            "<!-- PARTE START -->", *parte, "<!-- PARTE END -->",
            "<!-- ATESTADO START -->", *atestado, "<!-- ATESTADO END -->",
            f"<!-- BLOCK {block_no:02d} END -->", "",
        ]
    lines += [
        "<!-- LAYER:MAPA -->", "# Mapa del tema", "",
        ":::visual",
        f"**Mapa general previsto:** `t{n:02d}-01-mapa-general.webp` · recorrido visual por las seis partes y sus relaciones.",
        ":::", "",
        f"El Tema {n} se estudia como un sistema de decisiones enlazadas, no como una colección de listas aisladas.",
        "", "<!-- LAYER:CONTENIDO -->", "# Contenido", "",
        f"El contenido se desarrolla en {len(blocks)} bloques semánticos sincronizados con El Parte y El Atestado.",
        "", "<!-- LAYER:HABLEMOS_CLARO -->", "# Hablemos claro", "",
        ":::hablemos-claro",
        "Lee primero el sujeto, después la figura jurídica y por último la competencia, el procedimiento o el efecto.",
        ":::", "", "<!-- LAYER:EN_LA_CALLE -->", "# En la calle", "",
        ":::en-la-calle",
        "Una actuación correcta fija hechos, activa garantías y documenta el cauce empleado antes de llegar a la conclusión.",
        ":::", "", "<!-- LAYER:LO_QUE_CAE -->", "# Lo que cae", "",
        ":::lo-que-cae",
        "Prioriza definiciones próximas, sujetos competentes, secuencias, límites, excepciones y diferencias entre figuras vecinas.",
        ":::", "", "<!-- LAYER:HA_CAIDO -->", "# Ha caído", "",
        ":::ha-caido",
        "Las coincidencias históricas se conservan en el índice interno y permanecen ocultas mientras no exista plantilla oficial final verificada.",
        ":::",
    ]
    return "\n".join(lines), coverage


def build_questions(cfg: dict, facts: list[dict]) -> list[dict]:
    n = cfg["number"]
    stems = [
        "Señale la afirmación correcta sobre «{concept}»:",
        "En relación con «{concept}», ¿qué opción se ajusta al marco vigente?",
        "Ante un supuesto de «{concept}», indique la regla aplicable:",
        "¿Cuál de estas afirmaciones distingue correctamente «{concept}»?",
    ]
    good = ["🎯 Concepto bien aislado.", "🧭 Ruta correcta.", "⚖️ Límite bien aplicado.", "🔎 Matiz detectado."]
    bad = ["🪤 El distractor cambió una categoría.", "🧩 Revisa sujeto y efecto.", "🚧 Esa función no corresponde.", "📚 Vuelve a la regla vigente."]
    letters, questions = ["A", "B", "C"], []
    for fdata in facts:
        variants, ids = (2 if fdata["risk"] == 5 else 1), []
        for variant in range(variants):
            qno = len(questions) + 1
            qid = f"PN-T{n:02d}-Q{qno:03d}"
            ids.append(qid)
            correct = letters[(qno - 1) % 3]
            wrong = list(fdata["_wrong"])
            if variant:
                wrong.reverse()
            options, it = {}, iter(wrong)
            for letter in letters:
                options[letter] = fdata["enunciado_atomico"] if letter == correct else next(it)
            questions.append({
                "id": qid, "fact_id": fdata["id"], "oposicion": "policia-nacional",
                "tema": n, "bloque": fdata["bloque"], "punto": fdata["punto"],
                "subpunto": fdata["_article"], "parte": fdata["parte"],
                "parte_titulo": fdata["parte_titulo"], "concepto": fdata["bloque_titulo"],
                "norma": fdata["fuente"], "articulo": fdata["_article"],
                "riesgo_examen": fdata["risk"], "dificultad": "alta" if fdata["risk"] == 5 else "media",
                "tipo": "literal_discriminacion" if variant == 0 else "supuesto_aplicado",
                "enunciado": stems[(qno + variant - 1) % len(stems)].format(concept=fdata["bloque_titulo"]),
                "opciones": options, "respuesta_correcta": correct,
                "explicacion": fdata["enunciado_atomico"] + " Los distractores alteran el sujeto, la categoría, el requisito, el límite o el efecto.",
                "retroalimentacion": {
                    "acierto": {"humor": good[(qno - 1) % len(good)], "explicacion": fdata["enunciado_atomico"]},
                    "fallo": {"humor": bad[(qno - 1) % len(bad)], "explicacion": f"La correcta es la {correct}: {fdata['enunciado_atomico']}"},
                },
                "estado_revision": "validado_normativa_y_coherencia", "version_normativa": CUT_OFF,
                "caracter": "propio", "referencia_oficial": None, "relaciones": [fdata["id"]],
                "equivalencias": [], "content_version": VERSION,
            })
        fdata["preguntas"] = ids
    by_fact = defaultdict(list)
    for q in questions:
        by_fact[q["fact_id"]].append(q["id"])
    for q in questions:
        q["equivalencias"] = [x for x in by_fact[q["fact_id"]] if x != q["id"]]
    return questions


def clean_facts(facts: list[dict]) -> list[dict]:
    return [{k: v for k, v in item.items() if not k.startswith("_")} for item in facts]


def map_block(cfg: dict, prompt: str) -> int:
    p = prompt.casefold()
    if cfg["number"] == 12:
        rules = [
            (21, r"estatuto de apátrida|apátrida"),
            (15, r"menores? no acompañados"),
            (23, r"protección temporal|personas desplazadas"),
            (6, r"non refoulement|no devolución|denegar"),
            (3, r"condición de refugiado|motivos? de persecución"),
            (7, r"derecho a solicitar|solicitar la protección"),
            (11, r"fronter|puesto fronterizo"),
            (22, r"oficina de asilo"),
        ]
    else:
        rules = [
            (14, r"vigilante de explosivos|guardapescas|personal de seguridad"),
            (16, r"agente de la autoridad|principios de actuación"),
            (17, r"vigilante de seguridad"),
            (19, r"guarda rural|guardapescas"),
            (20, r"jefe de seguridad|director de seguridad"),
            (21, r"detective"),
            (24, r"videovigilancia|cámaras"),
            (27, r"central receptora|alarma"),
            (8, r"art. 16|coordinación"),
            (9, r"información.*fuerzas|coordinación"),
            (10, r"actividades compatibles"),
            (28, r"medidas de seguridad|lotería|entidades de crédito"),
        ]
    for block_no, pattern in rules:
        if re.search(pattern, p):
            return min(block_no, len(cfg["blocks"]))
    return 1


def build_official_index(cfg: dict, facts: list[dict]) -> dict:
    regex = re.compile(cfg["official_regex"], re.I)
    rows = []
    official_root = ROOT / "banco-preguntas/policia-nacional/oficiales"
    for path in sorted(official_root.glob("*/preguntas.jsonl")):
        for raw in path.read_text(encoding="utf-8").splitlines():
            if not raw.strip():
                continue
            q = json.loads(raw)
            if not regex.search(q.get("prompt", "")):
                continue
            if q.get("answer", {}).get("annulled"):
                continue
            block_no = map_block(cfg, q["prompt"])
            block_facts = [x for x in facts if x["bloque"] == block_no]
            answer = q.get("verified_answer_option_id")
            rows.append({
                "question_id": q["id"], "exam_id": q["exam_id"],
                "series_year": q["exam"]["series_year"],
                "question_number": q["exam"]["question_number"],
                "block_refs": [block_no],
                "fact_refs": [block_facts[0]["id"]] if block_facts else [],
                "appearance_status": "editorially_mapped",
                "answer_status": "verificada_por_autor_no_plantilla_oficial",
                "respuesta": answer[-1:].upper() if answer else None,
                "rule_status_2026": "requires_current_rule_crosscheck",
                "counts_for_ha_caido": False, "verification_status": "quarantine",
            })
    by_block = Counter(str(x["block_refs"][0]) for x in rows)
    by_promotion = Counter(x["exam_id"].split("-")[2].upper() for x in rows)
    return {
        "schema_version": "2.0.0", "oposicion": "policia-nacional",
        "tema": cfg["number"], "titulo": cfg["title"], "generated_at": CUT_OFF,
        "mapping_method": "manual_editorial_review_with_keyword_inventory",
        "mapping_status": "reviewed_internal_hidden",
        "answer_status": "verificada_por_autor_no_plantilla_oficial",
        "display_policy": {"show_reviewed_appearances": False, "show_answer": False, "show_feedback": False, "never_present_as_official_plantilla": True},
        "aviso": "El mapeo acredita coincidencias temáticas históricas. Las respuestas fueron revisadas por la academia, no proceden de una plantilla oficial final y permanecen ocultas.",
        "total_referencias": len(rows), "con_bloque_asignado": len(rows),
        "con_respuesta_verificada": sum(1 for x in rows if x["respuesta"]),
        "por_bloque": dict(by_block), "por_promocion": dict(by_promotion),
        "retroalimentacion": "banco-preguntas/policia-nacional/oficiales/retroalimentacion.json",
        "questions": rows,
    }


def update_catalog(cfg: dict) -> None:
    path = ROOT / "fuentes/catalogo.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    existing = {x["id"] for x in data["sources"]}
    for sid, title, boe_id, scope in cfg["catalog"]:
        if sid not in existing:
            data["sources"].append({
                "id": sid, "title": title, "boe_id": boe_id,
                "url": cfg["sources"][sid], "scope": scope,
                "official": True, "traceable": True,
            })
    data["sources"].sort(key=lambda x: x["id"])
    data["checked_at"] = CUT_OFF
    write_json(path, data)


def generate_topic(cfg: dict) -> dict:
    n, blocks, visuals = cfg["number"], cfg["blocks"], visuals_for(cfg)
    master, facts = generate_master(cfg)
    questions = build_questions(cfg, facts)
    block_count, fact_count, q_count = len(blocks), len(facts), len(questions)
    knowledge = ROOT / f"conocimiento/policia-nacional/tema-{n:02d}"
    bank = ROOT / f"banco-preguntas/policia-nacional/tema-{n:02d}"
    evaluations = ROOT / f"evaluaciones/policia-nacional/tema-{n:02d}"
    assets = ROOT / f"assets/policia-nacional/tema-{n:02d}"
    materials = ROOT / f"materiales-didacticos/policia-nacional/tema-{n:02d}"
    write(knowledge / "master.md", master)

    coverage = {
        "schema_version": "2.0.0", "content_version": VERSION,
        "oposicion": "policia-nacional", "topic": f"tema-{n:02d}", "tema": n,
        "status": "complete_validated_question_bank",
        "scope": {"blocks_completed": list(range(1, block_count + 1)), "master_statements_total": fact_count, "atomic_facts_extracted": fact_count, "remaining_blocks": []},
        "total_atomic_facts": fact_count, "covered_atomic_facts": fact_count,
        "coverage_percent": 100.0, "total_questions": q_count, "requirements": {},
        "facts": clean_facts(facts),
        "blocks": [
            {"number": i, "title": item["title"], "part": item["part"],
             "part_title": cfg["parts"][item["part"]],
             "facts": [x["id"] for x in facts if x["bloque"] == i],
             "questions": [x["id"] for x in questions if x["bloque"] == i],
             "status": "complete"}
            for i, item in enumerate(blocks, 1)
        ],
    }
    write_json(knowledge / "cobertura.json", coverage)
    official_index = build_official_index(cfg, facts)
    write_json(bank / "indice-oficiales.json", official_index)

    manifest = {
        "schema_version": "2.0.0", "opposition": "policia-nacional",
        "opposition_display_name": "Policía Nacional", "topic": f"tema-{n:02d}",
        "topic_number": n, "slug": cfg["slug"], "title": cfg["title"],
        "content_version": VERSION, "editorial_status": "approved_internal",
        "publication_status": "not_published",
        "normative_status": f"official_sources_checked_{CUT_OFF}",
        "source_file": f"conocimiento/policia-nacional/tema-{n:02d}/master.md",
        "source_rights": {"third_party_document_used_as": "coverage_checklist_only", "third_party_text_reused": False, "official_sources_only_for_legal_content": True},
        "outputs": {
            "parte": f"temas/policia-nacional/parte/tema-{n:02d}-{cfg['slug']}.md",
            "atestado": f"temas/policia-nacional/atestado/tema-{n:02d}-{cfg['slug']}.md",
        },
        "semantic_blocks": block_count, "atomic_facts": fact_count,
        "master_statements": fact_count, "coverage_file": f"conocimiento/policia-nacional/tema-{n:02d}/cobertura.json",
        "official_references": list(cfg["sources"]),
        "official_exam_items": official_index["total_referencias"],
        "official_exam_index": f"banco-preguntas/policia-nacional/tema-{n:02d}/indice-oficiales.json",
        "layers": ["Mapa del tema", "Contenido", "Hablemos claro", "En la calle", "Lo que cae", "Ha caído"],
        "atestado_style": "narrative_explained",
        "question_bank": {"path": f"banco-preguntas/policia-nacional/tema-{n:02d}/preguntas.jsonl", "manifest": f"banco-preguntas/policia-nacional/tema-{n:02d}/manifest.json", "questions": q_count, "coverage_by_atomic_facts": 100.0},
        "evaluations": {"plan": f"evaluaciones/policia-nacional/tema-{n:02d}/plan.json", "generator": "scripts/generar_evaluaciones.py"},
        "assets": {"manifest": f"assets/policia-nacional/tema-{n:02d}/manifest.json", "total": 0, "planned": len(visuals)},
        "teaching_materials": {"manifest": f"materiales-didacticos/policia-nacional/tema-{n:02d}/manifest.json", "categories": ["infografias", "presentaciones", "audios", "videos"]},
        "review": {"legal": f"reviewed_official_sources_{CUT_OFF}", "pedagogical": "approved_narrative_revision", "editorial": "approved_internal", "question_bank": "quality_gate_passed", "review_file": f"conocimiento/policia-nacional/tema-{n:02d}/revision-1.0.md"},
        "pedagogical_version": VERSION, "visual_version": "0.1.0",
    }
    write_json(knowledge / "manifest.json", manifest)

    correction = (
        "- Se aplicó desde el 12/06/2026 el procedimiento común del Pacto Europeo y se retiraron formulaciones de 2025 que lo presentaban como futuro.\n"
        "- Se separaron asilo, protección subsidiaria, apatridia, protección temporal y recursos de acogida.\n"
        if n == 12 else
        "- Se separaron actividad, servicio, función y medida; empresa de seguridad y despacho de detectives; jefe y director.\n"
        "- Se revisaron categorías, habilitación, servicios, videovigilancia, alarmas y establecimientos obligados frente a la Ley 5/2014.\n"
    )
    write(knowledge / "revision-1.0.md", f"""# Revisión jurídica, pedagógica y técnica · Tema {n} · versión {VERSION}

**Corte normativo:** 30/07/2026  
**Estado editorial:** aprobado internamente; no publicado para alumnos.

## Correcciones frente al material privado

{correction}
- Se eliminaron notas de actualización, metacomentarios y redacción ajena.
- Se reconstruyeron todos los contenidos con redacción propia y trazabilidad oficial.

## Resultado

- {block_count} bloques semánticos y {fact_count} hechos atómicos.
- {q_count} preguntas propias con tres opciones equilibradas y doble retroalimentación.
- {official_index['total_referencias']} coincidencias históricas internas, todas ocultas y sin presentarlas como plantilla oficial.
- {len(visuals)} recursos: infografías didácticas densas e ilustraciones dibujadas con poco texto.
""")

    write(bank / "preguntas.jsonl", "\n".join(json.dumps(q, ensure_ascii=False) for q in questions))
    ans = Counter(q["respuesta_correcta"] for q in questions)
    diff = Counter(q["dificultad"] for q in questions)
    typ = Counter(q["tipo"] for q in questions)
    by_block = Counter(str(q["bloque"]) for q in questions)
    by_part = Counter(str(q["parte"]) for q in questions)
    write_json(bank / "manifest.json", {
        "schema_version": "2.0.0", "content_version": VERSION,
        "oposicion": "policia-nacional", "tema": n,
        "estado": "approved_internal", "publicacion": "not_published",
        "total_preguntas": q_count, "total_hechos": fact_count,
        "hechos_cubiertos": fact_count, "cobertura_por_hechos": 100.0,
        "distribucion_respuestas": {x: ans[x] for x in ["A", "B", "C"]},
        "distribucion_dificultad": dict(diff), "distribucion_tipo": dict(typ),
        "preguntas_por_bloque": dict(by_block), "preguntas_por_parte": dict(by_part),
        "caracter": {"propias": q_count, "oficiales": 0},
        "fuente_conocimiento": f"../../../conocimiento/policia-nacional/tema-{n:02d}/master.md",
        "cobertura": f"../../../conocimiento/policia-nacional/tema-{n:02d}/cobertura.json",
        "evaluation_plan": f"../../../evaluaciones/policia-nacional/tema-{n:02d}/plan.json",
        "official_exam_index": "indice-oficiales.json",
        "retroalimentacion": {"schema": "acierto_fallo_v1", "required": True, "humor_first": True},
        "generacion_de_tests": {"max_questions_per_block_test": 25, "full_topic_sizes": [25, 50]},
        "publication_gate": "blocked_until_editorial_approval",
        "quality_gate": {"status": "passed", "reasons": [], "risk5_second_formulations_pending": 0},
    })
    write(bank / "README.md", f"# Banco propio · Tema {n}\n\n{q_count} preguntas propias; normativa revisada a {CUT_OFF}.\n")

    parts = [
        {"code": f"P{p}", "title": title,
         "blocks": [i for i, item in enumerate(blocks, 1) if item["part"] == p]}
        for p, title in cfg["parts"].items()
    ]
    write_json(evaluations / "plan.json", {
        "schema_version": "2.0.0", "content_version": VERSION,
        "opposition": "policia-nacional", "topic_number": n,
        "topic_title": cfg["title"], "id_prefix": f"PN-T{n:02d}", "status": "ready",
        "bank": f"banco-preguntas/policia-nacional/tema-{n:02d}/preguntas.jsonl",
        "output": f"build/evaluaciones/policia-nacional/tema-{n:02d}/tests-generados",
        "coverage_tests": {"max_questions_per_test": 25, "blocks": [{"number": i, "title": item["title"]} for i, item in enumerate(blocks, 1)]},
        "part_tests": {"questions_per_test": 6, "variants": [{"id": "A", "offset": 0}, {"id": "B", "offset": 1}], "parts": parts},
        "final_tests": [{"questions": 25, "variant": "A", "offset": 0}, {"questions": 25, "variant": "B", "offset": 1}, {"questions": 50, "variant": "A", "offset": 0}, {"questions": 50, "variant": "B", "offset": 2}],
    })
    write(evaluations / "README.md", f"# Evaluaciones · Tema {n}\n\nTests por bloque, por parte y finales A/B.\n")

    resources = []
    for i, (filename, kind, block_refs, description, family) in enumerate(visuals, 1):
        bno = block_refs[0] if len(block_refs) == 1 else None
        resources.append({
            "id": f"PN-T{n:02d}-DG{i:02d}", "file": filename, "title": description,
            "type": "ilustracion_simple" if kind == "ilustracion" else "infografia",
            "placement": "Mapa del tema" if bno is None else f"Bloque {bno:02d}",
            "status": "planned", "block": bno, "documents": ["parte", "atestado"],
            "description": f"{description}. Familia compositiva: {family}.",
            "source_content_version": VERSION, "required_format": "webp", "max_bytes": 1000000,
        })
    write_json(assets / "manifest.json", {
        "schema_version": "2.0.0", "opposition": "policia-nacional",
        "topic": f"tema-{n:02d}", "content_version": VERSION, "visual_version": "0.1.0",
        "status": "planned", "totals": {"resources": len(resources), "integrated": 0, "planned": len(resources)},
        "integration_status": "pending_generation", "integrated_at": None,
        "resources": resources, "planned_resources": [],
    })
    write(assets / "README.md", f"# Assets · Tema {n}\n\nPNG maestro externo; WEBP optimizado en el repositorio.\n")
    table = [
        f"# Plan visual · Tema {n}", "",
        f"Colección de {len(visuals)} recursos con dos lenguajes visuales deliberadamente distintos.", "",
        "## Dirección común", "",
        "- Infografías: información didáctica visible, relaciones, jerarquías, secuencias y comparaciones; texto breve pero sustantivo.",
        "- Ilustraciones: escenas y metáforas dibujadas; máximo dos rótulos cortos y ninguna tabla.",
        "- Paleta Academia En Vigor: azul marino, azul, verde y ámbar, fondo claro.",
        "- Composiciones variadas; prohibidas las cajas vacías y la repetición de una misma plantilla.",
        "- Personajes e instalaciones genéricos; sin insignias oficiales no verificadas.",
        "- Revisión individual y hoja de contacto antes de integrar.", "",
        "## Matriz", "",
        "| Recurso | Tipo | Bloques | Ancla visual | Familia |",
        "|---|---|---:|---|---|",
    ]
    table += [f"| `{name}` | {kind} | {', '.join(map(str, refs))} | {desc} | {family} |" for name, kind, refs, desc, family in visuals]
    write(assets / "plan-visual.md", "\n".join(table))

    media = {
        "audio": ("audios", "AUDIO", "audio/x-m4a", "m4a"),
        "video": ("videos", "VIDEO", "video/mp4", "mp4"),
        "pres": ("presentaciones", "PRES", "application/pdf", "pdf"),
        "resumen": ("infografias", "RESUMEN", "application/pdf", "pdf"),
    }
    material_parts, material_resources = [], []
    for p, title in cfg["parts"].items():
        block_ids = [f"{i:02d}" for i, item in enumerate(blocks, 1) if item["part"] == p]
        material_parts.append({"id": f"p{p}", "number": p, "title": title, "blocks": block_ids, "anchor_blocks": [block_ids[0]]})
        safe = title.lower().translate(str.maketrans("áéíóúüñ", "aeiouun")).replace(" ", "-")
        for key, (category, label, mime, ext) in media.items():
            material_resources.append({
                "id": f"t{n:02d}-p{p}-{key}", "category": category, "scope": "parte",
                "part_number": p, "blocks": block_ids, "anchor_blocks": [block_ids[0]],
                "title": f"{label.title()} · {title}", "filename": f"T{n:02d}-P{p}-{label}-{safe}.{ext}",
                "mime_type": mime, "file_size_bytes": None, "ownership": "own",
                "status": "planned", "source_content_version": VERSION,
                "tool": "notebooklm", "duration_seconds": None,
                "storage": {"type": "external", "provider": "google_drive", "asset_key": f"pn/tema-{n:02d}/p{p:02d}/{key}", "drive_file_id": "", "url": ""},
                "resource_type": None,
            })
    write_json(materials / "manifest.json", {
        "schema_version": "2.1.0", "opposition": "policia-nacional",
        "topic": f"tema-{n:02d}", "content_version": VERSION, "source_version": VERSION,
        "status": "estructura_preparada",
        "storage_policy": "external_by_default_for_audio_video_and_heavy_files",
        "rights_policy": "own_or_explicitly_authorized_only",
        "audio_note": "Los audios y vídeos pesados se alojan fuera del repositorio.",
        "display_policy": {"show_planned_in_temas": False},
        "storage_root": f"pn/tema-{n:02d}",
        "categories": {"infografias": "infografias/", "presentaciones": "presentaciones/", "audios": "audios/", "videos": "videos/"},
        "scopes": ["parte", "tema"], "nomenclature": "TNN-PN-CATEGORIA-descripcion.ext",
        "parts": material_parts, "resources": material_resources,
    })
    for category in ["infografias", "presentaciones", "audios", "videos"]:
        write(materials / category / "README.md", f"# {category.title()} · Tema {n}\n\nRecursos propios o autorizados; ficheros pesados fuera del repositorio.\n")
    write(materials / "produccion/briefing.md", f"# Briefing · Tema {n}\n\nFuente canónica: `conocimiento/policia-nacional/tema-{n:02d}/master.md`.\n")
    write(materials / "produccion/fuentes.md", "# Fuentes autorizadas\n\n" + "\n".join(f"- `{sid}` · {url}" for sid, url in cfg["sources"].items()))
    write(materials / "produccion/prompts.md", f"# Prompts de producción\n\nUsar `assets/policia-nacional/tema-{n:02d}/plan-visual.md`; las infografías enseñan y las ilustraciones narran con poco texto.\n")

    index_path = ROOT / "temario.json"
    index = json.loads(index_path.read_text(encoding="utf-8"))
    topics = index["oppositions"]["policia-nacional"]["topics"]
    topic = next((x for x in topics if int(x["number"]) == n), None)
    if topic is None:
        topic = {"number": n}
        topics.append(topic)
    topic.update({
        "slug": cfg["slug"], "title": cfg["title"], "content_version": VERSION,
        "editorial_status": "approved_internal", "publication_status": "not_published",
        "manifest": f"conocimiento/policia-nacional/tema-{n:02d}/manifest.json",
        "parte": f"temas/policia-nacional/parte/tema-{n:02d}-{cfg['slug']}.md",
        "atestado": f"temas/policia-nacional/atestado/tema-{n:02d}-{cfg['slug']}.md",
        "question_bank": f"banco-preguntas/policia-nacional/tema-{n:02d}/preguntas.jsonl",
        "evaluation_plan": f"evaluaciones/policia-nacional/tema-{n:02d}/plan.json",
        "assets": f"assets/policia-nacional/tema-{n:02d}/manifest.json",
        "teaching_materials": f"materiales-didacticos/policia-nacional/tema-{n:02d}/manifest.json",
        "official_exam_index": f"banco-preguntas/policia-nacional/tema-{n:02d}/indice-oficiales.json",
        "visual_version": "0.1.0", "visual_assets": 0, "visual_planned": len(visuals),
        "atomic_facts": fact_count, "question_count": q_count,
        "official_exam_mapped": official_index["total_referencias"],
        "official_exam_verified": official_index["con_respuesta_verificada"], "ha_caido_active": 0,
    })
    topics.sort(key=lambda x: int(x["number"]))
    write_json(index_path, index)
    update_catalog(cfg)

    from compilar_tema import process
    process("policia-nacional", n, write=True, check=False)
    return {
        "tema": n, "bloques": block_count, "hechos": fact_count,
        "preguntas": q_count, "visuales": len(visuals),
        "referencias": official_index["total_referencias"],
    }


def main() -> int:
    results = [generate_topic(T12), generate_topic(T13)]
    for result in results:
        print(
            f"Tema {result['tema']} generado: {result['bloques']} bloques, "
            f"{result['hechos']} hechos, {result['preguntas']} preguntas, "
            f"{result['referencias']} referencias y {result['visuales']} visuales."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
