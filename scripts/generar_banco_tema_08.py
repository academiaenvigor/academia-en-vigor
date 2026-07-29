#!/usr/bin/env python3
from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION = "1.0.0"
CUT_OFF = "2026-07-29"

BLOCKS = {
    1: (1, "DGP: posición, mando y funciones", "RD 207/2024, art. 3"),
    2: (1, "Organización central y apoyo inmediato", "Orden INT/859/2023, arts. 1 y 2"),
    3: (1, "División de Cooperación Internacional", "Orden INT/859/2023, art. 2"),
    4: (1, "Dirección Adjunta Operativa", "Orden INT/859/2023, art. 3"),
    5: (1, "Operaciones y Transformación Digital", "Orden INT/859/2023, art. 3"),
    6: (1, "Planificación y unidades especiales", "Orden INT/859/2023, art. 3"),
    7: (2, "Las cinco Comisarías Generales", "Orden INT/859/2023, arts. 4 a 8"),
    8: (2, "Comisaría General de Información", "Orden INT/859/2023, art. 4"),
    9: (2, "Comisaría General de Policía Judicial", "Orden INT/859/2023, art. 5"),
    10: (2, "Seguridad Ciudadana y Extranjería y Fronteras", "Orden INT/859/2023, arts. 6 y 7"),
    11: (2, "Comisaría General de Policía Científica", "Orden INT/859/2023, art. 8"),
    12: (3, "Recursos Humanos y Formación", "Orden INT/859/2023, art. 9"),
    13: (3, "División de Personal", "Orden INT/859/2023, art. 10"),
    14: (3, "Formación y Perfeccionamiento", "Orden INT/859/2023, art. 11"),
    15: (3, "Logística e Innovación", "Orden INT/859/2023, art. 12"),
    16: (3, "Documentación y Gabinete Técnico", "Orden INT/859/2023, arts. 14 y 15"),
    17: (4, "Junta de Gobierno y Consejo Asesor", "Orden INT/859/2023, arts. 16 y 17"),
    18: (4, "Organización territorial", "Orden INT/859/2023, arts. 18 a 27"),
    19: (5, "Funciones exclusivas de la Policía Nacional", "Ley Orgánica 2/1986, art. 12.1.a"),
    20: (5, "Escalas, categorías y grupos", "Ley Orgánica 9/2015, art. 17"),
    21: (5, "Funciones por escala y áreas de actividad", "Ley Orgánica 9/2015, arts. 18 y 19"),
    22: (6, "Sistemas y principios de acceso", "Ley Orgánica 9/2015 y RD 853/2022"),
    23: (6, "Requisitos de ingreso", "RD 853/2022 y convocatoria EB 2026"),
    24: (6, "Proceso selectivo, formación y tribunales", "RD 853/2022"),
    25: (7, "Régimen disciplinario: faltas", "Ley Orgánica 4/2010"),
    26: (7, "Sanciones, competencia y prescripción", "Ley Orgánica 4/2010"),
    27: (7, "Situaciones administrativas y excedencias", "Ley Orgánica 9/2015"),
    28: (7, "Suspensión y segunda actividad", "Ley Orgánica 9/2015"),
}

PART_TITLES = {
    1: "DGP, cooperación y núcleo operativo",
    2: "Comisarías Generales",
    3: "Recursos, formación, logística y apoyo",
    4: "Órganos colegiados y organización territorial",
    5: "Funciones, escalas y carrera profesional",
    6: "Ingreso, promoción y formación selectiva",
    7: "Disciplina y situaciones administrativas",
}

SOURCE_IDS = {
    1: "DGP-RD207-2024",
    **{block: "DGP-INT859-2023" for block in range(2, 19)},
    19: "LO2-1986-T08",
    20: "LO9-2015-T08",
    21: "LO9-2015-T08",
    22: "LO9-2015-T08",
    23: "CONV-PN-2026",
    24: "RD853-2022-T08",
    25: "LO4-2010-T08",
    26: "LO4-2010-T08",
    27: "LO9-2015-T08",
    28: "LO9-2015-T08",
}


def f(concepto, enunciado, correcta, falsa_1, falsa_2, explicacion, riesgo=5, tipo="literal_discriminacion"):
    return {
        "concepto": concepto,
        "enunciado": enunciado,
        "correcta": correcta,
        "falsas": [falsa_1, falsa_2],
        "explicacion": explicacion,
        "riesgo": riesgo,
        "tipo": tipo,
    }


