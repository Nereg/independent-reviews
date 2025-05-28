BEGIN;

-- Remove default from lectors.id and drop sequence
ALTER TABLE lectors ALTER COLUMN "id" DROP DEFAULT;
DROP SEQUENCE IF EXISTS lectors_id_seq;

-- Remove default from faculties.id and drop sequence
ALTER TABLE faculties ALTER COLUMN "id" DROP DEFAULT;
DROP SEQUENCE IF EXISTS faculties_id_seq;

-- Remove default from practitioners.id and drop sequence
ALTER TABLE practitioners ALTER COLUMN "id" DROP DEFAULT;
DROP SEQUENCE IF EXISTS practitioners_id_seq;

COMMIT;