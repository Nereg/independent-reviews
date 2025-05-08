BEGIN;

CREATE SEQUENCE my_serial AS integer START 1 OWNED BY subjects.id;

ALTER TABLE subjects ALTER COLUMN "id" SET DEFAULT nextval('my_serial');

ALTER TABLE IF EXISTS public.subjects
    ALTER COLUMN aisid SET NOT NULL;

ALTER TABLE IF EXISTS public.subjects
    ADD COLUMN "aisCode" text NOT NULL;

COMMIT;