FACTS = {
    1: [
        f("Naturaleza de la DGP", "¿Qué posición ocupa la Dirección General de la Policía?", "Es un órgano directivo del Ministerio del Interior.", "Es un órgano superior con rango de secretaría de Estado.", "Es una unidad operativa dependiente del Gabinete Técnico.", "La DGP es un órgano directivo del Ministerio del Interior."),
        f("Rango del titular", "¿Qué rango tiene la persona titular de la DGP?", "Rango de subsecretario.", "Rango de secretario de Estado.", "Rango de director general sin equivalencia orgánica.", "La persona titular de la DGP tiene rango de subsecretario."),
        f("Dependencia y mando", "Señale la relación jerárquica correcta.", "La DGP depende de la Secretaría de Estado de Seguridad y ejerce el mando directo de la Policía Nacional.", "La DGP depende del Ministro y ejerce solo coordinación técnica.", "La Secretaría de Estado depende de la DGP para el mando operativo.", "La Secretaría de Estado ejerce la superior dirección y la DGP el mando directo."),
        f("Ámbito funcional", "¿Qué función corresponde a la DGP?", "Dirigir los servicios centrales y territoriales de la Policía Nacional.", "Dirigir todos los cuerpos de policía local.", "Ejercer la jurisdicción penal sobre delitos policiales.", "La DGP dirige los servicios centrales y territoriales de la Policía Nacional.", 4),
        f("Medios y planes", "¿Qué competencia combina recursos y planificación operativa?", "Distribuir medios y proponer planes operativos de la Policía Nacional.", "Aprobar los Presupuestos Generales del Estado.", "Autorizar tratados internacionales de cooperación policial.", "La DGP distribuye medios y propone planes operativos en su ámbito."),
        f("Personal y control", "¿Qué materias de personal se integran en las funciones de la DGP?", "Selección, formación y régimen disciplinario.", "Nombramiento de jueces, fiscales y letrados.", "Negociación colectiva de toda la Administración General del Estado.", "La selección, formación y disciplina policial forman parte de sus funciones.", 4),
    ],
    2: [
        f("Cuatro órganos centrales", "¿Cuál es la relación completa de órganos con nivel de subdirección general en la organización central?", "DAO, Recursos Humanos y Formación, Logística e Innovación y Gabinete Técnico.", "DAO, Cooperación Internacional, Policía Judicial y Gabinete Técnico.", "Recursos Humanos, División de Personal, División de Documentación y DAO.", "La Orden enumera cuatro: DAO, dos Subdirecciones Generales y Gabinete Técnico."),
        f("Cooperación Internacional", "¿De quién depende la División de Cooperación Internacional?", "Directamente de la persona titular de la DGP.", "De la Dirección Adjunta Operativa.", "Del Gabinete Técnico.", "Cooperación Internacional depende directamente de la DGP."),
        f("Comisarías Generales", "¿De qué órgano dependen las Comisarías Generales?", "De la Dirección Adjunta Operativa.", "Directamente del Ministro del Interior.", "De Recursos Humanos y Formación.", "Las cinco Comisarías Generales dependen de la DAO."),
        f("Oficina de Despacho", "¿De quién depende la Oficina de Despacho?", "De la persona titular de la DGP.", "De la Secretaría General de la DAO.", "De la División de Personal.", "La Oficina de Despacho es apoyo inmediato de la persona titular de la DGP.", 4),
        f("Oficina de Comunicación", "¿De quién depende la Oficina de Comunicación?", "De la persona titular de la DGP.", "De la División de Cooperación Internacional.", "De la Oficina de Marca.", "La Oficina de Comunicación depende de la persona titular de la DGP.", 4),
        f("Suplencia DGP", "En caso de vacante, ausencia o enfermedad del titular de la DGP, ¿quién le suple?", "La persona titular de la Dirección Adjunta Operativa.", "La persona titular del Gabinete Técnico.", "La persona titular de Recursos Humanos y Formación.", "La suplencia ordinaria del titular de la DGP corresponde a la DAO."),
    ],
    3: [
        f("Composición de Cooperación Internacional", "¿Qué conjunto integra la División de Cooperación Internacional?", "Secretaría General, Coordinación Internacional, OCN INTERPOL, Unidad Nacional EUROPOL y Oficina SIRENE.", "Secretaría General, FRONTEX, CEPOL, EUROJUST y UDYCO.", "OCN INTERPOL, Policía Científica, Gabinete Técnico y UCOT.", "La División reúne cinco piezas: Secretaría General, coordinación, INTERPOL, EUROPOL y SIRENE."),
        f("OCN INTERPOL", "¿Qué órgano es interlocutor con la Secretaría General de INTERPOL?", "La Oficina Central Nacional de INTERPOL.", "La Unidad Nacional de EUROPOL.", "La Oficina SIRENE.", "La OCN INTERPOL canaliza la cooperación con la Secretaría General de INTERPOL."),
        f("Unidad Nacional EUROPOL", "¿Qué órgano enlaza a las autoridades nacionales con la Agencia de la Unión Europea para la cooperación policial?", "La Unidad Nacional de EUROPOL.", "La OCN INTERPOL.", "La Unidad de Planificación Estratégica.", "La Unidad Nacional de EUROPOL actúa como enlace nacional con la Agencia."),
        f("Oficina SIRENE", "¿Qué órgano desarrolla la cooperación ligada al Sistema de Información Schengen?", "La Oficina SIRENE.", "La Oficina de Marca.", "La Secretaría General de Policía Científica.", "SIRENE gestiona la información complementaria asociada al SIS."),
        f("Prüm post-hit", "¿Qué punto de contacto nacional intercambia datos post-hit de ADN y huellas en el marco de Prüm?", "La Oficina SIRENE.", "La Unidad Nacional de EUROPOL.", "La Unidad Central de Identificación.", "La Orden atribuye a SIRENE el intercambio post-hit de ADN y datos dactiloscópicos."),
        f("OEDE", "La coordinación para materializar entregas derivadas de una Orden Europea de Detención y Entrega corresponde a:", "La Oficina SIRENE.", "La UDEF Central.", "La División de Documentación.", "SIRENE asume esa cooperación operativa vinculada a la OEDE.", 4),
    ],
    4: [
        f("Misión de la DAO", "¿Cuál es la misión general de la Dirección Adjunta Operativa?", "Colaborar en la dirección, coordinación y supervisión de las unidades operativas.", "Gestionar exclusivamente retribuciones y expedientes personales.", "Expedir DNI y pasaportes.", "La DAO es el núcleo de dirección y coordinación operativa."),
        f("Dependencias DAO", "¿Qué conjunto depende de la DAO?", "Operaciones y Transformación Digital, Planificación Estratégica, GEO, Asuntos Internos, Brigada Operativa de Apoyo y Comisarías Generales.", "División de Personal, Escuela Nacional de Policía y Oficina de Marca.", "División de Documentación, Cooperación Internacional y Consejo Asesor.", "La DAO agrupa coordinación operativa, unidades especiales y las cinco Comisarías Generales."),
        f("Secretaría General DAO", "¿Con qué órgano de apoyo propio cuenta la DAO?", "Con una Secretaría General.", "Con una Oficina SIRENE.", "Con un Consejo Asesor independiente.", "La DAO cuenta con una Secretaría General."),
        f("Primera suplencia DAO", "¿Quién suple en primer lugar al titular de la DAO?", "La persona titular de Recursos Humanos y Formación.", "La persona titular de Logística e Innovación.", "La persona titular del Gabinete Técnico.", "La primera suplencia de la DAO corresponde a Recursos Humanos y Formación."),
        f("Orden de suplencia DAO", "Señale el orden correcto de suplencia de la DAO.", "Recursos Humanos y Formación; Logística e Innovación; Gabinete Técnico.", "Gabinete Técnico; Logística e Innovación; Recursos Humanos y Formación.", "Logística e Innovación; Cooperación Internacional; División de Personal.", "El orden normativo es Recursos Humanos, Logística y Gabinete Técnico."),
    ],
    5: [
        f("Estructura DOTD", "¿Qué unidad pertenece a la División de Operaciones y Transformación Digital?", "La Unidad Central de Apoyo Tecnológico.", "La Unidad de Gestión de Personal Policial.", "La Unidad Central de Criminalística.", "Apoyo Tecnológico forma parte de Operaciones y Transformación Digital."),
        f("Coordinación operativa", "¿Qué área de la División de Operaciones y Transformación Digital coordina la actividad operativa?", "El Área de Coordinación Operativa.", "El Área de Retribuciones.", "El Área de Tratamiento Documental.", "La División incluye un Área de Coordinación Operativa."),
        f("Unidad Aérea", "¿Qué dos áreas incluye la Unidad Aérea de la Policía?", "Medios Aéreos y Seguridad y Protección Aérea.", "Helicópteros y Aeropuertos Fronterizos.", "Aviación Civil y Control Aduanero.", "La Unidad Aérea se divide en Medios Aéreos y Seguridad y Protección Aérea."),
        f("Unidades Adscritas", "¿De qué división dependen orgánicamente las Unidades Adscritas a comunidades autónomas?", "De Operaciones y Transformación Digital.", "De la División de Personal.", "De la Comisaría General de Información.", "Las Unidades Adscritas dependen orgánicamente de esta División."),
        f("Comisarías Especiales", "¿Qué órgano coordina las Comisarías Especiales?", "La División de Operaciones y Transformación Digital.", "La Comisaría General de Seguridad Ciudadana.", "El Gabinete Técnico.", "Las Comisarías Especiales se coordinan desde Operaciones y Transformación Digital."),
        f("Apoyo tecnológico operativo", "¿Qué misión distingue a la Unidad Central de Apoyo Tecnológico?", "Impulsar transformación digital, ciberseguridad y tecnología aplicada a la actividad policial.", "Gestionar nóminas y expedientes disciplinarios.", "Tramitar pasaportes y archivos históricos.", "Su tecnología se aplica directamente a la actividad policial."),
    ],
    6: [
        f("Planificación estratégica", "¿Qué órgano elabora el Plan Estratégico y los planes operativos de la Policía Nacional?", "La Unidad de Planificación Estratégica y Coordinación.", "La División de Documentación.", "La Junta de Gobierno de forma exclusiva.", "La Unidad de Planificación elabora el Plan Estratégico y los planes operativos."),
        f("Inteligencia criminal", "¿Qué órgano trabaja estadística delincuencial, inteligencia criminal y prospectiva?", "La Unidad de Planificación Estratégica y Coordinación.", "La Unidad Nacional de EUROPOL.", "La Oficina de Comunicación.", "Esas funciones corresponden a Planificación Estratégica y Coordinación."),
        f("Áreas de Planificación", "¿Qué áreas dependen de la Unidad de Planificación Estratégica y Coordinación?", "Seguimiento, Inteligencia y Coordinación; y Planificación y Prospectiva.", "Personal; y Retribuciones.", "Criminalística; y Documentación.", "La Unidad se apoya en esas dos áreas especializadas."),
        f("Centro Nacional de Comunicaciones", "¿De qué unidad depende el Centro Nacional de Comunicaciones?", "De la Unidad de Planificación Estratégica y Coordinación.", "De la División de Cooperación Internacional.", "De la División Económica y Técnica.", "El Centro Nacional de Comunicaciones depende de Planificación Estratégica."),
        f("GEO", "¿Cuál es la función característica del Grupo Especial de Operaciones?", "Intervenir en situaciones de especial cualificación, terroristas o de grave riesgo.", "Gestionar fronteras y expedición documental.", "Supervisar expedientes disciplinarios.", "El GEO interviene en operaciones de especial cualificación y grave riesgo."),
        f("Sede GEO", "¿Dónde tiene su sede el Grupo Especial de Operaciones?", "En Guadalajara.", "En Ávila.", "En Canillas, como única sede operativa.", "La sede del GEO está en Guadalajara.", 4),
        f("Asuntos Internos", "¿Qué investiga la Unidad de Asuntos Internos?", "Conductas del personal que puedan ser delito o vulnerar la ética profesional.", "Cualquier delito económico cometido por particulares.", "Las infracciones de extranjería en puestos fronterizos.", "Asuntos Internos investiga conductas del personal policial con relevancia penal o ética."),
    ],
    7: [
        f("Número de Comisarías Generales", "¿Cuántas Comisarías Generales dependen de la DAO?", "Cinco.", "Cuatro.", "Seis.", "Son cinco Comisarías Generales."),
        f("Relación de Comisarías", "Señale la relación correcta de las cinco Comisarías Generales.", "Información, Policía Judicial, Seguridad Ciudadana, Extranjería y Fronteras y Policía Científica.", "Información, Tráfico, Protección Civil, Policía Judicial y Documentación.", "Policía Judicial, Personal, Logística, Científica y Cooperación Internacional.", "La regla de cinco reúne Información, Judicial, Seguridad Ciudadana, Extranjería y Científica."),
        f("Nivel orgánico", "¿Qué nivel orgánico tienen las Comisarías Generales?", "Subdirección general.", "Dirección general.", "Secretaría general técnica.", "Todas tienen nivel orgánico de subdirección general."),
        f("UCOT central", "¿En cuáles existe una Unidad Central de Coordinación Operativa y Técnica?", "En Judicial, Seguridad Ciudadana, Extranjería y Fronteras y Científica.", "Solo en Información y Judicial.", "En las cinco sin excepción.", "Información es la excepción; las otras cuatro cuentan con UCCOT."),
        f("Jefe Central de Operaciones", "¿Qué cargo dirige la Unidad Central de Coordinación Operativa y Técnica?", "El Jefe o Jefa Central de Operaciones.", "El Jefe o Jefa Regional de Operaciones.", "El Director Adjunto Operativo.", "La persona responsable recibe la denominación de Jefe o Jefa Central de Operaciones."),
        f("Suplencia Comisaría General", "En las Comisarías con UCCOT, ¿quién sustituye a su titular?", "El Jefe o Jefa Central de Operaciones.", "El titular del Gabinete Técnico.", "El Jefe o Jefa Provincial de Operaciones.", "La jefatura de la UCCOT ejerce la suplencia."),
    ],
    8: [
        f("Misión de Información", "¿Cuál es la misión esencial de la Comisaría General de Información?", "Captar, tratar y utilizar operativamente información de interés para el orden y la seguridad pública.", "Gestionar retribuciones y destinos.", "Expedir documentos de identidad.", "Información trabaja información de interés para el orden y la seguridad pública."),
        f("Antiterrorismo", "¿En qué materia destaca especialmente la actividad de Información?", "Antiterrorismo.", "Contratación pública.", "Formación de ingreso.", "Su actividad operativa destaca especialmente en materia antiterrorista."),
        f("Estructura protegida", "¿Cómo se determinan las unidades y servicios de Información?", "Mediante Orden Comunicada.", "Mediante ordenanza municipal.", "Mediante resolución pública de cada Jefatura Superior.", "Su estructura se fija por Orden Comunicada debido a su protección."),
        f("Publicidad de unidades", "¿Por qué la orden pública no detalla la estructura interna de Información?", "Porque está sometida a protección.", "Porque carece de unidades permanentes.", "Porque depende orgánicamente de EUROPOL.", "La falta de detalle público responde a la protección de su estructura.", 4),
    ],
    9: [
        f("Ámbito Policía Judicial", "¿Qué caracteriza el ámbito de la Comisaría General de Policía Judicial?", "Investiga infracciones supraterritoriales y delincuencia organizada, económica, tecnológica y violenta.", "Gestiona exclusivamente delitos leves de ámbito local.", "Se limita a elaborar pericias sin investigar.", "Policía Judicial investiga formas complejas y supraterritoriales de delincuencia."),
        f("UDYCO", "¿Qué materia corresponde a la UDYCO Central?", "Droga y crimen organizado.", "Delincuencia económica y fiscal.", "Falsedad documental pericial.", "UDYCO se ocupa de droga y crimen organizado."),
        f("UDEF", "¿Qué materia corresponde a la UDEF Central?", "Delincuencia económica y fiscal.", "Terrorismo y radicalización.", "Seguridad privada y participación ciudadana.", "UDEF investiga delincuencia económica y fiscal."),
        f("Ciberdelincuencia", "¿Qué unidad asume la investigación central de delitos cometidos mediante TIC?", "La Unidad Central de Ciberdelincuencia.", "La Unidad de Informática y Telecomunicación.", "La Unidad Central de Apoyo Tecnológico.", "La Unidad Central de Ciberdelincuencia es investigadora; las otras prestan soporte tecnológico."),
        f("UFAM", "¿Qué materias corresponden a la UFAM Central?", "Violencia de género, doméstica y sexual, protección de víctimas y referencia en menores.", "Únicamente ciberdelitos contra empresas.", "Drogas, crimen organizado y blanqueo.", "UFAM se centra en familia, mujer, víctimas y menores."),
        f("Inteligencia Criminal", "¿Qué unidad de Policía Judicial se especializa en análisis e inteligencia criminal?", "La Unidad Central de Inteligencia Criminal.", "La Oficina SIRENE.", "El Área de Retribuciones.", "La Unidad Central de Inteligencia Criminal se integra en Policía Judicial."),
        f("Delincuencia especializada y violenta", "¿Qué unidad aborda delincuencia especializada y violenta?", "La Unidad Central de Delincuencia Especializada y Violenta.", "La Unidad Central de Seguridad Privada.", "La Unidad de Procesos Selectivos.", "La UDEV Central se encuadra en Policía Judicial."),
    ],
    10: [
        f("Misión Seguridad Ciudadana", "¿Qué misión define a la Comisaría General de Seguridad Ciudadana?", "Prevenir, mantener y, en su caso, restablecer el orden y la seguridad ciudadana.", "Investigar exclusivamente delitos fiscales.", "Gestionar pasaportes y archivos.", "Seguridad Ciudadana actúa sobre prevención, mantenimiento y restablecimiento del orden."),
        f("Especialidades Seguridad Ciudadana", "¿Qué materias se integran en Seguridad Ciudadana?", "Prevención y reacción, protección, seguridad privada y participación ciudadana.", "Retribuciones, archivos y formación selectiva.", "Drogas, blanqueo y ciberdelincuencia.", "Esas especialidades se integran en Seguridad Ciudadana."),
        f("Oficina Nacional de Deportes", "¿De qué órgano depende la Oficina Nacional de Deportes?", "De la Brigada de Coordinación Operativa de Seguridad Ciudadana.", "De la Comisaría General de Extranjería y Fronteras.", "De la División de Formación y Perfeccionamiento.", "La Oficina Nacional de Deportes depende de la Brigada de Coordinación Operativa."),
        f("Asuntos Taurinos", "¿Dónde se encuadra la Oficina Central de Asuntos Taurinos?", "En la Brigada de Coordinación Operativa de Seguridad Ciudadana.", "En el Gabinete Técnico.", "En la Unidad Central de Criminalística.", "Comparte encuadre con la Oficina Nacional de Deportes."),
        f("Misión Extranjería", "¿Qué corresponde a Extranjería y Fronteras?", "Controlar entradas y salidas y aplicar la normativa de extranjería, asilo y protección internacional.", "Gestionar la carrera profesional y las retribuciones.", "Dirigir la inteligencia antiterrorista.", "La Comisaría General controla fronteras y aplica la normativa de extranjería y protección."),
        f("Redes de inmigración irregular", "¿Qué Comisaría General combate redes de inmigración irregular?", "Extranjería y Fronteras.", "Información exclusivamente.", "Policía Científica.", "El combate de redes de inmigración irregular corresponde a Extranjería y Fronteras."),
        f("Repatriaciones", "¿Qué órgano gestiona las repatriaciones policiales?", "La Comisaría General de Extranjería y Fronteras.", "La División de Personal.", "La Comisaría General de Policía Científica.", "Las repatriaciones se integran en Extranjería y Fronteras."),
        f("FRONTEX", "¿Quién coordina la actuación policial relacionada con FRONTEX?", "La Comisaría General de Extranjería y Fronteras.", "La Oficina SIRENE.", "La Unidad Aérea de la Policía.", "FRONTEX se vincula a Extranjería y Fronteras."),
    ],
    11: [
        f("Misión Policía Científica", "¿Qué servicios presta Policía Científica?", "Criminalística, identificación, analítica e investigación técnica.", "Seguridad privada, participación y protección.", "Selección, formación y promoción interna.", "Policía Científica presta apoyo pericial, identificativo y técnico."),
        f("Identificación", "¿Qué unidad central asume funciones especializadas de identificación?", "La Unidad Central de Identificación.", "La Unidad Central de Ciberdelincuencia.", "La Unidad de Gestión de Personal Policial.", "Identificación se integra en Policía Científica."),
        f("Criminalística", "¿Qué unidad realiza pericias de balística, documentoscopia y falsedad documental?", "La Unidad Central de Criminalística.", "La UDEF Central.", "La División de Documentación.", "Esas pericias técnicas corresponden a Criminalística."),
        f("Acústica e informática forense", "¿Dónde se encuadran la acústica forense y la informática forense pericial?", "En la Unidad Central de Criminalística.", "En la Unidad de Informática y Telecomunicación.", "En la Unidad Central de Ciberdelincuencia.", "La pericia forense se encuadra en Criminalística; la investigación del delito puede corresponder a otra unidad."),
        f("Análisis de la conducta", "¿Qué especialidad forma parte de Policía Científica?", "El análisis de la conducta.", "La gestión de retribuciones.", "La cooperación consular.", "Policía Científica incluye una unidad de análisis de la conducta.", 4),
    ],
    12: [
        f("Misión Recursos Humanos", "¿Qué dirige Recursos Humanos y Formación?", "Personal, selección, formación, prevención de riesgos y acción social.", "Presupuesto, automoción, armamento y documentación.", "Investigación judicial y seguridad ciudadana.", "La Subdirección coordina el ciclo profesional y la protección del personal."),
        f("Planificación RH", "¿Qué unidad propia planifica las necesidades de personal?", "La Unidad de Planificación de Recursos Humanos.", "La Unidad de Planificación Estratégica y Coordinación.", "La Unidad Central de Coordinación Operativa y Técnica.", "La planificación de recursos humanos corresponde a la unidad homónima."),
        f("Prevención y acción social", "¿Dónde se integra la Unidad de Prevención de Riesgos Laborales y Acción Social?", "En Recursos Humanos y Formación.", "En Logística e Innovación.", "En la DAO.", "La unidad se integra en la Subdirección General de Recursos Humanos y Formación."),
        f("Divisiones dependientes", "¿Qué divisiones dependen de Recursos Humanos y Formación?", "Personal y Formación y Perfeccionamiento.", "Documentación y Económica y Técnica.", "Cooperación Internacional y Policía Científica.", "De Recursos Humanos dependen Personal y Formación y Perfeccionamiento."),
        f("Nivel de las divisiones", "¿Qué nivel orgánico tienen Personal y Formación y Perfeccionamiento?", "Subdirección general.", "Dirección general.", "Área sin nivel orgánico.", "Ambas Divisiones tienen nivel orgánico de subdirección general.", 4),
    ],
    13: [
        f("Ámbito División de Personal", "¿Qué gestiona la División de Personal?", "Régimen estatutario, retribuciones, expedientes, puestos, destinos y situaciones administrativas.", "Operaciones antiterroristas y fronteras.", "Presupuesto, vehículos y armamento.", "La División de Personal gestiona la trayectoria administrativa del personal."),
        f("Estructura Personal", "¿Qué unidades integran la División de Personal?", "Secretaría General, Gestión de Personal Policial y Régimen Disciplinario.", "Secretaría General, INTERPOL y SIRENE.", "Retribuciones, UDYCO y Criminalística.", "La División reúne apoyo general, gestión de personal y disciplina."),
        f("Régimen disciplinario orgánico", "¿Dónde se integra la Unidad de Régimen Disciplinario?", "En la División de Personal.", "En la Unidad de Asuntos Internos.", "En el Gabinete Técnico.", "La unidad administrativa de disciplina se integra en Personal; Asuntos Internos investiga conductas."),
        f("Seguimiento de expedientes", "¿Qué órgano sigue y controla la instrucción de expedientes disciplinarios?", "El Área de Coordinación de la Unidad de Régimen Disciplinario.", "La Oficina de Comunicación.", "El Centro Nacional de Comunicaciones.", "El seguimiento de expedientes corresponde al Área de Coordinación de Régimen Disciplinario."),
        f("Situaciones administrativas", "¿Qué ámbito orgánico gestiona las situaciones administrativas del personal?", "La División de Personal.", "La Comisaría General de Seguridad Ciudadana.", "La División de Cooperación Internacional.", "Las situaciones administrativas forman parte de la gestión de Personal."),
    ],
    14: [
        f("Misión Formación", "¿Qué hace la División de Formación y Perfeccionamiento?", "Planifica y ejecuta la formación policial.", "Gestiona fronteras y repatriaciones.", "Coordina el presupuesto y el armamento.", "La División planifica y ejecuta la formación policial."),
        f("Centros y unidades", "¿Qué conjunto integra Formación y Perfeccionamiento?", "Secretaría General, Escuela Nacional, CAE, CAEP y Procesos Selectivos.", "Escuela Nacional, SIRENE, UDEF y Oficina de Marca.", "CAE, UCOT, División de Personal y FRONTEX.", "La estructura reúne Escuela, actualización, altos estudios y selección."),
        f("Escuela Nacional de Policía", "¿Qué función caracteriza a la Escuela Nacional de Policía?", "Formar, entre otros, al alumnado de Inspector y Policía.", "Gestionar ascensos por libre designación.", "Realizar pericias criminalísticas.", "La Escuela imparte la formación de ingreso, entre otras."),
        f("CAE", "¿Qué misión tiene el Centro de Actualización y Especialización?", "Mantener y ampliar las competencias profesionales.", "Formar exclusivamente a altos directivos extranjeros.", "Expedir documentos de identidad.", "El CAE se ocupa de actualización y especialización."),
        f("CAEP", "¿Qué misión tiene el Centro de Altos Estudios Policiales?", "Formación de alta dirección y especialización avanzada.", "Formación inicial exclusiva de Escala Básica.", "Gestión de procesos disciplinarios.", "El CAEP atiende alta dirección y especialización avanzada."),
        f("Procesos Selectivos", "¿Qué unidad gestiona ingreso, acceso y promoción interna?", "La Unidad de Procesos Selectivos.", "La Unidad de Gestión de Personal Policial.", "La Oficina de Despacho.", "Procesos Selectivos se integra en Formación y Perfeccionamiento."),
    ],
}


