/* Formatted on 2/6/2025 12:30:14 PM (QP5 v5.227.12220.39724) */
SELECT *
  FROM (SELECT rut,
               clave,
               (SELECT COUNT (*)
                  FROM CREDITO.CREDITO
                 WHERE ESTADO = 2 AND cedula = cli.rut)
                  credito,
               (SELECT COUNT (*)
                  FROM AHORRO.CUENTAAHORRO
                 WHERE ESTADOCUENTA = 2 AND ruttitular1 = cli.rut)
                  AS ahorro,
               (SELECT COUNT (*)
                  FROM DEPOSITO.OPERACION
                 WHERE ESTADO = 2 AND RUTCLIENTE = cli.rut)
                  AS desposto,
               (SELECT COUNT (*)
                  FROM LINEACC.LINEADECREDITO
                 WHERE ESTADO = 1 AND RUTCLIENTE = cli.rut)
                  AS LCC,
               (SELECT COUNT (*)
                  FROM LINEACRD.LINEACREDITO
                 WHERE ESTADO = 2 and CLIENTE = cli.rut)
                  AS LCR,
               (SELECT CSOCIAL.CUENTA.SALDODISPONIBLE
                  FROM CSOCIAL.CUENTA
                 WHERE ESTADO = 2 and  RUTTITULAR = cli.rut)
                  AS CSOCIAL
          FROM (SELECT a.rut, b.clave
                  FROM (SELECT 6, 'CREDITO' AS PRODUCTO, CEDULA AS RUT
                          FROM CREDITO.CREDITO
                         WHERE ESTADO = 2
                        UNION
                        SELECT 3, 'AHORRO', RUTTITULAR1
                          FROM AHORRO.CUENTAAHORRO
                         WHERE ESTADOCUENTA = 2
                        UNION
                        SELECT 2, 'DEPOSTO', RUTCLIENTE
                          FROM DEPOSITO.OPERACION
                         WHERE ESTADO = 20
                        UNION
                        SELECT 12, 'LCC', RUTCLIENTE
                          FROM LINEACC.LINEADECREDITO
                         WHERE ESTADO = 1
                        UNION
                        SELECT 10, 'LCR', CLIENTE
                          FROM LINEACRD.LINEACREDITO
                         WHERE ESTADO = 2
                        UNION
                        SELECT 8, 'CSOCIAL', RUTTITULAR
                          FROM CSOCIAL.CUENTA
                         WHERE ESTADO = 2) A,
                       CLIENTE.CLAVEINTERNET B
                 WHERE A.RUT = B.RUTCLIENTE) cli) dat




 
SELECT 6,'CREDITO' AS PRODUCTO FROM CREDITO.CREDITO WHERE CEDULA = :RUT AND ESTADO = 2
            UNION
            SELECT 3,'AHORRO' FROM AHORRO.CUENTAAHORRO WHERE RUTTITULAR1 = :RUT AND ESTADOCUENTA = 2
            UNION
            SELECT 2,'DEPOSTO' FROM DEPOSITO.OPERACION WHERE RUTCLIENTE = :RUT AND ESTADO = 20
            UNION
            SELECT 12,'LCC' FROM LINEACC.LINEADECREDITO WHERE RUTCLIENTE = :RUT AND ESTADO = 1 
            UNION
            SELECT 10,'LCR' FROM LINEACRD.LINEACREDITO WHERE CLIENTE = :RUT AND ESTADO = 2
            UNION
            SELECT 8,'CSOCIAL' FROM CSOCIAL.CUENTA WHERE RUTTITULAR = :RUT AND ESTADO = 2

 
SELECT a.rut,b.clave FROM (SELECT 6,'CREDITO' AS PRODUCTO, CEDULA AS RUT
FROM CREDITO.CREDITO
WHERE ESTADO = 2
UNION
SELECT 3,'AHORRO', RUTTITULAR1
FROM AHORRO.CUENTAAHORRO
WHERE ESTADOCUENTA = 2
UNION
SELECT 2,'DEPOSTO', RUTCLIENTE
FROM DEPOSITO.OPERACION
WHERE ESTADO = 20
UNION
SELECT 12,'LCC', RUTCLIENTE
FROM LINEACC.LINEADECREDITO
WHERE ESTADO = 1
UNION
SELECT 10,'LCR', CLIENTE
FROM LINEACRD.LINEACREDITO
WHERE ESTADO = 2
UNION
SELECT 8,'CSOCIAL', RUTTITULAR
FROM CSOCIAL.CUENTA
WHERE ESTADO = 2 ) A, CLIENTE.CLAVEINTERNET B
WHERE A.RUT = B.RUTCLIENTE AND A.RUT = :RUT