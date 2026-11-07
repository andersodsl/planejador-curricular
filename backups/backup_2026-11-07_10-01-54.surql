-- ------------------------------
-- OPTION
-- ------------------------------

OPTION IMPORT;

-- ------------------------------
-- TABLE: disciplina
-- ------------------------------

DEFINE TABLE disciplina TYPE ANY SCHEMALESS PERMISSIONS NONE;




-- ------------------------------
-- TABLE DATA: disciplina
-- ------------------------------

INSERT [ { carga_horaria: 80, codigo: 'ADS001', descricao: 'Introdução à lógica de programação e algoritmos.', id: disciplina:zp2q2mw92p4kngw0aswp, nome: 'Lógica de Programação', periodo: 1 } ];

-- ------------------------------
-- TABLE: prerequisito
-- ------------------------------

DEFINE TABLE prerequisito TYPE RELATION SCHEMALESS PERMISSIONS NONE;

DEFINE FIELD OVERWRITE in ON prerequisito TYPE record PERMISSIONS FULL;
DEFINE FIELD OVERWRITE out ON prerequisito TYPE record PERMISSIONS FULL;



-- ------------------------------
-- TABLE DATA: prerequisito
-- ------------------------------


