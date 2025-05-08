BEGIN;

ALTER TABLE subjects ADD UNIQUE ("aisid");

COMMIT;