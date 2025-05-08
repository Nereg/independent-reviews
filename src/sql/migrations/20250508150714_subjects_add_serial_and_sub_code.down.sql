BEGIN;

ALTER TABLE IF EXISTS public.subjects
    DROP COLUMN "aisCode";

ALTER TABLE subjects ALTER COLUMN "id" DROP DEFAULT;

DROP SEQUENCE my_serial;

COMMIT;