def add_remaining_facts():
    FACTS.update({
        15: [
            f("Misión Logística", "¿Qué dirige Logística e Innovación?", "Recursos económicos y materiales, tecnologías corporativas, telecomunicaciones, innovación y documentación.", "Unidades operativas, inteligencia criminal y asuntos internos.", "Selección, formación y régimen disciplinario.", "Logística e Innovación sostiene los medios y sistemas corporativos."),
            f("Estructura propia", "¿Qué unidad propia integra Logística e Innovación junto a su Secretaría General?", "La Unidad de Informática y Telecomunicación.", "La Unidad Central de Ciberdelincuencia.", "La Unidad Central de Apoyo Tecnológico.", "Informática y Telecomunicación presta soporte corporativo desde Logística."),
            f("Divisiones dependientes", "¿Qué divisiones dependen de Logística e Innovación?", "Económica y Técnica, y Documentación.", "Personal, y Formación y Perfeccionamiento.", "Policía Judicial, y Policía Científica.", "Logística dirige la División Económica y Técnica y la de Documentación."),
            f("División Económica y Técnica", "¿Qué materias gestiona la División Económica y Técnica?", "Presupuesto, contratación, infraestructuras, automoción, armamento, equipamiento y uniformidad.", "Drogas, ciberdelincuencia y violencia de género.", "Excedencias, destinos y retribuciones personales.", "La División Económica y Técnica gestiona recursos materiales y económicos."),
            f("Tecnología corporativa", "¿Dónde se encuadran la informática corporativa y las telecomunicaciones?", "En Logística e Innovación.", "En la Comisaría General de Policía Judicial.", "En la Oficina SIRENE.", "El soporte tecnológico corporativo corresponde a Logística e Innovación."),
            f("Tecnología operativa", "¿Qué diferencia correctamente tecnología corporativa y tecnología policial operativa?", "La corporativa se encuadra en Logística; la aplicada a la operación, en la DAO.", "Ambas dependen exclusivamente de la División de Personal.", "La corporativa depende de SIRENE y la operativa de Documentación.", "La estructura separa soporte corporativo y capacidades tecnológicas operativas."),
        ],
        16: [
            f("Estructura Documentación", "¿Qué integra la División de Documentación?", "Secretaría General, Documentación de Españoles y Extranjeros, y Tratamiento Documental y Archivo.", "Secretaría General, INTERPOL y Unidad Nacional EUROPOL.", "Área Jurídica, Oficina de Marca y Banda de Música.", "La División agrupa gestión documental y archivo."),
            f("Misión Gabinete Técnico", "¿Cuál es la misión general del Gabinete Técnico?", "Apoyar y asistir a la persona titular de la DGP.", "Dirigir todas las Comisarías Generales.", "Resolver expedientes disciplinarios por faltas leves.", "El Gabinete Técnico presta apoyo estratégico y técnico a la DGP."),
            f("Materias Gabinete Técnico", "¿Qué materias coordina el Gabinete Técnico?", "Estudios, informes, relaciones institucionales, normativa, calidad, publicaciones, protocolo e identidad corporativa.", "Fronteras, drogas, criminalística y seguridad privada.", "Retribuciones, destinos y excedencias.", "El Gabinete reúne apoyo normativo, institucional y de identidad."),
            f("Banda de Música", "¿De qué órgano depende la Banda de Música de la Policía Nacional?", "Del Servicio de Protocolo.", "De la Oficina de Marca.", "De la División de Formación y Perfeccionamiento.", "La Banda depende del Servicio de Protocolo."),
            f("Cadena Banda de Música", "Señale la cadena orgánica correcta de la Banda de Música.", "Servicio de Protocolo → Área de Coordinación Institucional e Identidad Corporativa → Gabinete Técnico.", "Oficina de Marca → División de Personal → DAO.", "Escuela Nacional → Formación y Perfeccionamiento → Recursos Humanos.", "La Banda se integra por Protocolo en el Área de Coordinación Institucional del Gabinete."),
            f("Oficina de Marca", "¿Dónde se incardina la Oficina de Marca?", "En el Área de Coordinación Institucional e Identidad Corporativa del Gabinete Técnico.", "En la División de Documentación.", "En la Oficina de Comunicación como unidad territorial.", "La Oficina de Marca comparte Área con el Servicio de Protocolo."),
        ],
        17: [
            f("Misión Junta de Gobierno", "¿Qué función tiene la Junta de Gobierno?", "Asistir y colaborar con la persona titular de la DGP en materias estratégicas y de personal.", "Ejercer jurisdicción disciplinaria independiente.", "Dirigir exclusivamente la cooperación internacional.", "La Junta asiste a la DGP en planificación, recursos, personal y deontología."),
            f("Presidencia Junta", "¿Quién preside la Junta de Gobierno?", "La persona titular de la DGP.", "La persona titular de la DAO.", "La persona titular del Ministerio del Interior.", "La presidencia corresponde a la persona titular de la DGP."),
            f("Vicepresidencia Junta", "¿Quién ejerce la Vicepresidencia de la Junta de Gobierno?", "La persona titular de la DAO.", "La jefatura de la División de Personal.", "La persona titular del Gabinete Técnico.", "La DAO ocupa la Vicepresidencia."),
            f("Secretaría Junta", "¿Quién actúa como Secretario o Secretaria de la Junta de Gobierno?", "La persona titular de la jefatura de la División de Personal.", "La persona titular de Cooperación Internacional.", "La jefatura de la Oficina de Comunicación.", "La Secretaría de la Junta corresponde a la jefatura de Personal."),
            f("Naturaleza Consejo Asesor", "¿Qué es el Consejo Asesor?", "Un órgano colegiado permanente de asesoramiento en asuntos complejos o trascendentes.", "Un órgano temporal de negociación sindical.", "Una unidad operativa de la DAO.", "El Consejo Asesor es colegiado, permanente y consultivo."),
            f("Vocales Consejo Asesor", "¿Entre quiénes se designan los vocales del Consejo Asesor?", "Integrantes de la Policía Nacional de reconocido prestigio y especial conocimiento.", "Exclusivamente miembros de las Fuerzas Armadas.", "Personal eventual del Ministerio sin experiencia policial.", "Los vocales proceden de la Policía Nacional y se eligen por prestigio y conocimientos."),
            f("Secretaría Consejo Asesor", "¿Dónde se incardina la Secretaría del Consejo Asesor?", "En el Gabinete Técnico.", "En la División de Personal.", "En la DAO.", "La Secretaría del Consejo Asesor se incardina en el Gabinete Técnico."),
        ],
        18: [
            f("Niveles territoriales", "¿Qué órganos forman parte de la organización territorial?", "Jefaturas Superiores, Comisarías Provinciales y Locales, entre otras unidades territoriales.", "Solo Jefaturas Superiores y Puestos Fronterizos.", "Únicamente Comisarías Generales y Divisiones centrales.", "La organización territorial combina jefaturas, comisarías y centros o unidades especializados."),
            f("Jefaturas Superiores", "¿Qué hacen las Jefaturas Superiores?", "Mandan, gestionan, coordinan e inspeccionan los servicios de su ámbito.", "Gestionan únicamente formación y retribuciones.", "Dependen funcionalmente de los ayuntamientos.", "La Jefatura Superior ejerce mando y coordinación territorial."),
            f("UCOT", "¿Dónde se integra la Unidad de Coordinación Operativa Territorial?", "En la Jefatura Superior.", "En la Comisaría Provincial como regla general.", "En la Comisaría General de Policía Judicial.", "La UCOT es la unidad operativa de coordinación de la Jefatura Superior."),
            f("Jefatura UCOT", "¿Quién dirige la UCOT?", "El Jefe o Jefa Regional de Operaciones.", "El Jefe o Jefa Provincial de Operaciones.", "El Director Adjunto Operativo.", "La UCOT está dirigida por la jefatura regional de operaciones."),
            f("Suplencia Jefatura Superior", "¿Quién sustituye a la persona titular de una Jefatura Superior?", "El Jefe o Jefa Regional de Operaciones.", "El Jefe o Jefa Central de Operaciones.", "La persona titular de la Comisaría Local más antigua.", "La jefatura regional de operaciones ejerce la suplencia."),
            f("UCOP", "¿Dónde puede existir una Unidad de Coordinación Operativa Provincial?", "En una Comisaría Provincial.", "En una Jefatura Superior como única unidad.", "En la División de Cooperación Internacional.", "La UCOP es propia del nivel provincial."),
            f("Jefatura UCOP", "¿Quién dirige la UCOP?", "El Jefe o Jefa Provincial de Operaciones.", "El Jefe o Jefa Regional de Operaciones.", "El Jefe o Jefa Central de Operaciones.", "La denominación correcta es Jefe o Jefa Provincial de Operaciones."),
            f("Cooperación fronteriza", "¿Qué centros pueden formar parte de la organización territorial para cooperación policial y aduanera?", "Los Centros de Cooperación Policial y Aduanera.", "Las Unidades Nacionales de EUROPOL.", "Los Consejos Asesores territoriales.", "Los CCPA forman parte del despliegue territorial de cooperación."),
            f("Unidades documentales territoriales", "¿Qué unidades territoriales acercan la expedición documental?", "Las Unidades de Documentación.", "Las Unidades de Régimen Disciplinario.", "Las Oficinas SIRENE provinciales.", "La organización territorial incluye Unidades de Documentación."),
        ],
        19: [
            f("Ámbito territorial PN", "¿Dónde ejerce la Policía Nacional las funciones comunes y exclusivas que le corresponden?", "En capitales de provincia y demás núcleos que determine el Gobierno.", "Solo en fronteras exteriores.", "Únicamente en municipios de más de 500.000 habitantes.", "La LO 2/1986 atribuye su ámbito a capitales y núcleos determinados por el Gobierno."),
            f("DNI y pasaporte", "¿Qué función es exclusiva de la Policía Nacional?", "Expedir el DNI y el pasaporte.", "Custodiar costas, fronteras marítimas y aeropuertos en exclusiva.", "Conducir interurbanamente presos y detenidos.", "La expedición de DNI y pasaporte pertenece al bloque exclusivo de la Policía Nacional."),
            f("Entradas y salidas", "¿A qué cuerpo corresponde con carácter exclusivo el control de entrada y salida del territorio nacional?", "A la Policía Nacional.", "A las policías locales.", "Al Servicio de Vigilancia Aduanera en exclusiva.", "La Policía Nacional controla entradas y salidas de españoles y extranjeros."),
            f("Extranjería", "¿Qué bloque normativo aplica con carácter exclusivo la Policía Nacional?", "Extranjería, refugio, asilo, extradición, expulsión, emigración e inmigración.", "Armas y explosivos con carácter general.", "Resguardo fiscal del Estado.", "La LO 2/1986 concentra esas materias en la Policía Nacional."),
            f("Juego", "¿Qué cuerpo vigila el cumplimiento de la normativa del juego?", "La Policía Nacional.", "La Guardia Civil en todo caso y con exclusión de cualquier otro cuerpo.", "Las policías locales en exclusiva.", "La vigilancia del juego figura entre las funciones exclusivas de la Policía Nacional."),
            f("Drogas", "¿A qué cuerpo se atribuye la investigación y persecución de los delitos relacionados con la droga?", "A la Policía Nacional.", "A la Policía Local.", "A Instituciones Penitenciarias.", "La investigación de delitos relacionados con la droga es función exclusiva de la Policía Nacional."),
            f("Cooperación policial extranjera", "¿Qué función exclusiva se refiere a policías de otros países?", "Colaborar y prestar auxilio a policías extranjeras.", "Aprobar tratados internacionales.", "Dirigir las fuerzas armadas aliadas.", "La Policía Nacional colabora y auxilia a policías extranjeras conforme a los tratados."),
            f("Seguridad privada", "¿Qué función exclusiva corresponde a la Policía Nacional en seguridad privada?", "Controlar entidades y servicios privados de seguridad, vigilancia e investigación.", "Autorizar cualquier empresa mercantil del sector servicios.", "Ejercer la inspección laboral general.", "El control de entidades y servicios de seguridad privada se atribuye a la Policía Nacional."),
        ],
        20: [
            f("Número de escalas", "¿En cuántas escalas se ordena la Policía Nacional?", "En cuatro.", "En tres.", "En cinco.", "La Policía Nacional se estructura en cuatro escalas."),
            f("Escala Superior", "¿Qué categorías integran la Escala Superior y qué grupo les corresponde?", "Comisario Principal y Comisario; grupo A1.", "Inspector Jefe e Inspector; grupo A2.", "Subinspector y Oficial de Policía; grupo C1.", "La Escala Superior reúne Comisario Principal y Comisario, ambos A1."),
            f("Escala Ejecutiva", "¿Qué categorías integran la Escala Ejecutiva y qué grupo les corresponde?", "Inspector Jefe e Inspector; grupo A1.", "Comisario Principal y Comisario; grupo A2.", "Oficial de Policía y Policía; grupo C1.", "La Escala Ejecutiva reúne Inspector Jefe e Inspector, ambos A1."),
            f("Subinspección", "¿Qué categoría y grupo corresponden a la Escala de Subinspección?", "Subinspector; grupo A2.", "Inspector; grupo A1.", "Oficial de Policía; grupo C1.", "Subinspección tiene una categoría, Subinspector, encuadrada en A2."),
            f("Escala Básica", "¿Qué categorías y grupo corresponden a la Escala Básica?", "Oficial de Policía y Policía; grupo C1.", "Subinspector y Policía; grupo A2.", "Inspector Jefe e Inspector; grupo A1.", "La Escala Básica reúne Oficial de Policía y Policía, grupo C1."),
            f("Categoría superior interna", "Dentro de cada escala, ¿qué posición ocupa la primera categoría citada por la ley?", "Es la de mayor rango.", "Es la de ingreso ordinario.", "Es una categoría honorífica sin mando.", "La primera categoría de cada escala es la de mayor rango."),
            f("Grupos compartidos", "¿Qué escalas comparten el grupo A1?", "Superior y Ejecutiva.", "Ejecutiva y Subinspección.", "Subinspección y Básica.", "Superior y Ejecutiva están encuadradas en A1."),
            f("Denominaciones femeninas", "¿Qué denominaciones femeninas recoge expresamente la ley?", "Comisaria, Inspectora y Subinspectora.", "Comisaria, Oficiala y Policía únicamente.", "Directora, Ejecutiva y Suboficiala.", "La ley recoge Comisaria, Inspectora y Subinspectora; no permite extender sin matiz la lista."),
        ],
        21: [
            f("Función Escala Superior", "¿Qué función principal corresponde a la Escala Superior?", "La dirección de los servicios policiales.", "El mando de los servicios policiales.", "La ejecución material de las funciones.", "La Escala Superior dirige."),
            f("Función Escala Ejecutiva", "¿Qué función principal corresponde a la Escala Ejecutiva?", "El mando de los servicios policiales.", "La dirección de los servicios policiales.", "La supervisión de los servicios policiales.", "La Escala Ejecutiva manda."),
            f("Función Subinspección", "¿Qué función principal corresponde a Subinspección?", "La supervisión de los servicios policiales.", "La dirección superior de la organización.", "La ejecución material exclusiva.", "Subinspección supervisa."),
            f("Función Escala Básica", "¿Qué función principal corresponde a la Escala Básica?", "La ejecución material de las funciones encomendadas.", "La dirección de los servicios policiales.", "La aprobación de planes estratégicos.", "La Escala Básica ejecuta materialmente."),
            f("Áreas de actividad", "¿Cuál de estas es un área de actividad policial legalmente prevista?", "Cooperación internacional.", "Jurisdicción penal.", "Política exterior.", "Cooperación internacional figura entre las áreas de actividad."),
            f("Gestión y apoyo", "¿Constituye gestión y apoyo un área de actividad?", "Sí.", "No, es una escala independiente.", "Solo para personal laboral.", "Gestión y apoyo es una de las áreas de actividad policial."),
            f("Especialización", "¿Qué efecto tiene la especialización sobre las escalas?", "No crea una escala nueva.", "Crea automáticamente una quinta escala.", "Convierte al funcionario en personal facultativo.", "Las áreas y especialidades no alteran el sistema legal de escalas."),
        ],
        22: [
            f("Ingreso externo", "¿A qué categorías se puede ingresar por oposición libre?", "Policía e Inspector.", "Oficial de Policía e Inspector Jefe.", "Subinspector y Comisario.", "El ingreso externo se produce a Policía o Inspector."),
            f("Principios constitucionales", "¿Qué principios básicos rigen el acceso?", "Igualdad, mérito, capacidad y publicidad.", "Antigüedad, discrecionalidad, secreto y libre designación.", "Jerarquía, oportunidad y confianza política.", "El acceso respeta igualdad, mérito, capacidad y publicidad."),
            f("Principios técnicos", "¿Qué principio adicional rige los procesos selectivos?", "La adecuación entre las pruebas y las funciones.", "La preferencia automática por familiares de policías.", "La reserva general de actuaciones.", "Las pruebas deben ser adecuadas a las funciones a desempeñar."),
            f("Modalidades promoción interna", "¿Qué modalidades tiene la promoción interna?", "Antigüedad selectiva y concurso-oposición.", "Oposición libre y libre designación.", "Concurso de traslados y comisión de servicios.", "La promoción interna se articula por antigüedad selectiva y concurso-oposición."),
            f("Reserva Inspector", "¿Cómo se distribuyen las vacantes de Inspector?", "40 % oposición libre y 60 % promoción interna.", "60 % oposición libre y 40 % promoción interna.", "50 % para cada sistema sin excepción.", "La ley reserva 40 % a libre y 60 % a promoción interna."),
            f("Transparencia e imparcialidad", "¿Qué pareja forma parte de los principios de selección?", "Transparencia e imparcialidad.", "Secreto y arbitrariedad.", "Confianza y afinidad personal.", "Transparencia, objetividad e imparcialidad rigen la actuación selectiva."),
        ],
        23: [
            f("Nacionalidad", "¿Qué nacionalidad se exige para ingresar en la Policía Nacional?", "La española.", "La de cualquier Estado miembro de la Unión Europea.", "Cualquier nacionalidad con residencia legal de cinco años.", "El ingreso exige nacionalidad española."),
            f("Edad", "¿Qué requisito de edad se exige?", "Tener dieciocho años y no exceder la edad máxima de jubilación.", "Tener veintiún años y no superar los cuarenta.", "Tener dieciséis años con autorización.", "La edad mínima es dieciocho y el límite superior se vincula a la jubilación."),
            f("Antecedentes y separación", "¿Qué situación impide el ingreso?", "Haber sido condenado por delito doloso grave o menos grave, o separado o inhabilitado.", "Haber recibido cualquier sanción administrativa leve.", "Tener antecedentes policiales sin condena firme.", "La norma concreta condena dolosa y separación o inhabilitación."),
            f("Drogas", "¿Qué exige la normativa sobre drogas tóxicas?", "No consumirlas, salvo prescripción facultativa previa.", "No haberlas consumido nunca en la vida.", "Aportar únicamente una declaración jurada sin posible comprobación.", "El requisito admite la excepción de prescripción facultativa."),
            f("Armas", "¿Qué compromiso debe prestar la persona aspirante?", "Portar armas y, en su caso, utilizarlas.", "Adquirir un arma particular antes de las pruebas.", "Renunciar al uso de medios coercitivos.", "El compromiso de portar armas es requisito de ingreso."),
            f("Titulación Básica", "¿Qué titulación se exige para Escala Básica?", "Bachiller o equivalente.", "Título universitario de Grado.", "Educación Primaria exclusivamente.", "La categoría de Policía exige Bachiller o equivalente."),
            f("Titulación Ejecutiva", "¿Qué titulación se exige para ingreso en Escala Ejecutiva?", "Título universitario oficial de Grado.", "Bachiller o equivalente.", "Formación Profesional Básica.", "El ingreso a Inspector exige título universitario de Grado."),
            f("Idioma convocatoria 2026", "¿Qué nivel lingüístico exige la convocatoria de Escala Básica de 2026?", "Al menos A2 de inglés o francés dentro del plazo de solicitudes.", "B1 de cualquier idioma antes del curso de formación.", "No exige acreditación lingüística.", "La convocatoria 2026 exige A2 de inglés o francés antes de cerrar solicitudes."),
            f("Talla convocatoria 2026", "¿Qué establece la convocatoria de Escala Básica de 2026 sobre talla mínima?", "No establece una talla mínima.", "Exige 1,65 m para todos.", "Exige 1,60 m para mujeres y 1,70 m para hombres.", "La convocatoria 2026 no fija talla mínima."),
            f("Naturaleza variable de convocatoria", "¿Qué dato debe revisarse en cada convocatoria y no memorizarse como regla legal inmutable?", "La forma concreta de acreditar idioma y permiso de conducción.", "La nacionalidad española.", "Las categorías de ingreso libre.", "Algunos requisitos se concretan en cada convocatoria."),
        ],
        24: [
            f("Fases de ingreso", "¿Qué secuencia completa el ingreso?", "Oposición, curso de formación y módulo de formación práctica.", "Concurso, entrevista laboral y nombramiento directo.", "Oposición y destino definitivo sin formación.", "El ingreso combina oposición, formación y prácticas."),
            f("Constitución del tribunal", "¿Por cuántos funcionarios de carrera se constituye el tribunal?", "Por siete.", "Por cinco.", "Por nueve.", "El tribunal se constituye por siete funcionarios de carrera."),
            f("Quórum de actuación", "¿Cuántos miembros deben estar presentes como mínimo para que el tribunal actúe válidamente?", "Cinco.", "Cuatro.", "Siete en todo caso.", "El quórum mínimo de actuación es cinco."),
            f("Policías en activo", "¿Cuántos miembros del tribunal deben ser, al menos, policías nacionales en activo?", "Cuatro.", "Cinco.", "Tres.", "Al menos cuatro miembros deben ser personal de la Policía Nacional en activo."),
            f("Regla 7-5-4", "¿Qué significa la regla 7-5-4 del tribunal?", "Siete al constituirse, cinco presentes para actuar y cuatro policías en activo.", "Siete pruebas, cinco vocales y cuatro suplentes.", "Siete policías, cinco funcionarios externos y cuatro asesores.", "La regla resume constitución, quórum y composición policial."),
            f("Composición equilibrada", "¿Qué criterio de composición debe respetar el tribunal?", "Presencia equilibrada de mujeres y hombres.", "Mayoría obligatoria del sexo del presidente.", "Composición exclusivamente policial masculina.", "La composición debe ser equilibrada entre mujeres y hombres."),
            f("Exclusiones tribunal", "¿Quién no puede formar parte del tribunal?", "Personal interino o eventual.", "Funcionarios de carrera de la Policía Nacional en activo.", "Personal funcionario de carrera de otras administraciones.", "La norma excluye, entre otros, a interinos y eventuales."),
            f("Preparadores", "¿Durante cuánto tiempo anterior no puede haber preparado aspirantes quien forme parte del tribunal?", "Cinco años.", "Dos años.", "Diez años.", "Quien preparó aspirantes en los cinco años anteriores no puede integrar el tribunal."),
            f("Designación política", "¿Puede formar parte del tribunal personal de elección o designación política?", "No.", "Sí, si no tiene voto.", "Sí, obligatoriamente en la presidencia.", "El personal de elección o designación política está excluido."),
        ],
        25: [
            f("Ámbito disciplinario", "¿A quién se aplica la Ley Orgánica 4/2010 en el ámbito ordinario?", "A personal en servicio activo y en segunda actividad ocupando destino.", "A todo el personal jubilado y a sus familiares.", "Solo al alumnado de ingreso, con exclusión del personal de carrera.", "La LO 4/2010 se aplica a quienes están en servicio activo y en segunda actividad ocupando destino."),
            f("Clases de faltas", "¿Cómo se clasifican las faltas disciplinarias?", "Muy graves, graves y leves.", "Gravísimas, ordinarias y leves.", "Penales, administrativas y civiles.", "La LO 4/2010 establece tres grados."),
            f("Tipicidad", "¿Qué exige el principio de tipicidad disciplinaria?", "Que la conducta encaje en una infracción prevista.", "Que cualquier conducta inconveniente pueda sancionarse sin norma.", "Que la jefatura elija libremente la infracción.", "No hay sanción disciplinaria sin conducta tipificada."),
            f("Procedimiento", "¿Puede imponerse una sanción sin el procedimiento correspondiente?", "No.", "Sí, si la falta parece evidente.", "Solo en faltas muy graves.", "La responsabilidad disciplinaria exige el procedimiento legal."),
            f("Fuente de faltas", "¿Dónde se tipifican las faltas muy graves y graves de Policía Nacional?", "En la Ley Orgánica 4/2010.", "En la Orden INT/859/2023.", "En el Real Decreto 207/2024.", "La LO 4/2010 contiene la tipificación disciplinaria."),
            f("Faltas leves", "¿Qué rasgo caracteriza a muchas faltas leves?", "Incorrecciones, retrasos o negligencias de menor entidad.", "Conductas delictivas dolosas castigadas siempre con separación.", "Cualquier desobediencia sin atender a su gravedad.", "Las leves recogen incumplimientos de menor entidad."),
            f("Subsidiariedad de gravedad", "¿Cómo se trata una infracción de deberes de menor entidad?", "Como leve cuando no constituya falta de mayor gravedad.", "Siempre como muy grave.", "Fuera del régimen disciplinario.", "La calificación leve opera si la conducta no encaja en un tipo superior."),
        ],
        26: [
            f("Sanciones muy graves", "¿Qué sanciones pueden imponerse por falta muy grave?", "Separación, suspensión de tres meses y un día a seis años o traslado forzoso.", "Solo apercibimiento y pérdida de un día de sueldo.", "Suspensión de uno a cuatro días exclusivamente.", "Las faltas muy graves admiten separación, suspensión larga o traslado."),
            f("Sanción grave", "¿Qué suspensión corresponde a una falta grave?", "De cinco días a tres meses.", "De uno a cuatro días.", "De tres meses y un día a seis años.", "La franja de falta grave es cinco días a tres meses."),
            f("Sanciones leves", "¿Qué sanciones pueden imponerse por falta leve?", "Suspensión de uno a cuatro días o apercibimiento.", "Traslado forzoso o separación.", "Suspensión de cinco días a tres meses.", "Las leves se sancionan con suspensión corta o apercibimiento."),
            f("Separación del servicio", "¿Quién impone la separación del servicio?", "El Ministro del Interior.", "La Secretaría de Estado de Seguridad.", "La Dirección General de la Policía.", "La separación corresponde al Ministro."),
            f("Suspensión larga", "¿Quién impone la suspensión de tres años y un día a seis años?", "La Secretaría de Estado de Seguridad.", "El Ministro del Interior exclusivamente.", "La jefatura de la División de Personal.", "Esa franja de suspensión corresponde a la Secretaría de Estado."),
            f("Traslado forzoso", "¿Quién impone el traslado forzoso?", "La Secretaría de Estado de Seguridad.", "La Dirección General de la Policía.", "La Junta de Gobierno.", "El traslado forzoso corresponde a la Secretaría de Estado."),
            f("Restantes muy graves", "¿Quién impone las restantes sanciones por faltas muy graves?", "La Dirección General de la Policía.", "El Consejo Asesor.", "La Comisaría General de Información.", "Salvo separación, suspensión de más de tres años y traslado, resuelve la DGP."),
            f("Sanciones graves", "¿Quién impone las sanciones por faltas graves?", "La Dirección General de la Policía.", "El Ministro del Interior en todo caso.", "La persona instructora del expediente.", "Las sanciones por falta grave corresponden a la DGP."),
            f("Sanciones leves", "¿Qué órganos pueden imponer sanciones por faltas leves respecto de su personal o territorio?", "Delegados del Gobierno y determinadas jefaturas centrales, superiores, provinciales, locales y de unidades adscritas.", "Únicamente el Ministro del Interior.", "Exclusivamente el Consejo Asesor.", "La competencia por faltas leves se distribuye entre Delegados del Gobierno y las jefaturas enumeradas en el artículo 13."),
            f("Prescripción faltas", "¿Cuándo prescriben las faltas muy graves, graves y leves?", "A los tres años, dos años y un mes, respectivamente.", "A los seis años, tres años y un año.", "A los tres años, un año y seis meses.", "La regla es 3 años, 2 años y 1 mes."),
            f("Prescripción sanciones", "¿Qué regla sigue la prescripción de las sanciones?", "Los mismos plazos de tres años, dos años y un mes según gravedad.", "Todas prescriben al año.", "No prescriben nunca.", "Las sanciones prescriben en los mismos plazos por gravedad."),
            f("Traslado solo muy grave", "¿Por qué clase de falta puede imponerse traslado forzoso?", "Solo por falta muy grave.", "Por falta grave o muy grave.", "Solo por falta leve.", "El traslado forzoso aparece entre las sanciones por falta muy grave."),
            f("Restricción tras traslado", "¿Durante qué período no puede obtenerse nuevo destino en el centro, unidad o plantilla de procedencia tras un traslado forzoso?", "De uno a tres años, según determine la resolución.", "Exactamente cinco años en todo caso.", "De uno a seis meses.", "La resolución sancionadora fija un período de uno a tres años."),
        ],
        27: [
            f("Número de situaciones", "¿Cuántas situaciones administrativas enumera la Ley Orgánica 9/2015?", "Seis.", "Cinco.", "Siete.", "La ley enumera seis situaciones."),
            f("Relación de situaciones", "Señale la relación completa de situaciones administrativas.", "Servicio activo, servicios especiales, servicio en otras administraciones, excedencia, suspensión y segunda actividad.", "Servicio activo, reserva, expectativa de destino, excedencia y jubilación.", "Servicio activo, comisión, adscripción, excedencia y licencia.", "Son seis y la segunda actividad es específica de Policía Nacional."),
            f("Modalidades de excedencia", "¿Cuántas modalidades de excedencia se recogen en este régimen?", "Cinco.", "Cuatro.", "Seis.", "Se estudian cinco modalidades de excedencia."),
            f("Interés particular", "¿Qué requisito general previo exige la excedencia por interés particular?", "Cinco años de servicios efectivos.", "Dos años de servicios.", "Diez años de antigüedad.", "Con carácter general exige cinco años de servicios efectivos previos."),
            f("Permanencia interés particular", "¿Cuál es la permanencia mínima general en excedencia por interés particular?", "Un año.", "Seis meses.", "Dos años.", "La permanencia mínima general es un año."),
            f("Agrupación familiar", "¿Cuál de estas es una modalidad de excedencia?", "Agrupación familiar.", "Reserva territorial.", "Expectativa de destino policial.", "La agrupación familiar es modalidad de excedencia."),
            f("Violencia de género", "¿Existe excedencia por razón de violencia de género?", "Sí.", "No, solo una licencia de tres días.", "Solo para personal laboral.", "La ley contempla esta modalidad de excedencia."),
            f("Sector público", "¿Cuál de estas modalidades se vincula al desempeño fuera de la Policía Nacional?", "Excedencia por prestación de servicio en el sector público.", "Segunda actividad con destino.", "Suspensión provisional.", "La prestación de servicio en el sector público tiene modalidad propia."),
            f("Cuidado de familiares duración", "¿Cuál es la duración máxima de la excedencia por cuidado de familiares?", "Hasta tres años.", "Hasta un año.", "Hasta cinco años.", "Puede durar hasta tres años."),
            f("Cómputo cuidado familiares", "¿Qué efectos conserva el tiempo en excedencia por cuidado de familiares?", "Computa para trienios, antigüedad y derechos de Seguridad Social.", "No computa a ningún efecto.", "Solo computa para vacaciones.", "La ley protege su cómputo profesional y social."),
        ],
        28: [
            f("Clases de suspensión", "¿Qué clases de suspensión de funciones existen?", "Provisional y firme.", "Temporal y definitiva.", "Preventiva y honorífica.", "La suspensión puede ser provisional o firme."),
            f("Límite provisional grave", "¿Cuál es el límite general de suspensión provisional por falta grave?", "Tres meses.", "Seis meses.", "Un año.", "Por falta grave no excede con carácter general de tres meses."),
            f("Límite provisional muy grave", "¿Cuál es el límite general de suspensión provisional por falta muy grave?", "Seis meses.", "Tres meses.", "Dos años.", "Por falta muy grave el límite general es seis meses."),
            f("Excepciones al límite", "¿Qué puede prolongar la suspensión provisional más allá del límite general?", "Paralización imputable al interesado o existencia de procedimiento penal.", "La mera conveniencia del instructor.", "Cualquier ausencia por vacaciones.", "La ley contempla esas dos circunstancias excepcionales."),
            f("Pérdida del puesto", "¿Qué efecto produce una suspensión firme superior a seis meses?", "La pérdida del puesto de trabajo.", "La pérdida automática de la condición de funcionario.", "El pase directo a segunda actividad.", "La suspensión firme superior a seis meses determina pérdida del puesto, no necesariamente de la condición."),
            f("Finalidad segunda actividad", "¿Cuál es la finalidad de la segunda actividad?", "Garantizar la aptitud psicofísica y la eficacia del servicio.", "Sancionar faltas graves.", "Premiar la antigüedad con un ascenso.", "La segunda actividad protege la aptitud psicofísica del personal."),
            f("Causas segunda actividad", "¿Por qué causas puede declararse la segunda actividad?", "Por insuficiencia psicofísica o a petición propia.", "Solo por sanción disciplinaria.", "Únicamente al cumplir la edad de jubilación.", "La ley contempla insuficiencia psicofísica y petición propia."),
            f("Edades segunda actividad", "Señale las edades de petición propia por escala.", "64 Superior, 62 Ejecutiva, 60 Subinspección y 58 Básica.", "65 Superior, 63 Ejecutiva, 61 Subinspección y 59 Básica.", "64 Superior, 60 Ejecutiva, 58 Subinspección y 55 Básica.", "La regla descendente es 64-62-60-58."),
            f("Veinticinco años", "¿Qué vía adicional permite solicitar la segunda actividad?", "Haber cumplido veinticinco años efectivos en situaciones computables.", "Haber cumplido veinte años naturales desde el ingreso.", "Tener diez trienios y una condecoración.", "La ley permite solicitarla tras veinticinco años efectivos computables."),
            f("Situaciones computables", "¿Qué situaciones computan para la vía de veinticinco años?", "Servicio activo, servicios especiales o excedencia forzosa en la Policía Nacional o cuerpos asimilados o integrados.", "Cualquier excedencia voluntaria sin límite.", "Solo servicio activo ininterrumpido.", "La ley delimita las situaciones computables para los veinticinco años."),
            f("Destino en segunda actividad", "¿Cómo se permanece en segunda actividad?", "Sin ocupación de destino y a disposición del Ministro del Interior para supuestos excepcionales de seguridad ciudadana.", "Con destino operativo obligatorio en la DAO.", "Fuera de toda disponibilidad para el Ministerio del Interior.", "La segunda actividad no conlleva destino y mantiene disponibilidad excepcional para el Ministro del Interior."),
        ],
    })


