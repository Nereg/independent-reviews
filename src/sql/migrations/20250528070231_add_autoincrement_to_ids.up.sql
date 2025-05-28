BEGIN;

-- fix the id not being a serial
CREATE SEQUENCE practitioners_id_seq AS integer START 1 OWNED BY practitioners.id;

ALTER TABLE practitioners ALTER COLUMN "id" SET DEFAULT nextval('practitioners_id_seq');

-- same
CREATE SEQUENCE faculties_id_seq AS integer START 1 OWNED BY faculties.id;

ALTER TABLE faculties ALTER COLUMN "id" SET DEFAULT nextval('faculties_id_seq');


CREATE SEQUENCE lectors_id_seq AS integer START 1 OWNED BY lectors.id;

ALTER TABLE lectors ALTER COLUMN "id" SET DEFAULT nextval('lectors_id_seq');

COMMIT;