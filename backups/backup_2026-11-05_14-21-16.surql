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

INSERT [ { carga_horaria: 60, codigo: 'GRA001', descricao: 'Teste de grafo', id: disciplina:fr7hatfm0i2qgr3bmpy9, nome: 'Disciplina Origem Teste', periodo: 1 }, { carga_horaria: 60, codigo: 'GRA002', descricao: 'Teste de grafo', id: disciplina:xzyrr9punqvf110b7u79, nome: 'Disciplina Destino Teste', periodo: 2 }, { carga_horaria: 80, codigo: 'ADS001', descricao: 'Introdução à lógica de programação e algoritmos.', id: disciplina:zp2q2mw92p4kngw0aswp, nome: 'Lógica de Programação', periodo: 1 } ];

-- ------------------------------
-- TABLE: prerequisito
-- ------------------------------

DEFINE TABLE prerequisito TYPE RELATION SCHEMALESS PERMISSIONS NONE;

DEFINE FIELD OVERWRITE in ON prerequisito TYPE record PERMISSIONS FULL;
DEFINE FIELD OVERWRITE out ON prerequisito TYPE record PERMISSIONS FULL;



-- ------------------------------
-- TABLE DATA: prerequisito
-- ------------------------------

INSERT RELATION [ { id: prerequisito:1nb7e0ldv5hgw7ra7lid, in: disciplina:xzyrr9punqvf110b7u79, out: disciplina:zp2q2mw92p4kngw0aswp } ];

