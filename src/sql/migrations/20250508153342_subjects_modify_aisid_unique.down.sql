BEGIN;

ALTER TABLE IF EXISTS public.subjects DROP CONSTRAINT IF EXISTS subjects_aisid_key;

COMMIT;