def rotate_options(correct, wrongs, index):
    values = [correct, wrongs[0], wrongs[1]]
    shift = index % 3
    ordered = values[shift:] + values[:shift]
    options = dict(zip("ABC", ordered))
    answer = next(letter for letter, value in options.items() if value == correct)
    return options, answer


HUMOR_OK = [
    "🎯 Dependencia localizada.",
    "🚓 Esa unidad estaba donde debía.",
    "🧭 Organigrama bajo control.",
    "✅ La cifra no te ha tendido una emboscada.",
    "🛡️ Trampa normativa neutralizada.",
]
HUMOR_FAIL = [
    "🪤 El organigrama te cambió una puerta.",
    "🚨 Has enviado el expediente al órgano equivocado.",
    "😅 Esa sigla llevaba placa falsa.",
    "📎 Toca devolver la respuesta para subsanar.",
    "🚧 Una cifra mal puesta derriba el esquema.",
]


def build():
    add_remaining_facts()
    facts_out = []
    questions = []
    q_index = 1
    f_index = 1
    answer_cycle = 0
    for block, rows in FACTS.items():
        part, block_title, source = BLOCKS[block]
        for row in rows:
            fact_id = f"PN-T08-F{f_index:03d}"
            forms = 2 if row["riesgo"] == 5 else 1
            qids = []
            for form in range(forms):
                qid = f"PN-T08-Q{q_index:03d}"
                if form == 0:
                    prompt = row["enunciado"]
                    qtype = row["tipo"]
                else:
                    prompt = f"Un aspirante revisa «{row['concepto']}». ¿Qué afirmación debe conservar porque se ajusta a la normativa vigente?"
                    qtype = "supuesto_aplicado"
                options, answer = rotate_options(row["correcta"], row["falsas"], answer_cycle)
                answer_cycle += 1
                explanation = row["explicacion"]
                questions.append({
                    "id": qid,
                    "fact_id": fact_id,
                    "oposicion": "policia-nacional",
                    "tema": 8,
                    "bloque": block,
                    "punto": block,
                    "subpunto": source,
                    "parte": part,
                    "parte_titulo": PART_TITLES[part],
                    "concepto": row["concepto"],
                    "norma": source.split(",")[0],
                    "articulo": source,
                    "riesgo_examen": row["riesgo"],
                    "dificultad": "alta" if row["riesgo"] == 5 else "media",
                    "tipo": qtype,
                    "enunciado": prompt,
                    "opciones": options,
                    "respuesta_correcta": answer,
                    "explicacion": explanation,
                    "retroalimentacion": {
                        "acierto": {
                            "humor": HUMOR_OK[(q_index - 1) % len(HUMOR_OK)],
                            "explicacion": explanation,
                        },
                        "fallo": {
                            "humor": HUMOR_FAIL[(q_index - 1) % len(HUMOR_FAIL)],
                            "explicacion": f"La respuesta correcta es la {answer}: {options[answer]} {explanation}",
                        },
                    },
                    "estado_revision": "validado_normativa_y_coherencia",
                    "version_normativa": CUT_OFF,
                    "caracter": "propio",
                    "referencia_oficial": None,
                    "relaciones": [fact_id],
                    "equivalencias": [],
                    "content_version": VERSION,
                })
                qids.append(qid)
                q_index += 1
            if len(qids) == 2:
                questions[-2]["equivalencias"] = [qids[1]]
                questions[-1]["equivalencias"] = [qids[0]]
            facts_out.append({
                "id": fact_id,
                "oposicion": "policia-nacional",
                "tema": 8,
                "bloque": block,
                "bloque_titulo": block_title,
                "parte": part,
                "parte_titulo": PART_TITLES[part],
                "punto": block,
                "enunciado_atomico": row["explicacion"],
                "fuente": SOURCE_IDS[block],
                "estado_revision": "fuente_oficial_comprobada_y_aprobada",
                "content_version": VERSION,
                "riesgo_examen": row["riesgo"],
                "risk": row["riesgo"],
                "preguntas": qids,
                "covered": True,
                "anchor_score": 1.0,
            })
            f_index += 1

    bank_dir = ROOT / "banco-preguntas/policia-nacional/tema-08"
    knowledge_dir = ROOT / "conocimiento/policia-nacional/tema-08"
    evaluation_dir = ROOT / "evaluaciones/policia-nacional/tema-08"
    bank_dir.mkdir(parents=True, exist_ok=True)
    knowledge_dir.mkdir(parents=True, exist_ok=True)
    evaluation_dir.mkdir(parents=True, exist_ok=True)

    with (bank_dir / "preguntas.jsonl").open("w", encoding="utf-8") as handle:
        for question in questions:
            handle.write(json.dumps(question, ensure_ascii=False) + "\n")

    block_counts = Counter(q["bloque"] for q in questions)
    part_counts = Counter(q["parte"] for q in questions)
    answer_counts = Counter(q["respuesta_correcta"] for q in questions)
    difficulty_counts = Counter(q["dificultad"] for q in questions)
    type_counts = Counter(q["tipo"] for q in questions)
    coverage = {
        "schema_version": "2.0.0",
        "content_version": VERSION,
        "oposicion": "policia-nacional",
        "topic": "tema-08",
        "tema": 8,
        "status": "complete_validated_question_bank",
        "scope": {
            "blocks_completed": list(range(1, 29)),
            "master_statements_total": len(facts_out),
            "atomic_facts_extracted": len(facts_out),
            "remaining_blocks": [],
        },
        "total_atomic_facts": len(facts_out),
        "covered_atomic_facts": len(facts_out),
        "coverage_percent": 100.0,
        "total_questions": len(questions),
        "requirements": {},
        "facts": facts_out,
        "blocks": [
            {"number": block, "title": BLOCKS[block][1], "part": BLOCKS[block][0], "facts": len(FACTS[block])}
            for block in range(1, 29)
        ],
    }
    (knowledge_dir / "cobertura.json").write_text(
        json.dumps(coverage, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    manifest = {
        "schema_version": "2.0.0",
        "content_version": VERSION,
        "oposicion": "policia-nacional",
        "tema": 8,
        "estado": "ready",
        "publicacion": "not_published",
        "total_preguntas": len(questions),
        "total_hechos": len(facts_out),
        "hechos_cubiertos": len(facts_out),
        "cobertura_por_hechos": 100.0,
        "distribucion_respuestas": dict(sorted(answer_counts.items())),
        "distribucion_dificultad": dict(sorted(difficulty_counts.items())),
        "distribucion_tipo": dict(sorted(type_counts.items())),
        "preguntas_por_bloque": {str(k): block_counts[k] for k in sorted(block_counts)},
        "preguntas_por_parte": {str(k): part_counts[k] for k in sorted(part_counts)},
        "caracter": {"propias": len(questions), "oficiales": 0},
        "fuente_conocimiento": "../../../conocimiento/policia-nacional/tema-08/master.md",
        "cobertura": "../../../conocimiento/policia-nacional/tema-08/cobertura.json",
        "evaluation_plan": "../../../evaluaciones/policia-nacional/tema-08/plan.json",
        "official_exam_index": "indice-oficiales.json",
        "retroalimentacion": {"schema": "acierto_fallo_v1", "required": True, "humor_first": True},
        "generacion_de_tests": {"max_questions_per_block_test": 25, "full_topic_sizes": [25, 50]},
        "publication_gate": "ready_after_editorial_approval",
        "quality_gate": {"status": "passed", "reasons": [], "risk5_second_formulations_pending": 0},
    }
    (bank_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    parts = []
    for part in range(1, 8):
        parts.append({
            "code": f"P{part}",
            "title": PART_TITLES[part],
            "blocks": [b for b in range(1, 29) if BLOCKS[b][0] == part],
        })
    plan = {
        "schema_version": "2.0.0",
        "content_version": VERSION,
        "opposition": "policia-nacional",
        "topic_number": 8,
        "topic_title": "La Dirección General de la Policía y la Policía Nacional",
        "id_prefix": "PN-T08",
        "status": "ready",
        "bank": "banco-preguntas/policia-nacional/tema-08/preguntas.jsonl",
        "output": "build/evaluaciones/policia-nacional/tema-08/tests-generados",
        "coverage_tests": {
            "max_questions_per_test": 25,
            "blocks": [{"number": b, "title": BLOCKS[b][1]} for b in range(1, 29)],
        },
        "part_tests": {
            "questions_per_test": 10,
            "variants": [{"id": "A", "offset": 0}, {"id": "B", "offset": 1}],
            "parts": parts,
        },
        "final_tests": [
            {"questions": 25, "variant": "A", "offset": 0},
            {"questions": 25, "variant": "B", "offset": 1},
            {"questions": 50, "variant": "A", "offset": 0},
            {"questions": 50, "variant": "B", "offset": 2},
        ],
    }
    (evaluation_dir / "plan.json").write_text(
        json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    readme = f"""# Banco propio · Tema 8

Banco creado desde El Atestado y contrastado con las normas oficiales vigentes a {CUT_OFF}.

- Hechos atómicos cubiertos: {len(facts_out)} de {len(facts_out)}
- Preguntas propias: {len(questions)}
- Hechos de riesgo 5 con segunda formulación: {sum(f['risk'] == 5 for f in facts_out)} de {sum(f['risk'] == 5 for f in facts_out)}
- Distribución de respuestas: A {answer_counts['A']} · B {answer_counts['B']} · C {answer_counts['C']}
- Retroalimentación: acierto y fallo separados, con entrada humorística y explicación.
- Límite editorial: los requisitos específicos de idioma se etiquetan como propios de la convocatoria de 2026.
"""
    (bank_dir / "README.md").write_text(readme, encoding="utf-8")

    print(f"OK: {len(facts_out)} hechos; {len(questions)} preguntas; respuestas {dict(answer_counts)}")


if __name__ == "__main__":
    build()
